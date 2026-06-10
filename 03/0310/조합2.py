arr = [1,2,3,4,5]
N = 5
R = 3

# cnt : 원소를 고른 횟수
# selected : 내가 지금까지 고른 원소 모음
# start : 내가 원소를 이전에 골랐다면, 고른 원소 뒤에 있는 원소들만 추가 가능하도록 범위를 지정
# 2번 인덱스에 있는 원소를 이전 단계에서 골랐다면, 다음 단계는 3번 이상 인덱스에서만 고르기 가능하도록 -> 같은 원소 중복 선택 방지 / 순서만 다른 상태를 방지(123, 321)

def comb(cnt, selected, start):
    # 1. 종료 조건

    if cnt == R:
        print(selected)
        return

    #2. 재귀 호출
    for i in range(start, N):
        # i번 인덱스에 있는 원소를 고르고 다음 단계로
        # selected.append(arr[i])
        # 다음 단계에서 원소를 고를 수 있는 인덱스 범위는 i + 1 부터
        comb(cnt+1, selected + [arr[i]], i + 1)
        # selected.pop()

# 고른 횟수 0번, 아무것도 고르지 않은 상태로 시작
# 인덱스 0부터 고를 수 있음
comb(0, [], 0)