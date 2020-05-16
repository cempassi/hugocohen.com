<template>
  <main class="wrapper">
    <div class="parent">
      <template v-for="video in videos">
        <div class="child" :key="video.id">
          <img :src="video.image" class="image" />
          <p class="title">{{video.name}}</p>
        </div>
      </template>
      <div class="child">End</div>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Video from "@/models/videos";
import { VideoAPI } from "@/api/VideoAPI";

@Component
export default class Home extends Vue {
  private videos: Video[] = [];

  async mounted(): Promise<void> {
    this.videos = await VideoAPI.getAllVideos();
  }
}
</script>

<style scoped lang="scss">
.wrapper {
  width: 100vw;
}

.parent {
  height: 100vh;
  display: grid;
  align-content: start;
  grid-template-rows: 80vh;
  grid-template-columns: 100vw;
  grid-auto-flow: column;
  overflow-y: hidden;
  overflow-x: scroll;
  column-gap: 50%;
  align-items: center;

  scroll-snap-type: x mandatory;
  overflow: -moz-scrollbars-none;
  -ms-overflow-style: none;
  &::-webkit-scrollbar {
    display: none;
  }
  &:first-child {
    padding-right: 20%;
  }
}

.child {
  display: flex;
  flex-direction: column;
  align-self: center;
  justify-self: center;
  scroll-snap-align: center;
}

.image {
  border: 1px solid black;
}

.title {
  padding: 5px;
}
</style>
