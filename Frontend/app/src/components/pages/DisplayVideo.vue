<template>
  <main>
    <div class="wrapper">
      <div v-if="dataready" class="video_wrapper" :key="video.id">
        <iframe
          ref="frame"
          class="video"
          :src="'https://player.vimeo.com' + video.uri +'?autoplay=1&autopause=1&loop=1'"
          frameborder="0"
          allow="autoplay; fullscreen"
          allowfullscreen
        >Working</iframe>
      </div>
      <p class="title">{{video.name}}</p>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Prop, Vue, Emit } from "vue-property-decorator";
import Video from "@/models/Videos";
import { VideoAPI } from "@/api/VideoAPI";

const passVideo = Vue.extend({
  props: {
    video: Video,
  },
});

@Component({

})

export default class DisplayVideo extends Vue {
  private video: Video | undefined;
  private dataready = false;

  @Emit()
  videoOff() {
    return false;
  }
  async mounted(): Promise<void> {
    this.video = await VideoAPI.getOneVideo(this.$route.params.id);
    this.dataready = true;
  }
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.video_wrapper {
  width: 100%;
  height: 100%;
  padding-bottom: 56.25%;
  padding-top: 30px;
  height: 0;
  overflow: hidden;
  & iframe {
    position: absolute;
    border: 0px;
    height: 80%;
    width: 100%;
    left: 0;
    top: 10vh;
  }
}

.title {
  padding: 10px;
}
</style>
