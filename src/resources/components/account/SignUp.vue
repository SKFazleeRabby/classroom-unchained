<template>
    <div id="sign-up">
        <v-container>
            <v-layout row wrap>
                <v-flex xs8 offset-xs2 class="text-xs-center">
                    <v-form v-model="valid" ref="register" lazy-validation @submit.prevent="SignUp">
                        <v-text-field
                                label="First Name"
                                v-model="first_name"
                                :rules="fnameRules"
                                required
                        >
                        </v-text-field>
                        <v-text-field
                                label="Last Name"
                                v-model="last_name"
                                :rules="lnameRules"
                                required
                        >
                        </v-text-field>
                        <v-text-field
                                label="Email"
                                v-model="email"
                                :rules="emailRules"
                                type="email"
                                required
                        >
                        </v-text-field>
                        <v-text-field
                                label="Password"
                                v-model="password"
                                type="password"
                                :rules="passwordRules"
                                required
                        >
                        </v-text-field>
                        <v-btn type="submit" :disabled="!valid" flat large class="red accent-1 white--text">Sign Up
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
        name: "sign-up",
        data() {
            return {
                snackbar:false,
                snackbarMessage: '',
                valid: true,
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                fnameRules: [
                    v => !!v || 'First Name is required'
                ],
                lnameRules: [
                    v => !!v || 'Last Name is required'
                ],
                emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
                ],
                passwordRules: [
                    v => !!v || 'Password is required',
                    v => (v && v.length >= 8) || 'Password must be at least 8 characters'
                ],
                errors: null
            }
        },
        methods: {
            SignUp() {
                let user = {
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'email': this.email,
                    'password': this.password
                };
                this.$store.dispatch('registerTeacher', user)
                    .then(() => {
                        this.snackbarMessage = 'Successfully Registered. Please Login To Your Account.'
                        this.snackbar = true;
                        this.$refs.register.reset()
                    })
                    .catch(() => {
                        this.$refs.register.reset()
                    });
            }
        }
    }
</script>

<style scoped>

</style>