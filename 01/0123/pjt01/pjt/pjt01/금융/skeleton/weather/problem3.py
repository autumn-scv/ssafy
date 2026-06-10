import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
    # feels_like : '체감온도',
    # humidity : '습도',
    # pressure : '기압',
    # temp : '온도',
    # temp_max : '최고온도',
    # temp_min : '최저온도',
    # description : '요약',
    # icon : '아이콘',
    # main : '핵심’
    # id : ‘식별자’

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
