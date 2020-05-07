<template>
  <div id="app" class="base">
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
*,
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  border: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin: 50px 50px 6vh 50px;
  height: 100%;
  width: 100%;
}
.base {
  flex-grow: 1;
  flex-shrink: 1;
  flex-basis: auto;
}
</style>
