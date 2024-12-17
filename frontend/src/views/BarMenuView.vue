<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute();
const barId = route.query.id;
console.log('Selected Bar ID:', barId);

</script>

<template>
  <div class="page-container">
    <!-- Profiili kaardi sektsioon -->
    <div class="profile-section">
      <div class="profile-card">
        <!-- Pildi ja nime ala -->
        <div class="profile-info">
          <div class="profile-image"></div>
          <h1 class="bar-name">Baari nimi.</h1>
          <p>Selected Bar ID: {{ barId }}</p>
        </div>
      </div>
    </div>

    <!-- Joogid sektsioon -->
    <div class="drinks-section">
      <div class="drinks-category">
        <h2>Cocktails</h2>
        <ul>
          <li><b>Classic Mojito</b><br />White rum, fresh mint, lime, sugar, soda water<br />[Price]</li>
          <li><b>Whiskey Sour</b><br />Bourbon, lemon juice, simple syrup, egg white<br />[Price]</li>
          <li><b>Margarita</b><br />Tequila, lime juice, triple sec, salt rim<br />[Price]</li>
          <li><b>Espresso Martini</b><br />Vodka, espresso, coffee liqueur, sugar syrup<br />[Price]</li>
        </ul>
      </div>
      <div class="drinks-category">
        <h2>Beers</h2>
        <ul>
          <li><b>Lager</b><br />Crisp and refreshing light lager<br />[Price]</li>
          <li><b>IPA</b><br />Hoppy and bold India Pale Ale<br />[Price]</li>
          <li><b>Stout</b><br />Rich and dark stout with roasted malts<br />[Price]</li>
        </ul>
      </div>
    </div>

    <!-- Kommentaarid sektsioon -->
    <div class="comments-section">
      <h2>Comments & reviews</h2>
      <div class="comment-input">
        <p>You must be logged in to comment</p>
        <textarea placeholder="Leave a comment..."></textarea>
      </div>
      <div class="comment-list">
        <div class="comment">
          <div class="comment-avatar"></div>
          <div class="comment-content">
            <p><b>Tõnu 420</b></p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae libero nec nulla suscipit facilisis ut eget metus.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

/* Üldine lehekülg */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

.page-container {
  margin: 0 auto;
  max-width: 1200px;
  padding: 20px;
}

/* Profiili kaart */
.profile-section {
  display: flex;
  justify-content: center;
  margin-bottom: 40px;
}

.profile-card {
  text-align: center;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 300px;
  width: 100%;
}

.profile-image {
  width: 100px;
  height: 100px;
  background-color: #ccc;
  border-radius: 50%;
  margin: 0 auto 10px;
}

.bar-name {
  font-size: 24px;
  margin: 0;
}

/* Joogid sektsioon */
.drinks-section {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 40px;
}

.drinks-category {
  flex: 1;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.drinks-category h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.drinks-category ul {
  list-style-type: none;
  padding: 0;
}

.drinks-category li {
  margin-bottom: 15px;
}

/* Kommentaarid sektsioon */
.comments-section {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.comment-input p {
  margin-bottom: 15px;
}

.comment-input {
  margin-bottom: 20px;
}

.comment-input textarea {
  width: 95%;
  height: 60px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  resize: none;
}

.comment-list {
  margin-top: 20px;
}

.comment {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.comment-avatar {
  width: 50px;
  height: 50px;
  background-color: #ccc;
  border-radius: 50%;
}

.comment-content p {
  margin: 0;
}

/* Responsiivsus */
@media (max-width: 768px) {
  .drinks-section {
    flex-direction: column;
  }

  .drinks-category {
    margin-bottom: 20px;
  }

  .comment-input textarea {
    width: 80%;
  }
}

@media (max-width: 480px) {
  .profile-card {
    max-width: 90%;
  }

  .comments-section {
    padding: 15px;
  }
}
</style>
