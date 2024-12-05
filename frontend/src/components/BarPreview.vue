<script setup lang="ts">

import { defineProps } from "vue";

const props = defineProps({
  barObject: Object,
});


</script>


<template>
  <div class="bar-card">
    <img :src="barObject.image" alt="Bar Image" class="bar-image"/>
    <div class="bar-name">{{ barObject.name }}</div>
    <p>Address: {{ barObject.address }}</p>
    <p>Description: {{ barObject.description }}</p>
    <p>Open Hours: {{ barObject.open_hours }}</p>
  </div>
</template>


<style scoped>
.bar-card {
  width: 25%;
  max-width: 300px;
  background-color: #f0f0f0;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: left;
}

.bar-image {
  width: 100%;
  height: 100px;
  display: block;
}

.bar-name {
  padding: 20px;
  font-size: 1.5em;
  color: #333;
  font-weight: 300;
}
</style>
