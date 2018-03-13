import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Account from '../components/Login'
import Login from '../components/account/SignIn'
import Register from '../components/account/SignUp'
import Navbar from '../components/Navbar'
import Classbar from '../components/classroom/Navbar'
import Discussion from '../components/classroom/Discussion'
import Classboard from '../components/classroom/Dashboard'
import Student from '../components/classroom/Student'
import Dashboard from '../components/dashboard/Dashboard'


Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            components: {
                default: Home,
                navbar: Navbar
            }
        },
        {
            path: '/account',
            redirect: '/account/login',
            name: 'Account',
            components: {
                default: Account,
                navbar: Navbar
            },
            children: [
                {
                    path: 'login',
                    name: 'Login',
                    component: Login
                },
                {
                    path: 'register',
                    name: 'Register',
                    component: Register
                }
            ]
        },
        {
            path: '/dashboard',
            name: 'Dashboard',
            components: {
                navbar: Navbar,
                default: Dashboard
            }
        },
        {
            path: '/classroom',
            components: {
                navbar: Classbar,
                default: Classboard,
            },
            children: [
                {
                    path: 'discussions',
                    name: 'Discussion',
                    component: Discussion
                },
                {
                    path: 'students',
                    name: 'Student',
                    component: Student
                }
            ]
        }
    ],
    mode: 'history'
})

