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
        sock.connect((HOST, PORT))
        init_command = f'INIT {nickname}'
        return submit(init_command)
    except Exception as e:
        print('[ERROR] 연결 실패', e)

def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))
        return receive()
    except Exception as e:
        print('[ERROR] 전송 실패', e)
    return None

def receive():
    try:
        game_data = (sock.recv(1024)).decode()
        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        close()
    except Exception as e:
        print('[ERROR] 수신 실패', e)

def close():
    try:
        if sock is not None: sock.close()
    except: pass

##############################
# 입력 데이터 변수 및 파싱
##############################
map_data = [[]]
my_allies = {}
enemies = {}
codes = []

def parse_data(game_data):
    game_data_rows = game_data.strip().split('\n')
    header = game_data_rows[0].split()
    map_height, map_width = int(header[0]), int(header[1])
    num_of_allies, num_of_enemies, num_of_codes = int(header[2]), int(header[3]), int(header[4])

    map_data.clear()
    map_data.extend([[ '' for _ in range(map_width)] for _ in range(map_height)])
    for i in range(map_height):
        col = game_data_rows[1 + i].split()
        for j in range(len(col)):
            map_data[i][j] = col[j].strip()

    curr = 1 + map_height
    my_allies.clear()
    for i in range(curr, curr + num_of_allies):
        ally = game_data_rows[i].split()
        my_allies[ally.pop(0).strip()] = [x.strip() for x in ally]
    
    curr += num_of_allies
    enemies.clear()
    for i in range(curr, curr + num_of_enemies):
        enemy = game_data_rows[i].split()
        enemies[enemy.pop(0).strip()] = [x.strip() for x in enemy]
    
    curr += num_of_enemies
    codes.clear()
    for i in range(curr, curr + num_of_codes):
        codes.append(game_data_rows[i].strip())

###################################
# 전략 알고리즘 파트
###################################

def get_entities():
    """아군/적군 위치 및 포탑 기호를 식별하고 수비 구역을 설정합니다."""
    my_tank = None
    enemy_tanks = []
    supplies = []
    ally_turret_pos = None
    
    ally_keys = list(my_allies.keys())
    enemy_keys = list(enemies.keys())
    
    # 동적 포탑 식별
    ally_turret_sym = next((k for k in ally_keys if k in ['H', 'X']), 'H')
    enemy_turret_sym = next((k for k in enemy_keys if k in ['H', 'X']), 'X')
    
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            cell = map_data[i][j]
            if cell == 'M': my_tank = (i, j)
            elif cell == 'F': supplies.append((i, j))
            elif cell == ally_turret_sym: ally_turret_pos = (i, j)
            elif cell in enemy_keys and cell != enemy_turret_sym:
                enemy_tanks.append((i, j))
                
    # 아군 포탑 3x3 결계 (옐로카드 방지)
    ally_turret_zone = set()
    if ally_turret_pos:
        ty, tx = ally_turret_pos
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ally_turret_zone.add((ty + dy, tx + dx))
                
    return my_tank, enemy_tanks, supplies, ally_turret_sym, enemy_turret_sym, ally_turret_zone

def get_immediate_target(my_tank, enemy_tanks):
    """사거리 3 이내 적 탱크 조준 (포탑은 절대 쏘지 않음)"""
    dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    ally_keys = list(my_allies.keys())
    
    for cmd, (dy, dx) in dirs.items():
        for step in range(1, 4):
            ny, nx = my_tank[0] + dy * step, my_tank[1] + dx * step
            if not (0 <= ny < len(map_data) and 0 <= nx < len(map_data[0])): break
            cell = map_data[ny][nx]
            if (ny, nx) in enemy_tanks: return cmd
            # 바위, 나무, 포탑, 아군에 막히면 사격 불가
            if cell in ['R', 'T', 'H', 'X'] or cell in ally_keys: break
    return None

def find_path(start, target_mode, ally_turret_zone, total_ammo, enemy_tanks):
    """A* 탐색을 통한 최단 경로 (수비 가중치 적용)"""
    N, M = len(map_data), len(map_data[0])
    pq = [(0, 0, start[0], start[1], [])]
    visited = {start: 0}
    ally_keys = list(my_allies.keys())
    
    while pq:
        _, cost, y, x, path = heapq.heappop(pq)
        
        if target_mode == 'F':
            if any(abs(y-fy)+abs(x-fx)==1 for fy, fx in target_mode): return path
        elif (y, x) in target_mode: return path
        
        for dy, dx, cmd in [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                cell = map_data[ny][nx]
                # 물리적 벽 및 아군 포탑 결계 회피
                if cell in ['R', 'W', 'H', 'X'] or cell in ally_keys: continue
                if (ny, nx) in ally_turret_zone and (ny, nx) not in target_mode: continue
                
                new_cost = cost + 1
                if cell == 'T': # 나무 파괴 비용
                    if total_ammo <= 0: continue
                    new_cost += 1
                
                if (ny, nx) not in visited or new_cost < visited[(ny, nx)]:
                    visited[(ny, nx)] = new_cost
                    # 휴리스틱: 대상까지의 거리 + 위험도 가중치
                    priority = new_cost + abs(ny - target_mode[0][0]) + abs(nx - target_mode[0][1])
                    heapq.heappush(pq, (priority, new_cost, ny, nx, path + [(ny, nx, cmd, cell)]))
    return []

def activate_decision(idx):
    my_tank, enemy_tanks, supplies, ally_turret_sym, enemy_turret_sym, ally_turret_zone = get_entities()
    if not my_tank: return "S"
    
    my_ammo = int(my_allies['M'][2])
    mega_ammo = int(my_allies['M'][3])
    total_ammo = my_ammo + mega_ammo
    
    # 1. 수비 사격: 사거리 내 적 탱크 즉시 제거
    attack_dir = get_immediate_target(my_tank, enemy_tanks)
    if attack_dir:
        return f"{attack_dir} F M" if mega_ammo > 0 else f"{attack_dir} F"

    # 2. 지능형 보급: 적이 멀리 있거나 보급소가 매우 가까울 때만 충전
    if mega_ammo < 6 and supplies:
        # 충전소 인접 여부 확인
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1), (0,0)]:
            if (my_tank[0]+dy, my_tank[1]+dx) in supplies:
                return f"G {''.join(chr((ord(c)-65 + idx) % 26 + 65) for c in codes[0])}" if codes else "S"
        
        path_f = find_path(my_tank, supplies, ally_turret_zone, total_ammo, enemy_tanks)
        path_e = find_path(my_tank, enemy_tanks, ally_turret_zone, total_ammo, enemy_tanks) if enemy_tanks else []
        
        # 적 탱크보다 보급소가 가깝거나 적과의 거리가 충분히 안전할 때 보급
        if len(path_f) < len(path_e) or len(path_e) > 5:
            if path_f:
                ny, nx, cmd, cell = path_f[0]
                return f"{cmd} F" if cell == 'T' else f"{cmd} A"

    # 3. 적 탱크 추격 (수비적 사냥)
    if enemy_tanks:
        path = find_path(my_tank, enemy_tanks, ally_turret_zone, total_ammo, enemy_tanks)
        if path:
            ny, nx, cmd, cell = path[0]
            return f"{cmd} F" if cell == 'T' else f"{cmd} A"

    return "S"

###################################
# 메인 루프
###################################
NICKNAME = '천방지축어리둥절빙글빙글'
game_data = init(NICKNAME)
if game_data: parse_data(game_data)
idx, prev_mega = 0, int(my_allies['M'][3]) if 'M' in my_allies else 0

while game_data:
    curr_mega = int(my_allies['M'][3]) if 'M' in my_allies else 0
    if prev_mega >= curr_mega and any(output.startswith('G') for output in [globals().get('last_output','')]):
        idx = (idx + 1) % 26
    
    last_output = activate_decision(idx)
    prev_mega = curr_mega
    game_data = submit(last_output)
    if game_data: parse_data(game_data)

close()