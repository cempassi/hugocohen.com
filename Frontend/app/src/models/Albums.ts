import PhotoDTO from "@/models/Photos";

type PhotoSet = PhotoDTO[];

export interface InterfaceAlbum {
  id: number;
  name: string;
  photos: PhotoSet;
  active: boolean;
}

export class AlbumDTO implements InterfaceAlbum {
  id = 0;
  name = "";
  photos = [{ id: 0, filename: "", album: "", cover: false }];
  active = true;
}

export default class Album extends AlbumDTO {
  constructor(dto: AlbumDTO, photos: string) {
    super();
    this.id = dto.id;
    this.name = dto.name;
    this.photos = JSON.parse(photos);
    this.active = dto.active;
  }

  static create(dto: InterfaceAlbum, photos: string): Album {
    return new Album(dto, photos);
  }
}
