const jsdom = require("E:\\Web-Scraping\\NodeJS\\node_modules\\jsdom");
const { JSDOM } = jsdom;

const resourceLoader = new jsdom.ResourceLoader({
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
});

const html = "`<!DOCTYPE html><p>Hello world</p>`";
const dom = new JSDOM(html, {
    url: "https://www.toutiao.com",
    referrer: "https://example.com/",
    contentType: "text/html",
    resources: resourceLoader
});


window = global;

const params = {
    location: {
        hash: "",
        host: "www.toutiao.com",
        hostname: "www.toutiao.com",
        href: "http://www.toutiao.com",
        origin: "https://www.toutiao.com",
        pathname: "/",
        port: "",
        protocol: "https:",
        search: ""
    },
    navigator: {
        appCodeName: "Mozilla",
        appName: "Netscape",
        appVersion: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        cookieEnabled: true,
        deviceMemory: 8,
        doNotTrack: null,
        hardwareConcurrency: 4,
        language: "zh-CN",
        languages: ["zh-CN", "zh"],
        maxTouchPoints: 0,
        onLine: true,
        platform: "MacIntel",
        product: "Gecko",
        productSub: "20030107",
        userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        vendor: "Google Inc.",
        vendorSub: "",
        webdriver: false
    }
};


Object.assign(global, params)


// 在下面如果你使用
location.href
navigator.appCodeName
window.location.href
window.appCodeName

// console.log(dom.window.location);
// console.log(dom.window.navigator.userAgent);
// console.log(dom.window.document.referrer);

// npm install canvas --canvas_binary_host_mirror=https://registry.npmmirror.com/-/binary/canvas