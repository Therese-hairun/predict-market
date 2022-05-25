<template lang="">
  <div id="dashboard-sidebar" class="h-100">
    <div class="notFound-container d-flex justify-content-center">
      <div class="d-flex flex-column align-items-center justify-content-center">
        <div class="img-wrapper mt-2 mb-5 d-lg-block">
          <router-link
            :to="{
              name: isAdmin ? 'ListesDesUtilisateurs' : 'Dashboard',
            }"
            class="d-flex align-items-center mx-auto goHome"
          >
            <img src="../../assets/images/logoNoir.png" alt="Logo Noir" />
          </router-link>
        </div>
        <span class="display-1 d-block">404</span>
        <div class="mb-4 lead text-center">{{ $t("pageNotFound") }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "404NotFound",
  data: function() {
    return {
      loading: false,
      isAdmin: null,
    };
  },
  methods: {},
  watch: {},
  mounted() {
    this.isAdmin = localStorage.getItem("token") !== "null" ? false : true;
  },
};
</script>
<style scoped>
.display-1 {
  color: var(--primary);
}
.notFound-container {
  min-height: 100vh;
  padding: 20px;
}
.goHome {
  text-decoration: none !important;
}
.goHome:hover {
  opacity: 0.75;
}
.lead {
  font-size: 16px;
}
@media screen and (max-width: 600px) {
  .img-wrapper {
    max-width: 60px;
    margin-bottom: 1rem !important;
  }
  .display-1 {
    font-size: 3rem;
  }
  .lead {
    font-size: 12px;
  }
  .goHome {
    font-size: 14px;
  }
}
</style>
