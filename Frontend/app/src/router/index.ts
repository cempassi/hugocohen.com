import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/pages/Home.vue";
import About from "@/components/pages/About.vue";
import Works from "@/components/pages/Works.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Hello",
      component: Home,
    },
    {
      path: "/about",
      name: "About",
      component: About,
    },
    {
      path: "/works",
      name: "Works",
      component: Works,
    },
  ],
});
