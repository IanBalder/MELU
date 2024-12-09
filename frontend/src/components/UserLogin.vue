<script setup lang="ts">
import { loginUser } from "@/services/userService"; // Replace with your login service function
import { useRouter } from "vue-router";
import { ref } from "vue";

const router = useRouter();

const username = ref("");
const password = ref("");

const responseMessage = ref("");
const isError = ref(false);

async function login() {
  responseMessage.value = "";
  isError.value = false;

  if (!username.value || !password.value) {
    responseMessage.value = "Both fields are required.";
    isError.value = true;
    return;
  }

  try {
    const response = await loginUser({
      username: username.value,
      password: password.value,
    });

    if (response.status === 200) {
      responseMessage.value = "Login successful!";
      isError.value = false;
      router.push("/dashboard"); // Redirect to dashboard
    }
  } catch (error) {
    console.error("Error during login:", error);
    responseMessage.value = "Login failed. Please check your credentials.";
    isError.value = true;
  }
}
</script>

<template>
  <div class="content-container">
    <div class="container">
      <div class="logo">
        <img src="@/assets/logo.svg" alt="App Logo" />
      </div>

      <div class="auth-tabs">
        <router-link to="/login">Login</router-link>
      </div>

      <form @submit.prevent="login">
        <div class="form-group">
          <span class="icon">
            <img src="@/assets/human_logo.svg" alt="Username Icon" />
          </span>
          <input
            type="text"
            placeholder="Username"
            v-model="username"
            aria-label="Username"
            required
          />
        </div>
        <div class="form-group">
          <span class="icon">
            <img src="@/assets/lock.svg" alt="Password Icon" />
          </span>
          <input
            type="password"
            placeholder="Password"
            v-model="password"
            aria-label="Password"
            required
          />
        </div>

        <button type="submit" class="btn">Login</button>
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
  transition: border-bottom 0.3s ease;
}

.form-group .icon {
  position: absolute;
  left: 5px;
  top: 10px;
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

.error-message {
  color: red;
  font-size: 14px;
  margin-top: 5px;
}

/* Responsiivsus */
@media (max-width: 600px) {
  .content-container {
    height: auto;
    padding: 10px;
    position: relative;
  }

  .container {
    width: 90%;
    height: auto;
    padding: 20px;
    position: relative;
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

  .modal-open .container {
    border: none;
    box-shadow: none;
  }

  .modal-open .form-group input {
    border-bottom: none;
  }
    /* Jooned jäävad alles */
  .modal-open .form-group input {
    border-bottom: 2px solid #333; /* Lisa joon tagasi */
  }
}


</style>