/*
    Expects a SEARCH object, as so:
    {
        name: "Roasts",
        url: "/url/to/search/roasts"
    }
*/

Vue.component('form-label', {
  template: `
  <label style="width: 100%;">
    <h2 style="border-bottom: 1px solid black;"><slot></slot></h2>
  </label>
  `
})

Vue.component('roast-input', {
  props: ["title", "placeholder"],
  data: function() {
    return {
      focused: false,
    }
  },
  methods: {
    showLine() {
      this.focused = !this.focused;
    }
  },  
  template:`
  <div>
    <label style="display: inline-block; margin-bottom: 0px;">
      <span style="margin-bottom: 0px; margin-right: 2px; font-size: 22px;">
        <strong>{{ title }}</strong>
      </span>
    </label>
    <input @mouseover="showLine" @mouseout="showLine" type="text" v-bind:placeholder="placeholder" style="display: inline-block; border: none; height: 100%;">
    <transition name="fade">
      <hr v-if="focused" style="margin: 0px; background-color: black;" v-bind:style="{ width: this.width+'%' }" />
    </transition>
  </div>
  `
})

Vue.component('roast-textarea', {
  props: ["title", "placeholder"],
  template:`
  <div>
    <label style="display: inline-block; margin-bottom: 0px;">
      <span style="margin-bottom: 0px; margin-right: 2px; font-size: 22px;">
        <strong>{{title}}</strong>
      </span>
    </label>
    <textarea type="text" style="display: inline-block; border: none; height: 100%;">{{placeholder}}</textarea>
    <hr style="margin: 0px; background-color: black;" />
  </div>
  `
})

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