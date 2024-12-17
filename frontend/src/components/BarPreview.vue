<script setup lang="ts">
import { useRouter } from "vue-router";
import { defineProps } from "vue";

const props = defineProps({
  barObject: {
    type: Object,
    required: true,
  },
});

const router = useRouter();

// Funktsioon, mis suunab uuele lehele
function goToBarMenu() {
  router.push({
    name: "barmenuview", // Kasutame marsruudi nime
    query: { id: props.barObject.id }, // Kasutame propsist saadavat barObject.id
  });
}

</script>

<template>
  <div class="bar-card" @click="goToBarMenu">
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
  cursor: pointer;
  transition: transform 0.2s ease-in-out;
}

.bar-card:hover {
  transform: scale(1.05);
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