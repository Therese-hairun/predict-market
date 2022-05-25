<template>
  <div id="connexion">
    <div class="row-fluid d-flex flex-wrap align-items-stretch">
      <div
        class="
          col-12 col-lg-6
          message-bienvenue-wrapper
          bgColor-primary
          d-flex
          flex-column
          justify-content-center
          align-items-center
        "
      >
        <HomeBienvenue></HomeBienvenue>
      </div>

      <div
        class="
          col-12 col-lg-6
          flex-grow-1
          position-relative
          d-flex
          flex-column
          justify-content-center
          align-items-center
          connexion-content-wrapper
        "
      >
        <div class="lang">
          <MainLayout></MainLayout>
        </div>
        <svg
          id="account_circle-24px"
          xmlns="http://www.w3.org/2000/svg"
          width="92"
          height="92"
          viewBox="0 0 92 92"
          style="margin-bottom: 32px"
        >
          <path
            id="Tracé_2166"
            data-name="Tracé 2166"
            d="M0,0H92V92H0Z"
            fill="none"
          />
          <g
            id="Groupe_14044"
            data-name="Groupe 14044"
            transform="translate(7.629 7.705)"
          >
            <path
              id="Tracé_19671"
              data-name="Tracé 19671"
              d="M162.639,159.613c-.275.33-.533.678-.829.989q-11.931,12.529-23.869,25.051c-.421.441-.864.832-1.531.57a1.752,1.752,0,0,1-.578-.384q-5.724-5.708-11.435-11.43a1.188,1.188,0,0,1-.324-1.459,1.086,1.086,0,0,1,1.252-.616,1.949,1.949,0,0,1,.833.51q5.108,5.078,10.193,10.179c.129.129.264.251.35.333.38-.348.757-.656,1.091-1.005q11.327-11.852,22.646-23.712a1.218,1.218,0,0,1,1.846-.205,3.765,3.765,0,0,1,.355.474Z"
              transform="translate(-104.921 -133.831)"
              fill="#f8bd25"
            />
            <path
              id="Tracé_19672"
              data-name="Tracé 19672"
              d="M38.362,76.742q-1.469,0-2.941-.112A38.363,38.363,0,1,1,69.557,60.736a1.5,1.5,0,1,1-2.434-1.75,35.373,35.373,0,1,0-8.136,8.137,1.5,1.5,0,1,1,1.749,2.434A38.365,38.365,0,0,1,38.362,76.742Z"
              transform="translate(0 0)"
              fill="#242c36"
            />
            <path
              id="Tracé_19673"
              data-name="Tracé 19673"
              d="M411.609,413.108a1.5,1.5,0,1,1,1.06-.439A1.51,1.51,0,0,1,411.609,413.108Z"
              transform="translate(-347.165 -347.165)"
              fill="#242c36"
            />
          </g>
        </svg>

        <div class="content-right text-center">
          <h1 class="titre-form-user">{{ $t("resetPassword:message") }}</h1>
          <p class="description-form-user">
            {{ $t("successPwd:descriptionForm") }}
          </p>
        </div>

        <div class="form-user-wrapper">
          <router-link to="/" class="btn-submit d-block text-center">{{
            $t("goToLogin")
          }}</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import HomeBienvenue from "../HomeBienvenue/HomeBienvenue.vue";
import MainLayout from "../language/MainLayout.vue";

export default {
  name: "SuccessPwd",
  components: {
    HomeBienvenue,
    MainLayout,
  },
  created() {
    document.title = this.$route.meta.title;
  },
};
</script>
