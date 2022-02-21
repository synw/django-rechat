"use strict";
var $chatroom;
var $rechat;
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
function initChatroom(name) {
    Alpine.store('chatroom', {
        name: "",
        users: new Array(),
        init: function (name) {
            console.log("Init chatroom model", name);
            this.name = name;
        }
    });
    Alpine.store('chatroom').init(name);
    $chatroom = Alpine.store("chatroom");
}
