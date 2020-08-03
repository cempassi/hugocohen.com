import Photo, { PhotoDTO } from "@/models/Photos";

type PhotoSet = Photo[];

export interface InterfaceAlbum {
  id: number;
  name: string;
  photos: PhotoSet;
  active: boolean;
}

export class AlbumDTO implements InterfaceAlbum {
  id = 0;
  name = "";
  photos = Array<Photo>();
  active = true;
}

export default class Album extends AlbumDTO {
  constructor(dto: AlbumDTO) {
    super();
    this.id = dto.id;
    this.name = dto.name;
    const photo = JSON.parse((dto.photos as unknown) as string);
    photo.forEach((pic: PhotoDTO) => this.photos.push(new Photo(pic)));
    this.active = dto.active;
  }

  static create(dto: InterfaceAlbum): Album {
    return new Album(dto);
  }
}
