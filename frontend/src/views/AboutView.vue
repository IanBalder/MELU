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
.about {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  min-height: 100vh;
  padding-top: 5vh;
  margin-left: -3vw;
}

.content-container {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
  padding: 5vw;
  box-sizing: border-box;
  align-items: center;
  justify-content: flex-start;
  gap: 10vw;
}

.contact-box {
  flex: 1 1 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 3vw;
  background-color: #fdfbf7;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  border-radius: 0;
  margin-right: 5vw;
  margin-bottom: 5vw;
  text-align: center;
  max-width: 30vw;
  height: 30vw; /* Määrame kõrguseks sama väärtuse, mis laiuseks */
  min-width: 250px;
}

.info-box {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #333;
  margin-top: -5vh; /* Liiguta kogu info-kasti ülespoole */
}

.info-box h1 {
  font-size: clamp(36px, 7vw, 48px); /* Suurendasime teksti suurust */
  font-weight: bold;
  color: #333;
  margin-bottom: 2vw;
  margin-top: 0;
}

.Nool1 {
  margin-top: -3vw; /* Liiguta pilti ülespoole */
  display: flex;
  justify-content: center;
}

.Nool1 img {
  width: clamp(300px, 50vw, 500px); /* Suurendasime pildi laiust */
  height: auto;
}

</style>

<script>
import { Options, Vue } from 'vue-class-component';
import ContactBox from '@/components/ContactBox.vue';

@Options({
  components: {
    ContactBox,
  },
})
export default class AboutView extends Vue {}
</script>
