import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/pages/Home.vue";
import AboutView from "@/components/pages/About.vue";
import VideoView from "@/components/pages/Video.vue";
import PhotoView from "@/components/pages/Photo.vue";
import DisplayVideo from "@/components/pages/DisplayVideo.vue";
import DisplayPhoto from "@/components/pages/DisplayPhoto.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Hello",
      component: Home,
      meta: {
        title: "Home - Hugo Cohen",
        metaTags: [
          {
            name: "description",
            content: "The Home page of Hugo Cohen's websiste.",
          },
          {
            property: "og:description",
            content: "The Home page of Hugo Cohen's website.",
          },
        ],
      },
    },
    {
      path: "/about",
      name: "About",
      component: AboutView,
      meta: {
        title: "About - Hugo Cohen",
        metaTags: [
          {
            name: "description",
            content: "The About page of Hugo Cohen's websiste.",
          },
          {
            property: "og:description",
            content: "The About page of Hugo Cohen's websiste.",
          },
        ],
      },
    },
    {
      path: "/photo",
      name: "Photo",
      component: PhotoView,
      meta: {
        title: "Photos - Hugo Cohen",
        metaTags: [
          {
            name: "description",
            content: "Hugo Cohen's photo albums.",
          },
          {
            property: "og:description",
            content: "Hugo Cohen's photo albums.",
          },
        ],
      },
    },
    {
      path: "/photo/:albumName",
      name: "DisplayPhoto",
      component: DisplayPhoto,
      props: true,
      meta: {
        title: "Photos - Hugo Cohen",
        metaTags: [
          {
            name: "description",
            content: "A photo album of Hugo Cohen.",
          },
        ],
      },
    },
    {
      path: "/video",
      name: "Video",
      component: VideoView,
      meta: {
        title: "Videos - Hugo Cohen",
        metaTags: [
          {
            name: "description",
            content: "The Videos of Hugo Cohen.",
          },
          {
            property: "og:description",
            content: "The Videos of Hugo Cohen.",
          },
        ],
      },
    },
    {
      path: "/video/:id",
      name: "Display Video",
      props: true,
      component: DisplayVideo,
      meta: {
        title: "Video - Hugo Cohen'",
        metaTags: [
          {
            name: "description",
            content: "A Video by Hugo Cohen.",
          },
        ],
      },
    },
  ],
});
