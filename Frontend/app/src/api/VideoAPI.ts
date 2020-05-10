import Axios from "axios";
import Video, { VideoDTO } from "@/models/Videos";

export abstract class VideoAPI {
  private static videosAxios = Axios.create();

  static async getAllVideos(): Promise<Video[]> {
    const response = await this.videosAxios.get(
      "http://localhost:5000/video/",
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
