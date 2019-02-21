var cRange = `
<div>
    <label>Color:</label>
    <label style="float: right;">
        {{ this.colors[this.index].name }}
    </label>
    <div class="progress">
        <div 
            v-for="c in this.colors"
            class="progress-bar" 
            role="progressbar"
            v-bind:style="{ width: percent + '%', backgroundColor: c.color }"
        >
        </div>
    </div>
    <input
        :name="name"
        class="form-control-range"
        id="formControlRange"
        type="range"
        v-model="count"
        min="1"
        max="100"
        step="1"
        v-on:change="setColorIndex"
    >
</div>
`

Vue.component('color-range', {
    props: ['name'],
    data() {
        return {
            colors: [
                { name: "Light", color: "#FFD659"},
                { name: "Medium", color: "#7F5B5A"},
                { name: "Dark", color: "#403736"},
            ],
            count: 0,
            index: 0,
        }
    },
    computed: {
        percent() {
            return ((1 / this.colors.length) * 100)
        }
    },
    methods: {
        setColorIndex() {
            var amt_names = this.colors.length
            this.index = Math.floor(this.count / this.percent)

            if (this.index < 0) {
                this.index = 0;
            }

            if (this.index > amt_names - 1) {
                this.index = amt_names - 1
            }
        },
    },
    template: cRange
})