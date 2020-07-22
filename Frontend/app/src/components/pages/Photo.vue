<template>
  <main class="main-wrapper">
    <div v-if="photoOn == false">
      <transition-group name="fade" class="album-container">
        <div class="grid-item" v-for="album in active" :key="album.id">
          <div class="image-container">
            <router-link :to="'/photo/' + album.id">
              <img :src="cover(album.photos)" @click="handler($event, album.id)" />
            </router-link>
          </div>
          <p class="title">{{album.name}}</p>
        </div>
      </transition-group>
    </div>
    <router-view v-else :photos="photos"></router-view>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Album from "@/models/Albums";
import Photo from "@/models/Photos";
import { AlbumAPI } from "@/api/AlbumAPI";

@Component
export default class AlbumView extends Vue {
  private albums: Album[] = [];
  private photoOn = false;
  private albumId = 0;
  private inactive = 0;

  async mounted(): Promise<void> {
    this.albums = await AlbumAPI.getAllAlbums();
  }

  get host() {
    return process.env.VUE_APP_API_URL + "/static/images/";
  }

  get active() {
    this.inactive = this.albums.filter((album: Album) => !album.active).length;
    return this.albums.filter((album: Album) => album.active);
  }

  get photos() {
    return this.albums.find((album) => album.id == this.albumId)?.photos;
  }

  cover(photos: Photo[]) {
    const photo = photos.find((x: Photo) => x.cover);
    if (photo) {
      return this.host + photo.filename;
    } else return this.host + photos[0].filename;
  }

  randomIndex() {
    return Math.floor(Math.random() * this.albums.length);
  }

  handler(e: Event, albumId: number) {
    this.currentAlbum(albumId);
    this.togglephoto(e);
  }

  currentAlbum(albumId: number) {
    this.albumId = albumId;
  }

  togglephoto(e: Event) {
    e.stopPropagation(); // this will stop propagation of this event to upper level
    this.photoOn = !this.photoOn;
    if (this.photoOn) {
      window.addEventListener("click", () => {
        this.photoOn = false;
      });
    } else {
      window.removeEventListener("click", () => {
        this.photoOn = false;
      });
    }
  }
}
</script>

<style lang="scss" scoped>
@media only screen and (min-width: 769px) {
  .main-wrapper {
    height: 85%;
    overflow-y: hidden;
  }

  .album-container {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-content: center;
    align-items: center;
    height: 80vh;
    width: auto;
    scroll-snap-type: x mandatory;
  }

  .grid-item {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    scroll-snap-align: center;
    //border: 2px solid;
  }

  .image-container {
    width: 100%;
    height: 100%;
    overflow: hidden;
    align-items: center;
    height: auto;
    width: auto;
    &:hover {
      transform: scale(1.02);
    }
  }

  .title {
    padding-top: 10px;
  }

  img {
    height: 40vh;
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
    //overflow-y: scroll;
    //width: auto;
		justify-content: center;
  }

  .album-container {
    display: flex;
    flex-flow: column;
    justify-content: center;
    align-content: center;
    align-items: center;
    height: 80vh;
    width: auto;
    padding: 1vw;
  }

  .grid-item {
    width: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    scroll-snap-align: center;
		padding: 2vw;
  }

  .image-container {
    width: auto;
    align-items: center;
    height: auto;
    width: auto;
  }

  .title {
    padding-top: 10px;
  }

  img {
    height: 20vh;
    width: auto;
    padding: 0% 1vh;
    object-fit: contain;
    scroll-snap-align: center;
  }
}
</style>
