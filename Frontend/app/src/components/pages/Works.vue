<template>
  <main v-bind:class="selector">
    <div ref="scroller" @scroll="scrolling" class="work_display">
      <template v-for="video in videos">
        <div
          class="work_item"
          :key="video.id"
          v-bind:style="{'background-image': 'url(' + video.image_small + ')'}"
        >
          <div class="name">{{ video.name }}</div>
        </div>
      </template>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Video from "@/models/videos";
import { VideoAPI } from "@/api/VideoAPI";

@Component
export default class Works extends Vue {
  private videos: Video[] = [];
  private ScrollStatus = 0;
  private ScrollMax = 0;

  scrolling(ev: any) {
    const post = ev.target;
    this.ScrollStatus = post.scrollLeft;
    this.ScrollStatus = post.scrollLeft;
    this.ScrollMax = post.scrollWidth - post.clientWidth;
  }

  get selector() {
    if (this.ScrollStatus > 0) {
      return this.ScrollStatus + 30 >= this.ScrollMax
        ? "main-wrapper-end"
        : "main-wrapper-middle";
    }
    return "main-wrapper-start";
  }

  async mounted(): Promise<void> {
    this.videos = await VideoAPI.getAllVideos();
  }
}
</script>
<style scoped lang="scss">
.main-wrapper {
  height: 100vh;

  &-start {
    padding-left: 25px;
  }
  &-middle {
    padding: 0px;
  }
  &-end {
    padding-right: 25px;
  }
}

.work_display {
  display: grid;
  height: 100%;
  width: 100%;
  align-content: start;
  grid-auto-columns: minmax(450px, calc(40%));
  grid-template-rows: repeat(4, minmax(250px, 50%));
  grid-row-gap: 1em;
  grid-column-gap: 1em;
  grid-auto-flow: column;
  overflow-y: scroll;
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
</style>
