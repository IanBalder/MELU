<script lang="ts">
import { defineComponent } from "vue";
import { fetchBars } from "@/services/barService";

export default defineComponent({
  name: "BarComponent",
  data() {
    return {
      bars: [] as Array<{
        id: number;
        name: string;
        address: string;
        description: string;
        open_hours: string;
        image: string;
      }>,
      loading: true,
      error: null as string | null,
    };
  },
});
</script>

<template>
  <div class="bar-card">
    <img :src="bar.image" alt="Bar Image" class="bar-image"/>
    <div class="bar-name">{{ bar.name }}</div>
    <p>Address: {{ bar.address }}</p>
    <p>Description: {{ bar.description }}</p>
    <p>Open Hours: {{ bar.open_hours }}</p>
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
