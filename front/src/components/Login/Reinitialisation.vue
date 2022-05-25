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
        <HomeBienvenue
          v-bind:title="pageTitle"
          v-bind:message="messageBienvenue"
        ></HomeBienvenue>
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
          <div class="img-wrapper mb-3 d-none d-lg-block">
            <img src="../../assets/images/logoNoir.png" alt="Logo Noir" />
          </div>

          <h1 class="titre-form-user">
            {{ $t("reinitialisation:titreForm") }}
          </h1>
          <p
            class="description-form-user"
            v-html="$t('reinitialisation:descriptionForm')"
          ></p>
        </div>

        <div class="form-user-wrapper">
          <form
            action=""
            class="form-user"
            @submit="checkForm"
            novalidate="true"
          >
            <div class="help_input">
              {{ $t("password-help-label") }}
              <ul>
                <li>
                  {{ $t("contain-a") }}
                  <strong>{{ $t("lowercase") }}</strong
                  >, {{ $tc("a", 2) }} <strong>{{ $t("uppercase") }}</strong
                  >, {{ $tc("a", 1) }} <strong>{{ $t("number") }}</strong>
                  {{ $t("and-a") }}

                  <strong>{{ $t("special-character") }}</strong> ;
                </li>
                <li>
                  {{ $t("at-least") }}
                  <strong>{{ $t("8-characters") }}</strong
                  >.
                </li>
              </ul>
            </div>
            <div class="form-group">
              <md-field>
                <label
                  for="password"
                  :class="errorPwd.length && 'error-input'"
                  >{{ $t("password") }}</label
                >
                <md-input
                  type="password"
                  name="password"
                  id="password"
                  autocomplete="password"
                  v-model="password"
                  :class="errorPwd.length && 'error-input'"
                />
              </md-field>
              <span v-if="errorPwd.length" class="d-flex flex-column">
                <span class="error" v-for="error in errorPwd" :key="error">{{
                  error
                }}</span>
              </span>
            </div>

            <div class="form-group">
              <md-field>
                <label
                  for="password"
                  :class="errorConfirmPwd.length && 'error-input'"
                  >{{ $t("confirm-password") }}</label
                >
                <md-input
                  type="password"
                  name="confirmPassword"
                  id="confirmPassword"
                  autocomplete="confirmPassword"
                  v-model="confirmPassword"
                  :class="errorConfirmPwd.length && 'error-input'"
                />
              </md-field>
              <span v-if="errorConfirmPwd.length" class="d-flex flex-column">
                <span
                  class="error"
                  v-for="error in errorConfirmPwd"
                  :key="error"
                  >{{ error }}</span
                >
              </span>
            </div>

            <PredictSubmit
              v-bind:label="textSubmit"
              v-bind:disabled="isDisabled"
            ></PredictSubmit>
          </form>
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
              {{ $t("haveAccount?") }}
              <router-link to="/">{{ $t("logIn") }}</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import HomeBienvenue from "../HomeBienvenue/HomeBienvenue.vue";
import PredictSubmit from "../Input/PredictSubmit.vue";
import { API_URL } from "../../utils/Constant";
import MainLayout from "../language/MainLayout.vue";

export default {
  name: "Reinitialisation",
  data: () => {
    return {
      pageTitle: "Bienvenue sur <span>Predictmarket !</span>",
      messageBienvenue:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pellentesque id purus eget auctor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
      textSubmit: "re-init",
      action: "/success-pwd",
      errorPwd: [],
      errorConfirmPwd: [],
      password: null,
      confirmPassword: null,
      messageHelpMotDePasse: `
        Pour que votre mot de passe soit valide, elle doit au moins :
        <ul>
        <li>Contenir une <strong>minuscule</strong> , une <strong>majuscule</strong>, un <strong>chiffre</strong> et un <strong>caractère spécial</strong>.</li>
        <li>Avoir au minimum <strong>8 caractères</strong>.</li>
        </ul>
      `,
    };
  },
  computed: {
    isDisabled() {
      if (this.password && this.confirmPassword) {
        return false;
      }
      return true;
    },
  },
  methods: {
    async checkForm(e) {
      e.preventDefault();
      this.errorPwd = [];
      this.errorConfirmPwd = [];

      if (!this.password) {
        this.errorPwd.push(this.$t("errorAddPwd"));
      }

      if (!this.validPassword(this.password)) {
        this.errorPwd.push(this.$t("errorPwdInvalid"));
      }

      if (!this.confirmPassword) {
        this.errorConfirmPwd.push(this.$t("errorConfirmPwd"));
      }

      if (this.confirmPassword != this.password) {
        this.errorConfirmPwd.push(this.$t("errorConfirmPwdConfirm"));
      }

      if (!this.errorPwd.length && !this.errorConfirmPwd.length) {
        const { id } = this.$route.params;
        const payload = {
          password: this.password,
        };
        await axios
          .patch(
            `${API_URL}/api/updatePassword`,
            {
              ...payload,
            },
            {
              headers: {
                Authorization: `Bearer ${id}`,
              },
            }
          )
          .then((response) => {
            if (response) this.$router.push(this.action);
          });
      }
    },
    validPassword(pwd) {
      var re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
      return re.test(pwd);
    },
    onVerify: function(response) {
      if (response) this.form.robot = true;
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
