let URLS = {
    "index": "/",
    "beans": "/bean/:id"
}

const GetUrl = (url) => URLS[url.toLowerCase()];

export default GetUrl;