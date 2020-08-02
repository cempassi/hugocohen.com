import Vue from "vue";
import Vuex from "vuex";
import Album from "@/models/Albums";
import Video from "@/models/Videos";
import { AlbumAPI } from "@/api/AlbumAPI";
import { VideoAPI } from "@/api/VideoAPI";

Vue.use(Vuex);

export default new Vuex.Store({
  state: () => ({
    loaded: false,
    albums: Array<Album>(),
    videos: Array<Video>(),
  }),
  mutations: {
    SAVE_ALBUMS(state, albums) {
      state.albums = albums;
    },
    SAVE_VIDEOS(state, videos) {
      state.videos = videos;
    },
    IS_LOADED(state, bool) {
      state.loaded = bool;
    },
  },
  actions: {
    async fetchAlbums({ commit }) {
      return AlbumAPI.getAllAlbums()
        .then((albums) => commit("SAVE_ALBUMS", albums))
        .catch((err) => {
          console.log(err);
        });
    },
    async fetchVideos(context) {
      return await VideoAPI.getAllVideos().then((result) => {
        context.commit("SAVE_VIDEOS", result);
        context.commit("IS_LOADED", true);
      });
    },
  },
  modules: {},
});
