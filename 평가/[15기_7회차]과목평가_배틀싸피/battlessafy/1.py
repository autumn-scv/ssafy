import sys
import socket
import heapq
from collections import deque

##############################
# 메인 프로그램 통신 변수 정의
##############################
HOST = '127.0.0.1'
PORT = 8747
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''
sock = socket.socket()

##############################
# 메인 프로그램 통신 함수 정의
##############################

def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}...')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'
        return submit(init_command)
    except Exception as e:
        print('[ERROR] Failed to connect.', e)

def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))
        return receive()
    except Exception as e:
        print('[ERROR] Failed to send data.', e)
    return None

def receive():
    try:
        game_data = (sock.recv(1024)).decode()
        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        print('[STATUS] No receive data from the main program.')    
        close()
    except Exception as e:
        print('[ERROR] Failed to receive data.', e)

def close():
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.', e)

##############################
# 입력 데이터 변수 정의
##############################
map_data = [[]]
my_allies = {}
enemies = {}
codes = []

##############################
# 입력 데이터 파싱 (데이터 정제)
##############################
def parse_data(game_data):
    game_data_rows = game_data.strip().split('\n')
    row_index = 0

    header = game_data_rows[row_index].split()
    map_height = int(header[0]) if len(header) >= 1 else 0
    map_width = int(header[1]) if len(header) >= 2 else 0
    num_of_allies = int(header[2]) if len(header) >= 3 else 0
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0
    num_of_codes = int(header[4]) if len(header) >= 5 else 0
    row_index += 1

    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split()
        for j in range(0, len(col)):
            map_data[i][j] = col[j].strip() 
    row_index += map_height

    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split()
        ally_name = ally.pop(0).strip() if len(ally) >= 1 else '-'
        my_allies[ally_name] = [x.strip() for x in ally] 
    row_index += num_of_allies

    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split()
        enemy_name = enemy.pop(0).strip() if len(enemy) >= 1 else '-'
        enemies[enemy_name] = [x.strip() for x in enemy]
    row_index += num_of_enemies

    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i].strip())

##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '천방지축어리둥절빙글빙글'
game_data = init(NICKNAME)

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

def get_positions():
    """팀 A/B 반전에 대비하여 아군/적군 포탑을 실시간으로 스캔하고 교차 검증합니다."""
    my_tank = None
    enemy_turret = None
    enemy_tanks = []
    supplies = []
    
    ally_keys = list(my_allies.keys())
    enemy_keys = list(enemies.keys())
    
    # 1. 맵에 존재하는 기호들 스캔 (알파벳 단일 문자 추출)
    map_symbols = set()
    for r in map_data:
        for c in r:
            map_symbols.add(c)
            
    # 보통 포탑은 H, X, Y 등으로 표기됨 (탱크나 지형이 아닌 대문자 추출)
    possible_turrets = [s for s in map_symbols if s.isalpha() and s not in ['M', 'R', 'W', 'T', 'F', 'G'] and len(s) == 1]
    
    ally_turret_sym = None
    enemy_turret_sym = None
    
    # 2. 확실한 명단(사전)에서 우선 파악
    for t in possible_turrets:
        if t in ally_keys: ally_turret_sym = t
        if t in enemy_keys: enemy_turret_sym = t
            
    # 3. 명단 누락 시 교차 검증 추론 (팀킬 방지 락)
    if ally_turret_sym and not enemy_turret_sym:
        for t in possible_turrets:
            if t != ally_turret_sym: enemy_turret_sym = t
    elif enemy_turret_sym and not ally_turret_sym:
        for t in possible_turrets:
            if t != enemy_turret_sym: ally_turret_sym = t
            
    # 4. 그래도 없으면 맵 기본값 할당 (안전장치)
    if not ally_turret_sym: ally_turret_sym = 'H'
    if not enemy_turret_sym: enemy_turret_sym = 'X'
    if ally_turret_sym == enemy_turret_sym:
        enemy_turret_sym = 'X' if ally_turret_sym == 'H' else 'H'
        
    ally_turret_pos = None

    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            cell = map_data[i][j]
            if cell == 'M':
                my_tank = (i, j)
            elif cell == enemy_turret_sym: 
                enemy_turret = (i, j)
            elif cell == ally_turret_sym:
                ally_turret_pos = (i, j)
            elif cell in enemy_keys and cell != enemy_turret_sym:
                enemy_tanks.append((i, j))
            elif cell == 'F':
                supplies.append((i, j))
                
    # 🚨 아군 포탑 주변 3x3 좌표 결계 (이동 불가 구역 - 옐로카드 방지)
    ally_turret_zone = set()
    if ally_turret_pos:
        ty, tx = ally_turret_pos
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ally_turret_zone.add((ty + dy, tx + dx))
                
    return my_tank, enemy_turret, enemy_tanks, supplies, ally_turret_sym, enemy_turret_sym, ally_turret_zone

def get_immediate_target(my_tank):
    """사거리 3 이내 적군 조준 (아군 포탑 100% 보호)"""
    if not my_tank: return None
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    
    _, _, _, _, ally_turret_sym, enemy_turret_sym, _ = get_positions()
    ally_keys = list(my_allies.keys())
    enemy_keys = list(enemies.keys())
    
    for cmd, (dy, dx) in directions.items():
        for step in range(1, 4): # 최대 사거리 3칸
            ny, nx = my_tank[0] + dy * step, my_tank[1] + dx * step
            if not (0 <= ny < len(map_data) and 0 <= nx < len(map_data[0])):
                break
                
            cell = map_data[ny][nx]
            
            # 사거리에 적(포탑 또는 탱크)이 포착되면 즉시 발포 명령 반환
            if cell == enemy_turret_sym or cell in enemy_keys:
                return cmd
                
            # 🚨 절대 금지: 바위, 보급소, 나무, 아군탱크 및 아군 포탑이 궤적에 있으면 격발 중지
            # 물(W)은 장애물이 아니므로 포탄 무사 통과 (저격)
            if cell in ['R', 'F', 'T'] or cell in ally_keys or cell == ally_turret_sym:
                break
                
    return None

def kaisar_find(codes, idx):
    code = codes[0]
    words = ""
    for i in code:
        words += chr((ord(i)-65 + idx) % 26 + 65)
    return f"G {words}"

def find_absolute_shortest_path(start, target_symbol, ally_turret_zone, total_ammo):
    """적의 사거리를 무시하고 무조건 적 포탑으로 닥돌하는 절대 최단 경로 (아군은 철저히 회피)"""
    N, M = len(map_data), len(map_data[0])
    pq = [(0, start[0], start[1], [])]
    visited = set([(start[0], start[1])])
    
    _, _, _, _, ally_turret_sym, enemy_turret_sym, _ = get_positions()
    ally_keys = list(my_allies.keys())
    enemy_keys = list(enemies.keys())
    
    while pq:
        cost, y, x, path = heapq.heappop(pq)
        
        # 보급소 탐색 시 반경 1칸 주변 도착
        if target_symbol == 'F':
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= y+dy < N and 0 <= x+dx < M and map_data[y+dy][x+dx] == 'F':
                    return path
                    
        # 목표 지점 도착
        elif map_data[y][x] == target_symbol:
            return path
            
        for dy, dx, cmd in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < N and 0 <= nx < M:
                cell = map_data[ny][nx]
                
                # 아군 포탑 3x3 진입 결계 (타겟이 아군 포탑이 아닐 때만 차단)
                if (ny, nx) in ally_turret_zone and cell != target_symbol:
                    continue
                
                # 🚨 물리적 이동 절대 불가 (바위, 물, 보급소 위, 아군 탱크, 아군 포탑)
                if cell in ['R', 'W', 'F'] or cell in ally_keys or cell == ally_turret_sym: 
                    continue
                    
                next_cost = cost + 1
                
                # 전방을 막고 있는 나무나 적(탱크, 포탑)은 포탄으로 뚫고 감 (파괴 1턴 + 전진 1턴 = +2)
                if cell == 'T' or cell in enemy_keys or cell == enemy_turret_sym:
                    if total_ammo <= 0: continue # 총알이 없으면 뚫을 수 없으므로 못 감
                    next_cost += 2 
                    
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    heapq.heappush(pq, (next_cost, ny, nx, path + [(ny, nx, cmd, cell)]))
                    
    return []

def get_fallback_move(my_tank, ally_turret_zone):
    """모든 경로가 막혔을 때, 제자리 멈춤(S) 옐로카드를 피하기 위한 안전 이동 구역 탐색"""
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for cmd, (dy, dx) in directions.items():
        ny, nx = my_tank[0] + dy, my_tank[1] + dx
        if 0 <= ny < len(map_data) and 0 <= nx < len(map_data[0]):
            cell = map_data[ny][nx]
            # 비어있는 평지인 경우에만 1칸 이동하여 턴을 넘김
            if cell not in ['R', 'W', 'T', 'F'] and cell not in list(my_allies.keys()) and cell not in list(enemies.keys()):
                if (ny, nx) not in ally_turret_zone:
                    return f"{cmd} A"
    return "S"

def activate_decision(idx):
    my_tank, enemy_turret, enemy_tanks, supplies, ally_turret_sym, enemy_turret_sym, ally_turret_zone = get_positions()
    if not my_tank: return "S" 
        
    my_ammo = int(my_allies['M'][2])
    mega_ammo = int(my_allies['M'][3])
    total_ammo = my_ammo + mega_ammo
    my_y, my_x = my_tank
    
    enemy_keys = list(enemies.keys())
    RECHARGE_THRESHOLD = 3 # 메가탄이 3개 미만이면 재충전

    # 1. 공격 최우선 (사거리 안에 적이 들어오면 우직하게 딜부터 박습니다)
    target_cmd = get_immediate_target(my_tank)
    if target_cmd:
        if mega_ammo > 0: return f"{target_cmd} F M"
        elif my_ammo > 0: return f"{target_cmd} F"
            
    # 2. 메가탄 재충전 모드
    if mega_ammo < RECHARGE_THRESHOLD and supplies and mega_ammo < 10:
        is_near_f = False
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1), (0,0)]:
            ny, nx = my_y + dy, my_x + dx
            if 0 <= ny < len(map_data) and 0 <= nx < len(map_data[0]) and map_data[ny][nx] == 'F':
                is_near_f = True
                break
                
        if is_near_f and codes:
            return kaisar_find(codes, idx)
            
        path = find_absolute_shortest_path(my_tank, 'F', ally_turret_zone, total_ammo)
        if path:
            ny, nx, cmd, cell = path[0]
            if cell == 'T' or cell in enemy_keys or cell == enemy_turret_sym:
                return f"{cmd} F" if my_ammo > 0 else f"{cmd} F M"
            return f"{cmd} A" 
            
    # 3. 포탑 격파 돌격 (회피 따위 없는 일직선 최단 경로 진격)
    if enemy_turret:
        path = find_absolute_shortest_path(my_tank, enemy_turret_sym, ally_turret_zone, total_ammo)
        
        if path:
            ny, nx, cmd, cell = path[0]
            # 🚨 닥돌 모드: 내 앞을 가로막는게 나무거나 "적(탱크/포탑)"이면 박살내면서 전진
            if cell == 'T' or cell in enemy_keys or cell == enemy_turret_sym: 
                return f"{cmd} F" if my_ammo > 0 else f"{cmd} F M"
            return f"{cmd} A"
            
    # 4. 할 수 있는 게 없을 때 (총알 0발, 사방이 막힘 등) 무빙 쳐서 옐로카드 방어
    return get_fallback_move(my_tank, ally_turret_zone)

###################################
# 알고리즘 메인 실행 루프
###################################

if game_data:
    parse_data(game_data)

idx = 0
prev_mega_ammo = int(my_allies['M'][3]) if 'M' in my_allies else 0
tried_password = False 

while game_data is not None:
    current_mega_ammo = int(my_allies['M'][3]) if 'M' in my_allies else 0
    
    if tried_password and (prev_mega_ammo >= current_mega_ammo) and codes:
        idx += 1
    
    output = activate_decision(idx)
    
    tried_password = output.startswith("G ")
    prev_mega_ammo = int(my_allies['M'][3]) if 'M' in my_allies else 0

    game_data = submit(output)
    if game_data:
        parse_data(game_data)

close()