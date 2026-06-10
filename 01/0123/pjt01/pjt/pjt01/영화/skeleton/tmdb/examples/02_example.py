# 데이터 추출 및 생성 예시

# 영화 정보를 담은 딕셔너리
# genre_ids: 장르 ID 리스트
# id: 영화 고유 ID
# original_title: 영화 원제
# release_date: 개봉일
# title: 한글 제목
# vote_average: 평점
movie = {
    'genre_ids': [18, 80],
    'id': 278,
    'original_title': 'The Shawshank Redemption',
    'release_date': '1995-01-28',
    'title': '쇼생크 탈출',
    'vote_average': 8.7,
}


def make_dict(data):
    """
    영화 데이터에서 원하는 정보만 추출하여 새로운 딕셔너리 생성

    Args:
        data (dict): 원본 영화 정보 딕셔너리

    Returns:
        dict: 필요한 정보만 담긴 새 딕셔너리
    """
    new_data = {
        '원제': data.get('original_title'),  # 영화 원제 추출
        '개봉년도': data.get('release_date')[:4],  # 개봉일에서 연도만 슬라이싱
        '평점': data.get('vote_average'),  # 평점 추출
    }
    return new_data


# 새로운 형식의 딕셔너리 출력
print(make_dict(movie))
