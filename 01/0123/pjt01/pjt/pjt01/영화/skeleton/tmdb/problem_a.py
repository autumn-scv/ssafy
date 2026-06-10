import json
from pprint import pprint


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    movie_json = open(current_dir / 'data' / 'movie.json', 'r', encoding='utf-8')
    movie = json.load(movie_json)

    pprint(movie_info(movie))
