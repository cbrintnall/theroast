Vue.component('color-range', {
    props: ['colors'],
    computed: {
        percent() {
            return ((1 / this.colors.length) * 100)
        }
    },
    data() {
        return {
            available_colors: ["#FF659"]
        }
    },
    methods: {
        getBackground(color) {
            return this.available_colors[0]
        },
    },
    template: `
    <div class="progress">
        <div 
            v-for="c in this.colors"
            class="progress-bar" 
            role="progressbar"
            v-bind:style="{ width: percent + '%', backgroundColor: getBackground(c.color) }"
        >
        </div>
    </div>
    `
})