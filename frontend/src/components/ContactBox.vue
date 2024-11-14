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
          <span>Email:</span>
          <span>&lt;firma emaili aadress&gt;</span>
        </div>

        <div class="contact-item">
          <span>Telefon:</span>
          <span>&lt;firma telefoninumber&gt;</span>
        </div>

        <div class="contact-item">
          <span>Aadress:</span>
          <span>&lt;firma kontori aadress&gt;</span>
        </div>
      </div>

      <!-- Nool, mis on paremal -->
      <div class="image-container right">
        <img src="@/assets/ContactNool.svg" alt="Kontakt pilt" />
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
  margin-bottom: 1vw;
}

.contact-item {
  margin-bottom: 2vw;
}

.image-container {
  display: flex;
  justify-content: center;
  margin: 2vw 0;
}

.image-container.horizontal {
  width: 100%;
}

.image-container.vertical {
  height: 100%;
}

.image-container img {
  width: 50px;
}

.image-container.vertical {

}

.image-container.horizontal {
  transform: rotate(90deg) translateX(60vh);
}
</style>