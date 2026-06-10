# 아래 함수를 수정하시오.
def find_min_max(lst):
    
    #일단 맨 앞에 있는 값을 최소값, 최대값이라 생각
    max_value = lst[0]
    min_value = lst[0]


    for num in lst:
        if num < min_value:
            #발견한 더 작은 값을 최소값으로 변경
            min_value = num
            #지금 꺼내 온 num이 max보다 크다
        if num > max_value:
            #발견한 더 큰 값을 최대값으로 변경
            max_value = num
    return min_value, max_value


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
