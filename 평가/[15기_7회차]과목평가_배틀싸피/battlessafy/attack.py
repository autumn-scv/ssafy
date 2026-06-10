import sys
import socket
from collections import deque
import heapq  # 다익스트라를 위한 필수 라이브러리

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
        print('[ERROR] Failed to connect. Please check if the main program is waiting for connection.')
        print(e)


def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))
        return receive()
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')
    return None


def receive():
    try:
        game_data = (sock.recv(1024)).decode()
        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        print('[STATUS] No receive data from the main program.')
        close()
    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')


def close():
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')


##############################
# 입력 데이터 변수 정의
##############################
map_data = [[]]
my_allies = {}
enemies = {}
codes = []


##############################
# 입력 데이터 파싱
##############################

def parse_data(game_data):
    global HIGHT, WIDTH
    game_data_rows = game_data.split('\n')
    row_index = 0

    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0
    map_width = int(header[1]) if len(header) >= 2 else 0
    num_of_allies = int(header[2]) if len(header) >= 3 else 0
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0
    num_of_codes = int(header[4]) if len(header) >= 5 else 0
    row_index += 1

    HIGHT = map_height
    WIDTH = map_width

    map_data.clear()
    map_data.extend([['' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])


def print_data():
    global CNT_M, PW_info
    print(f'\n----------입력 데이터----------\n{game_data}\n----------------------------')

    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(my_allies)})')
    for k, v in my_allies.items():
        if k == 'M':
            print(f'M (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
            CNT_M = int(v[3])
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')


##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '직진러쉬코드_버그픽스'
game_data = init(NICKNAME)


###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

# 출발지와 목적지의 위치 찾기
def find_positions(grid, start_mark, goal_mark):
    start = goal = None
    for i in range(HIGHT):
        for j in range(WIDTH):
            if grid[i][j] == start_mark:
                start = (i, j)
            elif grid[i][j] == goal_mark:
                goal = (i, j)
    return start, goal


# 🚀 다익스트라(Dijkstra) 경로 탐색 함수 (목적지 'X' 고정)
def dijkstra_rush(start_pos):
    global HIGHT, WIDTH, map_data, enemies, DIRS, MOVE_CMDS, FIRE_CMDS

    si, sj = start_pos

    # 1. 아군 기지(H) 반경 2칸 보호 구역 설정 (우회 로직 유지)
    restricted_zones = set()
    for r in range(HIGHT):
        for c in range(WIDTH):
            if map_data[r][c] == 'H':
                for dr in range(-2, 3):
                    for dc in range(-2, 3):
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < HIGHT and 0 <= cc < WIDTH:
                            restricted_zones.add((rr, cc))

    pq = [(0, si, sj, [])]
    distances = {(si, sj): 0}

    while pq:
        cost, ci, cj, path = heapq.heappop(pq)

        if distances.get((ci, cj), float('inf')) < cost:
            continue

        # 2. 제자리에서 사거리 내 상대 기지(X) 사격
        for d, (di, dj) in enumerate(DIRS):
            for m in range(1, 4):
                nr, nc = ci + di * m, cj + dj * m
                if 0 <= nr < HIGHT and 0 <= nc < WIDTH:
                    target_tile = map_data[nr][nc]

                    # 💡 X를 발견하면 묻지도 따지지도 않고 즉시 발사 명령 추가!
                    if target_tile == 'X':
                        return path + [FIRE_CMDS[d]]

                    # 시야가 막히는 조건 (돌, 나무, 적 탱크)
                    if target_tile in ('R', 'T') or (target_tile in enemies and target_tile != 'X'):
                        break

                        # 3. 4방향 이동 및 파괴 로직
        for d, (di, dj) in enumerate(DIRS):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < HIGHT and 0 <= nj < WIDTH:
                # 아군 기지 구역 우회
                if (ni, nj) in restricted_zones:
                    continue

                target_tile = map_data[ni][nj]

                # ========================================================
                # [NEW] S 랑 F는 벽(장애물)처럼 취급하여 절대 진입하지 않음!
                # ========================================================
                if target_tile in ('S', 'F'):
                    continue

                # 평지('G'), 시작점('M')만 밟고 이동 가능 (F 제외됨)
                if target_tile in ('G', 'M'):
                    new_cost = cost + 1
                    if new_cost < distances.get((ni, nj), float('inf')):
                        distances[(ni, nj)] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj, path + [MOVE_CMDS[d]]))

                # 나무('T')는 일반 포탄으로 부수면서 전진
                elif target_tile == 'T':
                    new_cost = cost + 2
                    if new_cost < distances.get((ni, nj), float('inf')):
                        distances[(ni, nj)] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj, path + [FIRE_CMDS[d], MOVE_CMDS[d]]))

    return ["S"]  # 갈 길이 완벽히 막히면 대기


# 상수 정의
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
HIGHT = 0
WIDTH = 0

# 최초 데이터 파싱
parse_data(game_data)
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
if not start or not target:
    print("[ERROR] Start or target not found in map")
    close()
    exit()

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################

# 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신
while game_data is not None:
    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################

    print_data()
    start, _ = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)

    if start:
        actions = dijkstra_rush(start)
        output = actions.pop(0) if actions else "S"
    else:
        output = "S"

    print(f"[ACTION] 이번 턴 명령어: {output}")

    game_data = submit(output)
    if game_data:
        parse_data(game_data)

    ##############################
    # 알고리즘 메인 구현 끝
    ##############################

close()