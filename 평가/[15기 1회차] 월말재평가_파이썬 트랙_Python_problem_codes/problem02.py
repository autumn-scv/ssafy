############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

def count_long_words(words, min_length):
    word_count = 0
    for word in words:
        cnt = 0
        for alphabet in word:
            cnt += 1
        if cnt >= min_length:
            word_count += 1
    return word_count
    

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_long_words(['apple', 'banana', 'cat', 'dog'], 4))  # 2 ('apple', 'banana')
print(count_long_words(['a', 'bb', 'ccc'], 5))                 # 0
#####################################################