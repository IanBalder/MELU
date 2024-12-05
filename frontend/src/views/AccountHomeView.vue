<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Bar from "@/components/Bar.vue"; // @ is an alias to /src
import axios from "axios";

@Options({
  components: {
    Bar,
  },
})
export default class HomeView extends Vue {
  bars: Array<{
    id: number;
    name: string;
    address: string;
    description: string;
    open_hours: string;
    image: string;
  }> = [];
  loading = true;
  error: string | null = null;

  async fetchBars() {
    try {
      const response = await axios.get("/api/fetch-bars");
      this.bars = response.data.bars;
    } catch (err: any) {
      this.error = "Failed to fetch bars: " + err.message;
    } finally {
      this.loading = false;
    }
  }

  created() {
    this.fetchBars();
  }
}
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
