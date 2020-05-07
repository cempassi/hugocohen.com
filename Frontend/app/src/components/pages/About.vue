<template>
  <main>
    <p>About</p>
    <p>About Hugo Cohen</p>
  </main>
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
