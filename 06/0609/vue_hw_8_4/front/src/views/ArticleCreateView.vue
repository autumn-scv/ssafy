<template>
    
    <h1>게시글 생성 페이지</h1>
    <form>
    <div>
        제목:<input type="text" v-model="title">
        내용:<input type="text" v-model="content">
        <button type="submit" @click="createArticle">create</button>
    </div></form>
</template>

<script setup>
import { useArticleStore } from '../stores/articles';
import { ref } from 'vue'
const store = useArticleStore()
const title = ref('')
const content = ref('')
const createArticle = function() {
    if (!title.value || !content.value) {
        alert('입력이 되지 않은 칸이 있습니다.')
    return
    }
   store.createArticle(title.value, content.value) 
}

</script>

<style scoped>

</style> 