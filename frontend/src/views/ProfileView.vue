<script setup lang="ts">

</script>

<template>
  <div class="profile-container">

    <!-- Profiili kaart -->
    <div class="profile-card">
      <div class="profile-view">
        <!-- Profiilipilt -->
        <img class="profile-image" src="@/assets/human_logo.svg" />

        <!-- Kasutaja nimi ja e-mail -->
        <h2>Peeter Nurmesalu <span class="edit-icon">✏️</span></h2>
        <p>peeter.nurmesalu@gmail.com</p>

        <button class="logout-button">Log out</button>

        <!-- Info sektsioon (nupud) -->
        <div class="info-section">
          <button class="info-button">Comments</button>
          <button class="info-button">Threads</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  background-color: #d8cec4;
}

.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  position: relative;
  padding: 20px; /* Jäta servadele ruumi mobiilivaates */
}

.profile-card {
  background-color: #fff;
  padding: 5%; /* Suhteline polster */
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 400px;
  width: 100%; /* Kohandub ekraaniga */
}

.profile-image {
  width: 80px;
  height: 80px;
  margin-bottom: 15px;
  border-radius: 50%;
}

h2 {
  font-size: 24px;
  margin: 0;
}

.logout-button {
  margin: 20px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #d8cec4;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.info-section {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-top: 30px;
  flex-wrap: wrap; /* Mobiilivaates liiguvad nupud uuele reale */
}

@media (max-width: 768px) {
  .profile-card {
    padding: 20px;
  }

  h2 {
    font-size: 20px;
  }

  .profile-image {
    width: 60px;
    height: 60px;
  }

  .info-section {
    gap: 10px;
  }
}

</style>
