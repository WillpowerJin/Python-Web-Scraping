const CryptoJS = require('crypto-js')

var a = 'a978df21';
var b = '9ff79820f5c76feb304dbc074fef5c100416acfaa4b83f38b4b5dea633f7dbc4c352ee55762fcf1c736ddd62efc716a712048bca7b086fb68adc4315694072965b997ab3e6df0279d843969a5ba3e6da51a77a52a55ea8152f189c3c9e934b275d99ec10a76e88b18b04943c30e78047885130f6eed599dcc882ca576dab58b8ed3e89f06adb118a';

function get_cookies(a, b) {
    var keyHex = CryptoJS['enc']['Utf8']['parse'](a),
        encrypted = CryptoJS['DES']['encrypt'](b, keyHex, {
            'mode': CryptoJS['mode']['ECB'],
            'padding': CryptoJS['pad']['Pkcs7']
        }),
        encryptvrscode = encrypted['ciphertext']['toString']();

    b = escape(encryptvrscode);

    return b;
}
