<template>
    <div>
        <li>{{ productData.name }} - {{ productData.price }}</li>
    </div>
</template>

<script setup>
defineProps({
    productData: Object
})
</script>

<style scoped>

</style>