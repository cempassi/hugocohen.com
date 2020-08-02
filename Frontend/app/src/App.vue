<template>
  <div class="app">
    <Navigation></Navigation>
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Home from "@/components/pages/Home.vue";
import About from "@/components/pages/About.vue";
import Navigation from "@/components/Navigation.vue";

@Component({
  name: "HugoCohen",
  metaInfo: {
    title: "Home",
    titleTemplate: "%s | Hugo Cohen",
  },
  components: {
    Navigation,
    Home,
    About,
  },
})
export default class App extends Vue {
}
</script>

<style lang="scss">
@import "styles/global.scss";

.app {
  height: 100vh;
  width: vw;
}
</style>
