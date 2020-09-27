<template>
  <main class="layout">
    <div class="video">
      <video class="video-vid" autoplay loop muted playsinline>
        <source type="video/mp4" src="@/assets/about.mp4" />Video isn't working
      </video>
    </div>
    <div class="content">
      <p class="content-bio">{{about.about}}</p>
    </div>
    <div class="clients">
      <p class="clients-text">{{about.clients}}</p>
    </div>
    <div class="links">
      <a :href="mail.link">
        <font-awesome-icon :icon="mail.icon"></font-awesome-icon>
      </a>
      <a :href="insta.link">
        <font-awesome-icon :icon="insta.icon"></font-awesome-icon>
      </a>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Navbar from "@/components/Navbar.vue";
import { faEnvelope } from "@fortawesome/free-regular-svg-icons";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";
import About from "@/models/About";
import { AboutAPI } from "@/api/AboutAPI";

@Component({
  name: "About",
  metaInfo: {
    title: "About",
  },
})
export default class AboutView extends Vue {
  private about: About = { id: 0, about: "", clients: "" };
  private insta: object = {
    link: "https://www.instagram.com/hugocohen",
    icon: faInstagram,
  };
  private mail: object = {
    link: "mailto:hugocohenpictures@gmail.com",
    icon: faEnvelope,
  };

  async mounted(): Promise<void> {
    this.about = await AboutAPI.getAbout();
  }
}
</script>

<style lang="scss" scoped>
@media only screen and (min-width: 769px) {
  $gutter: 5vw;

  .layout {
    padding-right: $gutter;
    padding-left: $gutter;

    display: grid;
    grid-gap: $gutter;
    grid-template-columns: 40vw 1vw 40vw;
    grid-template-rows: auto;
    grid-template-areas:
      "video . content"
      "clients clients clients"
      " links links links ";
  }

  .clients {
    grid-area: clients;
    justify-self: stretch;
    text-align: center;

    &-text {
      font-style: italic;
      font-size: 2em;
      white-space: nowrap;
    }
  }

  .content {
    grid-area: content;
    justify-self: stretch;
    height: 100%;
    width: 100%;

    &-bio {
      text-align: justify;
      font-size: 1rem;
      line-height: 2em;
    }
  }

  .links {
    grid-area: links;
    display: flex;
    width: auto;
    flex-direction: row;
    align-items: center;
    justify-content: space-evenly;
    font-size: 2em;
  }

  .video {
    grid-area: video;
    align-self: center;
    justify-self: center;

    &-vid {
      width: 75%;
      height: auto;
      object-fit: contain;
    }
  }
}

@media only screen and (max-width: 768px) {
  .content {
    height: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .text {
    order: 3;
    text-align: justify;
    font-size: 1em;
    padding: 4vw;
    line-height: 1em;
  }

  .links {
    order: 2;
    display: flex;
    justify-content: space-between;
    font-family: Avenir, Helvetica, Arial, sans-serif;
  }

  a {
    justify-content: space-between;
    padding-top: 5vh;
    padding-right: 10vw;
    padding-left: 10vw;
    font-size: 1.5vw;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    font-size: 1em;
  }
  .icon {
    font-size: 1.5em;
  }

  .av {
    grid-row-start: 2;
    grid-row-end: 4;
    grid-column-start: 3;
    grid-column-end: 4;
  }

  .video {
    order: 1;
    padding-right: 3vw;
    align-self: start;

    &-vid {
      width: 75%;
      height: auto;
      object-fit: contain;
    }
  }
}
</style>
