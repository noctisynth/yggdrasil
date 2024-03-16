<script setup lang="ts">
import Header from '@/components/Header.vue';
import packages from '@/scripts/packages';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
  <main>
    <Header></Header>
    <div class="p-6">
      <div class="flex align-items-center justify-content-between flex-wrap mb-3 m-1">
        <h1>索引列表</h1>
        <InputText v-if="packages.length !== 0" placeholder="搜索"></InputText>
      </div>
      <Listbox :options="packages" class="border-none" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);">
        <template #empty>
          <div>
            此世界树已经燃尽了。
          </div>
        </template>
        <template #header>
          <div class="flex align-items-center justify-content-between p-3 font-bold" style="border: solid #e2e8f0;
    border-width: 0 0 1px 0;
    border-color: transparent transparent #e2e8f0 transparent;">
            <div>规则包</div>
            <div>最新版本</div>
            <div>最后更新</div>
          </div>
        </template>
        <template #option="slot">
          <div class="flex align-items-center justify-content-between gap-3">
            <div><Button @click="router.push('/packages/' + slot.option.name)" :label="slot.option.name" class="pl-0"
                plain text></Button></div>
            <div>{{ slot.option.latestVersion }}</div>
            <div>{{ slot.option.lastUpdate }}</div>
          </div>
        </template>
      </Listbox>
    </div>
  </main>
</template>

<style scoped></style>