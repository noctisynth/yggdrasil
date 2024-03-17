<script setup lang="ts">
import Header from '@/components/Header.vue';
import MarkdownIt from 'markdown-it';
import jsonData from './index.json';
import Card from 'primevue/card';
import Button from 'primevue/button';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Panel from 'primevue/panel';

const md = new MarkdownIt();

md.render(jsonData.readme)
</script>

<template>
    <main>
        <Header></Header>
        <div class="w-full flex align-items-center justify-content-center">
            <div class="w-full flex flex-column align-items-start justify-content-center p-6 gap-6"
                style="max-width: 960px;">
                <Card class="w-full">
                    <template #title>
                        <div class="header gap-3 align-items-center justify-content-between">
                            <h1 class="text-5xl">
                                {{ jsonData.metadata.name }}
                                <span class="text-base text-gray-400">v{{ jsonData.metadata.version }}</span>
                            </h1>
                            <Button icon="pi pi-github" plain text></Button>
                        </div>
                    </template>
                    <template #content>
                        <p class="mt-0">
                            {{ jsonData.metadata.description }}
                        </p>
                    </template>
                </Card>

                <TabView class="w-full">
                    <TabPanel header="自述">
                        <div class="readme pt-2">
                            <div>
                                <Card>
                                    <template #content>
                                        <div v-html="md.render(jsonData.readme)"></div>
                                    </template>
                                </Card>
                            </div>
                            <div class="p-3 pt-2 pr-0">
                                <div>
                                    <h2 class="pl-2 text-lg">元数据</h2>
                                    <div class="flex flex-column align-items-start pb-1">
                                        <Button icon="pi pi-calendar-plus" :label="'now'" plain text></Button>
                                        <Button plain text>
                                            <div class="flex flex-row flex-wrap gap-2">
                                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                                                    viewBox="0 0 100 100" width="17" height="17">
                                                    <path
                                                        d="M40 62.5h-.003c0-2.528.21-1.364-13.29-28.36-2.757-5.515-10.654-5.526-13.416 0C-.322 61.366.003 60.051.003 62.5H0C0 69.403 8.955 75 20 75s20-5.597 20-12.5zm-20-25L31.25 60H8.75zm79.997 25c0-2.528.21-1.364-13.29-28.36-2.757-5.515-10.654-5.526-13.416 0C59.678 61.366 60.003 60.051 60.003 62.5H60C60 69.403 68.955 75 80 75s20-5.597 20-12.5zM68.75 60L80 37.5 91.25 60zM82.5 80H55V33.945c3.673-1.608 6.431-4.918 7.248-8.945H82.5a2.5 2.5 0 002.5-2.5v-5a2.5 2.5 0 00-2.5-2.5H59.944c-2.282-3.019-5.867-5-9.944-5-4.077 0-7.662 1.981-9.944 5H17.5a2.5 2.5 0 00-2.5 2.5v5a2.5 2.5 0 002.5 2.5h20.252c.817 4.025 3.573 7.337 7.248 8.945V80H17.5a2.5 2.5 0 00-2.5 2.5v5a2.5 2.5 0 002.5 2.5h65a2.5 2.5 0 002.5-2.5v-5a2.5 2.5 0 00-2.5-2.5z">
                                                    </path>
                                                </svg>
                                                <span class="text-cascadia">
                                                    {{ jsonData.metadata.license }}
                                                </span>
                                            </div>
                                        </Button>
                                    </div>
                                </div>
                                <div>
                                    <h2 class="pl-2 text-lg">安装</h2>
                                    <div class="flex flex-column align-items-start pb-1 pt-1 p-3 gap-3">
                                        <Panel header="IPM 安装" class="w-full">
                                            <p class="m-0">
                                                <code class="text-cascadia p-2 border-round"
                                                    style="background-color: var(--highlight-bg);">ipm add {{ jsonData.metadata.name
                                    }}</code>
                                            </p>
                                        </Panel>
                                        <Panel header="使用 infini.toml" class="w-full">
                                            <p class="m-0">
                                                <code class="text-cascadia p-2 border-round"
                                                    style="background-color: var(--highlight-bg);">{{ jsonData.metadata.name
                                    }} = {{ jsonData.metadata.version }}</code>
                                            </p>
                                        </Panel>
                                    </div>
                                </div>
                                <div>
                                    <h2 class="pl-2 text-lg">作者</h2>
                                    <div class="flex flex-column align-items-start pb-1 pt-1 p-3 gap-3">
                                        <div v-for="author in jsonData.metadata.authors">
                                            <Button icon="pi pi-user" :label="author.name" plain text></Button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </TabPanel>
                    <TabPanel header="指令文档"></TabPanel>
                </TabView>
            </div>
        </div>
    </main>
</template>

<style scoped>
.header {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    margin: 0;
    padding: 0;
    word-break: break-word;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-weight: bold;
}

.text-cascadia {
    font-family: 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

@media only screen and (min-width: 890px) {
    .readme {
        display: grid;
        grid-template-columns: minmax(0, 7fr) minmax(0, 3fr);
    }
}
</style>
