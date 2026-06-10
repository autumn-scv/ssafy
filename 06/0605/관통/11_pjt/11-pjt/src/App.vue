<template>
  <div class="app-container">
    <div class="mode-div">
      <button class="btn-style" @click="toggleDarkMode">
        {{ isDark ? "라이트 모드" : "다크 모드" }}
      </button>
    </div>
    <header class="header-container">
      <h1>데이터 분석</h1>
    </header>
    <p class="head-p-tag">원하시는 네비를 선택하세요!</p>
    <div class="nav-container">
      <span> | </span>
      <RouterLink :to="{name:'table'}">Table</RouterLink>
      <span> | </span>
      <RouterLink :to="{name:'2d'}">2D-graph</RouterLink>
      <span> | </span>
      <RouterLink :to="{name:'3d'}">3D-graph</RouterLink>
      <span> | </span>
    </div>
    <RouterView/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';

const isDark = ref(false)

const toggleDarkMode = () => {
  isDark.value = !isDark.value

  if (isDark.value) {
    document.body.classList.add('dark')
  } else {
    document.body.classList.remove('dark')
  }
}



</script>

<style scoped>
.app-container {
  padding: 50px;
  max-width: 850px;
  background-color: var(--box-bg);
  transition: background-color 0.3s ease;
  margin: 60px auto;
  border-radius: 16px;
  min-height: 800px;
}
.btn-style {
  padding: 2px 8px;
  border-radius: 6px;
  background-color: var(--box-bg);
  color: var(--text-color);
  transition: background-color 0.3s ease, color 0.3s ease;
}
.mode-div {
  display: flex;
  justify-content: right;
  color: white;
}
.header-container {
  text-align: center;
  padding-top: 30px;
  padding-bottom: 5px;
}
.head-p-tag {
  text-align: center;
}
.nav-container {
  background-color: var(--nav-bg);
  border: 1px solid var(--border-color);
  margin: 15px 20px;
  padding: 8px;
  border-radius: 12px;
  text-align: center;
}
.nav-container span {
  color: white;
  padding: 0 25px;
}
.nav-container a {
  color: white;
  text-decoration: none;
}
</style>