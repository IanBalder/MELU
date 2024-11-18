<script lang="ts">
export default {
  name: 'aboutView'
}
</script>

<template>
  <div class="contact-info">
    <div class="container1">
      <div class="contact-details">
        <div class="contact-item">
          <span class="label">Email:</span>
          <span class="value">&lt;firma emaili aadress&gt;</span>
        </div>

        <div class="contact-image">
          <img class="dekoratsiooni_nool" src="@/assets/ContactNool.svg" alt="dekoratsioon" />
        </div>

        <div class="contact-item">
          <span class="label">Telefon:</span>
          <span class="value">&lt;firma telefoninumber&gt;</span>
        </div>

        <div class="contact-image">
          <img class="dekoratsiooni_nool" src="@/assets/ContactNool.svg" alt="dekoratsioon" />
        </div>

        <div class="contact-item">
          <span class="label">Aadress:</span>
          <span class="value">&lt;firma kontori aadress&gt;</span>
        </div>
      </div>

      <!-- Nool, mis on paremal -->
      <div class="image-container right">
        <img src="@/assets/ComponentsideNool.svg" alt="Kontakt pilt" />
      </div>
    </div>
    <!-- Nool, mis on all -->
    <div class="image-container bottom">
      <img src="@/assets/ComponentsideNool.svg" alt="Kontakt pilt" />
    </div>
  </div>
</template>

<style scoped>
.contact-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  margin-bottom: 1vw;
}

.contact-details {
  padding: 1vw;
  position: relative;
  z-index: 1;
  width: 90%;
  max-width: 500px;
  min-height: 150px;
  height: auto;
}

.contact-item {
  display: flex;
  align-items: center;
  margin-bottom: 1vw;
  font-size: 1rem;
  line-height: 1.5;
}

.contact-item .label {
  font-weight: bold;
  margin-right: 0.5rem;
}

.contact-item .value {
  font-weight: normal;
  color: #333;
  white-space: nowrap;
}

.image-container {
  position: absolute;
  z-index: 0;
}

.image-container.right {
  top: -6vw;
  left: 133%;
  transform: translateX(-50%);
}

.image-container.bottom {
  bottom: -27vw;
  left: 50%;
  transform: translateX(-50%) rotate(90deg);
}

.image-container img {
  height: 30vw;
  width: auto;
}

.contact-image {
  text-align: left;
}

.dekoratsiooni_nool {
  width: 200px;
  height: auto;
}

/* Ainult suuremate ekraanide jaoks (contact-details) */
@media (min-width: 1200px) {
  .contact-details {
    width: 50%;
  }

  .image-container.right {
    top: -3.5vw;
    left: calc(100% + 4.5vw);
  }

  .image-container.bottom {
    bottom: -19.5vw;
  }

  .image-container img {
    max-height: 23vw;
    height: auto;
  }
}

/* Ainult suuremate ekraanide jaoks (contact-item) */
@media (min-width: 1200px) {
  .contact-item {
    font-size: 1.2rem;
    line-height: 1.8;
    text-align: Left;
    color: #000;
  }

  .dekoratsiooni_nool {
    width: 220px;
  }
}

</style>