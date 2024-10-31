<template>
  <div>
    <h1>{{ message }}</h1>
    <button @click="fetchMessage">Fetch Message</button>
    <button @click="sendData">Send Data</button>
  </div>

  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
    };
  },
  methods: {
    fetchMessage() {
      axios.get('http://127.0.0.1:5000/')
        .then(response => {
          this.message = response.data.message;
        })
        .catch(error => {
          console.error("There was an error fetching the message!", error);
        });
    },
    sendData() {
      axios.post('http://127.0.0.1:5000/api/data', {
        myData: 'This is some data!'
      })
      .then(response => {
        console.log("Data sent successfully:", response.data);
      })
      .catch(error => {
        console.error("There was an error sending the data!", error);
      });
    }
  }
};
</script>

