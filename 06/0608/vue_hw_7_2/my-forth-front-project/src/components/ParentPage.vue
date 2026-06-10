<template>
  <div>
    <h3>부모 컴포넌트</h3>
    <p>{{ familyData.father }}</p>
    <p>{{ familyData.mother }}</p>
    <ChildPage v-for="(child, index) in familyData.children" :key="index" :child-data="child"/>
  </div>
</template>

<script setup>

import ChildPage from './ChildPage.vue';
defineProps({
    familyData: Object
})

</script>

<style scoped>

</style>