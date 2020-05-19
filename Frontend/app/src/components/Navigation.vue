<template>
  <nav>
    <div class="wrapper">
      <div class="title">
        <router-link to="/">Hugo Cohen</router-link>
      </div>
	  <div class="menu">
          <router-link class="menu-item" to="/works">Works</router-link>
          <router-link class="menu-item" to="/about">About</router-link>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class Navigation extends Vue {}
</script>

<style scoped lang="scss">
.wrapper {
  display: flex;
  flex-flow: row nowrap;
  flex-shrink: 0;
  justify-content: space-between;
  align-items: center;
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
	margin:30px;
}
</style>
