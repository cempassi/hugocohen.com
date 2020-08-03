<template>
  <section v-bind:class="selector">
    <transition-group name="fade" class="img-container">
      <div class="img-container-inner" v-for="(photo, index) in photoUri" :key="`photo-${index}`">
        <img :src="photo" />
      </div>
    </transition-group>
  </section>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Photo from "@/models/Photos";
import Album from "@/models/Albums";

@Component
export default class DisplayPhoto extends Vue {
  @Prop() id!: number;
  private index = 0;
  private ScrollStatus = 0;
  private ScrollMax = 0;

  get host() {
    return process.env.VUE_APP_API_URL + "/static/images/";
  }

  created() {
    console.log(this.id);
    this.$store.dispatch("fetchAlbums", this.id);
  }

  get photos() {
    const albums: Album[] = this.$store.state.albums;
    return albums.find((e: Album) => e.id === this.id)?.photos;
  }

  get photoUri() {
    return this.photos?.map((photo) => this.host + photo.filename);
  }

  randomIndex() {
    if (this.photos) {
      return Math.floor(Math.random() * this.photos.length);
    }
  }

  get selector() {
    if (this.ScrollStatus > 0) {
      return this.ScrollStatus + 30 >= this.ScrollMax
        ? "main-wrapper-end"
        : "main-wrapper-middle";
    }
    return "main-wrapper-start";
  }

  scrolling(ev: any) {
    const post = ev.target;
    this.ScrollStatus = post.scrollLeft;
    this.ScrollStatus = post.scrollLeft;
    this.ScrollMax = post.scrollWidth - post.clientWidth;
  }
}
</script>

<style scoped lang="scss">
@media only screen and (min-width: 769px) {
  .main-wrapper {
    height: 100vh;
    width: 100%;

    &-start {
      //padding-left: 1rem;
    }
    &-middle {
      //padding: 0px;
    }
    &-end {
      //padding-right: 1rem;
    }
  }

  .img-container {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-content: center;
    align-items: center;
    height: 80vh;
    width: auto;
    scroll-snap-type: x mandatory;
  }

  img {
    height: 60vh;
    width: auto;
    padding: 0% 1vh;
    object-fit: contain;
    scroll-snap-align: center;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
}

@media only screen and (max-width: 768px) {
  .main-wrapper {
    height: 100vh;
    width: 100%;

    &-start {
      //padding-left: 1rem;
    }
    &-middle {
      //padding: 0px;
    }
    &-end {
      //padding-right: 1rem;
    }
  }

  .img-container {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-content: center;
    align-items: center;
    flex-direction: column;
    height: auto;
    width: 100%;
  }

  img {
    height: auto;
    width: 100%;
    justify-items: center;
    object-fit: contain;
    scroll-snap-align: center;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
}
</style>
