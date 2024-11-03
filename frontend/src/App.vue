<template>
  <div id="app">
    <TopBar />
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


<script>
import axios from 'axios';
import TopBar from "@/components/TopBar.vue";

export default {
  name: 'App',
  components: {
    TopBar
  },

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

