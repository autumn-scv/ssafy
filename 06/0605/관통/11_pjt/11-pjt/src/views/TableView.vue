<template>
<<<<<<< 11-pjt/src/views/TableView.vue
  <div>
    <h1>데이터 확인용 테이블</h1>
    <AgeCharTable v-if="pets.length > 0" :items="pets" />
    <p v-else>데이터를 불러오는 중입니다...</p>
=======
  <div class="router-content">
    <div class="title-content">
      <h1>제목</h1>
    </div>
    <div>
      <p class="main-content-description">설명</p>
      <div class="main-graph-content">
      </div>
    </div>
>>>>>>> 11-pjt/src/views/TableView.vue
  </div>
</template>

<script setup>
<<<<<<< 11-pjt/src/views/TableView.vue
import { ref, onMounted } from 'vue';
import { getTableData } from '@/services/dataService'; 
import AgeCharTable from '@/components/AgeCharTable.vue';

const pets = ref([]);

onMounted(async () => {
  const data = await getTableData();
  console.log("데이터 확인:", data); 
  pets.value = data;
});

=======

</script>

<style scoped>
  .router-content {
    border: 1px solid lightgray;
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

    border: 1px solid lightgray;
    min-height: 100px;
  }
</style>
>>>>>>> 11-pjt/src/views/TableView.vue
