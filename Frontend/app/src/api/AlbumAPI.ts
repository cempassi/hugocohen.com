import Axios from "axios";
import Album, { AlbumDTO } from "@/models/Albums";

export abstract class AlbumAPI {
  private static albumAxios = Axios.create();

  static async getOneAlbum(id: string): Promise<Album> {
    const response = await this.albumAxios.get(
      process.env.VUE_APP_API_URL + "/album/" + id,
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    return new Album(response.data as AlbumDTO);
  }

  static async getAllAlbums(): Promise<Album[]> {
    const response = await this.albumAxios.get(
      process.env.VUE_APP_API_URL + "/album/",
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    return response.data
      .filter((albumDto: AlbumDTO) => albumDto.active)
      .map((albumDto: AlbumDTO) => new Album(albumDto));
  }

  static async getAllAlbumsCover(): Promise<Album[]> {
    const response = await this.albumAxios.get(
      process.env.VUE_APP_API_URL + "/album/cover",
      {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    return response.data
      .filter((albumDto: AlbumDTO) => albumDto.active)
      .map((albumDto: AlbumDTO) => new Album(albumDto));
  }
}
