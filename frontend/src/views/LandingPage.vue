<script setup lang="ts">

</script>

<template>
  <div class="landing-page">
    <!-- Hero Section -->
    <header class="hero">
      <div class="hero-content">
        <h1>Welcome to Our Website!</h1>
        <p>Discover amazing features and places.</p>
      </div>
    </header>

    <!-- Features Section -->
    <section class="features">
      <h2>What are we offering?</h2>
      <div class="feature-grid">
        <div class="feature">
          <h3>Bars</h3>
          <p>You can search for all different kinds of bars that you would like to visit someday.</p>
        </div>
        <div class="feature">
          <h3>Menus</h3>
          <p>If you are still unsure if the bar is good, you can check the menu by choosing the right bar.</p>
        </div>
        <div class="feature">
          <h3>Ratings</h3>
          <p>Give your rating to the bar or check others ratings before going.</p>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
      <p>&copy; 2024 Melu. All rights reserved.</p>
    </footer>
  </div>
</template>

<style scoped>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  color: #333;
}

.landing-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  min-height: 87.29vh;
  background-image: url("https://images.squarespace-cdn.com/content/v1/66d86247519ea05910ef4f62/78bd1a77-13b8-4553-84c3-c000b0aa748c/GiltBar-36-2.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 20px;
  box-sizing: border-box;
}

.hero {
  margin-top: 50px;
  text-align: center;
  color: white;
}

.hero-content h1 {
  font-size: 3rem;
}

.hero-content p {
  font-size: 1.2rem;
}

.features {
  margin-top: 50px;
  text-align: center;
  color: white;
}

.feature-grid {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
  max-height: 100vh;
  overflow-y: auto;
  padding: 20px;
  box-sizing: border-box;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 10px;
}

.feature {
  max-width: 800px;
  text-align: center;
  color: white;
}

/* Footer Section */
.footer {
  text-align: center;
  padding: 10px 10px;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  width: 100%;
  box-sizing: border-box;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.footer p {
  margin: 0;
  font-size: 0.9rem;
}
</style>
