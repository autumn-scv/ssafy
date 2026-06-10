food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for food in food_list:
    name = food['이름']
    kind = food['종류']
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    elif food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{name} 은/는 {kind} (이)다.')
#  '''
#  f스트링으로 출력해
#  if 토마토면 종류를 과일로 바꿔서 출력해
#  elif 자장면이면 자장면엔 고춧가루지를 추가로 출력해
#  food_list를 출력해
#  for을 while로 바꿔
#  '''

print(food_list)