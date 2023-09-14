const CryptoJS = require("crypto-js");

function newEncrypt(l) {
    var n = CryptoJS.enc.Utf8.parse("wkyzWNWwiQY6KasB"),
        t = CryptoJS.enc.Utf8.parse("wkyzWNWwiQY6KasB"),
        e = CryptoJS.enc.Utf8.parse(l),
        a = CryptoJS.AES.encrypt(e, n, {
            iv: t,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        });

    return a.ciphertext.toString(CryptoJS.enc.Base64);
}

f = { "jin": "15910887649" };

var jsonKey = newEncrypt(JSON.stringify(f));
console.log(jsonKey);