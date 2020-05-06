<template>
  <div>
    <h1>About</h1>
    <p>About Hugo Cohen</p>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Navbar from "@/components/Navbar.vue";

@Component
export default class About extends Vue {
	@Prop({default: "About Hugo Cohen"}) private msg!: string;
}
</script>
<style></style>
