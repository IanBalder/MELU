<script lang="ts">
export default {
  name: 'barView'
}
</script>

<template>
  <div class="bar-card">
    <!-- Baaripilt -->
    <img src="https://images.squarespace-cdn.com/content/v1/66d86247519ea05910ef4f62/78bd1a77-13b8-4553-84c3-c000b0aa748c/GiltBar-36-2.jpg" alt="Bar Image" class="bar-image" />

    <!-- Nimi -->
    <div class="bar-name">Möku</div>
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

.bar-image{
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