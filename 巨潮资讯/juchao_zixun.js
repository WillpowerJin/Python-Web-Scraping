const CryptoJS = require("crypto-js")

var ts = Math.floor(Date.now() / 1000);

function getResCode(ts) {
    var key = CryptoJS.enc.Utf8.parse('1234567887654321')
    var _0x27ee95 = CryptoJS.AES.encrypt(
        CryptoJS.enc.Utf8.parse(ts), key, { iv: key, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 }
    );

    return CryptoJS.enc.Base64.stringify(_0x27ee95['ciphertext']);
}

console.log(ts);
console.log(getResCode(ts));
