<template>
  <nav class="nav-desktop">
    <ul class="navigation">
      <li class="nav-name">
        <router-link class="nav-name" to="/">Hugo Cohen</router-link>
      </li>
      <li class="nav-elements">
        <router-link to="/works">Works</router-link>
      </li>
      <li class="nav-elements">
        <router-link to="/about">About</router-link>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class Navigation extends Vue {}
</script>

<style lang="scss">
.nav-desktop{
  width: 100%;
  overflow: hidden;
}

.navigation {
  display: flex;
  justify-content: flex-start;
  height: 20vh;
}

li {
  list-style-type: none;
  font-size: 1.5vh;
}

a {
  text-decoration: none;

  &:hover {
    text-decoration: underline;
  }
  &:link,
  &:visited {
    color: black;
  }
}

.nav-name {
  margin-right: 33vw;
}
.nav-elements {
  padding: 0 2vw;
}
</style>
