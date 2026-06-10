T = int(input())

for tc in range(1, T+1):
    #도크에서 처리해야 하는 작업의 수
    N = int(input())
    # N개의 작업의 시작시간, 종료시간 입력
    # [[s1, e1], [s2, e2]...]
    work_list = [list(map(int, input().split())) for _ in range(N)]

    #이 작업 리스트를 종료 시간이 빠른 게 앞에 오도록 정렬
    # x = [s1, e1] x의 1번 인덱스가 작업의 종료시간이므로 이 숫자를 기준으로 정렬
    work_list.sort(key=lambda x: x[1])

    #최대 배정 작업 개수
    count = 0

    #작업이 빨리 끝나는 순서대로 하나씩 골라가면 된다.
    # 다음 작업을 선택할 때 이전 작업의 종료시간보다 빨리 시작하면 안 되니까 이전 작업의 종료 시간을 기억
    last_end = 0

    # work_list에서 작업 하나 꺼내서
    # 이 작업이 이전 작업의 종료 시간보다 같거나 늦게 시작하면 선택
    for start, end in work_list:
        #현대 직업의 시작 시간: start
        #현재 작업의 종료 시간: end