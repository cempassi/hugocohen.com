<template>
  <section class="gallery">
    <figure v-for="photo in photos" :key="photo.id" class="img-container" >
      <img :src="host + photo.filename" />
    </figure>
  </section>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Photo from "@/models/Photos";
@Component
export default class DisplayPhoto extends Vue {
  @Prop() readonly photos: Photo[] | undefined;

  get host() {
    return process.env.VUE_APP_API_URL + "/static/images/";
  }
}
</script>

<style scoped lang="scss">
.gallery {
  padding: 0 0 4rem 0;
	overflow-y: scroll;
	display: grid;
	grid-auto-flow: column;
  grid-gap: 1rem;
  scroll-snap-type: x mandatory;
}

.img-container {
  width: 100vw;
  height: 50vh;
  cursor: pointer;
  overflow: hidden;

  scroll-snap-align: center;
  &:hover .img-content-hover {
    display: block;
  }
}

img {
	width: 100%;
  height: 50vh;
	object-fit: contain;
  transform: scale(1);
  transition: all 0.3s ease-in-out;
}

</style>
