<template>
  <main class="main-wrapper">
    <div v-if="photoOn == false">
      <transition-group name="fade" class="grid-container">
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
    <router-view v-else :photos="albums[albumId].photos"></router-view>
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

  async mounted(): Promise<void> {
    this.albums = await AlbumAPI.getAllAlbums();
  }

  get host() {
    return process.env.VUE_APP_API_URL + "/static/images/";
  }

	get active() {
		return this.albums.filter((album: Album) => album.active)
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
    console.log(albumId);
    this.albumId = albumId - 1;
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
.main-wrapper {
  height: 85%;
  overflow-y: hidden;
}


.grid-container {
  height: 100vh;
  padding: 0 0 4rem 0;
  grid-gap: 2rem;

  display: grid;
  grid-template-rows: 40vh;
  grid-auto-columns: 40vw;
  grid-template-rows: 40vh 40vh;
  grid-auto-rows: 40vh;
  grid-auto-flow: column;
  justify-content: center;
  align-content: start;

  overflow-y: hidden;
  overflow-x: scroll;

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
    transform: scale(1.05);
  }
}

.title {
  padding-top: 10px;
}

img{
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
