<template lang="">
  <div id="bloc-expiredSubscription" class="dashboard">
    <PermanentFull :titre="titre" :icon="icon" :menuItems="menuItems">
      <div class="expiredSbuscription-container">
        <div class="expiredSbuscription-content">
          <p class="text">{{ $t("expiredSubscription") }}</p>
          <md-button
            class="btn-submit text-center text-normal py-0 btn-redirection"
          >
            {{ $t("renewSubscription") }}
          </md-button>
          <p class="ignore-text">
            <a href="" title=""> {{ $t("ignore") }}</a>
          </p>
        </div>
      </div>
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import MenuUser from "../../data/MenuUser.js";

export default {
  name: "ExpiredSubscription",
  components: {
    PermanentFull,
  },
  data: () => {
    return {
      titre: "Abonnement expiré",
      menuItems: MenuUser,
    };
  },
};
</script>

<style>
#bloc-expiredSubscription .dashboard-title {
  justify-content: center;
  padding-top: 2rem;
}
#bloc-expiredSubscription .md-app-side-drawer .md-drawer,
#bloc-expiredSubscription .permanentfull-icon-button {
  pointer-events: none;
}
</style>
<style scoped>
.expiredSbuscription-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 2rem;
  width: 100%;
}
.expiredSbuscription-container .expiredSbuscription-content {
  max-width: 360px;
  margin: 0 auto;
  padding: 0 16px;
  text-align: center;
}
.expiredSbuscription-content .text {
  font-size: 16px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-align: center;
}
@media (max-width: 960px) {
  .expiredSbuscription-content .text {
    font-size: 14px;
  }
}
.expiredSbuscription-content .btn-redirection {
  margin: 0;
  width: auto;
  padding-left: 16px;
  padding-right: 16px;
}
@media (max-width: 960px) {
  .expiredSbuscription-content .btn-redirection {
    font-size: 14px;
    padding-left: 8px;
    padding-right: 8px;
  }
}
.expiredSbuscription-content .ignore-text {
  text-align: center;
  padding-top: 12px;
}
.expiredSbuscription-content .ignore-text a {
  font-size: 12px;
  color: var(--placeholder) !important;
  font-family: "Poppins-Regular", Arial, Helvetica, sans-serif;
}
.expiredSbuscription-content .ignore-text a:hover {
  color: var(--gray-dark) !important;
}
</style>
