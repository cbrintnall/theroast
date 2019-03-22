Vue.component('color-range', {
    // props: ['name'],
    data() {
        return {
            colors: [
                { color: "#FFD659", amount: 33},
                { color: "#7F5B5A", amount: 33},
                { color: "#403736", amount: 33},
            ],
        }
    },
    template: `
    <div class="progress">
        <div 
            v-for="c in this.colors"
            class="progress-bar" 
            role="progressbar"
            v-bind:style="{ width: amount + '%', backgroundColor: c.color }"
        >
        </div>
        <h1>Hello.</h1>
    </div>
    `
})