<template>
  <li>
    {{ productData.name }} - {{ productData.price }}원
    <button>장바구니에 추가</button>
  </li>
</template>

<script setup>
defineProps({
  productData: Object
})
</script>