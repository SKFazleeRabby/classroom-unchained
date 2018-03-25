import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { store } from './vuex/index'
import Vuetify from 'vuetify'
import '../node_modules/vuetify/dist/vuetify.min.css'

import './style.css'

Vue.use(Vuetify);

Vue.config.devtools=true;

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
    // created() {
    //     this.$store.dispatch('refreshToken');
    // }
});
