<template>
        <table>
            <thead>
                <tr>
                    <th>종류</th>
                    <th>나이</th>
                    <th>비용</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(pet, index) in items" :key="index">
                    <td>{{ pet.pet_type }}</td>
                    <td>{{ pet.age_years }}세</td>
                    <td>{{ pet.monthly_care_cost_krw.toLocaleString() }}원</td>
                </tr>
            </tbody>
        </table>
</template>

<script setup>
const props = defineProps(['items'])
</script>

<style scoped>

</style>