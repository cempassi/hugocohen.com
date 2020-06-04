<template>
  <nav class="wrapper-relative">
    <div class="wrapper-absolute">
      <div class="wrapper-fixed">
        <div class="title">
          <router-link to="/">Hugo Cohen</router-link>
        </div>
        <div class="menu">
          <router-link class="menu-item" to="/photo">Photo</router-link>
          <router-link class="menu-item" to="/video">Video</router-link>
          <router-link class="menu-item" to="/about">About</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { Component, Vue} from "vue-property-decorator";

@Component
export default class Navigation extends Vue {}
</script>

<style scoped lang="scss">
.wrapper-relative {
    position: relative;
    width: 100vw;
    height: 15vh;
    margin: 0 auto;
}
.wrapper-absolute {
    position: absolute;
    width: 220px;
    position: absolute;
    top: 0;
}

.wrapper-fixed {
  position: fixed;
  top: 0px;
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  flex-shrink: 0;
  justify-content: space-between;
  align-items: center;
  background-color: white;
}

.title {
  margin: 45px;
}

.menu {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-flow: row nowrap;
  align-items: center;
}

.menu-item {
  flex: 0 1;
  margin: 30px;
}
</style>
