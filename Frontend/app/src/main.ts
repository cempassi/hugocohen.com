import "./class-component-hooks";
import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import VueAnalytics from "vue-analytics";
import Meta from "vue-meta";

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.productionTip = false;
Vue.use(Meta);

Vue.use(VueAnalytics, {
  id: "UA-173153031-1",
  router,
});


new Vue({ router, store, render: (h) => h(App) }).$mount("#app");
