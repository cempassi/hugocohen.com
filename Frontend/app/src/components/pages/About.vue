<template>
  <main>
    <div class="content">
      <div class="text">
        <p class="text-bio">{{about.about}}</p>
      </div>
      <div class="links">
        <a :href="mail.link">Mail</a>
        <a :href="insta.link">Instagram</a>
      </div>
      <div class="video">
        <video class="video-vid" autoplay loop muted playsinline>
          <source type="video/mp4" src="@/assets/about.mp4" />Video isn't working
        </video>
      </div>
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
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: start;
    justify-content: flex-start;
  }

  .text {
    width: 100%;

    &-bio {
      text-align: justify;
      font-size: 1em;
	  padding-left: 3vw;
      line-height: 2em;
    }
  }

  .links {
    display: flex;
    width: 50%;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;

    a {
      padding-bottom: 5vh;
      font-size: 1em;
    }
  }

  .video {
	padding-right: 3vw;
	align-self: start;

    &-vid {
      width: 100%;
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
