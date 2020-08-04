<template>
  <main>
    <div class="wrapper">
      <div class="video_wrapper" :key="video.id">
        <iframe
          ref="aFrame"
          class="video"
          :src="homelink"
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

@Component({
  name: "DisplayVideo",
  metaInfo: {},
})
export default class DisplayVideo extends Vue {
  @Prop({ default: false }) readonly home!: boolean;
  @Prop() readonly id!: number;
  @Ref("aFrame") readonly frame!: HTMLIFrameElement;

  //public $refs: Vue["$refs"] & { aFrame: HTMLIFrameElement };

  metaInfo() {
    return {
      title: `${this.video?.name} | Hugo Cohen `,
      meta: [
        {
          name: this.video?.name,
        },
      ],
    };
  }

  get video() {
    const id = this.id;
    return this.$store.state.videos.find((video: Video) => video.id == id);
  }

  mounted() {
    if (this.home == false) {
      this.$nextTick(() => {
        (this.$refs.aFrame as HTMLIFrameElement).requestFullscreen();
      });
    }
  }

  get homelink(){
	  if (this.home === true){
		  return this.link + '?autoplay=1&autopause=1&loop=1&muted=1'
	  }
	  else {
		  return this.link + '?loop=1'
	  }
  }

  get link() {
    if (this.video.host == "vimeo") {
      return "https://player.vimeo.com" + this.video.uri;
    }
    return "https://www.youtube.com/embed/" + this.video.uri;
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
