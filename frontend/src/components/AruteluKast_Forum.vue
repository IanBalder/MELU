<script setup lang="ts">

</script>

<template>
  <div class="arutelu-kast">
    <div class="header">
      <h2>Arutelu/teema nimi</h2>
    </div>
    <div class="description">
      <p>Lühike kirjeldus, mida see teema endast kujutab.</p>
    </div>
    <div class="comments">
      <span>"number" kommentaare</span>
    </div>
  </div>
</template>

<style scoped>
  .arutelu-kast {
  border: 1px solid #ddd;
  padding: 16px;
  border-radius: 8px;
  font-family: Arial, sans-serif;
}

.header h2 {
  font-size: 18px;
  margin: 0;
  color: #333;
}

.description p {
  margin: 8px 0;
  font-size: 14px;
  color: #666;
}

.comments span {
  font-size: 12px;
  color: #999;
}
</style>