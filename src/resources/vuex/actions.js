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

    logoutUser() {
        console.log("Loggedout");
        auth.logout();
    },

    createClassroom({commit}, payload) {
        commit('setAxiosHeader');
        return new Promise((resolve, reject) => {
            axios.post('http://dev.classunchained.com/api/classroom/create/', payload)
                .then(response => {
                    let classroom = {
                        id: response.data.id,
                        title: response.data.title,
                        description: response.data.description,
                        code: response.data.code
                    };
                    commit('createClassroom', classroom);
                    resolve();
                })
                .catch(error => {
                    reject();
                });
        });
    },

    getAllClassroom({commit}) {
        commit('setAxiosHeader');
        axios.get('http://dev.classunchained.com/api/classroom/all/')
            .then(response => {
                commit('allClassroom', response.data);
                console.log(response);
            })
            .catch(error => {
                console.log(error.response)
            })
    },

    getClassroomDetails({commit}, payload) {
        commit('setAxiosHeader');
        axios.get('http://dev.classunchained.com/api/classroom/' + payload)
            .then(response => {
                commit('classroomDetail', response.data);
            })
            .catch(error => {
                if (error.response.status === 404) {
                    this.$route.push({name: 'Dashboard'});
                }
            })
    },

    createLecture({commit}, payload) {
        commit('setAxiosHeader');
        let classroom = payload.classroom;
        let lecture = {
            title: payload.title,
            description: payload.description
        };
        axios.post('http://dev.classunchained.com/api/classroom/' + classroom + '/lecture/create/',
            lecture).then(response => {
                commit('createLecture', response.data);
            })
            .catch(error => {
                console.log(error.response);
            })
    },

    getAllLectures ({commit}, payload) {
        axios.get('http://dev.classunchained.com/api/classroom/' + payload + '/lecture/')
            .then(response => {
                commit('allLectures', response.data);
            })
            .catch(error => {
                console.log(error.response);
            })
    }
}