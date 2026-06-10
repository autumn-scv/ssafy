<template>
  <div>
    <div v-for="article in articles" :key="article.pk" class="article-item">
      <h5>{{ article.pk }}번 게시글</h5>
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
import { storeToRefs } from 'pinia'

const store = useArticleStore()
const { articles } = storeToRefs(store)
onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>