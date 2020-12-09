<template>
  <main class="lines">
    <div v-for="line in lines" :key="line.nb" class="line">
      <div v-for="video in line.videos" :key="video.id" class="video">
        <router-link class="link" :to="'/video/' + video.id" :id="video.id">
          <div class="img-wrapper">
            <img :src="videoImage(video)" />
            <div class="transition">
              <div class="name">{{ video.name }}</div>
            </div>
          </div>
        </router-link>
      </div>
    </div>
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

  videoImage(video: Video) {
    return process.env.VUE_APP_API_URL + "/static/images/video/" + video.image;
  }

  videolen() {
    const videos: Array<Video> = this.$store.state.videos;
    return videos.length;
  }
  get lines() {
    const videos: Array<Video> = this.$store.state.videos;
    const pack: Array<{}> = [];
    for (let i = 0, nb = 0; i < videos.length; i += 3, nb++) {
      let control = 0;
      const line: { nbr: number; videos: Array<Video> } = {
        nbr: nb,
        videos: [],
      };
      control = i < videos.length ? line.videos.push(videos[i]) : -1;
      control = i + 1 < videos.length ? line.videos.push(videos[i + 1]) : -1;
      control = i + 2 < videos.length ? line.videos.push(videos[i + 2]) : -1;
      pack.push(line);
      if (control < 0) break;
    }
    return pack;
  }

  randomIndex() {
    return Math.floor(Math.random() * this.videolen());
  }
}
</script>

<style scoped lang="scss">
$gutter: 3vw;

.lines {
  padding-right: $gutter;
  padding-left: $gutter;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: space-evenly;
}

.link {
  height: 100%;
  width: 100%;
  text-decoration: none;
}

.video {
  padding: 10px;
}

.img-wrapper {
  width: 100%;
  max-width: 600px;
  overflow: hidden;
  position: relative;
}

.img-wrapper img {
  width: inherit;
}

.img-wrapper:hover img {
  opacity: 0.3;
}

.img-wrapper:hover .transition {
  opacity: 1;
}

.name {
  color: black;
  font-size: 16px;
  padding: 16px 32px;
}

.transition {
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

@media only screen and (min-width: 769px) {
  .line {
    display: flex;
    flex-flow: row nowrap;
    flex: 0 2 auto;
    justify-content: space-evenly;
    align-items: center;
  }
}

@media only screen and (max-width: 768px) {
  .line {
    display: flex;
    flex-flow: row wrap;
    justify-content: space-evenly;
    align-items: center;
  }
}
</style>
