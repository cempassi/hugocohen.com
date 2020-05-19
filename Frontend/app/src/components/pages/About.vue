<template>
  <main class="content">
    <p class="text">
      Hugo Cohen Sprung is born in 1989 in Paris where he work now as filmmaker, cinematographer and photographer.
      His works are commercials, fashion and beauty films, as well as music videos with company such as Ed Banger Record, Nina Ricci, Hermès, Zadig&Voltaire, Mixa ect...
      In 2018 he co-directed with Adi Walter a documentary named "Marin Karmitz, un portrait".
      He is know focusing on writing and directing personal projects of fictions and documentary.
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
		<video width="320" height="240" autoplay loop muted playsinline>
			<source src="@/assets/about.mp4" type="video/mp4">
			Video isn't working
		</video>
	</div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Navbar from "@/components/Navbar.vue";
import { faEnvelope } from "@fortawesome/free-regular-svg-icons";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";

@Component
export default class About extends Vue {
  private insta: object = {
    link: "https://www.instagram.com/hugocohen",
    icon: faInstagram,
  };
  private mail: object = {
    link: "mailto:hugocohenpictures@gmail.com",
    icon: faEnvelope,
  };
}
</script>
<style lang="scss" scoped>
.content {
  height: 100vh;
  display: grid;
  grid-template-rows: 20vh 20vh 10vh 10vh;
  grid-template-columns: 10vw 40vw 40vw 10vw;
}

.text {
  grid-row-start: 2;
  grid-row-end: 3;
  grid-column-start: 2;
  grid-column-end: 3;
}

.links {
  grid-row-start: 3;
  grid-row-end: 4;
  grid-column-start: 2;
  grid-column-end: 3;
  display: flex;
  justify-content: space-evenly;
}

.icon {
	font-size: 1.5em;
}

.av {
  grid-row-start: 2;
  grid-row-end: 3;
  grid-column-start: 3;
  grid-column-end: 4;
}
</style>
