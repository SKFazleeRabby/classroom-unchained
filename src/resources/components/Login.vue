<template>
    <div id="login">
        <v-container class="mt-5">
            <v-layout justify-center>
                <v-flex sm6 xs12>
                    <v-card class="white" tile style="max-height: 475px">
                        <v-card-title>
                            <v-layout row wrap>
                                <v-flex xs6>
                                    <router-link to="/account/login">
                                        <h2 class="text-xs-center">Login</h2>
                                    </router-link>
                                </v-flex>
                                <v-flex xs6>
                                    <router-link to="/account/register">
                                        <h2 class="text-xs-center">Register</h2>
                                    </router-link>
                                </v-flex>
                            </v-layout>
                        </v-card-title>

                        <v-container class="justify-center">
                            <transition name="fade">
                                <router-view>

                                </router-view>
                            </transition>
                        </v-container>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        name: "login",
        data() {
            return {
                valid: true,

            }
        }
    }
</script>

<style scoped>

</style>