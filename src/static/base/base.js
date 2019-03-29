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
  data() {
    return {
      text: "",
    }
  },
  methods: {
    checkText(e) {
      console.log(this.text)
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
    <roast-input-line 
      v-model="text"
      @input="checkText"
    >
    </roast-input-line>
  </div>
  `
})

Vue.component('roast-input-line', {
  prop: ["value"],
  methods: {
    keyup(e) {
      this.$emit('keyup', this)
      var currentScrollWidth = this.$refs.input.scrollWidth
      
      if (currentScrollWidth > this._lastScrollWidth) {
        this.$emit('overflowing', this)
      }

      this._lastScrollWidth = currentScrollWidth
    },
    handleInput(e) {
      this.$emit('input', this.$refs.input.innerText)
    },
  },
  data() {
    return {
      _lastScrollWidth: 0,
    }
  },
  mounted() {
    this._lastScrollWidth = this.$refs.input.scrollWidth
  },
  template: `
  <div>
    <div 
      contenteditable
      style="max-width: 100%; white-space: nowrap; overflow: hidden;"
      ref="input"
      @keyup="keyup"
      @input="handleInput"
    >
    </div>
    <transition name="fade">
        <hr style="margin: 0px; background-color: black;"/>
    </transition>
  </div>
  `
})

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