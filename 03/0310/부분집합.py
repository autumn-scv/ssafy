arr = [1,2,3,4,5]
N = 5

#모든 부분집합을 구하는 재귀함수
# i : 내가 선택한 원소의 개수 //
# 내가 부분집합에 포함할 지 안 할 지 결정하고 있는 원소의 인덱스
# selected : 내가 지금까지 포함시킨 원소들(부분집합)

def subset(i, selected):

    # 1. 종료 조건
    # 각 원소를 부분집합에 포함한다 / 포함하지 않는다
    # 이 선택을 5번 하면 끝
    if i == N:
        print(selected)
        return


   # 2. 재귀 호출
   # 경우의 수가 2가지로 나뉜다.
   # i번 원소를 부분집합에 포함하고 다음 단계로
   #  selected.append(arr[i])
    subset(i + 1, selected + [arr[i]])
    # i번 원소를 부분집합에 포함하지 않고 다음 단계로
    subset(i + 1, selected)

#아직 선택한 횟수는 0번, 부분집합에 포함한 원소는 아무것도 없는 상태로 시작
subset(0, [])