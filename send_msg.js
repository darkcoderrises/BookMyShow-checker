const login = require("facebook-chat-api");
const fs = require("fs");

login({email: "harshil.goel@rediffmail.com", password: "harshil98"}, {pageID: 748050705342928}, (err, api) => {
    if (err) return console.error(err);
    data = fs.readFileSync('./theaters.txt', {encoding: 'utf-8'});
    console.log(data);
    api.sendMessage(data, "100001002823892");
});
