<script setup lang="ts">
import Header from '@/components/Header.vue';
import InputText from 'primevue/inputtext';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import Divider from 'primevue/divider';
import { useThemeStore } from '@/stores/theme';

const themestore = useThemeStore()
</script>

<template>
    <main>
        <Header></Header>
        <div :class="`${themestore.bg_class} p-8 pt-7 mt-0 flex align-items-center justify-content-center mb-3 flex-column`">
            <div class="flex flex-column text-white pb-7 align-items-center justify-content-center">
                <h1>世界树</h1>
                <span>Infini 社区的规则包服务器, 此节点由浊莲提供服务</span>
            </div>
            <div>
                <IconField>
                    <InputIcon class="pi pi-search"> </InputIcon>
                    <InputText placeholder="规则包搜索" class="border-round-2xl"></InputText>
                </IconField>
            </div>
        </div>
        <div class="flex align-items-center justify-content-center flex-column">
            <div style="max-width: 960px;">
                <div class="flex p-4 pb-5 gap-8 align-items-center justify-content-center">
                    <Button label="安装 IPM" rounded></Button>
                    <Button label="开始使用" rounded></Button>
                </div>
                <div class="w-full" style="border: 0.15rem solid #d5d3cb;"></div>
                <Card class="pt-2 mt-6 m-3" style="max-width: 960px;">
                    <template #title>世界树</template>
                    <template #content>
                        <p class="mb-0">
                            你可以立即发布您的规则包并使用 IPM 安装它们。
                            成为一个贡献者，用你的工作来完善世界树站点。
                            社区会铭记你的贡献。
                        </p>
                    </template>
                </Card>
            </div>
        </div>
        <div :class="`${themestore.bg_class}`">
            <div class="p-8 pt-7 mt-6 flex align-items-center justify-content-between mb-3 flex-row flex-wrap gap-7">
                <div class="flex flex-column text-white align-items-start justify-content-center">
                    <h3 class="pl-3">帮助</h3>
                    <Button icon="pi pi-book" label="Infini 文档" plain text></Button>
                    <Button icon="pi pi-book" label="IPM 文档" plain text></Button>
                </div>
                <div class="flex flex-column text-white align-items-start justify-content-center">
                    <h3 class="pl-3">联系</h3>
                    <Button icon="pi pi-link" label="夜骰公测群" plain text></Button>
                    <Button icon="pi pi-link" label="水系公测群" plain text></Button>
                </div>
                <div class="flex flex-column text-white align-items-start justify-content-center">
                    <h3 class="pl-3">项目</h3>
                    <Button icon="pi pi-github" label="HydroRoll-Team/infini" plain text></Button>
                    <Button icon="pi pi-github" label="HydroRoll-Team/ipm" plain text></Button>
                </div>
            </div>
            <Divider class="mb-0"></Divider>
            <div class="flex align-items-center justify-content-center p-7 text-white">
                <span>Copyright © 2011-PRESENT Noctisynth, org</span>
            </div>
        </div>
    </main>
</template>

<style scoped></style>