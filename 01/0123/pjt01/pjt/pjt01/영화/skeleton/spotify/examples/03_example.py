# open 및 json 모듈 사용예시

# JSON 형식의 파일을 처리하기 위한 내장 모듈
import json

# 파일 시스템 경로를 객체 지향적으로 다루기 위한 모듈
from pathlib import Path

# 현재 실행 중인 파일의 절대 경로를 기준으로 부모 디렉토리 경로 설정
# - Path(__file__): 현재 파일의 경로를 Path 객체로 변환
# - resolve(): 실제 경로로 변환하고 절대 경로를 반환
# - parent: 부모 디렉토리 경로를 반환
current_dir = Path(__file__).resolve().parent


# 파일 열기
# open('파일경로', encoding='인코딩방식')
# - current_dir / 'sample.json': Path 객체의 / 연산자로 경로 결합
# - encoding="utf-8"은 한글 등 유니코드 문자를 올바르게 처리하기 위한 설정
artist = open(current_dir / 'sample.json', encoding='utf-8')

# json.load()로 JSON 파일의 내용을 파이썬 데이터로 변환
# - JSON의 object → 파이썬 딕셔너리
# - JSON의 array → 파이썬 리스트
# - JSON의 string → 파이썬 문자열
# - JSON의 number → 파이썬 정수/실수
artist_detail = json.load(artist)

# 변환된 파이썬 데이터 출력
print(artist_detail)
# 파이썬 딕셔너리로 변환됨을 확인
print(type(artist_detail))
