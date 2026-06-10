<template>
  <div>
    <h3>자식 페이지</h3>
    <p>{{ childData.name }}</p>
  </div>
</template>

<script setup>
defineProps({
    childData: Object
})
</script>

<style scoped>
div {
  border: 1px solid #eee;     
  padding: 15px;               
  margin: 15px 0;              
  background-color: #fafafa;   
  border-radius: 4px;           
}

h5 {
  margin: 0 0 8px 0;        
  font-size: 1.1rem;
  color: #333;
}

p {
  margin: 0;
  color: #666;
}
</style>