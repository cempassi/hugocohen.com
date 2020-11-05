<template>
  <main class="main-wrapper full">
    <transition-group name="fade" class="work_display">
      <template v-for="video in videos">
        <div
          v-bind:style="{'background-image': 'url(' + video.image_small + ')'}"
          :key="video.id"
          class="work_item"
        >
          <router-link class="link" :to="'/video/' + video.id" :id="video.id">
            <div class="name">{{ video.name }}</div>
          </router-link>
        </div>
      </template>
    </transition-group>
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

  videolen() {
    const videos: Array<Video> = this.$store.state.videos;
    return videos.length;
  }

  randomIndex() {
    return Math.floor(Math.random() * this.videolen());
  }
}
</script>

<style scoped lang="scss">
@media only screen and (min-width: 769px) {
  $gutter: 3vw;

  .main-wrapper {
    padding-right: $gutter;
    padding-left: $gutter;
  }

  .link {
    height: 100%;
    width: 100%;
    text-decoration: none;
  }

  .work_display {
    display: grid;
    height: 100%;
    width: 100%;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-rows: 20vh;
    grid-gap: $gutter / 2;
    grid-auto-flow: row;
    align-content: start;

    overflow-y: hidden;
    overflow-x: hidden;
    overflow: -moz-scrollbars-none;
    -ms-overflow-style: none;
    &::-webkit-scrollbar {
      display: none;
    }
  }

  .work_item {
    display: flex;
    justify-content: center;
    align-items: center;
    background-size: cover;
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
