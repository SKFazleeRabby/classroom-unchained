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
            </v-toolbar-items>
        </v-toolbar>
        <v-navigation-drawer temporary
                             v-model="drawer"
                             absolute class="white">
            <v-list class="pt-0">
                <div v-for="item in menu" :key="item.route" :to="item.route">
                    <v-list-tile class="pa-2">
                        <v-list-tile-action>
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-divider class="grey lighten-4"></v-divider>
                </div>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>
    export default {
        name: "navbar",
        data() {
            return {
                drawer: null,
                menu: [
                    {
                        'icon': 'home',
                        'title': 'Home',
                        'route': '/'
                    },
                    {
                        'icon': 'lock_open',
                        'title': 'Login',
                        'route': '/account'
                    },
                    {
                        'icon': 'school',
                        'title': 'Classroom',
                        'route': '/dashboard'
                    },
                    {
                        'icon': 'exit_to_app',
                        'title': 'Logout',
                        'route': '/logout'
                    }
                ]
            }
        }
    }
</script>

<style scoped>

</style>