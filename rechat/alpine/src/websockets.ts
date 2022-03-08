import { Instant } from "djangoinstant";

async function initWs(chatroom: typeof Alpine.store): Promise<Instant> {
  const _instant = new Instant(
    "http://localhost:8000", // Django backend's address
    "ws://localhost:8427", // Centrifugo server's address
    true, // verbosity (optional, default: false)
  );
  await _instant.get_token();
  _instant.onMessage = (msg) => {
    console.log("---> msg --", msg);
    chatroom.incomingMessage(msg);
  }
  await _instant.connect();
  console.log("Websockets connected");
  return _instant;
}

export { initWs }