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
    const photos = response.data[0].photos;
    return new Album(response.data as AlbumDTO, photos);
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
      .map(
        (albumDto: AlbumDTO) =>
          new Album(albumDto, response.data[albumDto.id - 1].photos)
      );
  }
}
