<template lang="">
  <div
    id="bloc-abonnement"
    class="d-flex flex-wrap justify-content-between align-items-strecth"
  >
    <div class="d-flex flex-nowrap align-items-center abonnement">
      <span v-if="iconAbonnement" v-html="iconAbonnement"></span>

      <div class="d-flex flex-column">
        <h3 class="titre-abonnement mb-0" v-if="titreAbonnement">
          {{ titreAbonnement }}
        </h3>
        <span class="type-abonnement" v-if="typeAbonnement">{{
          typeAbonnement
        }}</span>
        <span v-if="dateExpiration" class="mt-1">
          <svg
            class="Trac_19699"
            width="15"
            height="16.5"
            viewBox="2 1 15 16.5"
          >
            <path
              id="Trac_19699"
              d="M 15.5 2.5 L 14.75 2.5 L 14.75 1 L 13.25 1 L 13.25 2.5 L 5.75 2.5 L 5.75 1 L 4.25 1 L 4.25 2.5 L 3.5 2.5 C 2.675000190734863 2.5 2 3.175000190734863 2 4 L 2 16 C 2 16.82500076293945 2.675000190734863 17.5 3.5 17.5 L 15.5 17.5 C 16.32500076293945 17.5 17 16.82500076293945 17 16 L 17 4 C 17 3.175000190734863 16.32500076293945 2.5 15.5 2.5 Z M 15.5 16 L 3.5 16 L 3.5 6.25 L 15.5 6.25 L 15.5 16 Z"
              fill="#a7aaae"
            ></path>
          </svg>
          {{ $t("expiryAt") }} :
          <span class="date-expiration">{{ dateExpiration }}</span>
        </span>
      </div>
    </div>
    <div class="d-flex flex-column justify-content-center emplacement-dispo">
      <h3 class="titre-abonnement mb-0">{{ $t("availableLocation") }}</h3>
      <div class="card-wrapper d-flex align-items-center">
        <svg class="Trac_42045" width="30" height="24" viewBox="2 4 30 24">
          <path
            id="Trac_42045"
            d="M 14 4 L 5 4 C 3.350000381469727 4 2.014999866485596 5.350000381469727 2.014999866485596 7 L 2 25 C 2 26.65000152587891 3.350000381469727 28 5 28 L 29 28 C 30.65000152587891 28 32 26.65000152587891 32 25 L 32 10 C 32 8.350000381469727 30.65000152587891 7 29 7 L 17 7 L 14 4 Z"
            fill="#fff"
          ></path>
        </svg>
        <div
          class="card border-0 bg-transparent d-flex flex-row align-items-center"
        >
          {{
            +emplacementDispo === 0
              ? emplacementUtilise
              : emplacementDispo - emplacementUtilise
          }}
          <span class="small"
            >/{{
              +emplacementDispo === 0 ? $t("unlimited") : emplacementDispo
            }}</span
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlocAbonnement",
  props: {
    typeAbonnement: String,
    dateExpiration: String,
    emplacementUtilise: String,
    emplacementDispo: String,
    titreAbonnement: String,
    iconAbonnement: String,
  },
};
</script>
<style>
@media (max-width: 479px) {
  #couple-crypto .md-tabs-navigation {
    justify-content: center;
    margin-bottom: 5px;
    width: 100%;
  }
}
@media (max-width: 479px) {
  #couple-crypto .md-tabs-navigation .md-button {
    position: relative;
  }
}
@media (max-width: 479px) {
  #couple-crypto .md-tabs-navigation .md-button .md-ripple {
    justify-content: center;
    position: relative;
  }
}
@media (max-width: 479px) {
  #couple-crypto .md-tabs-navigation .md-button .md-ripple:after {
    background-color: #fdca40;
    content: "";
    height: 2px;
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    transition: all 0.25s ease-in-out;
    width: 0;
  }
}
@media (max-width: 479px) {
  #couple-crypto .md-tabs-navigation .md-button.md-active .md-ripple:after {
    width: 50%;
  }
}
@media (max-width: 479px) {
  #couple-crypto .md-tabs-navigation .md-tabs-indicator {
    display: none;
  }
}
</style>
<style scoped>
#bloc-abonnement {
  border-radius: 12px;
  -webkit-border-radius: 12px;
  -moz-border-radius: 12px;
  -ms-border-radius: 12px;
  -o-border-radius: 12px;
  background-color: var(--black);
  color: var(--placeholder);
  padding: 10px 16px;
  margin-bottom: 36px;
}
@media (max-width: 479px) {
  #bloc-abonnement {
    margin-bottom: 18px;
  }
}
#bloc-abonnement .abonnement {
  padding-top: 6px;
  padding-bottom: 6px;
}
.titre-abonnement {
  font-size: 12px;
  letter-spacing: 0.1px;
}
.type-abonnement {
  font-size: 24px;
  color: var(--primary);
  line-height: 36px;
}
.date-expiration {
  color: #fff;
  font-size: 14px;
  line-height: 20px;
}
.emplacement-dispo {
  padding-left: 43px;
  padding-right: 20px;
  border-left: 1px solid #5c626a;
}
@media (max-width: 1200px) {
  .emplacement-dispo {
    padding-top: 10px;
  }
}
@media (max-width: 480px) {
  .emplacement-dispo {
    border-left: 0;
    padding-left: 0;
  }
}
.emplacement-dispo .card-wrapper {
  font-size: 34px;
  color: #fff;
}
.emplacement-dispo .card {
  margin-left: 10px;
}
.emplacement-dispo .card .small {
  font-size: 14px;
}
</style>
