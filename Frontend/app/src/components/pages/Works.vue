<template>
  <main v-bind:class="selector">
    <div ref="scroller" @scroll="scrolling" class="work_display">
      <template v-for="item in videos">
        <div
          class="work_item"
          :key="item"
          v-bind:style="{'background-image': 'url(' + item.image + ')'}"
        >
          <div class="name">{{item.name}}</div>
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
  @Prop({ default: "Home page of Hugo Cohen's website" }) private msg!: string;

  private videos: Video[] = [];
  private list: Array<string> = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thriteen",
    "Fourteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
  ];
  private ScrollStatus = 0;
  private ScrollMax = 0;
  scrolling(ev: any) {
    const post = ev.target;
    this.ScrollStatus = post.scrollLeft;
    console.log("Current scroll pos: " + post.scrollLeft);
    console.log(
      "Current scroll width: " + (post.scrollWidth - post.clientWidth)
    );
    this.ScrollStatus = post.scrollLeft;
    this.ScrollMax = post.scrollWidth - post.clientWidth;
  }

  get selector() {
    if (this.ScrollStatus > 0) {
      return this.ScrollStatus == this.ScrollMax
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
.background__img {
  width: 100%;
  height: 100%;
}

.name {
  opacity: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  color: white;
  &:hover {
    transition: opaticy 0.9s ease-in-out;
    opacity: 1;
  }
}

.work_display {
  display: grid;
  height: 100%;
  align-content: start;
  grid-auto-columns: calc(40%);
  grid-template-rows: repeat(3, minmax(250px, 50%));
  grid-row-gap: 1em;
  grid-column-gap: 1em;
  grid-auto-flow: column;
  overflow-y: scroll;
}

.work_item {
  display: flex;
  justify-content: center;
  align-items: center;
  background-size: cover;
  flex-direction: column;
  background-position: center;
  border: 2px solid black;
  &:hover {
    transition: filter 0.5s ease-in-out;
    filter: gray;
    -webkit-filter: grayscale(80%);
  }
  //font-size: 1em;
}
</style>
