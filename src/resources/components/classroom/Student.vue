<template>
    <div id="student">
        <v-app>
            <v-container>
                <v-layout wrap>
                    <v-flex xs8 offset-xs2>
                        <v-card class="white">
                            <v-card-title>
                                <h2 class="text-xs-center py-3">Student List</h2>
                            </v-card-title>
                            <v-container>
                                <v-list two-line v-for="(student, index) in students">
                                    <v-list-tile avatar>
                                        <v-list-tile-avatar class="pt-1">
                                            <img :src="student.image" alt="">
                                        </v-list-tile-avatar>
                                        <v-list-tile-content>
                                                <v-list-tile-title>{{ student.name }}</v-list-tile-title>
                                                <v-list-tile-sub-title>{{ student.email }}</v-list-tile-sub-title>
                                        </v-list-tile-content>
                                        <v-list-tile-action>
                                            <v-btn icon ripple>
                                                <v-icon color="grey lighten-1">cancel</v-icon>
                                            </v-btn>
                                        </v-list-tile-action>
                                    </v-list-tile>
                                    <v-divider v-if="index!=students.length-1"></v-divider>
                                </v-list>
                            </v-container>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    export default {
        name: "student",
        data() {
            return {
                students: [
                    {
                        'name': 'SK. Fazlee Rabby',
                        'image': '/static/images/johndoe.jpg',
                        'email': 'fazleerabby@gmail.com'
                    },
                    {
                        'name': 'Asif Mahmud Shuvo',
                        'image': '/static/images/johndoe.jpg',
                        'email': 'asifmahmud@gmail.com'
                    },
                    {'name': 'Ahmad Ali Sany', 'image': '/static/images/johndoe.jpg', 'email': 'ahmadali@gmail.com'},
                    {
                        'name': 'Pranta Kumer Bhuiyan',
                        'image': '/static/images/johndoe.jpg',
                        'email': 'prantakumer@gmail.com'
                    },
                    {
                        'name': 'Shahed Uddin Emon',
                        'image': '/static/images/johndoe.jpg',
                        'email': 'shahedemon@gmail.com'
                    }
                ]
            }
        }
    }
</script>

<style scoped>
    .card__title {
        background-color: #eee;
    }
</style>