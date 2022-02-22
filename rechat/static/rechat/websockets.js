import { Instant } from "/static/instant/lib/index.js";

async function initWs() {
  const _instant = new Instant(
    "http://localhost:8000", // Django backend's address
    "ws://localhost:8427", // Centrifugo server's address
    true, // verbosity (optional, default: false)
  );
  await _instant.get_token();
  _instant.onMessage = (msg) => $chatroom.incomingMessage(msg);
  await _instant.connect();
  console.log("Websockets connected");
  $instant = _instant;
}

export { initWs }