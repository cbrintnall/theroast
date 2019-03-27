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
    showLine() { 
      this.focused = !this.focused; 
    },
    checkText(e) {
      console.log(this.text)
      console.log(e)
    }
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
    <input 
      v-model="text"
      style="visibility: hidden; height: 0%;"
    >
    <div ref="lines">
      <roast-input-line 
        v-model="text"
        @keyup="checkText"
      >
      </roast-input-line>
    </div>
    <transition name="fade">
      <hr v-if="focused" style="margin: 0px; background-color: black;" v-bind:style="{ width: this.width+'%' }" />
    </transition>
  </div>
  `
})

Vue.component('roast-input-line', {
  methods: {
    keyup(e) {
      this.$emit('keyup', e)
    }
  },
  template: `
  <div 
    contenteditable="true" 
    @keyup="keyup"
  >
  </div>
  `
})

    // <textarea @focus="showLine"
    //           @blur="showLine"
    //           @keyup="checkText"
    //           v-model="text"
    //           v-bind:placeholder="placeholder"
    //           v-bind:name="name"
    //           style="overflow: hidden; border: none; height: 100%; width: 100%;"
    //           v-if="!textarea"
    // ></textarea>

Vue.component('roast-image-upload', {
  props: ["name", "title", "buttonText"],
  computed: {
    btnText() {
      if (this.files.length > 0) {
        return "Change Files"
      }

      if (!this.buttonText) {
        return "Select Files"
      }

      return this.buttonText;
    }
  },
  data() {
    return {
      files: []
    }
  },
  methods: {
    toBase(item) {
      console.log(item)
      console.log(btoa(item))
      return btoa(item)
    },
    clickFileUpload() {
      this.$refs.imageInput.click()
    },
    getImageFromUpload(e) {
      var files = e.target.files
      var self = this

      for (var i = 0; i < files.length; i++) {
        var reader = new FileReader()

        reader.onload = function(f) {
          var item = f.target.result
          self.files.push(item)
        }

        reader.readAsDataURL(files[i])
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
    <hr v-if="files.length >= 1" />
    <button
      style="margin-top: 6px;"
      type="button" 
      class="btn btn-outline-dark"
      @click="clickFileUpload"
      v-if="files.length == 0"
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
      multiple
    >
    <div style="backgroundColor: none;">
      <img 
        v-for="file in files" 
        v-bind:src="file"
        width="100"
        height="100"
        class="shadow-lg p-3 mb-5"
        style="margin: 6px !important; padding: 8px !important;"
      >
      <br v-if="files.length >= 1" />
      <button
        type="button" 
        class="btn btn-outline-dark"
        @click="clickFileUpload"
        style="margin-top: 12px;"
        v-if="files.length >= 1"
      >
        {{ btnText }}
      </button>
    </div>
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