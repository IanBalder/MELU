<script setup lang="ts">
import AruteluKast_Forum from "@/components/AruteluKast_Forum.vue";

</script>

<template>
     <div class="forum-container">
    <div class="header">
      <div class="search-navigation">
        <input type="text" placeholder="Search" class="search-box" />
        <div class="navigation">
          <span class="nav-item">teema 1</span> /
          <span class="nav-item">teema 2</span> /
          <span class="nav-item">teema 3</span> /
          <span class="nav-item">teema 4</span> /
          <span class="nav-item">teema 5</span>
        </div>
      </div>
      <button class="new-thread-btn">Create new thread</button>
    </div>
    <div class="discussion-stack">
      <AruteluKast_Forum />
      <AruteluKast_Forum />
      <AruteluKast_Forum />
    </div>
  </div>
</template>

<style scoped>

.forum-container {
  font-family: Arial, sans-serif;
  background-color: #fdfbf7;
  padding: 16px;
  margin-top: 1vh;
  border-radius: 8px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.search-navigation {
  display: flex;
  flex-direction: column;
  gap: 3vh;
  width: 31%;
}

.search-box {
  width: 150%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.new-thread-btn {
  padding: 8px 12px;
  background-color: white;
  border: 1px solid black;
  border-radius: 4px;
  font-size: 14px;
}

.new-thread-btn:hover {
  background-color: #ddd;
}

.navigation {
  font-style: italic;
  color: #555;
}

.nav-item {
  color: black;
}

.nav-item:hover {
  text-decoration: underline;
}

.discussion-stack {
  display: flex;
  flex-direction: column;
  gap: 8vh;
}

@media (min-width: 1200px) {
  .forum-container {
    width: 100%; /* Täida ekraani laius */
    max-width: 1600px; /* Lase konteineril olla kuni 1600px lai */
    margin-top: 10vh; /* Liiguta konteinerit ülespoole suurematel ekraanidel */
    margin-left: auto;
    margin-right: auto; /* Keskendame konteineri sisu */
    padding: 32px; /* Rohkem ruumi suurematele ekraanidele */
    min-height: 80vh; /* Tagab, et konteiner on vähemalt 80% ekraani kõrgusest */
  }

  .discussion-stack {
    gap: 60px; /* Suurematel ekraanidel suurendame vahelist ruumi */
  }

  .search-navigation {
    width: 50%; /* Suurematel ekraanidel väiksem otsinguala */
  }

  .search-box {
    width: 150%; /* Kohandame otsingukasti laiust */
  }
}

@media (min-width: 1600px) {
  .forum-container {
    width: 95%; /* Täida ekraani laius */
    max-width: 1800px; /* Lase konteineril olla kuni 1800px lai */
    padding: 40px; /* Veelgi rohkem ruumi suurematele ekraanidele */
    min-height: 85vh; /* Veel suurem konteiner kõrguses */
    margin-top: 0.5vh; /* Veel suurem ülespoole liikumine suurematel ekraanidel */
  }

  .search-navigation {
    width: 25%; /* Väiksem otsinguosa väga suurte ekraanide jaoks */
  }
}
</style>