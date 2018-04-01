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
import Lecture from '../components/classroom/Lecture'
import Assignment from '../components/classroom/Assignment'
import Dashboard from '../components/dashboard/Dashboard'
import {auth} from "../auth/Auth";

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
            meta: {
                forVisitor: true
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
            path: '/teacher/dashboard',
            name: 'TeacherDashboard',
            components: {
                navbar: Navbar,
                default: Dashboard
            },
            meta: {
                authentication: true
            }
        },
        {
            path: '/teacher/classroom/:classroom',
            redirect: {name: 'Discussion'},
            name:'Classroom',
            components: {
                navbar: Classbar,
                default: Classboard,
            },
            meta: {
                authentication: true
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
                },
                {
                    path: 'lectures',
                    name: 'Lectures',
                    component: Lecture
                },
                {
                    path: 'assignments',
                    name: 'Assignments',
                    component: Assignment
                }
            ]
        }
    ],
    mode: 'history'
})

