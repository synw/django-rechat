export default class ChatMessage {
  date: Date;
  user: string;
  content: string;

  constructor(date: Date, user: string, content: string) {
    this.date = date;
    this.user = user;
    this.content = content;
  }

  get time(): string {
    let buf = new Array<string>();
    let h = this.date.getHours().toString();
    if (h.length == 1) {
      h = `0${h}`
    }
    buf.push(h)
    let mn = this.date.getMinutes().toString();
    if (mn.length == 1) {
      mn = `0${mn}`;
    }
    buf.push("h", mn)
    return buf.join("")
  }
}