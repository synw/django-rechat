"use strict";
var $chatroom;
var $rechat;
var $instant;
var ChatMessage = /** @class */ (function () {
    function ChatMessage(date, user, content) {
        this.date = date;
        this.user = user;
        this.content = content;
    }
    return ChatMessage;
}());
/**
 * Initialize the global rechat store
 */
function initRechatStore(username) {
    Alpine.store('rechat', {
        name: "",
        user: "",
        init: function (username) {
            console.log("Username:", username);
            this.user = username !== null && username !== void 0 ? username : "anonymous";
            console.log("Init rechat store for user", this.user);
        },
        hxget: function (url, destination) {
            htmx.ajax('GET', url, destination);
        },
    });
    Alpine.store('rechat').init(username);
    $rechat = Alpine.store("rechat");
}
/**
 * Initialize the chatroom object type
 * @param instant the websockets controller
 */
function initChatroomStore() {
    Alpine.store('chatroom', {
        name: "",
        users: new Array(),
        messages: Array(),
        init: function () {
            console.log("Init chatroom store");
        },
        open: function (name, url, destination) {
            if (destination === void 0) { destination = '#room'; }
            console.log("Opening room", name);
            this.name = name;
            this.users.push($rechat.user);
            htmx.ajax('GET', url, destination);
        },
        incomingMessage: function (msg) {
            console.log("Incoming msg", msg);
        }
    });
    Alpine.store('chatroom').init();
    $chatroom = Alpine.store("chatroom");
}
