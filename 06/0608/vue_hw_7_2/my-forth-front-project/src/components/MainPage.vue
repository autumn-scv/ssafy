<template>
    <h1>pinia 연습하기</h1>
  <div>
    <ParentPage v-for="(family, index) in store.familyInfo" :key="index" :family-data="family"/>
  </div>
</template>

<script setup>
import { useFamilyStore } from '@/stores/family.js';
import ParentPage from './ParentPage.vue';

const store = useFamilyStore()
</script>

<style scoped>
div {
  border: 1px solid #ddd;     
  padding: 20px;             
  margin: 20px auto;            
  max-width: 600px;             
  background-color: #ffffff;   
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); 
  text-align: center;           
}

h3 {
  margin-top: 0;               
  font-size: 1.3rem;
}

p {
  margin: 5px 0;                
  color: #555;
}
</style>