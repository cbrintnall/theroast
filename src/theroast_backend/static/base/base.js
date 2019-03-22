/*
    Expects a SEARCH object, as so:
    {
        name: "Roasts",
        url: "/url/to/search/roasts"
    }
*/
Vue.component('roast-search', {
  props: ["options"],
  template: `
  <form class="form-inline my-2 my-lg-0" v-bind:action="options.url" action="GET">
    <div class="input-group">
        <div class="input-group-prepend">
        <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{{ options.name }}</button>
            <div class="dropdown-menu">
            </div>
        </div>
        <input type="text" class="form-control" aria-label="Text input with dropdown button">
        <div class="input-group-append">
            <button class="btn btn-outline-secondary" type="button">Search</button>
        </div>
    </div>
  </form>  
    `
});

var app = new Vue({
  el: "#app"
});