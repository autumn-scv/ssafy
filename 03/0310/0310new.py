arr = [1, 2, 3, 4, 5]
N = 5

# 이중에서 3개를 뽑겠다.
R = 3


# 모든 부분집합을 구하는 재귀함수
# i : 내가 부분집합에 포함할지 안할지 결정하고 있는 원소의 인덱스
# selected : 내가 지금까지 포함시킨 원소들 (부분집합)
# cnt : 내가 지금까지 부분집합에 포함시킨 횟수
def subset(i, selected, cnt):
    # 1. 종료 조건
    # 각 원소를 부분집합에 포함o / 포함x
    # 모든 원소에 대해서 부분집합에 포함할지 안할지 고려가 끝났다면 종료
    # 부분집합의 원소의 개수를 세서 R개라면 출력
    if cnt == R:
        # if len(selected) == R:
        #     print(selected)
        return

    if i == N:
        return

    # 2. 재귀 호출
    # 경우의 수가 2가지로 나뉜다.
    # i번 원소를 부분집합에 포함 하고 다음단계로
    # selected.append(arr[i])
    subset(i + 1, selected + [arr[i]], cnt + 1)
    # i번 원소를 부분집합에 포함하지 않고 다음단계로
    # selected.pop()
    subset(i + 1, selected, cnt)

# 아직 선택한 횟수는 0번, 부분집합에 포함한 원소는 아무것도 없는상태로 시작
subset(0,[], 0)
