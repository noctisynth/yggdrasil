import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { type RouteRecordRaw } from "vue-router";

const views = import.meta.glob([
  "../views/**/index.vue",
  "../views/**/\\[*\\].vue",
]);

const routes: RouteRecordRaw[] = Object.entries(views).map(
  ([filePath, component]) => {
    let path = filePath.replace(/^\.\.\/views\//, "");
    path = path.replace(/^(.+)\/index\.vue$/, "$1");
    path = path.replace(/\[(\w+)\]\.vue$/, ":$1");
    path = "/" + path;

    return {
      path,
      name: filePath.replace(/^\.\.\/views\//, ""),
      component,
    } satisfies RouteRecordRaw;
  }
);

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    ...routes,
  ],
});

export default router;
