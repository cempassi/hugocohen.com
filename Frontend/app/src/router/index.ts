import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/pages/Home.vue";
import About from "@/components/pages/About.vue";
import VideoView from "@/components/pages/Video.vue";
import DisplayVideo from "@/components/pages/DisplayVideo.vue";

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
      path: "/video",
      name: "Video",
      component: VideoView,
      children: [
        {
          path: "/video/:id",
          name: "Display Video",
          component: DisplayVideo,
        },
      ],
    },
  ],
});
