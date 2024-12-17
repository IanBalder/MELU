<script setup lang="ts">
import BarPreview from "@/components/BarPreview.vue";
import axios from "axios";
import {onMounted, ref} from "vue";

const errorMsg = ref('');
const barsList = ref([]);

async function fetchBars() {

  try {
    const response = await axios.get("http://localhost:5000/api/fetch-bars");

    if (response.status === 200) {
      barsList.value = response.data;
    } else {
      console.log("Failed to fetch bars: "  + response.data);
    }

  } catch (err: any) {
    errorMsg.value = "Failed to fetch bars: " + err.message;
  }
}

onMounted(() => {
  fetchBars()
})

const errorMsg = ref('');
const barsList = ref([]);

async function fetchBars() {

  try {
    const response = await axios.get("http://localhost:5000/api/fetch-bars");

    if (response.status === 200) {
      barsList.value = response.data;
    } else {
      console.log("Failed to fetch bars: "  + response.data);
    }

  } catch (err: any) {
    errorMsg.value = "Failed to fetch bars: " + err.message;
  }
}

onMounted(() => {
  fetchBars()
})
</script>

<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">
      <p>{{ errorMsg }}</p>
    </div>
    <div v-else>
      <!--Popular Bars-->
      <div class="popular">
        <h1 class="text-popular">Popular</h1>
        <div class="popular-bars">
          <BarPreview
            v-for="bar in barsList"
            :key="bar.id"
            :barObject="bar"
          />
        </div>
      </div>

      <!-- Cheap Bars -->
      <div class="cheap">
        <h1 class="text-cheap">Cheap</h1>
        <div class="cheap-bars">
        </div>
      </div>

      <!-- Expensive Bars -->
      <div class="expensive">
        <h1 class="text-expensive">Expensive</h1>
        <div class="expensive-bars">
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
