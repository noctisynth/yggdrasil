import "primeflex/primeflex.min.css";
import "primeicons/primeicons.css";
import "@/assets/markdown.css"

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import TabMenu from "primevue/tabmenu";
import Toolbar from "primevue/toolbar";
import Listbox from "primevue/listbox";
import Button from "primevue/button";
import Card from "primevue/card";

const app = createApp(App);

app.use(PrimeVue);
app.use(router);

app.component("Toast", Toast);
app.component("TabMenu", TabMenu);
app.component("Toolbar", Toolbar);
app.component("Listbox", Listbox);
app.component("Button", Button);
app.component("Card", Card);
app.use(ToastService);

app.mount("#app");
