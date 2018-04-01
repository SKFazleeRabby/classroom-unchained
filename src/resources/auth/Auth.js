import axios from 'axios'
import {store} from '../vuex/index'

export const auth = {
    refreshVar: null,

    setToken(token, user, expire) {
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
        localStorage.setItem('expire', expire);
    },

    getToken() {
        var token = localStorage.getItem('token');
        var expiration = localStorage.getItem('expire');

        if (!token || !expiration) {
            return null;
        }

        if (Date.now() > Date.parse(expiration)) {
            this.logout();
            return null;
        }
        return token;
    },

    login(payload) {
        return new Promise((resolve, reject) => {
            axios.post('http://dev.classunchained.com/api/jwt/authentication/', payload)
                .then(response => {
                    this.setToken(response.data.token, response.data.user, response.data.exp);
                    this.continuousRefreshToken();
                    resolve();
                })
                .catch(error => {
                    reject();
                });
        });
    },

    isAuthenticated() {
        if (this.getToken()) {
            return true;
        }
        return false;
    },

    initialRefreshToken() {
        if (this.isAuthenticated()) {
            let timeout = Math.abs(Date.now() - Date.parse(localStorage.getItem('expire')));
            setTimeout(() => {
                this.RefreshToken();
            }, timeout);
        }
    },

    RefreshToken() {
        let token = {
            'token': localStorage.getItem('token')
        };
        axios.post('http://dev.classunchained.com/api/jwt/refresh/token', token)
            .then(response => {
                this.setToken(response.data.token, response.data.user, response.data.exp);
                store.commit('authenticateUser');
                if (!this.refreshVar){
                    this.continuousRefreshToken();
                }
            })
            .catch(error => {
                console.log(error.response);
            })
    },

    continuousRefreshToken() {
        if (this.isAuthenticated()) {
            this.refreshVar = setInterval(() => {
                this.RefreshToken();
            }, 240000);
            return;
        }
        clearInterval(this.refreshVar);
    },

    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        localStorage.removeItem('expire');
        this.continuousRefreshToken();
        store.commit('logoutUser');
    }
};