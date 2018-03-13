<template>
    <div id="navbar">
        <v-parallax src="https://vuetifyjs.com/static/doc-images/parallax/material.jpg" height="350"
                    style="padding: 0px">
            <v-layout column align-center justify-center>
                <h1>Artificial Intelligence</h1>
                <h3 class="mt-2">Spring 2018, Section: D</h3>
            </v-layout>
        </v-parallax>
        <v-toolbar class="white px-5" flat height="70px">
            <v-toolbar-items class="hidden-sm-and-down px-5">
                <v-btn flat v-for="item in menu"
                       :key="item.title" :to="item.route" active-class="none" exact-active-class="tab-active">
                    {{ item.title }}
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>
    </div>
</template>

<script>
    export default {
        name: "navbar",
        data() {
            return {
                menu: [
                    {'title': 'Discussions', 'route': '/classroom/discussions'},
                    {'title': 'Lectures', 'route': '/classroom/lectures'},
                    {'title': 'Assignments', 'route': '/'},
                    {'title': 'Students', 'route': '/classroom/students'}
                ]
            }
        }
    }
</script>

<style scoped>
.tab-active{
    background-color: #eee !important;
}
</style>