# 데이터 추출 및 생성 예시

# Spotify API에서 받아온 아티스트 정보를 담은 딕셔너리
# id: 아티스트 고유 ID
# name: 아티스트 이름
# type: 데이터 유형
# uri: Spotify 리소스 식별자
# genres_ids: 장르 ID 리스트
artist = {
    'id': 427,
    'name': 'LE SSERAFIM',
    'type': 'artist',
    'uri': 'spotify:artist:4SpbR6yFEvexJuaBpgAU5p',
    'genres_ids': [84, 580, 696, 674, 108],
}


def make_dict(data):
    """
    아티스트 데이터에서 필요한 정보만 추출하여 새로운 딕셔너리 생성

    Args:
        data (dict): 원본 아티스트 정보 딕셔너리

    Returns:
        dict: 가공된 새 딕셔너리
    """
    new_data = {
        '이름': data.get('name'),  # 아티스트 이름
        '타입': data.get('type'),  # 데이터 유형
        'URI-0': data.get('uri').split(':')[
            0
        ],  # URI를 ':'로 분리하여 첫 부분만 추출
    }
    return new_data


# 새로운 형식의 딕셔너리 출력
print(make_dict(artist))
