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
    <div class="auth-links">
      <router-link class="auth-link" to="/login">Login</router-link>
      <router-link class="auth-link" to="/register">Register</router-link>
    </div>
  </nav>
  <router-view/>
</template>

<style>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #eeeeee;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
}

.auth-link {
  color: #333333;
  text-decoration: none;
  font-size: 25px;
  font-weight: bold;
}
.auth-link:hover {
  text-decoration: underline;
}

.auth-links {
  display: flex;
  gap: 30px;
  padding-right: 30px;
}
</style>
