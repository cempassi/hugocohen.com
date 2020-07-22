import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import VueAnalytics from "vue-analytics";

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.productionTip = false;
Vue.use(VueAnalytics, {
  id: "UA-173153031-1",
  router,
});

router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.title);
  const nearestWithMeta = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.metaTags);
  const previousNearestWithMeta = from.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.metaTags);

  if (nearestWithTitle) document.title = nearestWithTitle.meta.title;

  Array.from(
    document.querySelectorAll("[data-vue-router-controlled]")
  ).map((el) => el.parentNode?.removeChild(el));

  if (!nearestWithMeta) return next();

  nearestWithMeta.meta.metaTags
    .map((tagDef) => {
      const tag = document.createElement("meta");

      Object.keys(tagDef).forEach((key) => {
        tag.setAttribute(key, tagDef[key]);
      });
      tag.setAttribute("data-cue-router-controlled", "");

      return tag;
    })
    .forEach((tag) => document.head.appendChild(tag));

  next();
});

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
