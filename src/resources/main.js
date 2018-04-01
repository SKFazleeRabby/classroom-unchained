import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {store} from './vuex/index'
import Vuetify from 'vuetify'
import Moment from 'vue-moment'
import {auth} from './auth/Auth'
import '../node_modules/vuetify/dist/vuetify.min.css'

import './style.css'

Vue.use(Vuetify);
Vue.use(Moment);
Vue.config.devtools = true;


router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.authentication)) {
        if (!auth.isAuthenticated()) {
            return next({name: 'Login'});
        }
    }
    if (to.matched.some(record => record.meta.forVisitor)) {
        if (auth.isAuthenticated()) {
            return next({name: 'TeacherDashboard'});
        }
    }
    return next();
});


new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
    created() {
        this.$store.dispatch('refreshToken');
    }
});

