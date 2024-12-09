<script setup lang="ts">
import ContactBox from '@/components/ContactBox.vue';

</script>

<template>
  <div class="about">
    <div class="content-container">
      <div class="contact-box">
        <ContactBox />
      </div>
      <div class="info-box">
        <h1>Küsi julgelt!</h1>
        <div class="Nool1">
          <img src="../assets/KüsijulgeltNool.svg">
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
html, body {
  overflow: hidden;
  height: 100%;
  margin: 0;
}

.about {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: 60vh;
  padding-top: 5vh;
  margin-left: -2vw;
  overflow: hidden;
}

.content-container {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  padding: 5vw;
  box-sizing: border-box;
  align-items: center;
  justify-content: flex-start;
  gap: 5vw;
  margin-top: -6vh;
}

.contact-box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2vw 1vw;
  background-color: #fdfbf7;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  border-radius: 0;
  text-align: center;
  width: clamp(250px, 30vw, 500px);
  height: clamp(200px, 30vw, 400px);
}

.info-box {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #333;
  margin-top: -1vw;
  padding-left: 13vw;
}

.info-box h1 {
  font-size: clamp(24px, 5vw, 48px);
  font-weight: bold;
  color: #333;
  margin-bottom: 2vw;
  margin-top: 0;
}

.Nool1 {
  margin-top: -3vw;
  display: flex;
  justify-content: center;
}

.Nool1 img {
  width: clamp(200px, 40vw, 500px);
  height: auto;
}

/* Suuremate ekraanide jaoks */
@media (min-width: 1200px) {
  .contact-box {
    width: 370px;
    height: 360px;
  }
}

@media (min-width: 1200px) {
  .info-box {
    margin-left: 200px;
    margin-right: 50px;
  }
}

/* Väiksemate ekraanide jaoks */
@media (max-width: 768px) {
  .content-container {
    padding: 5% 5%;
    gap: 2vw;
    margin-top: 0;
  }

  .contact-box {
    width: 90%;
    height: auto;
    padding: 4vw 3vw;
    box-shadow: none;
  }

  .info-box {
    padding-left: 0;
    margin-top: 8vw;
    text-align: center;
    width: 100%;
  }

  .info-box h1 {
    font-size: clamp(18px, 6vw, 28px);
    margin-bottom: 5vw;
  }

  .Nool1 img {
    width: 70%;
    max-width: 300px;
  }
}

/* Väiksemate ekraanide jaoks */
@media (max-width: 480px) {
  .content-container {
    padding: 5%;
  }

  .contact-box {
    width: 100%;
    padding: 6vw 4vw;
    height: auto;
  }

  .info-box h1 {
    font-size: clamp(16px, 8vw, 24px);
  }

  .Nool1 img {
    width: 80%;
    max-width: 250px;
  }
}

</style>
