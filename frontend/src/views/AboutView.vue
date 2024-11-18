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

/* Suuremate ekraanide jaoks (contact-box) */
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

</style>
