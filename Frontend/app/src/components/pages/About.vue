<template>
  <main class="content">
    <video class="vid" autoplay loop muted playsinline>
      <source type="video/mp4" src="@/assets/about.mp4" />Video isn't working
    </video>
    <div class="links">
      <a :href="mail.link" class="link">Mail</a>
      <a :href="insta.link" class>Instagram</a>
    </div>
    <p class="text">{{about.about}}</p>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Navbar from "@/components/Navbar.vue";
import { faEnvelope } from "@fortawesome/free-regular-svg-icons";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";
import About from "@/models/About";
import { AboutAPI } from "@/api/AboutAPI";

@Component
export default class AboutView extends Vue {
  private about: About = { id: 0, about: "" };
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
.content {
  height: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.text {
  text-align: justify;
  font-size: 1.5vw;
  padding: 4vw;
}

.links {
  display: flex;
  justify-content: space-between;
}

a {
  justify-content: space-between;
  padding: 1rem;
  font-size: 1.5vw;
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

.vid {
  width: 50%;
  height: 50%;
  object-fit: contain;
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
    text-align: justify;
    font-size: 14px;
    padding: 4vw;
  }

  .links {
    display: flex;
    justify-content: space-between;
    font-family: Avenir, Helvetica, Arial, sans-serif;
  }

  a {
    justify-content: space-between;
    padding: 1rem;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    font-size: 12px;
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

  .vid {
    width: 50%;
    height: 50%;
    object-fit: contain;
  }
}
</style>
