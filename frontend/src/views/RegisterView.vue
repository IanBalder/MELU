<script>
import UserRegister from "@/components/UserRegister.vue";

export default {
  name: 'LoginPage',
  components: {UserRegister},
  data() {
    return {
      username: '',
      password: ''
    };
  },
};
</script>

<template>
  <div>
    <UserRegister />
  </div>
</template>