/*
    Expects a SEARCH object, as so:
    {
        name: "Roasts",
        url: "/url/to/search/roasts"
    }
*/

function isOverflown(element) {
  return element.scrollHeight > element.clientHeight || element.scrollWidth > element.clientWidth;
}

Vue.component('form-label', {
  template: `
  <label style="width: 100%;">
    <h2 style="border-bottom: 1px solid black;"><slot></slot></h2>
  </label>
  `
})

Vue.component('roast-input', {
  props: ["title", "placeholder", "name", "textarea"],
  data: function() {
    return {
      focused: false,
      text: "",
    }
  },
  methods: {
    showLine() { this.focused = !this.focused; },
    checkText(e) { }
  },  
  template:`
  <div>
    <span ref="invisibleTextHash" style="visibility: hidden; position: fixed;">
      {{ text }}
    </span>
    <label style="display: inline-block; margin-bottom: 0px;">
      <span style="margin-bottom: 0px; margin-right: 2px; font-size: 22px;">
        <strong>{{ title }}</strong>
      </span>
    </label>
    <input @focus="showLine"
           @blur="showLine"
           @keyup="checkText"
           v-model="text"
           v-bind:placeholder="placeholder"
           v-bind:name="name"
           style="overflow: hidden; border: none; height: 100%; width: 100%;"
           v-if="textarea"
    >
    <textarea @focus="showLine"
              @blur="showLine"
              @keyup="checkText"
              v-model="text"
              v-bind:placeholder="placeholder"
              v-bind:name="name"
              style="overflow: hidden; border: none; height: 100%; width: 100%;"
              v-if="!textarea"
    ></textarea>
    <transition name="fade">
      <hr v-if="focused" style="margin: 0px; background-color: black;" v-bind:style="{ width: this.width+'%' }" />
    </transition>
  </div>
  `
})

Vue.component('roast-image-upload', {
  props: ["name", "title", "buttonText"],
  computed: {
    btnText() {
      if (!this.buttonText) {
        return "Select Files"
      } else {
        return this.buttonText
      }
    }
  },
  methods: {
    clickFileUpload() {
      this.$refs.imageInput.click()
    },
    getImageFromUpload() {
      var reader = new FileReader();
      reader.onload = function() {
        console.log(this.$refs.imageInput.result)
      }
    }
  },
  template:`
  <div>
    <label style="display: inline-block; margin-bottom: 0px;">
      <span style="margin-bottom: 0px; margin-right: 2px; font-size: 22px;">
        <strong>{{ title }}</strong>
      </span>
    </label>
    <br />
    <button
      style="margin-top: 6px;"
      type="button" 
      class="btn btn-outline-dark"
      @click="clickFileUpload"
    >
      {{ btnText }}
    </button>
    <input 
      ref="imageInput" 
      style="display: none;" 
      v-bind:name="name" 
      type="file" 
      class="form-control-file" 
      id="image"
      @change="getImageFromUpload"
    >
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