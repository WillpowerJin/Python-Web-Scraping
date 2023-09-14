// sign({
//     ...c,
//     ...b
// }, g, v)

const { log } = require("console")
const MD5123 = require("crypto")

c = {
    "hot_list_id": "0",
    "tag": "61e541324fe6649d1b8a2ee3",
    "service_name": "author.AdStarAuthorService",
    "service_method": "GetHotListData",
    "sign_strict": 1
}

l = {
    "include": [
        "hot_list_id",
        "tag",
        "download",
        "image_download",
        "province",
        "city",
        "rlid"
    ]
}

v = true

function isInvalid(c) {
    return c == null
}

function isScalar(c) {
    return ["string", "number"].includes(typeof c)
}

function sign(c, l, v) {
    const { include: m, enforceWithKeys: g = [] } = l != null ? l : {};
    let b = Object.keys(c);
    if (v && m) {
        const C = m.concat(["service_name", "service_method", "sign_strict"]);
        b = b.filter(w => C.includes(w))
    }
    const E = b.sort().map(C => {
        const w = c[C];
        return isInvalid(w) ? "" : C + (!g.includes(C) && isScalar(w) ? w : C)
    }
    ).join("");
    return (E + "e9fefef711becf4c3d7bfef829578b0c")
}

text = sign(c, l, v)
console.log(text);

function getSigndata(data){
    return MD5123.createHash("md5").update(data).digest("hex")
}
sign_data = getSigndata(text)
console.log(sign_data);
