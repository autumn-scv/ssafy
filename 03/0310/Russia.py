# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T + 1):

    # N = 행 개수, M = 열 개수
    N, M = map(int, input().split())

    # 깃발 입력
    flag = [input() for _ in range(N)]

    ans = float('inf')  # 최소값 저장

    # i = 흰색 마지막 줄
    # j = 파란색 마지막 줄
    # 조건: 1 ≤ i < j < N
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):

            repaint = 0  # 다시 칠해야 하는 칸 수

            # 흰색 영역 0 ~ i
            for r in range(0, i + 1):
                for c in range(M):
                    # 현재 칸이 W가 아니면 다시 칠해야 함
                    if flag[r][c] != 'W':
                        repaint += 1

            # 파란색 영역 i+1 ~ j
            for r in range(i + 1, j + 1):
                for c in range(M):
                    if flag[r][c] != 'B':
                        repaint += 1

            # 빨간색 영역 j+1 ~ N-1
            for r in range(j + 1, N):
                for c in range(M):
                    if flag[r][c] != 'R':
                        repaint += 1

            # 최소값 갱신
            ans = min(ans, repaint)

    # 결과 출력
    print(f"#{test_case} {ans}")