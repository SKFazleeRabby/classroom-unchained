import Vuex from 'vuex'
import Vue from 'vue'
import getters from './getters'
import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        errors: {
            register: null
        },
        auth: {
            token: localStorage.getItem('token') || null,
            expire: localStorage.getItem('expire') || null,
            user: JSON.parse(localStorage.getItem('user')) || null,
            isAuthenticated: false,
        },
        classrooms: [],
        classroomDetail: {},
        lectures: [],
        posts: []
    },
    getters,
    mutations,
    actions,
});

