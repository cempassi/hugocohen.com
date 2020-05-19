<template>
  <main class="wrapper">
    <div class="parent"  @keyup.esc="stopping">
      <template v-for="video in videos">
        <div class="video_wrapper" :key="video.id" v-if="play == true && current == video.id">
          <iframe
            class="video"
            :src="'https://player.vimeo.com' + video.uri +'?autoplay=1&autopause=1&loop=1'"
            frameborder="0"
            allow="autoplay; fullscreen"
            allowfullscreen
          >Working</iframe>
        </div>
        <div  class="child" :key="video.id" v-else>
          <img @mouseenter="stopping" :src="video.image_large" class="image" @click="playing($event,
			video.id)" />
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
  private play = false;
  private current = 0;

  async mounted(): Promise<void> {
    this.videos = await VideoAPI.getAllVideos();
  }

  playing(e: Event, id: number) {
    if (id >= 1) {
      this.play = !this.play;
      this.current = id;
    } else {
      this.play = false;
      this.current = 0;
    }
  }

  stopping(e: Event) {
      this.current = 0;
      this.play = false;
      console.log("stopping");
  }

  runvideo(): string {
    const iframe = document.createElement("div");
    return iframe.innerHTML;
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
}

.child {
  display: flex;
  flex-direction: column;
  align-self: center;
  justify-self: center;
  scroll-snap-align: center;
}

.video_wrapper {
  display: flex;
  flex-direction: column;
  align-self: stretch;
  justify-self: stretch;
  scroll-snap-align: center;
  & iframe {
    position: relative;
    top: 0;
    left: 0;
    width: 100vh;
    height: 100vw;
    border: 0;
    scroll-snap-align: center;
  }
}

.image {
  border: 1px solid black;
}

.title {
  padding: 5px;
}
</style>
