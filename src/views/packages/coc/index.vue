<script setup lang="ts">
import Header from '@/components/Header.vue';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
    <main>
        <Header></Header>
        <div class="p-6">
            <div class="flex align-items-center justify-content-between flex-wrap mb-3 m-1">
                <h1>COC规则包</h1>
            </div>
        </div>
    </main>
</template>

<style scoped></style>