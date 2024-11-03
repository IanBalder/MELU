<script lang="ts">
export default {
  name: 'topBar',
}
</script>

<template>
  <nav>
    <router-link to="/">
      <img class="home-logo" src="../assets/logo.svg" alt="MELU logo">
    </router-link>
    <router-link class="login" to="/login">Login</router-link>
  </nav>
  <router-view/>
</template>

<style>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #F4F1EB;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
}

.login {
  width: 150px;
  height: 60px;
  background: #EFE2D4;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 1);
  border-radius: 15px;
  color: #333333;
  text-decoration: none;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 25px;
}
</style>