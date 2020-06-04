import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/pages/Home.vue";
import About from "@/components/pages/About.vue";
import VideoView from "@/components/pages/Video.vue";
import PhotoView from "@/components/pages/Photo.vue";
import DisplayVideo from "@/components/pages/DisplayVideo.vue";
import DisplayPhoto from "@/components/pages/DisplayPhoto.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Hello",
      component: Home,
      meta: { title: "Home" },
    },
    {
      path: "/about",
      name: "About",
      component: About,
      meta: { title: "About" },
    },
    {
      path: "/photo",
      name: "Photo",
      component: PhotoView,
      meta: { title: "Photo" },
      children: [
        {
          path: "/photo/:id",
          name: "Display Photo",
          component: DisplayPhoto,
          meta: { title: "DisplayPhoto" },
        },
      ],
    },
    {
      path: "/video",
      name: "Video",
      component: VideoView,
      meta: { title: "Video" },
      children: [
        {
          path: "/video/:id",
          name: "Display Video",
          component: DisplayVideo,
          meta: { title: "DisplayVideo" },
        },
      ],
    },
  ],
});
