export interface InterfacePhoto {
  id: number;
  filename: string;
  album: string;
  cover: boolean;
}

export class PhotoDTO implements InterfacePhoto {
  id = 0;
  filename = "";
  album = "";
  cover = false;
}

export default class Photo extends PhotoDTO {
  constructor(dto: PhotoDTO) {
    super();
    Object.assign(this, dto);
  }

  static create(dto: InterfacePhoto): Photo {
    return new Photo(dto);
  }
}
