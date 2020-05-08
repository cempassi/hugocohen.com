<template>
  <div>
    <Navigation />
    <router-view />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Home from "@/components/pages/Home.vue";
import About from "@/components/pages/About.vue";
import Navigation from "@/components/Navigation.vue";

@Component({
  components: {
    Navigation,
    Home,
    About,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
@import 'styles/global.scss';

</style>
