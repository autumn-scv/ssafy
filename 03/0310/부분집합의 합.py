A = [i for i in range(1, 13)]

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

# 부분 집합 중에 원소의 개수가 N개
# 합이 K인 부분집합의 개수
count = 0

def comb(cnt, selected, start):

    if cnt == N: