<template>
  <main class="layout">
    <div class="video">
      <video class="video-vid" autoplay loop muted playsinline>
        <source type="video/mp4" src="@/assets/about.mp4" />
        Video isn't working
      </video>
    </div>
    <div class="content">
      <p class="content-bio">{{ about.about }}</p>
    </div>
		<div class="clients-wrapper">
    	<div v-for="client in clients" :key="client" class="clients">
      	<p class="clients-text">{{client}}</p>
    	</div>
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

  get clients() {
    const clients = this.about.clients.split("|");
    return clients;
  }

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

  .video {
    grid-area: video;
    align-self: center;
    justify-self: center;
    padding-left: 8vw;

    &-vid {
      width: 75%;
      height: auto;
      object-fit: contain;
    }
  }

  .content {
    grid-area: content;
    justify-self: stretch;
    height: 100%;
    width: 100%;

    &-bio {
      font-size: 1rem;
      line-height: 2em;
      padding-right: 10vw;
    }
  }

	.clients-wrapper{
    grid-area: clients;
		width:100%;
		align-items:stretch;
		justify-items: center;

		display: flex;
		flex-flow: row wrap;
		justify-content: center;
		align-content: space-around;

  	.clients {

    	&-text {
      	font-style: italic;
      	font-size: 1em;
      	text-align: justify-center;
      	white-space: wrap;
				padding:10px;
    	}
  	}
	}
 
  .links {
    grid-area: links;
    display: flex;

    width: auto;
    padding-left: 25vw;
    padding-right: 25vw;

    flex-direction: row;
    align-items: center;
    justify-content: space-evenly;
    font-size: 2em;
  }

}

@media only screen and (max-width: 768px) {
  $gutter: 5vw;

  .layout {
    display: flex;
		flex-flow: column wrap;
		padding-left: $gutter;
		padding-right: $gutter;
  }

  .video {
    width: 100%;
		display: none;
		justify-content: center;

    &-vid {
      width: 70%;
      object-fit: contain;
			}
	}

  .content {
    width: 100%;
		display:flex;
		justify-content: center;
		padding-top: 5vh;
		padding-bottom: 5vh;
    &-bio {
			text-align: center;
      font-size: 1rem;
      line-height: 2em;
    }
	}

	.clients-wrapper{
		display: flex;
		flex-flow: row wrap;
		justify-content: center;
		align-content: space-around;
		 
  	.clients {
    		&-text {
      	font-style: italic;
      	font-size: 1em;
      	text-align: justify-center;
      	white-space: wrap;
				padding:10px;
				}
			}
	}

  .links {
    display: flex;

    width: auto;
    padding-top: 1em;

    flex-direction: row;
    align-items: center;
    justify-content: space-evenly;
    font-size: 2em;
		padding-bottom: 5vh;
	}
}
</style>
