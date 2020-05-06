<template>
  <div>
	  <div>
	  <router-link to="/">Hugo Cohen  </router-link>
	  <router-link to="/about">About</router-link>
	  </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class Navigation extends Vue{
}
</script>
<style>
</style>
