export interface InterfaceVideo {
  id?: number;
  name: string;
  link: string;
  uri: string;
  image_small: string;
  image_large: string;
  OnHome: boolean;
}

export class VideoDTO implements InterfaceVideo {
  id?: number;
  name = "";
  link = "";
  uri = "";
  image_small = "";
  image_large = "";
  OnHome = false;
}

export default class Video extends VideoDTO {
  constructor(dto: VideoDTO) {
    super();
    Object.assign(this, dto);
  }
}
