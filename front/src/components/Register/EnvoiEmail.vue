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
        <div class="content-right text-center">
          <h1 class="titre-form-user">{{ $t("envoiEmail:titreForm") }}</h1>
          <p
            class="description-form-user"
            v-html="$t('envoiEmail:descriptionForm')"
          ></p>
        </div>

        <div class="form-user-wrapper">
          <form
            action=""
            class="form-user"
            novalidate="true"
            @submit.prevent="checkForm"
          >
            <div class="form-group">
              <md-field>
                <label for="email" :class="errorMail.length && 'error-input'">{{
                  $t("email")
                }}</label>
                <md-input
                  type="email"
                  name="email"
                  id="email"
                  autocomplete="email"
                  v-model="email"
                  :class="errorMail.length && 'error-input'"
                />
              </md-field>
              <span v-if="errorMail.length" class="d-flex flex-column">
                <span class="error" v-for="error in errorMail" :key="error">{{
                  error
                }}</span>
              </span>
            </div>

            <PredictSubmit
              v-bind:label="label"
              v-bind:disabled="isDisabled"
            ></PredictSubmit>
            <div
              class="
                form-additionnel
                row-fluid
                d-flex
                flex-column
                w-100
                justify-content-center
              "
            >
              <hr />
              <div class="inscription-link-container text-center">
                {{ $t("haveAccount") }}
                <router-link to="/">{{ $t("logIn") }}</router-link>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import HomeBienvenue from "../HomeBienvenue/HomeBienvenue.vue";
import PredictSubmit from "../Input/PredictSubmit.vue";
import axios from "axios";
import { API_URL } from "../../utils/Constant";
import MainLayout from "../language/MainLayout.vue";

export default {
  name: "EnvoiDEmail",
  data: () => {
    return {
      label: "send",
      errorMail: [],
      email: localStorage.getItem("email") || null,
      action: "/verification-email",
      success: [],
    };
  },
  computed: {
    isDisabled() {
      if (this.email) {
        return false;
      }
      return true;
    },
  },
  mounted() {
    this.handleMail();
  },
  methods: {
    handleMail() {
      if (this.email === null || this.email === "null") this.email = "";
    },
    checkForm(e) {
      e.preventDefault();

      this.errorMail = [];
      this.buttonDisable = true;

      if (!this.email) {
        this.errorMail.push(this.$t("addEmail"));
      } else if (!this.validEmail(this.email)) {
        this.errorMail.push(this.$t("emailInvalid"));
      }

      if (!this.errorMail.length) {
        axios
          .post(
            `${API_URL}/api/sendMail?language=${localStorage.getItem(
              "language"
            )}`,
            {
              email: this.email,
              id: localStorage.getItem("id"),
            }
          )
          .then(() => {
            this.success.push(this.$t("emailSent"));

            localStorage.setItem("email", this.email);
            this.$router.push(this.action);
          })
          .catch((err) => {
            if (err.response.status === 406) {
              this.errorMail.push(this.$t("fakeEmail"));
            } else if (err.response.status === 409) {
              this.errorMail.push(this.$t("emailAlreadyExist"));
            }
          });
      }
    },
    validEmail(email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
  },
  components: {
    HomeBienvenue,
    PredictSubmit,
    MainLayout,
  },
  created() {
    document.title = this.$route.meta.title;
  },
};
</script>
