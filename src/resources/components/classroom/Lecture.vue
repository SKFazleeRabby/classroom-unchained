<template>
    <v-app id="lecture">
        <v-content>
            <v-container>
                <v-layout>
                    <v-flex sm8 offset-sm2>
                        <v-expansion-panel class="elevation-0">
                            <v-expansion-panel-content v-for="(lecture, index) in lectures" :key="lecture.id"
                                                       class="mb-4 pa-2 elevation-2" :value="index===0">
                                <div slot="header">
                                    <h2>{{ lecture.title }}</h2>
                                </div>
                                <v-divider></v-divider>
                                <v-card>
                                    <v-container>
                                        <h4 class="subheader mb-0">Description</h4>
                                        <v-card-text class="pt-0">
                                            {{ lecture.description }}
                                        </v-card-text>
                                        <h4 v-if="lecture.content.length>0" class="subheader">Contents</h4>
                                        <v-card-text v-if="lecture.content.length>0" v-for="content in lecture.content"
                                                     class="pt-0" :key="lecture.id+content.id">
                                            <v-card class="grey lighten-3">
                                                <v-container>
                                                    <v-layout row>
                                                        <v-flex xs10>
                                                            <v-card-title>
                                                                <h4>A Handbook to Learn Your Knowledge.pdf</h4>
                                                            </v-card-title>
                                                        </v-flex>
                                                        <v-spacer></v-spacer>
                                                        <v-flex xs1>
                                                            <v-btn icon flat>
                                                                <v-icon>close</v-icon>
                                                            </v-btn>
                                                        </v-flex>
                                                    </v-layout>
                                                </v-container>
                                            </v-card>
                                        </v-card-text>
                                        <v-divider></v-divider>
                                    </v-container>
                                    <v-card-actions>
                                        <v-btn color="indigo" dark large>
                                            <v-icon left>add</v-icon>
                                            Add Content
                                        </v-btn>
                                        <v-spacer></v-spacer>
                                        <v-btn icon fab @click.stop="editLecture(lecture)">
                                            <v-icon>edit</v-icon>
                                        </v-btn>
                                        <v-btn icon fab>
                                            <v-icon>delete</v-icon>
                                        </v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-flex>
                </v-layout>
                <v-btn fab dark fixed right bottom icon color="indigo" @click.stop="createLecture">
                    <v-icon>add</v-icon>
                </v-btn>
            </v-container>
            <v-dialog v-model="dialog.show" max-width="600">
                <v-card>
                    <v-container>
                        <v-card-title class="header"><h2>{{ dialog.header }}</h2></v-card-title>
                        <v-card-text>
                            <v-form ref="lectureForm" v-model="valid" lazy-validation>
                                <v-text-field
                                        label="Title"
                                        v-model="dialog.lectureTitle"
                                        :rules="rules.lectureTitle"
                                        required
                                >
                                </v-text-field>
                                <v-text-field
                                        label="Description"
                                        multi-line
                                        rows="5"
                                        no-resize
                                        v-model="dialog.lectureDescription"
                                        :rules="rules.lectureDescription"
                                        :counter="200"
                                        required
                                >
                                </v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn @click="submit" color="indigo" dark>{{ dialog.button }}</v-btn>
                        </v-card-actions>
                    </v-container>
                </v-card>
            </v-dialog>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        name: "lecture",
        data() {
            return {
                valid: true,
                dialog: {
                    show: false,
                    header: 'Create New Lecture',
                    button: 'Create Lecture',
                    action: 'create',
                    lectureTitle: '',
                    lectureDescription: ''
                },
                rules: {
                    lectureTitle: [
                        v => !!v || 'Please enter lecture title.'
                    ],
                    lectureDescription: [
                        v => !!v || 'Please enter a lecture description',
                        v => !!v && v.length > 9 || 'Use at least 8 characters to describe.'
                    ]
                }
            }
        },
        created() {
            this.$store.dispatch('getAllLectures', this.$route.params.classroom);
        },
        methods: {
            editLecture(lecture) {
                this.$refs.lectureForm.reset();
                this.dialog.header = 'Edit Lecture';
                this.dialog.button = 'Update Lecture';
                this.dialog.action = 'update';

                this.dialog.lectureTitle = lecture.title;
                this.dialog.lectureDescription = lecture.description;
                this.dialog.show = true;
            },
            createLecture() {
                this.$refs.lectureForm.reset();
                this.dialog.header = 'Create New Lecture';
                this.dialog.button = 'Create Lecture';
                this.dialog.action = 'create';
                this.dialog.show = true;
            },
            submit() {
                if (this.$refs.lectureForm.validate()) {
                    let lecture = {
                        classroom: this.$route.params.classroom,
                        title: this.dialog.lectureTitle,
                        description: this.dialog.lectureDescription
                    };
                    if (this.dialog.action === 'create') {
                        this.$store.dispatch('createLecture', lecture);
                    }
                    else if (this.dialog.action === 'update') {
                        return;
                    }
                    this.dialog.show = false;
                    this.$refs.lectureForm.reset();
                }
            }
        },
        computed: {
            lectures() {
                return this.$store.getters.getAllLecutres;
            }
        }
    }
</script>

<style scoped>

</style>