<template>
    <div id="sign-in">
        <v-container>
            <v-layout row wrap>
                <v-flex xs8 offset-xs2 class="text-xs-center">
                    <v-form v-model="valid" ref="form" lazy-validation>
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
                    </v-form>
                </v-flex>
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
                if (this.$refs.form.validate()) {
                    axios.post('/api/submit', {
                        name: this.name,
                        email: this.email,
                        select: this.select,
                        checkbox: this.checkbox
                    })
                }
            },
        }
    }
</script>

<style scoped>

</style>