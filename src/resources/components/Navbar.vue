<template>
    <div id="navbar">
        <v-toolbar class="px-3 white" flat height="70px">
            <v-toolbar-side-icon class="hidden-md-and-up" @click.stop="drawer=!drawer"></v-toolbar-side-icon>
            <v-toolbar-title class="logo">
                <router-link to="/">
                    ClassroomUnchained
                </router-link>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-btn flat v-for="item in menu" active-class="none"
                       :key="item.title" :to="item.route">
                    <v-icon left>{{ item.icon }}</v-icon>
                    {{ item.title }}
                </v-btn>
                <v-btn flat active-class="none" @click.stop="logout">
                    <v-icon left>exit_to_app</v-icon>
                    Logout
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-navigation-drawer temporary
                             v-model="drawer"
                             absolute class="white">
            <v-list class="pt-0">
                <div v-for="item in menu" :key="item.title" :to="item.route">
                    <v-list-tile class="pa-2">
                        <v-list-tile-action>
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </div>
                <v-list-tile>
                    <v-list-tile-action>
                        <v-icon>exit_to_app</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Logout</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>
    import {auth} from "../auth/Auth";

    export default {
        name: "navbar",
        data() {
            return {
                drawer: null,
                isAuth: false,
                menu: [
                    {
                        icon: 'home',
                        title: 'Home',
                        route: {name: 'Home'}
                    },
                    {
                        icon: 'lock_open',
                        title: 'Login',
                        route: {name: 'Login'}
                    },
                    {
                        icon: 'school',
                        title: 'Classroom',
                        route: {name: 'TeacherDashboard'}
                    },
                    {
                        icon: 'school',
                        title: 'Enrolled',
                        route: {name: 'StudentDashboard'}
                    }
                ]
            }
        },
        created () {
            this.$store.commit('isAuthenticated');
        },
        methods:{
            logout () {
                this.$store.dispatch('logoutUser');
                this.$router.push({name: 'Home'});
            }
        },
        computed: {
            authenticateOrRedirect(){
                if(! this.$store.getters.isAuthenticated) {
                    this.$router.push({name: 'Login'})
                }
            }
        }
    }
</script>

<style scoped>

</style>