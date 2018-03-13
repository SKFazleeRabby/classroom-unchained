<template>
    <div id="dashboard" class="mt-3">
        <v-app>
            <v-container>
                <h1 class="white text-xs-center py-4 mb-4">All Classrooms</h1>
                <v-btn color="indigo" dark bottom right fixed fab @click.stop="dialog=true" slot="activator">
                    <v-icon class="white--text">add</v-icon>
                </v-btn>
                <v-layout row wrap>
                    <v-flex md4 v-for="course in courses" :key="course.title" class="pa-2">
                        <v-card hover>
                            <v-card-media src="https://vuetifyjs.com/static/doc-images/parallax/material.jpg"
                                          height="200px">
                            </v-card-media>
                            <v-card-title primary-title>
                                <h3 class="headline">{{ course.title }}</h3>
                                <p class="grey--text">{{ course.description }}</p>
                            </v-card-title>
                            <v-container>
                                <v-layout row wrap>
                                    <v-btn class="indigo white--text">Visit Classroom</v-btn>
                                    <v-spacer></v-spacer>
                                    <v-chip color="indigo" text-color="white">
                                        <v-avatar>
                                            <v-icon>account_circle</v-icon>
                                        </v-avatar>
                                        {{ course.enrolled }} Students
                                    </v-chip>
                                </v-layout>
                            </v-container>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
            <v-dialog class="white" v-model="dialog" max-width="500px">
                <v-card>
                    <v-card-title>
                        <h2 class="text-xs-center">Create New Classroom</h2>
                    </v-card-title>
                    <v-container>
                        <v-form v-model="valid" ref="form" lazy-validation>
                            <v-text-field
                                    label="Title"
                                    v-model="title"
                                    type="text"
                                    :rules="titleRules"
                                    required
                            >
                            </v-text-field>
                            <v-text-field
                                    label="Description"
                                    v-model="description"
                                    required
                                    :rules="descriptionRules"
                                    type="text"
                            >
                            </v-text-field>
                            <p class="grey--text">eg. Spring 2018, Section: D</p>
                            <v-layout>
                                <v-spacer></v-spacer>
                                <v-btn @click="submit" :disabled="!valid" large depressed
                                       class="indigo white--text">
                                    Create
                                </v-btn>
                            </v-layout>
                        </v-form>
                    </v-container>
                </v-card>
            </v-dialog>
        </v-app>
    </div>
</template>

<script>
    export default {
        name: "dashboard",
        data() {
            return {
                dialog: false,
                valid: true,
                courses: [
                    {'title': 'Artificial Intelligence', 'description': 'Spring 2018, Section: D', 'enrolled': '32'},
                    {'title': 'Data Mining', 'description': 'Fall 2017, Section: G', 'enrolled': '14'},
                    {'title': 'Web Engineering Lab', 'description': 'Spring 2018, Section: D', 'enrolled': '40'},
                    {'title': 'Introduction to JavaScript', 'description': 'Summer 2016, Section: A', 'enrolled': '4'}
                ]
            }
        },
        methods: {
            submit() {
                if (this.$refs.form.validate()) {
                    axios.post('/api/submit', {
                        name: this.name,
                        email: this.email,
                        select: this.select,
                        checkbox: this.checkbox
                    });
                    this.dialog = false;
                }
            },
        }
    }
</script>

<style scoped>

</style>