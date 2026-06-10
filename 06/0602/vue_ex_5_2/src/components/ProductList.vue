<template>
  <ul>
    <ProductListItem 
      v-for="(product, index) in products" 
      :key="index" 
      :product-data="product" 
    />
  </ul>
</template>

<script setup>
import ProductListItem from './ProductListItem.vue'

defineProps({
  products: Array
})
</script>