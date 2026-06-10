# 아래 함수를 수정하시오.
def count_character(word, char): #파라미터 2개



    return word.count(char)

# 만약 count 못 쓰게 한다면 
# count = 0 우리가 원하는 답을 저장할 변수를 하나 만듦(count)

# 답을 구하는 과정

# for c in word:
#c가 char랑 같으면 갯수+1
#     if c == char:
#         count = count + 1
# return count



result = count_character("Hello, World!", "o")
print(result)  # 2
