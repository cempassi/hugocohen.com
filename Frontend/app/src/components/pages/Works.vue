<template>
  <main class="main-wrapper">
    <div class="work_display">
      <div class="work_item" v-for="item in list" :key="item">{{ item }}</div>
    </div>
  </main>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class Works extends Vue {
  @Prop({ default: "Home page of Hugo Cohen's website" }) private msg!: string;
  private list: Array<string> = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thriteen",
    "Fourteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
  ];
}
</script>
<style scoped lang="scss">
.main-wrapper {
	padding: 25px;
}
.work_display {
  display: grid;
  height: 100%;
  align-content: start;
  grid-auto-columns: calc(40%);
  grid-template-rows: repeat(3, minmax(250px, 40%));
  grid-row-gap: 1em;
  grid-column-gap: 1em;
  grid-auto-flow: column;
  overflow-y: scroll;
}
.work_display:before,
.work_display:after {
  width: 10px;
}

.work_item {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px solid black;
  font-size: 1em;
}
</style>
