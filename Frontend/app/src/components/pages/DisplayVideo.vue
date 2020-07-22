<template>
  <main>
    <div class="wrapper">
      <div v-if="dataready" class="video_wrapper" :key="video.id">
        <iframe
          ref="frame"
          class="video"
          :src="link + '?autoplay=1&autopause=1&loop=1&muted=1'"
          frameborder="0"
          allow="autoplay; fullscreen"
          allowfullscreen
          mozallowfullscreen
          webkitallowfullscreen
        >Working</iframe>
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Prop, Vue, Emit, Ref, Watch } from "vue-property-decorator";
import Video from "@/models/Videos";
import { VideoAPI } from "@/api/VideoAPI";

const passVideo = Vue.extend({
  props: {
    //video: Video,
  },
});

@Component({})
export default class DisplayVideo extends passVideo {
  private dataready = false;

  @Prop(Video) video!: Video | undefined;
  @Prop({ default: false }) readonly home!: boolean;

  @Ref("frame") readonly frame!: HTMLIFrameElement;

  @Emit()
  videoOff() {
    return false;
  }

  async mounted(): Promise<void> {
    if (!this.video) {
      this.video = await VideoAPI.getOneVideo(this.$route.params.id);
    }
    this.dataready = true;
    if (this.home == false) {
      this.$nextTick(() => {
        this.frame.requestFullscreen();
      });
    }
  }
	get link() {
		if (this.video?.host == 'vimeo') {
			return 'https://player.vimeo.com' + this.video?.uri
		}
		return 'https://www.youtube.com/embed/' + this.video?.uri
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
