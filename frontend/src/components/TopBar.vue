<script lang="ts">
export default {
  name: 'topBar',
  methods: {
    closeMenu() {
      const menuToggle = document.getElementById('menu-toggle') as HTMLInputElement;
      if (menuToggle) {
        menuToggle.checked = false;
      }
    }
  }
}
</script>

<template>
  <nav>
    <router-link to="/">
      <img class="home-logo" src="../assets/logo.svg" alt="MELU logo">
    </router-link>

    <input type="checkbox" id="menu-toggle" class="menu-toggle">
    <label for="menu-toggle" class="hamburger">☰</label>

    <div class="auth-links">
      <router-link class="auth-link" to="/explore">Explore</router-link>
      <router-link class="auth-link" to="/profile">Profile</router-link>
      <router-link class="auth-link" to="/about">Contacts</router-link>
    </div>

    <div class="close-menu" @click="closeMenu">✖</div>
  </nav>
  <router-view/>
</template>

<style>
/* Üldine stiil nav jaoks */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #eeeeee;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
}

/* Logo paigutus */
.home-logo {
  max-width: 150px;
}

.auth-link {
  color: #333333;
  text-decoration: none;
  font-size: 25px;
  font-weight: bold;
}

.auth-link:hover {
  text-decoration: underline;
}

.auth-links {
  display: flex;
  gap: 30px;
  padding-right: 30px;
  margin-left: auto;
}

/* Hamburger nupp */
.hamburger {
  display: none;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
  position: absolute;
  right: 20px;
  top: 15px;
  z-index: 2;
  transition: opacity 0.3s ease, visibility 0.3s ease;
  color: #3e3e3e;
}

.menu-toggle:checked + .hamburger {
  opacity: 0;
  visibility: hidden;
}

.menu-toggle {
  display: none;
}

/* Kaldristi nupp */
.close-menu {
  display: none;
  position: absolute;
  top: 5px;
  right: 20px;
  font-size: 30px;
  cursor: pointer;
  color: #333333;
  font-weight: bold;
  transition: opacity 0.4s ease, right 1s ease;
  opacity: 0;
  z-index: 1000;
}

/* Responsiivsus */
@media (max-width: 768px) {
  nav {
    justify-content: center;
  }

  .auth-links {
    position: fixed;
    top: 0;
    right: -100%;
    width: 300px;
    height: 100vh;
    background-color: #eeeeee;
    padding: 20px;
    transition: right 0.3s ease;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    flex-direction: column;
    gap: 20px;
    z-index: 1000;
  }

  .hamburger {
    display: block;
  }

  .menu-toggle:checked + .hamburger + .auth-links {
    right: 0;
  }

  .close-menu {
    display: block;
  }

  .menu-toggle:checked ~ .close-menu {
    opacity: 1;
    right: 20px;
  }
}
</style>
