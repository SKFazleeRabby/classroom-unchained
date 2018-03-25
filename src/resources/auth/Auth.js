import axios from 'axios'

export const auth = {
    refreshVar: null,

    setToken(token, user, expire) {
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
        localStorage.setItem('expire', expire);
    },

    login(payload) {
        return new Promise((resolve, reject) => {
            axios.post('http://dev.classunchained.com/api/jwt/authentication/', payload)
                .then(response => {
                    console.log(response.data);
                    this.setToken(response.data.token, response.data.user, response.data.exp);
                    resolve();
                    this.continuousRefreshToken();
                })
                .catch(error => {
                    reject(error.response)
                });
        });
    },

    // initialRefreshToken(timeout){
    //     return;
    // },

    RefreshToken(){
        let token = {
            'token': localStorage.getItem('token')
        };
        axios.post('http://dev.classunchained.com/api/jwt/refresh/token', token)
            .then(response => {
                this.setToken(response.data.token, response.data.user, response.data.exp);
                console.log(response.data);
            })
            .catch(error => {
                console.log(error.response);
            })
    },

    continuousRefreshToken() {
        if (localStorage.getItem('token')) {
            this.refreshVar = setInterval(() => { this.RefreshToken() }, 300000);
            return;
        }
        clearInterval(this.refreshVar);
    },

    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        localStorage.removeItem('expire');
        this.continuousRefreshToken();
    }
};