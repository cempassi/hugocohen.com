import Axios from "axios";
import Video, { VideoDTO } from "@/models/Videos";

export abstract class VideoAPI {
  private static videosAxios = Axios.create();

  static async getOneVideo(id: string): Promise<Video> {
    const response = await this.videosAxios.get(
      process.env.VUE_APP_API_URL + "/video/" + id,
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    console.log(response.data);
    return new Video(response.data as VideoDTO);
  }

  static async getAllVideos(): Promise<Video[]> {
    const response = await this.videosAxios.get(
      process.env.VUE_APP_API_URL + "/video/",
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    console.log(response.data);
    return response.data.map((videoDto: VideoDTO) => new Video(videoDto));
  }

  static async getHomeVideos(): Promise<Video[]> {
    const response = await this.videosAxios.get(
      process.env.VUE_APP_API_URL + "/video/home",
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    console.log(response.data);
    return response.data.map((videoDto: VideoDTO) => new Video(videoDto));
  }
}
