import axios from "axios/index";

export default {
    setAxiosHeader(state) {
        axios.defaults.headers.common['Authorization'] = 'jwt ' + state.auth.token;
    },

    addAuthErrors(state, payload) {
        state.errors.register = payload;
    },

    authenticateUser(state) {
        state.auth.token = localStorage.getItem('token');
        state.auth.user = JSON.parse(localStorage.getItem('user'));
        state.auth.expire = localStorage.getItem('expire');
    },

    createClassroom(state, payload) {
        state.classrooms.unshift(payload);
    },

    allClassroom(state, payload) {
        state.classrooms = payload;
    },

    classroomDetail(state, payload) {
        state.classroomDetail = payload;
    },

    createLecture(state, payload) {
        state.lectures.unshift(payload);
    },

    allLectures(state, payload) {
        state.lectures = payload;
    },
}