/* 
  fetchAlbums 함수를 완성합니다. fetchAlbums 함수는 아래의 조건을 만족해야합니다. 
검색창에 해당하는 input 태그는 search-box__input 클래스를 가지고 있습니다. 선택자를 이용하여 해당 요소의 value 값을 가져온 뒤 keyword라는 이름의 변수에 저장합니다.
사용자가 입력한 검색어(keyword)를 포함하여 앨범 검색 요청을 보냅니다. 
(참고 문서) https://www.last.fm/api/show/album.search
앨범 검색을 위한 ajax 요청에는 axios를 활용합니다.
요청이 성공했을 경우 응답 결과에서 앨범 리스트만 뽑아서 albums라는 변수에 저장합니다.
요청이 실패했을 경우 alert()를 이용하여 잠시 후 다시 시도해주세요 라는 메세지를 출력합니다.
*/

const searchBtn = document.querySelector('.search-box__button') 

function fetchAlbums(page = 1, limit = 10){
  const keyword = document.querySelector('.search-box__input').value
  const API_KEY = '4fe82dbf950c10abed440655f440d9ce'
  const URL = 'https://ws.audioscrobbler.com/2.0/'
  axios({
    method: 'GET',
    url: URL,
    params: {
      method: 'album.search',
      album: keyword,
      api_key: API_KEY,
      page: page,
      limit: limit,
      format: 'json'
    }
  }).then((response)=> {
    const albums = response.data.results.albummatches.album
    console.log(albums)
  })
  .catch((error)=> {
    alert('잠시 후 다시 시도해주세요')
    console.error(error)
  })
}
searchBtn.addEventListener('click',()=>{
  fetchAlbums()
})





