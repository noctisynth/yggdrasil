<script setup lang="ts">
import { ref } from "vue";
import Avatar from 'primevue/avatar';
import router from "@/router";
import Button from "primevue/button";
import { usePrimeVue } from "primevue/config";
import { useThemeStore } from "@/stores/theme";

const themestore = useThemeStore()
const PrimeVue = usePrimeVue()
const items = ref([
    {
        label: '主页',
        icon: 'pi pi-home',
        command: () => {
            router.push("/")
        }
    },
    {
        label: '索引',
        icon: 'pi pi-list',
        command: () => {
            router.push("/packages")
        }
    },
]);
const active = ref<number>();
let path = router.currentRoute.value.path.toLocaleLowerCase();
if (path.endsWith('/')) {
    path = path.slice(0, -1);
}

if (path === '') {
    active.value = 0;
} else if (path == "/packages") {
    active.value = 1
}
</script>

<template>
    <div class="flex justify-content-between w-full pl-3 pr-3 pb-0 pt-1" style="border: solid #e2e8f0;
    border-width: 0 0 1px 0;
    border-color: transparent transparent #e2e8f0 transparent;">
        <div class="flex align-items-center flex-row gap-3">
            <Avatar label="∞"></Avatar>
            <span>世界树</span>
        </div>
        <div class="flex flex-row">
            <Button @click="themestore.changeTheme(PrimeVue)" v-if="!themestore.dark" icon="pi pi-sun" plain text></Button>
            <Button @click="themestore.changeTheme(PrimeVue)" v-else icon="pi pi-moon" plain text></Button>
            <TabMenu :active-index="active" :model="items"></TabMenu>
        </div>
    </div>
</template>

<style scoped></style>