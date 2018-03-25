export default {
    addAuthErrors(state, payload) {
        state.errors.register = payload;
    },

    authenticateUser(state) {
        state.auth.token = localStorage.getItem('token');
        state.auth.user = JSON.parse(localStorage.getItem('user'));
        state.auth.expire = localStorage.getItem('expire');
    }
}