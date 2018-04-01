<template>
    <div id="sign-in">
        <v-container>
            <v-layout row wrap>
                <v-flex xs8 offset-xs2 class="text-xs-center">
                    <v-form v-model="valid" ref="signInForm" lazy-validation>
                        <v-text-field
                                label="Email"
                                v-model="email"
                                type="email"
                                :rules="emailRules"
                                required
                        >
                        </v-text-field>
                        <v-text-field
                                label="Password"
                                v-model="password"
                                required
                                :rules="passwordRules"
                                type="password"
                        >
                        </v-text-field>
                        <v-btn @click="submit" :disabled="!valid" large flat depressed class="red accent-1 white--text">
                            Login
                        </v-btn>
                        <v-btn @click="verify" large flat depressed class="red accent-1 white--text">
                            Verify
                        </v-btn>
                    </v-form>
                </v-flex>
                <v-snackbar :timeout=6000 v-model="snackbar" multi-line bottom>
                    {{ snackbarMessage }}
                    <v-btn icon flat color="pink" @click.native="snackbar = false">
                        <v-icon>close</v-icon>
                    </v-btn>
                </v-snackbar>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        name: "sign-in",
        data() {
            return {
                valid: true,
                snackbar: false,
                snackbarMessage: '',
                email: '',
                password: '',
                emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
                ],
                passwordRules: [
                    v => !!v || 'Password is required',
                ]
            }
        },
        methods: {
            submit() {
                if (this.$refs.signInForm.validate()) {
                    let authenticatedData = {
                        'email': this.email,
                        'password': this.password
                    };
                    this.$store.dispatch('AuthenticateUser', authenticatedData).then(() => {
                        this.$router.push({name: 'TeacherDashboard'});
                    }).catch(() => {
                        this.snackbarMessage = 'Email or Password is wrong.';
                        this.snackbar = true;
                    });
                    this.$refs.signInForm.reset();
                }
            },
            verify() {
                let token = this.$store.state.auth.token;
                let expire = new Date(this.$store.state.auth.expire);
                let now = new Date();
                console.log(expire - now);
            }
        }
    }
</script>

<style scoped>

</style>