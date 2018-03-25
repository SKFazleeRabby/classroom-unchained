import axios from 'axios'
import {auth} from '../auth/Auth'

export default {
    registerTeacher({commit}, payload) {
        let user = {
            'first_name': payload.first_name,
            'last_name': payload.last_name,
            'email': payload.email,
            'password': payload.password
        };
        return new Promise((resolve, reject) => {
            axios.post('http://dev.classunchained.com/api/user/register/', user)
                .then(response => {
                    console.log(response);
                    resolve();
                })
                .catch(function (error) {
                    console.log(error.response.data);
                    commit('addAuthErrors', error.response.data);
                    reject();
                });
        });
    },

    AuthenticateUser({commit}, payload) {
        auth.login(payload)
            .then(() => {
                commit('authenticateUser');
            })
            .catch(error => {
                console.log(error)
            });
    },

    // refreshToken(){
    //     auth.refreshToken();
    // },

    logoutUser(){
        console.log("Loggedout");
        auth.logout();
    }
}