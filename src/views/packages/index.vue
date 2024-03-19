<script setup lang="ts">
import Header from '@/components/Header.vue';
import packages from '@/scripts/packages';
import Button from 'primevue/button';
import Card from 'primevue/card';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
  <main>
    <Header></Header>
    <div class="p-6">

      <div class="flex w-full align-items-center justify-content-center flex-column">
        <div class="w-full" style="max-width: 890px;">
          <div class="bg-primary-100 border-round flex align-items-center justify-content-between flex-wrap mb-3 p-4">
            <h1>索引列表</h1>
            <InputText v-if="packages.length !== 0" placeholder="搜索" style="max-width: 100%;"></InputText>
          </div>
          <Card v-if="Object.keys(packages).length === 0">
            <template #title>
              <div class="flex justify-content-center">
                此世界树已经燃尽了
              </div>
            </template>
            <template #content>
              <p class="m-0">
                此世界树节点没有录入任何规则包。
              </p>
            </template>
          </Card>
          <div class="flex flex-column gap-3">
            <Card v-for="pkg in packages" :key="pkg.name">
              <template #title>
                <h1 @click="router.push('/packages/' + pkg.name)" class="text-4xl">
                  {{ pkg.name }}
                  <span class="text-base text-gray-400">v{{ pkg.latestVersion }}</span>
                </h1>
              </template>
              <template #subtitle>
                {{ pkg.description }}
              </template>
              <template #footer>
                <Button icon="pi pi-sync" :label="`最后更新: ${pkg.lastUpdate}`" plain text size="small"></Button>
              </template>
            </Card>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
:deep(.p-card .p-card-caption) {
  gap: 0.2rem;
}

:deep(.p-card-content) {
  display: none;
}

:deep(.p-button.p-button-sm) {
  font-size: 0.875rem;
  padding: 0;
}
</style>