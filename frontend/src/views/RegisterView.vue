<template>
  <div class="content-container">
    <div class="container">
      <div class="logo">
        <img src="@/assets/logo.svg">
      </div>

      <div class="auth-tabs">
        <router-link to="/register">Register</router-link>
      </div>

      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <span class="icon"> <img src="@/assets/human_logo.svg"> </span>
          <input type="text" placeholder="Username" v-model="username">
        </div>
        <div class="form-group">
          <span class="icon"> <img src="@/assets/human_logo.svg"> </span>
          <input type="text" placeholder="Email" v-model="email">
        </div>
        <div class="form-group">
          <span class="icon"> <img src="@/assets/lock.svg"> </span>
          <input type="password" placeholder="Password" v-model="password">
        </div>
        <div class="form-group">
          <span class="icon"> <img src="@/assets/lock.svg"> </span>
          <input type="password" placeholder="Password" v-model="password_vol2">
        </div>

        <button type="submit" class="btn">Create new account</button>
      </form>
    </div>
  </div>
</template>

<script>
import UserRegister from "@/components/UserRegister.vue";

export default {
  name: 'LoginPage',
  components: {UserRegister},
  data() {
    return {
      username: '',
      password: ''
    };
  },
};
</script>

<template>
  <div>
    <UserRegister />
  </div>
</template>