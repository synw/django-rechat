"use strict";
var $chatroom;
var $rechat;
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
function initRechatStore() {
    Alpine.store('rechat', {
        name: "",
        users: new Array(),
        init: function () {
            console.log("Init main rechat store");
        },
        hxget: function (url, destination) {
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
            this.name = name;
            htmx.ajax(url, destination);
        },
        incomingMessage: function (msg) {
            console.log("Incoming msg", msg);
        }
    });
    Alpine.store('chatroom').init();
    $chatroom = Alpine.store("chatroom");
}
