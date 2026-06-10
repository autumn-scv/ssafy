<template>
    <div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 10px; ">
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ childData.name }}</p>
        <p>나이 : {{ childData.age  }}</p>
    </div>
</template>

<script setup>
defineProps({
    childData: Object
})
</script>

<style scoped>

</style>