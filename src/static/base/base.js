function isOverflown(element) {
  return element.scrollHeight > element.clientHeight || element.scrollWidth > element.clientWidth;
}

Vue.component('form-label', {
  template: `
  <label style="width: 100%; margin: 0px;">
    <h3 style="margin: 0px;"><slot></slot></h3>
  </label>
  `
})

Vue.component('roast-input', {
  props: ["title", "placeholder", "name"],
  data() {
    return {
      _count: 0,
      lines: []
    }
  },
  mounted() {
    this.addLine()
  },
  methods: {
    onOverflow(e) {
      // var lastCharacter = this.text.charAt(this.text.length - 1)
      // var newText = this.text.substring(0, this.text.length - 1)

      // this.text = newText
      this.addLine()
    },
    addLine() {
      this.lines.push({"id": "line" + this._count++})
    },
    removeLine() {

    }
  },
  template:`
  <div>
    <label style="display: inline-block; margin-bottom: 0px;">
      <span style="margin-bottom: 0px; margin-right: 2px; font-size: 22px;">
        {{ title }}
      </span>
    </label>
    <input
      style="visibility: hidden; height: 0%;"
    >
    <div>
      <roast-input-line
        v-for="line in lines"
        ref="line.id"
        @overflowing="onOverflow"
      >
      </roast-input-line>
    </div>
  </div>
  `
})

Vue.component('roast-input-line', {
  props: ["name", "maxlength"],
  methods: {
    keyup(e) {
      this.$emit('keyup', this)
      var currentScrollWidth = this.$refs.input.scrollWidth
      
      if (currentScrollWidth > this._lastScrollWidth) {
        this.$emit('overflowing', e)
      }

      this._lastScrollWidth = currentScrollWidth
    },
    handleInput(e) {
      this.$emit('input', divContent)

      if (this.content.length >= this.maxlength) {
        this.$emit('overflowing', e)
        return;
      }

      var divContent = this.$refs.input.innerText;
      this.content = divContent;
    },
    keydown(e) {
      this.$emit('keydown', e)
    },
    onFocus(e) {
      this.$emit('focus', e)
      this.focused = true;
    },
    onBlur(e) {
      this.$emit('blur', e)
      this.focused = false;
    },
  },
  data() {
    return {
      _lastScrollWidth: 0,
      content: "",
      focused: false,
    }
  },
  mounted() {
    this._lastScrollWidth = this.$refs.input.scrollWidth
  },
  template: `
  <div>
    <input 
      v-bind:name="name"
      v-bind:maxlength="maxlength"
      :value="content"
      type="hidden"
    >
    <div 
      v-bind:maxlength="maxlength"
      ref="input"
      @keydown="keydown"
      @keyup="keyup"
      @input="handleInput"
      @focus="onFocus"
      @blur="onBlur"
      contenteditable
      class="bg-dark text-light"
      style="max-width: 100%; white-space: nowrap; overflow: hidden; background-color: "
    >
    </div>
    <transition name="fade">
        <hr v-if="focused" class="bg-light" style="margin: 0px;"/>
    </transition>
  </div>
  `
})

Vue.component('roast-image-upload', {
  props: ["name", "title", "buttonText"],
  computed: {
    btnText() {
      if (this.files.length > 0) {
        return "Add Files"
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
    clickFileUpload() {
      this.$refs.imageInput.click()
    },
    getImageFromUpload(e) {
      var files = e.target.files
      var self = this

      for (var i = 0; i < files.length; i++) {
        var reader = new FileReader()

        reader.onload = function(f) {
          var item = {
            "content" : f.target.result
          }
          self.files.push(item)
        }

        reader.readAsDataURL(files[i])
      }
    }
  },
  template:`
  <div>
    <form-label>
      {{ title }}
    </form-label>
    </label>
    <hr v-if="files.length >= 1" />
    <br v-if="files.length == 0" />
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
      <div>
        <img 
          v-for="file in files" 
          v-bind:src="file.content"
          width="100"
          height="100"
          class="shadow-lg p-3 mb-5"
          style="margin: 6px !important; padding: 8px !important;"
        >
      </div>
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
    <form v-bind:action="options.url" action="GET">
      <div class="input-group">
          <div class="input-group-prepend">
              <button 
                class="btn btn-secondary dropdown-toggle" 
                type="button" 
                data-toggle="dropdown" 
                aria-haspopup="true" 
                aria-expanded="false"
              >
                {{ options.name }}
              </button>
              <div class="dropdown-menu">
              </div>
          </div>
          <input type="text" class="form-control">
          <div class="input-group-append">
              <button class="btn btn-secondary" type="button">Search</button>
          </div>
      </div>
    </form>  
    `
});

var app = new Vue({
  el: "#app"
})