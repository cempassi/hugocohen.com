<template>
  <main class="wrapper">
    <div class="parent" @keyup.esc="stopping">
      <div class="video_wrapper" v-if="id !== -1">
        <DisplayVideo :id="id" :home="true" />
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from "vue-property-decorator";
import Video from "@/models/Videos";
import { VideoAPI } from "@/api/VideoAPI";
import DisplayVideo from "@/components/pages/DisplayVideo.vue";

@Component<Home>({
  name: "Home",
  metaInfo: {
    title: "Home",
  },
  components: { DisplayVideo },
})
export default class Home extends Vue {
  async created() {
    await this.$store
      .dispatch("fetchVideos")
      .then((res) => console.log("fetching sent"));
  }

  get videos() {
    return this.$store.state.videos;
  }

  @Watch("$store.state.videos")
  update() {
    console.log(this.$store.state.videos);
  }

  get id() {
    const videos = this.videos;
    if (videos.length !== 0) {
      return videos.find((video: Video) => video.OnHome).id;
    } else {
      return -1;
    }
  }
}
</script>

<style scoped lang="scss">
.wrapper {
  width: 90%;
  overflow-y: hidden;
}

.link {
  height: 100%;
  width: 100%;
  text-decoration: none;
}

.parent {
  height: 90%;
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
