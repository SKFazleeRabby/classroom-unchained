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
                                    <v-container>
                                        <v-text-field multi-line no-resize placeholder="What's The Problem?">
                                        </v-text-field>
                                    </v-container>
                                    <v-card-actions>
                                        <v-container>
                                            <v-layout row wrap>
                                                <v-flex md4 xs12>
                                                    <v-select :items="select_lectures" v-model="selected_lectures"
                                                              label="Select"
                                                              single-line bottom>
                                                    </v-select>
                                                </v-flex>
                                                <v-spacer></v-spacer>
                                                <v-flex md2 xs12>
                                                    <v-btn color="indigo" class="white--text mt-3"> Post</v-btn>
                                                </v-flex>
                                            </v-layout>
                                        </v-container>
                                    </v-card-actions>
                                </v-card>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-flex>
                </v-layout>
                <v-layout column wrap v-for="item in posts" :key="item.content" class="mb-5">
                    <v-flex xs6 offset-xs3>
                        <v-card class="white">
                            <v-card-title class="pb-0">
                                <v-layout fill-height>
                                    <v-flex xs1>
                                        <v-avatar>
                                            <img :src="item.image" alt="John Doe">
                                        </v-avatar>
                                    </v-flex>
                                    <v-flex xs11 class="px-3 py-1">
                                        <h3>{{ item.posted_by }} <span class="posted_at grey--text">23 min ago</span>
                                        </h3>
                                        <v-spacer></v-spacer>
                                        <p class="grey--text">{{ item.lecture }}</p>
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
                                <v-card-title class="pb-0">
                                    <v-layout fill-height>
                                        <v-flex xs1>
                                            <v-avatar size="40px" class="pt-3">
                                                <img src="../../assets/johndoe.jpg" alt="John Doe">
                                            </v-avatar>
                                        </v-flex>
                                        <v-flex xs10 class="px-3">
                                            <v-text-field placeholder="Write Your Comment..." v-model="comment">
                                            </v-text-field>
                                        </v-flex>
                                        <v-flex xs1>
                                            <v-btn flat depressed class="comment-btn" fab>
                                                <v-icon>
                                                    send
                                                </v-icon>
                                            </v-btn>
                                        </v-flex>
                                    </v-layout>
                                </v-card-title>
                                <v-card-text>
                                    <v-layout row wrap v-for="comment in item.comments" :key="comment.comment">
                                        <v-flex xs1 class="py-1">
                                            <v-avatar size="35px">
                                                <img :src="comment.image" alt="John Doe">
                                            </v-avatar>
                                        </v-flex>
                                        <v-flex xs11 class="px-1">
                                            <p class="comment"><span class="username">{{ comment.commented_by }}</span>
                                                {{
                                                comment.comment }}</p>
                                        </v-flex>
                                    </v-layout>
                                </v-card-text>
                            </v-card>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    export default {
        name: "lecture",
        data() {
            return {
                selected_lectures: null,
                select_lectures: [
                    {text: 'Lecture 1'},
                    {text: 'Lecture 2'},
                    {text: 'Lecture 3'},
                    {text: 'Lecture 4'},
                    {text: 'Lecture 5'},
                    {text: 'Lecture 6'},
                    {text: 'Lecture 7'}
                ],
                comment: '',
                posts: [
                    {
                        'posted_by': 'Asif Mahmud Shuvo',
                        'image': '/static/images/johndoe.jpg',
                        'lecture': 'lecture1',
                        'content': 'Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no.',
                        'comments': [
                            {
                                'commented_by': 'Ahmad Ali Sany',
                                'image': '/static/images/johndoe.jpg',
                                'comment': 'This Post Sucks'
                            },
                            {
                                'commented_by': 'SK. Fazlee Rabby',
                                'image': '/static/images/johndoe.jpg',
                                'comment': 'This is no way to post a problem. Please come to class regularly to understand the contents.'
                            }
                        ]
                    },
                    {
                        'posted_by': 'Ahmad Ali Sany',
                        'image': '/static/images/johndoe.jpg',
                        'lecture': 'lecture1',
                        'content': 'Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no.',
                    }
                ]
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
    .expansion-panel--inset .expansion-panel__container, .expansion-panel--popout .expansion-panel__container{
        max-width: 100%;
        padding: 5px;
        background-color: #f5f5f5!important;
    }
</style>