<template>
    <div id="dashboard" class="mt-3">
        <v-app>
            <v-container>
                <h1 class="white text-xs-center py-4 mb-4">All Classrooms</h1>
                <h1 class="text-xs-center my-5" v-if="courses.length < 1">Create Your First Classroom</h1>
                <v-btn color="indigo" dark bottom right fixed fab @click.stop="dialog=true" slot="activator">
                    <v-icon class="white--text">add</v-icon>
                </v-btn>
                <v-layout row wrap>
                    <v-flex md4 v-for="course in courses" :key="course.id" class="pa-2">
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
                                    <v-btn class="indigo white--text" @click="visitClassroom(course.id)">Visit Classroom</v-btn>
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
                        <v-form v-model="valid" ref="classroomform" lazy-validation>
                            <v-text-field
                                    label="Title"
                                    v-model="classroom.title"
                                    type="text"
                                    :rules="rules.titleRules"
                                    required
                            >
                            </v-text-field>
                            <v-text-field
                                    label="Description"
                                    v-model="classroom.description"
                                    required
                                    :rules="rules.descriptionRules"
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

            <v-snackbar
                    bottom
                    multi-line
                    :timeout=6000
                    v-model="snackbar"
            >
                {{ snackbarMessage }}
                <v-btn icon flat color="pink" @click.native="snackbar = false">
                    <v-icon>close</v-icon>
                </v-btn>
            </v-snackbar>
        </v-app>
    </div>
</template>

<script>
    export default {
        name: "dashboard",
        data() {
            return {
                dialog: false,
                snackbar: false,
                snackbarMessage: '',
                valid: true,
                classroom: {
                    title: '',
                    description: ''
                },
                rules: {
                    titleRules: [
                        v => !!v || 'Title is required.'
                    ],
                    descriptionRules: [
                        v => !!v || 'Description is required.',
                        v => v.length > 9 || 'Description must be at least 10 characters long.'
                    ]
                }
            }
        },
        computed: {
            courses() {
                return this.$store.getters.getAllClassroom;
            }
        },
        mounted() {
            this.$store.dispatch('getAllClassroom');
        },
        methods: {
            submit() {
                if (this.$refs.classroomform.validate()) {
                    this.$store.dispatch('createClassroom', this.classroom)
                        .then(() => {
                            this.snackbarMessage = 'Classroom Has Been Successfully Created.';
                            this.snackbar = true;
                        });
                    this.dialog = false;
                }
            },
            visitClassroom (id) {
                this.$router.push({name: 'Classroom', params:{classroom: id}});
            }
        }
    }
</script>

<style scoped>

</style>