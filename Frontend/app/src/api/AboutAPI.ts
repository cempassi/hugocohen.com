import Axios from "axios";
import About, { AboutDTO } from "@/models/About";

export abstract class AboutAPI {
  private static aboutAxios = Axios.create();

  static async getAbout(): Promise<About> {
    const response = await this.aboutAxios.get(
      process.env.VUE_APP_API_URL + "/about/",
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    return new About(response.data as AboutDTO);
  }
}
