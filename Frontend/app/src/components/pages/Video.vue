<template>
  <main v-bind:class="selector">
    <div v-if="videoOn == false">
      <transition-group name="fade" ref="scroller" @scroll="scrolling" class="work_display">
        <template v-for="video in videos">
          <div
            v-bind:style="{'background-image': 'url(' + video.image_small + ')'}"
            :key="video.id"
            class="work_item"
            @click="togglevideo"
          >
            <router-link class="link" :to="'/video/' + video.id">
              <div class="name">{{ video.name }}</div>
            </router-link>
          </div>
        </template>
      </transition-group>
    </div>
    <div v-else>
      <router-view></router-view>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Video from "@/models/videos";
import { VideoAPI } from "@/api/VideoAPI";

@Component
export default class VideoView extends Vue {
  private videos: Video[] = [];
  private ScrollStatus = 0;
  private ScrollMax = 0;
  private videoOn = false;

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

  togglevideo(e: Event) {
    e.stopPropagation(); // this will stop propagation of this event to upper level
    this.videoOn = !this.videoOn;
    if (this.videoOn) {
      window.addEventListener("click", () => {
        this.videoOn = false;
      });
    } else {
      window.removeEventListener("click", () => {
        this.videoOn = false;
      });
    }
  }

  randomIndex() {
    return Math.floor(Math.random() * this.videos.length);
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

.link {
  height: 100%;
  width: 100%;
  text-decoration: none;
}
.work_display {
  display: grid;

  height: 100%;
  width: 100%;

  grid-auto-columns: minmax(450px, calc(40%));
  grid-template-rows: repeat(4, minmax(250px, 50%));
  grid-row-gap: 1em;
  grid-column-gap: 1em;
  grid-auto-flow: column;

  align-content: start;

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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
