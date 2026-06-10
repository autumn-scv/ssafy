<template>
  <div class="router-content">
    <div class="title-content">
      <h1>제목</h1>
    </div>
    <div>
      <p class="main-content-description">설명</p>
      <div class="main-graph-content">
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
  .router-content {
    border: 1px solid var(--border-color);
    border-radius: 12px;
    margin: 30px 20px;
    min-height: 500px;
  }
  .title-content {
    text-align: center;
  }
  .main-content-description {
    text-align: center;
    font-size: 15px;
  }
  .main-graph-content {
    width: 90%;
    margin: 10px auto 30px;

    display: flex;
    justify-content: center;
    align-items: center;

    border: 1px solid var(--border-color);
    min-height: 100px;
  }
</style>