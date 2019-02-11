Vue.component('search', {
    data: function() {
        return {

        }
    },
    template: `
    <form class="dropdown-menu p-4">
        <div class="form-group">
            <label for="exampleDropdownFormEmail2">Email address</label>
            <input>
        </div>
    </form>
    `
})

Vue.component('inner-topbar', {
    data: function() {
        return {
            message_title: "Welcome to The Roast!",
            message_main: "Search for shops or beans."
        }
    },
    template: `
    <div>
        <h4 class="text-white h3"> {{ message_title }} </h4>
        <span class="text-muted h5"> {{message_main}} </span>
        <div>
            <search>
            </search>
        </div>
    </div>
    `
})

Vue.component('topbar', {
    data: function() {
        return { 
            title: "The Roast"
        }
    },
    template: `
    <div class="pos-f-t">
        <div class="collapse" id="navbarToggleExternalContent">
            <div class="bg-dark p-4">
                <inner-topbar>
                </inner-topbar>
            </div>
        </div>
        <nav class="navbar navbar-dark bg-dark">
            <button 
                class="navbar-toggler" 
                type="button" 
                data-toggle="collapse" 
                data-target="#navbarToggleExternalContent" 
                aria-controls="navbarToggleExternalContent" 
                aria-expanded="false" 
                aria-label="Toggle navigation"
            >

            <!-- #TODO: Change this icon. -->
            <span class="navbar-toggler-icon"></span>
            </button>
        </nav>
    </div>
    `
})