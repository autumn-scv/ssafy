# 데이터 추출 예시

# 주식 정보를 담은 딕셔너리들의 리스트
# 각 딕셔너리는 회사명(name)과 주가(price)를 키로 가짐
# 마지막 '토스'는 price 키가 없는 비상장 기업
stocks = [
    {'name': '삼성전자', 'price': '78,000'},
    {'name': 'SK하이닉스', 'price': '124,500'},
    {'name': '삼성전자우', 'price': '70,900'},
    {'name': '삼성바이오로직스', 'price': '836,000'},
    {'name': 'NAVER', 'price': '335,000'},
    {'name': 'LG화학', 'price': '710,000'},
    {'name': '현대차', 'price': '209,500'},
    {'name': '카카오', 'price': '96,600'},
    {'name': '삼성SDI', 'price': '624,000'},
    {'name': '기아', 'price': '83,800'},
    {'name': 'POSCO', 'price': '304,000'},
    {'name': '셀트리온', 'price': '187,000'},
    {'name': '현대모비스', 'price': '262,000'},
    {'name': '카카오뱅크', 'price': '51,100'},
    {'name': 'KB금융', 'price': '57,800'},
    {'name': 'SK이노베이션', 'price': '246,000'},
    {'name': '삼성물산', 'price': '115,000'},
    {'name': 'LG전자', 'price': '130,000'},
    {'name': '신한지주', 'price': '38,550'},
    {'name': '카카오페이', 'price': '148,500'},
    {'name': '토스'},  # price 키가 없는 딕셔너리
]

# 방법 1: get() 메서드 기본 사용
# price 키가 없는 경우 None 반환
for stock in stocks:
    print(stock.get('price'))

# 방법 2: get() 메서드에 기본값 설정
# price 키가 없는 경우 '비상장 주식입니다.' 반환
for stock in stocks:
    print(stock.get('price', '비상장 주식입니다.'))
