import ChatMessage from "./models/chat_message";


function initRechatStore(username?: string): typeof Alpine.store {
  Alpine.store('rechat', {
    name: "",
    user: "",
    create(username?: string) {
      console.log("Username:", username)
      this.user = username ?? "anonymous";
      console.log("Init rechat store for user", this.user);
    },
    hxget(url: string, destination: string) {
      htmx.ajax('GET', url, destination);
    },
  });
  const s = Alpine.store('rechat');
  s.create(username);
  return s;
}

function initChatroomStore(): typeof Alpine.store {
  Alpine.store('chatroom', {
    name: "",
    users: new Array<string>(),
    messages: Array<ChatMessage>(),
    url: "",
    postUrl: "",
    open(name: string, url: string, postUrl: string, destination = '#room') {
      this.url = url;
      this.postUrl = postUrl;
      this.name = name;
      htmx.ajax('GET', url, destination);
    },
    incomingMessage(msg: any) {
      const m = new ChatMessage(msg.date, msg.data.username, msg.msg);
      this.messages.push(m);
    },
    async postMessage(msg: string) {
      //console.log("Post msg", msg, "in", this.postUrl);
      const payload = { msg: msg };
      await htmx.ajax('POST', this.postUrl, { values: payload });
    }
  });
  const s = Alpine.store('chatroom');
  return s;
}

export { initChatroomStore, initRechatStore }