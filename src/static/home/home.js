Vue.component('color-range', {
    props: ['name'],
    data() {
        return {
            colors: [
                { color: "#FFD659", amount: 33.3},
                { color: "#7F5B5A", amount: 33.3},
                { color: "#403736", amount: 33.3},
            ],
        }
    },
    template: `
    <div class="progress">
        <div 
            v-for="c in this.colors"
            class="progress-bar" 
            role="progressbar"
            v-bind:style="{ width: c.amount + '%', backgroundColor: c.color }"
        >
        </div>
    </div>
    `
})

var EXISTS_REGEX = /(\w+)\ already exists/
var app = new Vue({
    el: '#home-app',
    delimiters: ["[[", "]]"],
    methods: {
        submitted() {
            this.loading = true;
        },
        done(response) {
            console.log(response)
            this.loading = false;
            this.submitText = "Done 😊"
            document.location.href = "/r/" + response.data.name
        },
        error(err) {
            if (err.response.status >= 300) {
                this.errors = err.response.data
            }

            this.loading = false;
            this.submitText = "Error 😞"
        }
    },
    data: {
        loading: false,
        submitText: "Submit",
        errors: {}
    }
})