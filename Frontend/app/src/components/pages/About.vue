<template>
  <main>
    <div class="content">
      <video class="vid" autoplay loop muted playsinline>
        <source type="video/mp4" src="@/assets/about.mp4" />Video isn't working
      </video>
      <div class="links">
        <a :href="mail.link" class="link">Mail</a>
        <a :href="insta.link" class>Instagram</a>
      </div>
      <p class="text">{{about.about}}</p>
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
@media only screen and (min-width: 769px) {
  .content {
    height: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .text {
    text-align: justify;
    font-size: 1em;
    padding: 4vw;
	line-height: 2em;
  }

  .links {
    display: flex;
    justify-content: space-between;
  }

  a {
    justify-content: space-between;
    padding-top: 5vh;
	padding-right: 10vw;
	padding-left: 10vw;
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
	max-height: 50vh;
	max-width: 50vw;
    width: 50%;
    height: 50%;
    object-fit: contain;
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
    text-align: justify;
    font-size: 1em;
    padding: 4vw;
	line-height: 1em;
  }

  .links {
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

  .vid {
    width: 50%;
    height: 25%;
    object-fit: contain;
  }
}
</style>
