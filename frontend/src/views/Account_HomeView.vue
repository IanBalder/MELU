<template>

  <!-- Popular -->
  <div class="popular">
    <h1 class="text-popular">Popular</h1>
    <div class="popular-bars">
      <Bar />
      <Bar />
      <Bar />
      <Bar />
      <Bar />
    </div>
  </div>

  <!-- Cheap -->
  <div class="cheap">
    <h1 class="text-cheap">Cheap</h1>
    <div class="cheap-bars">
      <Bar />
      <Bar />
      <Bar />
      <Bar />
      <Bar />
    </div>
  </div>

  <!-- Expensive -->
  <div class ="expensive">
    <h1 class="text-expensive">Expensive</h1>
    <div class="expensive-bars">
      <Bar />
      <Bar />
      <Bar />
      <Bar />
      <Bar />
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
  gap: 20px
}

.text-cheap {
  margin: 20px;
  display: flex;
}

.cheap{
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

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Bar from '@/components/Bar.vue'; // @ is an alias to /src

@Options({
  components: {
    Bar,
  },
})
export default class HomeView extends Vue {}
</script>
