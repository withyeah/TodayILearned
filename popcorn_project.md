# popcorn_project

대전 2반 김예랑, 김호영

> 영화 추천 사이트 어쩌구



## 20190509

- 사이트 구상
  - OAuth
  - 디테일
    - 평점
    - comment
    - 영화정보
  - 영화추천(filter by genre, 국가, (평점순))

- 데이터 어디서 가져올까

  - 영진위
  - 네이버영화
  - TMDB (여기로 선택)

- 데이터 가져오기

  1. API getting started :  <https://developers.themoviedb.org/3/getting-started/authentication> 
  2. Get a list of the current popular movies on TMDb : 이유> query string으로 page 줄 수 있어서! <https://developers.themoviedb.org/3/movies/get-popular-movies>

- c9에서 기본 세팅

  - pyenv, virtualenv <https://gist.github.com/edujunho/bee20c196ecacc3e8cdf068b4ec64d9f>

    ```shell
    $ pip install Django ==2.1.8
    $ pip install requests
    $ pip install pprint
    ```

  - 

사용한 도구들

- tmdb api > api 



- 크롤링

- ```python
  import requests
  import json
  from pprint import pprint
  
  # 200 개 가져오기
  result = []
  
  for i in range(1):
      pageNum = i + 1
      url = f'https://api.themoviedb.org/3/movie/popular?<<api_key>>&region=^KR$&language=ko-KR&page={pageNum}'
      data = requests.get(url).json()
      movieData = data['results']
      for movie in movieData:
          movie['poster_path'] = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
          result.append(movie)
  
  with open('data.json', 'w') as outfile:
      json.dump(result, outfile, ensure_ascii = False)       
  # jsonData = json.dumps(result, ensure_ascii = False)
  # pprint(jsonData)
  
  ```

  - page 기준으로 쿼리 불러올 수 있기 때문에 for문 돌면서 필요한 페이지 양 만큼 불러옴( 1페이지에 영화 20개)
  - url : base url 에 발급받은 api key 넣음
  - requests.get(url).json() > json : json 요청 받음
  - pprint 로 구조 찍어보고 필요한 부분(영화)만 변수에 할당(movieData)
  - 현재 movieData 에는 20개의 영화가 담겨있는데 poster_path 가 / 뒤의 주소만 있어서 이미지 url을 불러올 수 없음 >> 구글링
  - TMDb getting started - image <https://developers.themoviedb.org/3/getting-started/images> 문서 보니까 base url + 사이즈 + poster_path 붙이면 된다고 함
  - 그래서 movieData의 20개 영화 돌면서 poster_path를 image url로 수정, 결과 값에 append
  - result에 json 형태로 저장됨
  - with open~ json 파일로 쓰기

- 장고 모델링

- JSON > DB

  -  json > sql/csv : <https://sqlify.io/convert>

    - 한 영화에 장르가 2개 이상인 경우 convert 시 에러 발생

  - DB에 정보 넣을 때 csv로 할 지 sql로 할 지 고민고민

  - json > csv : <http://convertcsv.com/json-to-csv.htm> (장르가 복수일 때 자동으로 genre1 genre2 이런 식으로 컬럼을 생성해줌) 여기로 선택

  - 터미널에서 sqlite3이용해서 table 생성

    ```sqlite
    > .mode csv
    > .import multi-genre.csv movies
    > .tables
    > .schema
    ```

    

- 스키마 확인
  - <https://stackoverflow.com/questions/4654762/how-can-one-see-the-structure-of-a-table-in-sqlite>
  - `.schema [tablename]`
- admin 들어가서 확인 > ? 영화가 하나도 없음

,.ㅁㄴ우히맞둫;ㅣㅁㅈ둫;미ㅏㅈ둫밎닿'ㅈㄷ

`db와의 싸움`

문제는 admin > list_display 길이가 너무 길어서,.,,,string index out of range 뜸

후