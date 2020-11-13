<template>
  <main class="lines">
    <div v-for="line in lines" :key="line.nb" class="line">
      <div v-for="video in line.videos" :key="video.id" >
        <router-link class="link" :to="'/video/' + video.id" :id="video.id">
          <div class="img-wrapper">
            <img :src="videoImage(video)" />
          </div>
        </router-link>
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Video from "@/models/Videos";
import { VideoAPI } from "@/api/VideoAPI";

@Component({
  name: "Videos",
  metaInfo: {
    title: "Videos",
  },
})
export default class VideoView extends Vue {
  private ScrollStatus = 0;
  private ScrollMax = 0;

  created() {
    this.$store.dispatch("fetchVideos");
  }

  get videos() {
    return this.$store.state.videos;
  }

	videoImage(video: Video){
		return process.env.VUE_APP_API_URL + '/static/images/video/' + video.image;

	}

  videolen() {
    const videos: Array<Video> = this.$store.state.videos;
    return videos.length;
  }
  get lines() {
    const videos: Array<Video> = this.$store.state.videos;
    const pack: Array<{}> = [];
    for (let i = 0, nb = 0; i < videos.length; i += 3, nb++) {
      let control = 0;
      const line: { nbr: number; videos: Array<Video> } = {
        nbr: nb,
        videos: [],
      };
      control = i < videos.length ? line.videos.push(videos[i]) : -1;
      control = i + 1 < videos.length ? line.videos.push(videos[i + 1]) : -1;
      control = i + 2 < videos.length ? line.videos.push(videos[i + 2]) : -1;
      pack.push(line);
      if (control < 0) break;
    }
    return pack;
  }

  randomIndex() {
    return Math.floor(Math.random() * this.videolen());
  }
}
</script>

<style scoped lang="scss">
@media only screen and (min-width: 769px) {
  $gutter: 3vw;

  .lines {
    padding-right: $gutter;
    padding-left: $gutter;
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .line {
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-evenly;
    align-items: center;
  }

  .link {
    height: 100%;
    width: 100%;
    text-decoration: none;
  }

  .img-wrapper {
    width: 100%;
		max-width: 600px;
    overflow: hidden;
    margin: 0;
    position: relative;
  }

  .image-wrapper img {
    position: absolute;
		width: inherit;
    top: 50%;
    left: 50%;
    width: 100%;
    transform: translate(-50%, -50%);
  }

  .name {
    opacity: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    color: white;
    font-size: 1em;
    &:hover {
      transition: opaticy 0.9s ease-in-out;
      opacity: 1;
    }
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 1s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
}

@media only screen and (max-width: 768px) {
  .work_display {
    display: inline-flex;

    flex-direction: column;
    justify-content: space-between;
    flex-wrap: nowrap;
    padding-left: 5vw;
  }

  .work_item {
    display: flex;
    height: 100%;
    width: 100%;
    justify-content: center;
    align-items: center;
    background-size: contain;
    background-repeat: no-repeat;
    flex-direction: column;
    background-position: center;
    &:hover {
      transition: filter 0.5s ease-in-out;
      filter: gray;
      -webkit-filter: grayscale(80%);
    }
  }

  .name {
    opacity: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    color: white;
    font-size: 1em;
    &:hover {
      transition: opaticy 0.9s ease-in-out;
      opacity: 1;
    }
  }
}
</style>
