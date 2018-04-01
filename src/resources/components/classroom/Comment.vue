<template>
    <v-card-title class="pb-0">
        <v-layout fill-height>
            <v-flex xs1>
                <v-avatar size="40px" class="pt-3">
                    <img src="../../assets/johndoe.jpg" alt="John Doe">
                </v-avatar>
            </v-flex>
            <v-flex xs10 class="px-3">
                <v-form v-model="valid" ref="commentForm" lazy-validation>
                    <v-text-field multi-line rows="1" auto-grow required
                                  placeholder="Write Your Comment..." v-model="comment">
                    </v-text-field>
                </v-form>
            </v-flex>
            <v-flex xs1>
                <v-btn flat depressed class="comment-btn" fab small :disabled="!commentButton" @click.stop="submitComment">
                    <v-icon>send</v-icon>
                </v-btn>
            </v-flex>
        </v-layout>
    </v-card-title>
</template>

<script>
    export default {
        name: "Comment",
        props: ['post_id'],
        data() {
            return {
                valid: true,
                comment: ''
            }
        },
        methods: {
            submitComment () {
                let payload = {
                    post_id: this.post_id,
                    url: 'http://dev.classunchained.com/api/post/' + this.post_id + '/comment/',
                    comment: this.comment
                };
                this.comment = '';
                this.$store.dispatch('createComment', payload);
            }
        },
        computed: {
            commentButton () {
                return this.comment.length > 0;
            }
        }
    }
</script>

<style scoped>

</style>