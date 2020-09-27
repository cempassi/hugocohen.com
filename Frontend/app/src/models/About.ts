export interface InterfaceAbout {
  id: number;
  about: string;
  clients: string;
}

export class AboutDTO implements InterfaceAbout {
  id = 0;
  about = "";
  clients = "";
}

export default class About extends AboutDTO {
  constructor(dto: AboutDTO) {
    super();
    Object.assign(this, dto);
  }

  static create(dto: InterfaceAbout): About {
    return new About(dto);
  }
}
