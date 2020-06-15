<template>
  <main class="content">
    <p class="text">
			{{about.about}}
    </p>
    <div class="links">
      <div class="icon">
        <a :href="mail.link">
          <font-awesome-icon :icon="mail.icon"></font-awesome-icon>
        </a>
      </div>
      <div class="icon">
        <a :href="insta.link">
          <font-awesome-icon :icon="insta.icon"></font-awesome-icon>
        </a>
      </div>
    </div>
    <div class="av">
      <video class="vid" autoplay loop muted playsinline>
        <source type="video/mp4" src="@/assets/about.mp4" />Video isn't working
      </video>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Navbar from "@/components/Navbar.vue";
import { faEnvelope } from "@fortawesome/free-regular-svg-icons";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";
import About from "@/models/About";
import {AboutAPI} from "@/api/AboutAPI";

@Component
export default class AboutView extends Vue {
	private about: About = {id: 0, about: ""};
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
  height: 90vh;
  display: grid;
  grid-template-rows: 20vh 20vh 10vh 10vh;
  grid-template-columns: 10vw 40vw 40vw 10vw;
  grid-gap: 2rem;
  align-items: center;
  justify-content: center;
}

.text {
  grid-row-start: 2;
  grid-row-end: 3;
  grid-column-start: 2;
  grid-column-end: 3;
}

.links {
  display: flex;
  grid-row-start: 3;
  grid-row-end: 4;
  grid-column-start: 2;
  grid-column-end: 3;
  justify-content: space-evenly;
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
</style>
