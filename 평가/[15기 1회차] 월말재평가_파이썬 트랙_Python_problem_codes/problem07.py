############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.

def categorize_books(books):
    library = {}
# 카테고리 = key
# title의 리스트 = value
    for book in books_data:
        category = book['category']
        title = book['title']

        if category not in library:
            library[category] = []
        library[category].append(title)
    return library

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
books_data = [
    {'title': 'Python Basic', 'category': 'IT'},
    {'title': 'Java Standard', 'category': 'IT'},
    {'title': 'History of World', 'category': 'History'},
    {'title': 'Cooking 101', 'category': 'Life'}
]
# 결과:
# {
#   'IT': ['Python Basic', 'Java Standard'],
#   'History': ['History of World'],
#   'Life': ['Cooking 101']
# }
print(categorize_books(books_data))
#####################################################