<template>
  <nav class="wrapper-relative">
    <div class="wrapper-absolute">
      <div class="wrapper-fixed">
        <div class="title" ref="home">
          <router-link to="/"  @click.native="reset">Hugo Cohen</router-link>
        </div>
        <div class="main-menu">
          <ul class="menu" ref="menu">
            <li>
              <router-link class="menu-item" @click.native="toggle" to="/photo">Photo</router-link>
            </li>
            <li>
              <router-link class="menu-item" @click.native="toggle" to="/video">Video</router-link>
            </li>
            <li>
              <router-link class="menu-item" @click.native="toggle" to="/about">About</router-link>
            </li>
          </ul>
          <div class="menu-toogle">
            <div v-if="toggleMenu">
              <font-awesome-icon :icon="menu.bars" @click="toggle"></font-awesome-icon>
            </div>
            <div v-else>
              <font-awesome-icon :icon="menu.cross" @click="toggle"></font-awesome-icon>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { faBars, faTimes } from "@fortawesome/free-solid-svg-icons";

@Component
export default class Navigation extends Vue {
  $refs!: {
    menu: HTMLUListElement;
    home: HTMLDivElement;
  };
  private showNavbar = true;
  private lastScrollPos = 0;
  private toggleMenu = true;
  private menu: object = {
    bars: faBars,
    cross: faTimes,
  };

  mounted() {
    window.addEventListener("scroll", this.onScroll);
  }

  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  }

  onScroll() {
    const currentScrollPos =
      window.pageXOffset || document.documentElement.scrollTop;
    if (Math.abs(currentScrollPos - this.lastScrollPos) < 60) {
      return;
    }

    this.showNavbar = currentScrollPos < this.lastScrollPos;
    this.lastScrollPos = currentScrollPos;
  }

  reset() {
    if (document.documentElement.clientWidth > 768) return;
    this.toggleMenu = true;
    this.$refs.menu.style.visibility = "hidden";
    this.$refs.menu.style.opacity = "0";
  }
  toggle() {
    if (document.documentElement.clientWidth > 768) return;
    this.$refs.menu.style.visibility = this.toggleMenu ? "visible" : "hidden";
    this.$refs.menu.style.opacity = this.toggleMenu ? "1" : "0";
    this.toggleMenu = !this.toggleMenu;
  }
}
</script>

<style scoped lang="scss">
.wrapper-relative {
  position: relative;
  width: 100vw;
  height: 15vh;
  margin: 0 auto;
}
.wrapper-absolute {
  z-index: 1000;
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

.menu-toogle {
  display: none;
}

.main-menu {
  display: flex;
  align-items: center;
}

@media only screen and (max-width: 768px) {
  .wrapper-relative {
    position: relative;
    width: 100vw;
    height: 100px;
    z-index: 1;
  }

  .wrapper-absolute {
    z-index: 1;
    position: absolute;
    width: 150px;
    position: absolute;
    top: 0;
  }

  .wrapper-fixed {
    z-index: 1;
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
  body {
    overflow-x: hidden;
  }
  .menu-toogle {
    display: flex;
    margin: 45px;
    align-items: center;
  }

  .menu {
    z-index: -1;
    position: absolute;
    right: 0px;
    height: 100vh;
    top: 0vh;
    background-color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    width: 100%;
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s, opacity 0.2s;
  }
}

.menu-item {
  flex: 0 1;
  margin: 30px;
}
</style>
