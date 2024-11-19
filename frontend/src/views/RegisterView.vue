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
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: ''
    };
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f3ece6;
}

.content-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 550px;
}

.container {
  background-color: #fdfbf7;
  width: 450px;
  height: 500px;
  padding: 40px;
  text-align: center;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  border: 1px solid #000;
}

.logo img {
  width: 80px;
  margin-bottom: 20px;
}

.auth-tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.auth-tabs a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  font-size: 20px;
}

.auth-tabs a:hover {
  text-decoration: underline;
}

.form-group {
  margin: 15px 0;
  position: relative;
}

.form-group input {
  width: 100%;
  padding: 10px;
  padding-left: 30px;
  font-size: 16px;
  border: none;
  border-bottom: 2px solid #333;
  background: transparent;
}

.form-group .icon {
  position: absolute;
  left: 5px;
  top: 10px;
  font-size: 18px;
  color: #333;
}

.btn {
  background-color: #e7dfd6;
  border: none;
  padding: 10px;
  width: 100%;
  font-size: 18px;
  cursor: pointer;
  font-weight: bold;
  margin-top: 20px;
}

.btn:hover {
  background-color: #d8cec4;
}
</style>