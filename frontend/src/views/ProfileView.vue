<template>
  <div class="profile-view">
    <!-- Profiilipilt -->
    <img class="profile-image" src="@/assets/human_logo.svg"/>

    <!-- Kasutaja nimi ja e-mail -->
    <h2>Peeter Nurmesalu <span class="edit-icon">✏️</span></h2>
    <p>peeter.nurmesalu@gmail.com</p>

    <button class="logout-button">Log out</button>

    <div class="info-section">
      <h3>Comments</h3>
      <h3>Threads</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileView'
}
</script>

<style>
.profile-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f5f5f5;
}

.profile-image {
  width: 100px;
  height: 100px;
  margin-bottom: 15px;
}

h2 {
  font-size: 24px;
  margin: 0;
}

.edit-icon {
  font-size: 16px;
  cursor: pointer;
  margin-left: 8px;
}

p {
  color: #555;
  font-size: 16px;
  margin-top: 5px;
}

.logout-button {
  margin: 20px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #e0e0e0;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.info-section {
  display: flex;
  gap: 40px;
  font-size: 20px;
  font-weight: bold;
  margin-top: 30px;
}
</style>
