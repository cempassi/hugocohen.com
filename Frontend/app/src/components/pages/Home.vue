<template>
  <main>
    <p>Home page of hugo cohen's website</p>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class Home extends Vue {
  @Prop({ default: "Home page of Hugo Cohen's website" }) private msg!: string;
}
</script>
<style></style>
