<template>
	<div id="app">
		<Navigation/>
		<router-view/>
	</div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Home from "@/components/pages/Home.vue"
import About from "@/components/pages/About.vue"
import Navigation from "@/components/Navigation.vue"

@Component({
  components: {
	Navigation,
    Home,
    About
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 4vh;
  margin-left: 8vmax;
}
</style>
