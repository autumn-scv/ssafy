import requests
from pprint import pprint

# 문제2. 날씨 데이터 중 다음 조건에 해당하는 값만 딕셔너리 형태로 반환하는 함수를 구성합니다.
#   KEY 값이“main” 인 데이터
#   KEY 값이 “weather” 인 데이터
# 함수에서 두 데이터를 새로운 dictionary 에 담아서 return 합니다.

def get_result(api_key):
    
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    return result

# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = 'MY_API_KEY'

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)
