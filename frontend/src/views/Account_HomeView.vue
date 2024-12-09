
<script setup lang="ts">
import Bar from '@/components/Bar.vue';

</script>

<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
    </div>
    <div v-else>
      <!-- Popular Bars -->
      <div class="popular">
        <h1 class="text-popular">Popular</h1>
        <div class="popular-bars">
          <Bar
            v-for="bar in bars.slice(0, 3)"
            :key="bar.id"
            :bar="bar"
          />
        </div>
      </div>

      <!-- Cheap Bars -->
      <div class="cheap">
        <h1 class="text-cheap">Cheap</h1>
        <div class="cheap-bars">
          <Bar
            v-for="bar in bars.slice(3, 6)"
            :key="bar.id"
            :bar="bar"
          />
        </div>
      </div>

      <!-- Expensive Bars -->
      <div class="expensive">
        <h1 class="text-expensive">Expensive</h1>
        <div class="expensive-bars">
          <Bar
            v-for="bar in bars.slice(6, 9)"
            :key="bar.id"
            :bar="bar"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Popular */
.popular-bars {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.text-popular {
  margin: 20px;
  display: flex;
}

.popular {
  margin: 20px;
}

/* Cheap */
.cheap-bars {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.text-cheap {
  margin: 20px;
  display: flex;
}

.cheap {
  margin: 20px;
}

/* Expensive */
.expensive-bars {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.text-expensive {
  margin: 20px;
  display: flex;
}

.expensive {
  margin: 20px;
}
</style>

