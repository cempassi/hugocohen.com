export interface InterfaceVideo {
  id?: number;
  name: string;
  link: string;
  image: string;
}

export class VideoDTO implements InterfaceVideo {
  id?: number;
  name = "";
  link = "";
  image = "";
}

export default class Video extends VideoDTO {
  constructor(dto: VideoDTO) {
    super();
    Object.assign(this, dto);
  }
}
