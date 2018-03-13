<template>
    <div id="app">
        <router-view name="navbar">

        </router-view>
        <transition name="fade">
            <router-view default="{ name: 'Home' }">

            </router-view>
        </transition>
    </div>
</template>

<script>
    import Navbar from './components/Navbar'

    export default {
        name: 'app',
        components: {
            'navbar': Navbar
        },
        data() {
            return {}
        }
    }
</script>