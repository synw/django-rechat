var $chatroom;
var $rechat;

class ChatMessage {
  date: Date;
  user: string;
  content: string;

  constructor(date: Date, user: string, content: string) {
    this.date = date;
    this.user = user;
    this.content = content;
  }
}

/**
 * Initialize the global rechat store
 */
function initRechatStore(): void {
  Alpine.store('rechat', {
    name: "",
    users: new Array<string>(),

    init() {
      console.log("Init main rechat store");
    },
    hxget(url: string, destination: string) {
      htmx.ajax('GET', url, destination);
    },
  });
  Alpine.store('rechat').init();
  $rechat = Alpine.store("rechat");
}

/**
 * Initialize the chatroom object type
 * @param name the name of the chatroom
 */
function initChatroomStore(): void {
  Alpine.store('chatroom', {
    name: "",
    users: new Array<string>(),
    messages: Array<ChatMessage>(),

    init() {
      console.log("Init chatroom store");
    },
    open(name: string, url: string, destination = '#room') {
      this.name = name;
      htmx.ajax(url, destination);
    },
    incomingMessage(msg: any) {
      console.log("Incoming msg", msg)
    }
  });
  Alpine.store('chatroom').init();
  $chatroom = Alpine.store("chatroom")
}