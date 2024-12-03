<script setup lang="ts">
import { ref } from 'vue';
import UserLogin from "@/components/UserLogin.vue";

const username = ref('');
const password = ref('');
</script>

<template>
  <div>
    <UserLogin />
  </div>
</template>