<template>
  <div>
    <h1>{{ message }}</h1>
    <button @click="fetchMessage">Fetch Message</button>
    <button @click="sendData">Send Data</button>
  </div>
</template>

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
      axios.get('http://127.0.0.1:5000/api/hello')
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

