<template>
  <div
    class="home-bienvenue d-flex flex-column justify-content-center align-items-center"
  >
    <div class="img-wrapper mb-3">
      <router-link to="/"
        ><img src="../../assets/images/logoBlanc.png" alt="Logo Blanc" />
      </router-link>
    </div>
    <h2 class="page-title d-flex flex-column align-items-center">
      {{ $t("welcome") }} <span>Predictmarket !</span>
    </h2>
    <p class="text-center">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
      pellentesque id purus eget auctor. Pellentesque habitant morbi tristique
      senectus et netus et malesuada fames ac turpis egestas.
    </p>
  </div>
</template>

<script>
export default {
  name: "HomeBienvenue",
};
</script>
