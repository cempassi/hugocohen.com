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
    albumsCover: Array<Album>(),
    videos: Array<Video>(),
  }),
  mutations: {
    SAVE_ALBUMS(state, album) {
      state.albums.push(album);
    },
    SAVE_VIDEOS(state, videos) {
      state.videos = videos;
    },
    SAVE_ALBUMS_COVER(state, albums) {
      state.albumsCover = albums;
    },
  },
  actions: {
    async fetchAlbums(context, id) {
      return AlbumAPI.getOneAlbum(id)
        .then((album) => {
          if (context.state.albums.find((album) => album.id === id)) {
            console.log("Already loaded");
          } else {
            context.commit("SAVE_ALBUMS", album);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async fetchAlbumsCover(context) {
      return await AlbumAPI.getAllAlbumsCover().then((result) => {
        context.commit("SAVE_ALBUMS_COVER", result);
      });
    },
    async fetchVideos(context) {
      return await VideoAPI.getAllVideos().then((result) => {
        context.commit("SAVE_VIDEOS", result);
      });
    },
  },
  modules: {},
});
