<script setup lang="ts">
import {registerUser} from "@/services/userService";
import {useRouter} from "vue-router";
import {ref} from "vue";

const router = useRouter();

const username = ref('');
const email = ref('');
const password = ref('');

const responseMessage = ref('');
const isError = ref(false);
const emailError = ref('');

const validateEmail = (emailToCheck: string) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(emailToCheck);
};

async function register() {
  emailError.value = '';
  responseMessage.value = '';
  isError.value = false;

  // Validate email format
  if (!validateEmail(email.value)) {
    emailError.value = 'Invalid email format';
    return;
  }
  try {
    const response = await registerUser({
      username: username.value,
      email: email.value,
      password: password.value,
    });
    if (response.status === 201) {
      router.push('/explore');
      window.location.reload();
    }
  } catch (error) {
    console.error('Error during registration:', error);
    alert('Registration failed');
  }
}
</script>

<template>
  <div class="content-container">
    <div class="container">
      <div class="logo">
        <img src="@/assets/logo.svg">
      </div>

      <div class="auth-tabs">
        <router-link to="/register">Register</router-link>
      </div>

      <form @submit.prevent="register">
        <div class="form-group">
          <span class="icon"> <img src="@/assets/human_logo.svg"> </span>
          <input type="text" placeholder="Username" v-model="username">
        </div>
        <div class="form-group">
          <span class="icon"> <img src="@/assets/human_logo.svg"> </span>
          <input type="text" placeholder="Email" v-model="email">
          <p v-if="emailError" class="error-message" :style="{ color: isError ? 'green' : 'red' }">{{ emailError }}</p>
        </div>
        <div class="form-group">
          <span class="icon"> <img src="@/assets/lock.svg"> </span>
          <input type="password" placeholder="Password" v-model="password">
        </div>

        <button type="submit" class="btn">Create new account</button>
      </form>

      <p v-if="responseMessage" :style="{ color: isError ? 'red' : 'green' }">
        {{ responseMessage }}
      </p>

    </div>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
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

/* Responsiivsus */
@media (max-width: 600px) {
  .content-container {
    height: auto;
    padding: 10px;
  }

  .container {
    width: 90%;
    height: auto;
    padding: 20px;
  }

  .logo img {
    width: 60px;
  }

  .form-group input {
    font-size: 14px;
  }

  .btn {
    font-size: 16px;
    padding: 8px;
  }


  .form-group .icon {
    top: 5px;
    font-size: 22px;
  }
}

</style>
