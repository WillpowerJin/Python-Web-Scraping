// __m__
// u.default.encrypt() -> "03963fcd4a870203bfd21feacee98dcf6a16479f"
// u.default.encryptToken(u.default.encrypt()) -> "471625df510a86d23a38704cc0e5f79f"
// e.data["__m__"] = u.default.encryptToken(u.default.encrypt());

[{
    key: "getRandomKey",
    value: function (t) {
        var n = "";
        var r = ("" + t).substr(4);
        r.split("").forEach(function (e) {
            n += e.charCodeAt()
        });
        var i = (0,
            f.default)(n).toString();
        return i.substr(-6)
    }
}, {
    key: "getToken",
    value: function () {
        var t = {};
        t[this.getRandomKey(this.getQtTime((0,
            s.default)(this.dencryptCode(this.qtTime))))] = this.encrypt();
        return t
    }
}, {
    key: "encryptFunction",
    value: function () {
        return [function (e) {
            var t = (0,
                u.default)(e).toString();  // u.default -> SHA1
            return (0,
                f.default)(t).toString()   // f.default -> MD5
        }
            , function (e) {
                var t = (0,
                    f.default)(e).toString();
                return (0,
                    u.default)(t).toString()
            }
        ]
    }
}, {
    key: "dencryptCode",
    value: function (t) {
        // ASCII编码
        return t.map(function (e) {
            return String.fromCharCode(e - 2)
        }).join("")
    }
}, {
    key: "getQtTime",
    value: function (t) {
        // 时间戳
        return t ? Number(t.split(",").map(function (e) {
            return String.fromCharCode(e - 2)
        }).join("")) : 0
    }
}, {
    key: "getTokenStr",
    value: function () {
        var t = this.dencryptCode(this.tokenStr);  // "qunar_api_token"
        var n = document.getElementById(t).innerHTML;  // "b936f284-f732-43f8-bc43-e43a07554d72"
        return n ? n : (0,
            s.default)(this.dencryptCode(this.cookieToken))
    }
}, {
    key: "encrypt",
    value: function () {
        // u.default.encrypt()
        var t = this.getTokenStr()
            , n = this.getQtTime((0,
                s.default)(this.dencryptCode(this.qtTime)))
            , r = n % 2;
        return this.encryptFunction()[r](t + n)  // t -> "b936f284-f732-43f8-bc43-e43a07554d72"; n -> 时间戳
    }
}, {
    key: "encryptToken",
    value: function (t) {
        // u.default.encryptToken()
        return (0,
            f.default)(t).toString()  // f.default -> MD5
    }
}]