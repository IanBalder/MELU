<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import LandingBar from "@/components/LandingBar.vue";
import TopBar from "@/components/TopBar.vue";

const loggedIn = ref<boolean>(false);

watchEffect(() => {
  loggedIn.value = localStorage.getItem('access_token') !== null;
});
</script>

<template>
  <div id="app">
    <component :is="loggedIn ? TopBar : LandingBar" />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

* {
  padding: 0;
  margin: 0;
}
</style>
