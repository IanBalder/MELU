<script setup lang="ts">
import { ref } from 'vue';
import UserRegister from "@/components/UserRegister.vue";

const username = ref('');
const password = ref('');
</script>

<template>
  <div>
    <UserRegister />
  </div>
</template>