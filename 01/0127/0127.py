data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for item in data:

    for in key_list:
        # 1. 
        #get으로 해당 키가 없으면 'unknown'으로 임시 조회
        value = item.get(key, 'unknown')
        print(f'{key}은/는 {value}입니다.')
        # 2.
        #setdefault로 해당 키가 없으면 'unknown' 값 할당까지
    #     item.setdefault(key, 'unknown')
    #     print(f'{key}은/는 {item[key]}입니다.')
    # print()