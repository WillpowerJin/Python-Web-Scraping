const CryptoJS = require("crypto-js")

function newEncrypt(l) {
    var n = CryptoJS.enc.Utf8.parse("Hj6WfS4DskDSmFGP")
        , t = CryptoJS.enc.Utf8.parse("Hj6WfS4DskDSmFGP")
        , e = CryptoJS.enc.Utf8.parse(l)
        , a = CryptoJS.AES.encrypt(e, n, {
            iv: t,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });

    return CryptoJS.enc.Base64.stringify(a.ciphertext)
}

f = {
    "body": {
        "loginMethod": "1",
        "name": "15910887649",
        "password": "12345678"
    },
    "head": {
        "userCode": null,
        "channelCode": "101",
        "transTime": 1694422136021,
        "transToken": "",
        "customerId": null,
        "transSerialNumber": ""
    }
}

// var jsonKey = newEncrypt(JSON.stringify(f));
// console.log(jsonKey);
console.log(newEncrypt(JSON.stringify(f)));


function newDecoto(l) {
    var n = CryptoJS.enc.Base64.parse(l)
        , t = CryptoJS.enc.Utf8.parse("Hj6WfS4DskDSmFGP")
        , e = CryptoJS.enc.Utf8.parse("Hj6WfS4DskDSmFGP")
        , a = CryptoJS.lib.CipherParams.create({
            ciphertext: n
        });
    return CryptoJS.AES.decrypt(a, t, {
        iv: e,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8)
}

encryctReturns = 't25+y2GZdO8f2xNhlsqDBpHySSF/tZFmza/UcUlA9OGa2c6t+AjwWLtygKER7I/mBzWb1hje6gQM\nTKMc1bRNtniBsFYNrIuP+ObvFCUPfO9ZZIFW5cfdv07jAyZsKgSL4zzfdfTtMqcjioxUDfHLWomO\nSmggU8zp8aT6vDv4dyNgrk0aoxyc1evCgZ+4jhM6zm1V9U1RcsLNd1Qaf9mKjjIwc2BzAUwuSGiU\nuf6y66p3ZRCbun54iUmlbALKzDk77JhKqF3t8PPRdHAvDTJGLoD4+pi5LONJHBnusRmc+RSMxuG4\nqn1cv78Jm/8UH+IT'
n = encryctReturns.replace(/[\r\n]/g, "")
console.log(n);
console.log(newDecoto(n));
