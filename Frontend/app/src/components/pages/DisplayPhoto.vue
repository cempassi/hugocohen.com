<template>
  <section class="gallery">
		<vue-gallery-slideshow :images="photoUri" :index="index" @close="index = null"></vue-gallery-slideshow>
  </section>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Photo from "@/models/Photos";
import VueGallerySlideshow from 'vue-gallery-slideshow'

@Component({
	components: {
		VueGallerySlideshow
	}
})
export default class DisplayPhoto extends Vue {
  @Prop() readonly photos: Photo[] | undefined;
	private index = 0;

  get host() {
    return process.env.VUE_APP_API_URL + "/static/images/";
  }

	get photoUri() {
		return this?.photos.map((photo) => this.host + photo.filename);
	}

	onClick(i: number) {
		this.index = i;
	}
}
</script>

<style scoped lang="scss">
.gallery {
  //padding: 0 0 4rem 0;
	overflow-y: scroll;
	display: flex;
	grid-auto-flow: column;
  grid-gap: 1rem;
}

.img-container {
  width: 100vw;
  height: 80vh;
  cursor: pointer;
  overflow: hidden;

  //scroll-snap-align: center;
  &:hover .img-content-hover {
    display: block;
  }
}

img {
	width: 100%;
  height: 50vh;
	object-fit: contain;
  transition: all 0.3s ease-in-out;
}

</style>
