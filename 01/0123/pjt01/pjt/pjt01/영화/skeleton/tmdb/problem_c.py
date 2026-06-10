import json
from pprint import pprint


def movies_info(movies, genres):
    pass
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    movies_json = open(current_dir / 'data' / 'movies.json', 'r', encoding='utf-8')
    movies = json.load(movies_json)

    genres_json = open(current_dir / 'data' / 'genres.json', 'r', encoding='utf-8')
    genres = json.load(genres_json)

    pprint(movies_info(movies, genres))
