var $chatroom: typeof Alpine.store;
var $rechat: typeof Alpine.store;
var $instant: typeof Instant;

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
function initRechatStore(username?: string): void {
  Alpine.store('rechat', {
    name: "",
    user: "",

    init(username?: string) {
      console.log("Username:", username)
      this.user = username ?? "anonymous";
      console.log("Init rechat store for user", this.user);
    },
    hxget(url: string, destination: string) {
      htmx.ajax('GET', url, destination);
    },
  });
  Alpine.store('rechat').init(username);
  $rechat = Alpine.store("rechat");
}

/**
 * Initialize the chatroom object type
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
      console.log("Opening room", name)
      this.name = name;
      this.users.push($rechat.user);
      htmx.ajax('GET', url, destination);
    },
    incomingMessage(msg: any) {
      console.log("Incoming msg", msg)
    }
  });
  Alpine.store('chatroom').init();
  $chatroom = Alpine.store("chatroom")
}