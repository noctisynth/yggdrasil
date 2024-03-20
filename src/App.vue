<script setup lang="ts">
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'
import { isLightTheme, useThemeStore } from './stores/theme';
import { usePrimeVue } from 'primevue/config';

const themestore = useThemeStore()
const PrimeVue = usePrimeVue()

onMounted(() => {
  if (themestore.dark && isLightTheme()) {
    themestore.changeTheme(PrimeVue)
  }
})
</script>

<template>
  <RouterView />
</template>

<style scoped></style>
