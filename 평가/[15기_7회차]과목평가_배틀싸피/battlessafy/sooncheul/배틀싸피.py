import sys
import socket
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

# 메인 프로그램 연결 및 초기화
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

# 메인 프로그램으로 데이터(명령어) 전송
def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))

        return receive()
        
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')

    return None

# 메인 프로그램으로부터 데이터 수신
def receive():
    try:
        game_data = (sock.recv(1024)).decode()

        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data

        print('[STATUS] No receive data from the main program.')    
        close()

    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')

# 연결 해제
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
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
my_allies = {}  # 아군 정보. 예) my_allies['M'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

##############################
# 입력 데이터 파싱
##############################

# 입력 데이터를 파싱하여 각각의 리스트/딕셔너리에 저장
def parse_data(game_data):
    global HIGHT, WIDTH
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0 # 맵의 세로 크기
    map_width = int(header[1]) if len(header) >= 2 else 0  # 맵의 가로 크기
    num_of_allies = int(header[2]) if len(header) >= 3 else 0  # 아군의 수
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0  # 적군의 수
    num_of_codes = int(header[4]) if len(header) >= 5 else 0  # 암호문의 수
    row_index += 1

    HIGHT = map_height
    WIDTH = map_width

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# 파싱한 데이터를 화면에 출력
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

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])
        PW_info = codes[i]

##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '기본코드'
game_data = init(NICKNAME)

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

def password():
    pw_result = ''

    for i in range(len(PW_info)):
        for j in range(len(alpa)):
            if PW_info[i] == alpa[j]:
                idx = (j + 9) if j + 9 <= 25 else (j + 9 - 26)
                print(idx)
                pw_result += alpa[idx]
                break

    return pw_result

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

# 경로 탐색 알고리즘
# def bfs(grid, start, target, wall):
#     rows, cols = len(grid), len(grid[0])
#     queue = deque([(start, [])])
#     visited = {start}
#
#     while queue:
#         (r, c), actions = queue.popleft()
#
#         for d, (dr, dc) in enumerate(DIRS):
#             for m in range(1, 4):
#                 ni, nj = r + dr * m, c + dc * m
#                 if 0 <= ni < rows and 0 <= nj < cols:
#                     if grid[ni][nj] == wall:
#                         break
#
#                     if (ni, nj) == target:
#                         return actions + [FIRE_CMDS[d]]
#
#         for d, (dr, dc) in enumerate(DIRS):
#             nr, nc = r + dr, c + dc
#
#             if 0 <= nr < rows and 0 <= nc < cols :
#                 if grid[nr][nc] == 'T':
#                     actions += [MEGA_FIRE_CMDS[d]]
#                 if grid[nr][nc] != wall and (nr, nc) not in visited and not grid[nr][nc] == 'W':
#                     visited.add((nr, nc))
#                     queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))
#
#     return []

def dfs(next, cnt, path, skill):
    # print(skill)
    global COUNT, CONTROL, PW_info
    if COUNT <= cnt:
        return

    i, j = next
    # print(i, j)
    if PW_info:
        CONTROL += [f"G {password()}"]
        PW_info = ''
        return

    for d, (di, dj) in enumerate(DIRS):

        for m in range(1, 4):
            nr = i + di * m
            nc = j + dj * m
            if 0 <= nr < HIGHT and 0 <= nc < WIDTH:
                if map_data[nr][nc] == 'R':
                    break

                if map_data[nr][nc] == 'X':
                    COUNT = cnt
                    CONTROL = path + [FIRE_CMDS[d]]
                    return

                elif map_data[nr][nc] in enemies:
                    CONTROL = path + [MEGA_FIRE_CMDS[d]]
                    return

        ni = i + di
        nj = j + dj

        if 0 <= ni < HIGHT and 0 <= nj < WIDTH:
            if map_data[ni][nj] == 'G' and visited[ni][nj] == 0:

                visited[ni][nj] = 1
                # for idx in range(HIGHT):
                #     print(visited[idx])
                # print(ni, nj)
                dfs((ni, nj), cnt + 1, path + [MOVE_CMDS[d]], skill)
                visited[ni][nj] = 0

            if map_data[ni][nj] == 'F' and CNT_M < 10:
                visited[ni][nj] = 1
                CONTROL = path + [MOVE_CMDS[d]]
                return

            if skill > 0 and map_data[ni][nj] == 'T':
                # print(1)
                visited[ni][nj] = 1
                dfs((ni, nj), cnt + 2, path + [MEGA_FIRE_CMDS[d], MOVE_CMDS[d]], skill - 1)
                visited[ni][nj] = 0

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
MEGA_FIRE_CMDS = {0: "R F M", 1: "D F M", 2: "L F M", 3: "U F M"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = 'RW'
TREE_SYMBOL = 'T'
HIGHT = 0
WIDTH = 0
CNT_M = 0
PW_info = ''

# 최초 데이터 파싱
parse_data(game_data)

# 출발지점, 목표지점의 위치 확인
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
if not start or not target:
    print("[ERROR] Start or target not found in map")
    close()
    exit()

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################

# 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
while game_data is not None:

    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################
    #--------------------------------------------------
    '''
    핵심 전략!!
    스킬을 써야하는 5번 테스트 케이스 존재!
    매 판 한정된 테스트 케이스!
    bfs 보다 dfs로 풀이한다!
    하여 최적의 루트를 찾아 쏠 수 있는 범위에 있는 적은 쏠 수 있게 구현하였습니다.
    감사합니다.
    '''
    # --------------------------------------------------


    # 파싱한 데이터를 화면에 출력하여 확인

    print_data()

    # for i in range(HIGHT):
    #     print(map_data[i])
    # print()
    # 방문 배열
    visited = [[0] * WIDTH for _ in range(HIGHT)]
    alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 이전 경로 탐색 결과가 존재하지 않을 경우 다시 탐색
    start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)

    si, sj = start

    COUNT = float('inf')

    CONTROL = []

    dfs((si, sj), 0, [], CNT_M)

    print(CONTROL)


    # 탱크를 제어할 명령어를 output의 값으로 지정(type: string)
    output = CONTROL.pop(0)

    # 메인 프로그램에서 명령을 처리할 수 있도록 명령어를 submit()의 인자로 전달
    game_data = submit(output)

    # submit()의 리턴으로 받은 갱신된 데이터를 다시 파싱
    if game_data:
        parse_data(game_data)

    ##############################
    # 알고리즘 메인 구현 끝
    ##############################

# 반복문을 빠져나왔을 때 메인 프로그램과의 연결을 완전히 해제하기 위해 close() 호출
close()