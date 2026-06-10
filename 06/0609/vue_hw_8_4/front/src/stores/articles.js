import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const router = useRouter()
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => {
      articles.value = res.data
    })
    .catch((err) => console.log(err)) 
  } 

  const createArticle = function (title, content) {
    axios({
      method: 'post', 
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,  
        content 
      }
    })
    .then((res) => {
      console.log('생성 완료:', res.data)
      getArticles() 
      router.push({ name: 'HomeView' }) 
    })
    .catch((err) => console.log(err))
  }

  return { articles, getArticles, createArticle }
}, 
{ persist: true }
)