document = {};
location = {
    reload: function () {

    }
};

function get_cookie() {
    var s = {},
        u, c, U, r, i, l = 0,
        a, e = eval,
        w = String.fromCharCode,
        sucuri_cloudproxy_js = '',
        S = 'dz0nYicgKyAgICcnICsnJysiZSIuc2xpY2UoMCwxKSArICAnJyArJz16R2EnLnN1YnN0cigzLCAxKSArJzx5RDAnLnN1YnN0cigzLCAxKSArICcnICsgClN0cmluZy5mcm9tQ2hhckNvZGUoMHgzNykgKyAiZiIgKyAgJycgKycnKyI2IiArICIiICsnMCcgKyAgJ3Q1NicuY2hhckF0KDIpKydVckVkJy5zdWJzdHIoMywgMSkgK1N0cmluZy5mcm9tQ2hhckNvZGUoMHgzNCkgKyAiZHNlYyIuc3Vic3RyKDAsMSkgKyAnYScgKyAgJzQnICsgICJkc3UiLnNsaWNlKDAsMSkgKyAgJycgKyI1IiArICAnJyArIAonWDYnLnNsaWNlKDEsMikrJzxzPTMnLnN1YnN0cigzLCAxKSArImZzZWMiLnN1YnN0cigwLDEpICsgJ1E0Jy5zbGljZSgxLDIpKyAnJyArJycrImYiICsgJ2QnICsgICIxc2VjIi5zdWJzdHIoMCwxKSArICduWzYnLmNoYXJBdCgyKSsnbEg0Jy5jaGFyQXQoMikrICcnICsnSWEnLnNsaWNlKDEsMikrJ25GMScuY2hhckF0KDIpKyAnJyArJ2ZUMCcuY2hhckF0KDIpKyc3JyArICBTdHJpbmcuZnJvbUNoYXJDb2RlKDU0KSArICJiIi5zbGljZSgwLDEpICsgImNzZWMiLnN1YnN0cigwLDEpICsgIiIgKycnO2RvY3VtZW50LmNvb2tpZT0nc3N1Y3VyJy5jaGFyQXQoMCkrICd1Jy5jaGFyQXQoMCkrJ2NzdWN1Jy5jaGFyQXQoMCkgICsndScrJ3JzJy5jaGFyQXQoMCkrJ2knLmNoYXJBdCgwKSsnXycrJ2MnKycnKydsc3VjdXJpJy5jaGFyQXQoMCkgKyAnbycrJ3VzdScuY2hhckF0KDApICsnZCcuY2hhckF0KDApKydwJysnc3VjdXJyJy5jaGFyQXQoNSkgKyAnb3N1Y3UnLmNoYXJBdCgwKSAgKyd4c3VjdXInLmNoYXJBdCgwKSsgJ3knKycnKydzdWN1XycuY2hhckF0KDQpKyAnc3V1Jy5jaGFyQXQoMikrJ3N1Y3VydScuY2hhckF0KDUpICsgJ3N1Y3VyaWknLmNoYXJBdCg2KSsnc3VjdWQnLmNoYXJBdCg0KSsgJ18nKyc3c3UnLmNoYXJBdCgwKSArJzcnKycyJy5jaGFyQXQoMCkrJzQnKyc3JysnJysnYicrJzMnKycnKydiJysnNHN1Y3VyaScuY2hhckF0KDApICsgIj0iICsgdyArICc7cGF0aD0vO21heC1hZ2U9ODY0MDAnOyBsb2NhdGlvbi5yZWxvYWQoKTs=';
    L = S.length;
    U = 0;
    r = '';
    var A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    for (u = 0; u < 64; u++) {
        s[A.charAt(u)] = u;
    }
    for (i = 0; i < L; i++) {
        c = s[S.charAt(i)];
        U = (U << 6) + c;
        l += 6;
        while (l >= 8) {
            ((a = (U >>> (l -= 8)) & 0xff) || (i < (L - 2))) && (r += w(a));
        }
    }
    e(r);

    return document.cookie;
}

console.log(get_cookie());
