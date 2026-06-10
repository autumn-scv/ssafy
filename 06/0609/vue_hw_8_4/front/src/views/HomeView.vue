<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{ name: 'create' }">
      <button>게시글 생성</button>
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '../components/ArticleList.vue';
</script>

<style lang="scss" scoped>

</style>