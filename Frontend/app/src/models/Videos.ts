export interface InterfaceVideo {
  id: number;
  name: string;
  host: string;
  link: string;
  uri: string;
  image: string;
  OnHome: boolean;
}

export class VideoDTO implements InterfaceVideo {
  id = 0;
  name = "";
  host = "";
  link = "";
  uri = "";
  image = "";
  OnHome = false;
}

export default class Video extends VideoDTO {
  constructor(dto: VideoDTO) {
    super();
    Object.assign(this, dto);
  }

  static create(dto: InterfaceVideo): Video {
    dto.image =
      process.env.VUE_APP_API_URL + "/static/images/videos/" + dto.image;
    console.log(dto.image);
    return new Video(dto);
  }
}
