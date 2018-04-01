<template>
    <div id="lecture">
        <v-app>
            <v-container>
                <v-layout wrap class="mb-3">
                    <v-flex xs6 offset-xs3>
                        <v-expansion-panel popout>
                            <v-expansion-panel-content>
                                <div slot="header"><h3>Post Your Problem</h3></div>
                                <v-card class="white">
                                    <v-form ref="postForm" v-model="valid" lazy-validation>
                                        <v-container>
                                            <v-text-field multi-line no-resize v-model="newPost.content"
                                                          placeholder="What's The Problem?" counter="500"
                                                          persistent-hint
                                                          hint="Problem should be more than 10 characters long">
                                            </v-text-field>
                                        </v-container>
                                        <v-card-actions>
                                            <v-container>
                                                <v-layout row wrap>
                                                    <v-flex md6 xs12>
                                                        <v-select :items="select_lectures" v-model="newPost.lecture_id"
                                                                  item-text="title"
                                                                  item-value="id"
                                                                  label="Select Related Lecture"
                                                                  min-width="400"
                                                                  auto
                                                                  single-line bottom>
                                                        </v-select>
                                                    </v-flex>
                                                    <v-spacer></v-spacer>
                                                    <v-flex md2 xs12>
                                                        <v-btn @click.stop="submit" :disabled="!postButton"
                                                               color="indigo"
                                                               class="white--text mt-3"> Post
                                                        </v-btn>
                                                    </v-flex>
                                                </v-layout>
                                            </v-container>
                                        </v-card-actions>
                                    </v-form>
                                </v-card>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-flex>
                </v-layout>
                <h1 class="text-xs-center" v-if="posts.length < 1"> No Post Yet</h1>
                <v-layout column wrap v-for="item in posts" :key="item.id" class="mb-5">
                    <v-flex xs6 offset-xs3>
                        <v-card class="white">
                            <v-card-title class="pb-0">
                                <v-layout fill-height>
                                    <v-flex xs1>
                                        <v-avatar>
                                            <img :src="item.user.details.image" alt="John Doe">
                                        </v-avatar>
                                    </v-flex>
                                    <v-flex xs10 class="px-3 py-1">
                                        <h3>{{ item.user.details.first_name }} {{ item.user.details.last_name }}
                                            <span class="posted_at grey--text">{{ item.created_at | moment("from")  }}</span>
                                        </h3>
                                        <v-spacer></v-spacer>
                                        <p class="grey--text">{{ item.lecture.title }}</p>
                                    </v-flex>
                                    <v-flex xs1>
                                        <v-menu offset-y>
                                            <v-btn icon fab small slot="activator">
                                                <v-icon>more_horiz</v-icon>
                                            </v-btn>
                                            <v-list>
                                                <v-list-tile @click="">
                                                    <v-list-tile-title>Edit</v-list-tile-title>
                                                </v-list-tile>
                                                <v-list-tile @click="">
                                                    <v-list-tile-title>Delete</v-list-tile-title>
                                                </v-list-tile>
                                            </v-list>
                                        </v-menu>
                                    </v-flex>
                                </v-layout>
                            </v-card-title>
                            <v-card-text class="pt-0">
                                <v-container>
                                    <p>
                                        {{ item.content }}
                                    </p>
                                </v-container>
                            </v-card-text>
                            <v-card tile class="grey lighten-3">
                                <v-flex xs12>
                                    <comment-form :post_id="item.id"></comment-form>
                                </v-flex>
                                <v-card-text>
                                    <v-layout row wrap v-for="comment in item.comments" :key="item.id + comment.id">
                                        <v-flex xs1 class="py-1">
                                            <v-avatar size="35px">
                                                <img :src="comment.user.details.image" alt="John Doe">
                                            </v-avatar>
                                        </v-flex>
                                        <v-flex xs10 class="px-1">
                                            <p class="comment"><span class="username">
                                                {{ comment.user.details.first_name + comment.user.details.last_name  }}</span>
                                                {{ comment.content }}</p>
                                        </v-flex>
                                        <v-flex xs1>
                                            <v-menu offset-y>
                                                <v-btn icon fab small slot="activator">
                                                    <v-icon>more_horiz</v-icon>
                                                </v-btn>
                                                <v-list>
                                                    <v-list-tile @click="">
                                                        <v-list-tile-title>Delete</v-list-tile-title>
                                                    </v-list-tile>
                                                </v-list>
                                            </v-menu>
                                        </v-flex>
                                    </v-layout>
                                </v-card-text>
                            </v-card>
                        </v-card>
                    </v-flex>
                </v-layout>
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
            </v-container>
        </v-app>
    </div>
</template>

<script>
    import axios from 'axios'
    import CommentForm from './Comment'

    export default {
        name: "lecture",
        components: {
            'comment-form': CommentForm
        },
        data() {
            return {
                valid: true,
                newPost: {
                    content: '',
                    lecture_id: null
                },
                select_lectures: [],
                comment: '',
                snackbar: false,
                snackbarMessage: ''
            }
        },
        created() {
            axios.get('http://dev.classunchained.com/api/classroom/' + this.$route.params.classroom + '/lecture/list/')
                .then(response => {
                    this.select_lectures = response.data;
                })
                .catch(error => {
                    console.log(error.response);
                });
        },
        mounted() {
            let url = 'http://dev.classunchained.com/api/post/' + this.$route.params.classroom + '/post';
            this.$store.dispatch('getAllPost', url);
        },
        methods: {
            submit() {
                if (this.$refs.postForm.validate()) {
                    let new_post = {
                        content: this.newPost.content,
                        url: 'http://dev.classunchained.com/api/post/' + this.$route.params.classroom + '/' +
                        this.newPost.lecture_id.toString() + '/post/'
                    };

                    this.$store.dispatch('createPost', new_post).then(() => {
                        this.snackbarMessage = 'Post Has been Created.';
                        this.snackbar = true;
                        this.newPost.content='';
                        this.newPost.lecture_id=null;
                    });
                }
            }
        },
        computed: {
            postButton() {
                return this.newPost.content.length > 10 &&
                    this.newPost.lecture_id != null;
            },
            posts() {
                return this.$store.getters.getAllPosts;
            }
        }
    }
</script>

<style scoped>
    .comment-btn {
        min-width: 30px;
        margin: 8px 0px;
    }

    .comment-btn:hover {
        background-color: #eee !important;
    }

    .username {
        font-weight: bold;
        margin-right: 5px;
    }

    .comment {
        background-color: white;
        padding: 15px;
        border-radius: 30px;
    }

    .posted_at {
        font-weight: lighter;
        font-size: 12px;
        margin-left: 5px;
    }

    .card__actions {
        background-color: #f3f3f3;
        padding: 0px;
        height: 90px;
    }

    .expansion-panel--inset .expansion-panel__container, .expansion-panel--popout .expansion-panel__container {
        max-width: 100%;
        padding: 5px;
        background-color: #f5f5f5 !important;
    }
</style>