import axios from "axios/index";
import {auth} from "../auth/Auth";

export default {
    setAxiosHeader(state) {
        axios.defaults.headers.common['Authorization'] = 'jwt ' + state.auth.token;
    },

    isAuthenticated(state) {
        state.auth.isAuthenticated = auth.isAuthenticated();
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

    createNewPost(state, payload) {
        state.posts.unshift(payload);
    },

    getAllPosts(state, payload) {
        state.posts = payload;
    },

    deletePost(state, payload) {
        state.posts.splice(state.posts.indexOf(state.posts.find(x => x.id === payload)), 1);
    },

    createNewComment(state, payload) {
        state.posts.find(x => x.id === payload.post).comments.unshift(payload.data);
    },

    deleteComment(state, payload) {
        let post = state.posts.find(x => x.id === payload.post_id);
        post.comments.splice(post.comments.indexOf(post.comments.find(x => x.id === payload.comment_id)), 1);
    },


    logoutUser(state) {
        state.auth.token = null;
        state.auth.expire = null;
        state.auth.user = null;
        state.auth.isAuthenticated = false;
    }
}