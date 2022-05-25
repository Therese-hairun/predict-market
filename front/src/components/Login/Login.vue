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
          <div class="img-wrapper mb-3 d-none d-lg-block">
            <img src="../../assets/images/logoNoir.png" alt="Logo Noir" />
          </div>

          <h1 class="titre-form-user">{{ $t("connexion") }}</h1>
          <p class="description-form-user">
            {{ $t("left-thanks") }}
            <strong> predictmarket </strong>
            {{ $t("right-thanks") }}
          </p>
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
              <span v-if="credentionError.length" class="d-flex flex-column">
                <span
                  class="error"
                  v-for="error in credentionError"
                  :key="error"
                >
                  {{ error }}
                </span>
              </span>
            </div>
            <div
              class="captcha-wrapper"
              id="cap"
              :style="connectionLimitReached ? '' : 'display: none;'"
            >
              <vue-recaptcha
                sitekey="6Lc0FGccAAAAAKbydlgQekIURGrgF-bo2E-Etfp_"
                @verify="verifyCaptcha"
                :loadRecaptchaScript="true"
              >
              </vue-recaptcha>
            </div>
            <PredictSubmit
              v-bind:label="login"
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
              <div
                class="
                  w-100
                  row-fluid
                  d-flex
                  flex-column flex-sm-row
                  align-items-center
                  justify-content-between
                  rememberMe-wrapper
                "
              >
                <md-checkbox
                  id="rememberMe"
                  name="rememberMe"
                  v-model="rememberMe"
                  >{{ $t("remember-me") }}</md-checkbox
                >

                <router-link to="/mot-de-passe-oublie">{{
                  $t("forgotten-password")
                }}</router-link>
              </div>
              <hr />
              <div class="inscription-link-container text-center">
                {{ $t("no-account") }}
                <router-link to="/register">{{ $t("subscribe") }}</router-link>
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
import { API_URL, ERROR_COUNT, EMAIL, PARAPHRASE } from "../../utils/Constant";
import VueRecaptcha from "vue-recaptcha";
import MainLayout from "../language/MainLayout.vue";

export default {
  name: "Login",
  components: {
    HomeBienvenue,
    PredictSubmit,
    MainLayout,
    "vue-recaptcha": VueRecaptcha,
  },
  data: () => {
    return {
      login: "login",
      action: "/dashboard",
      errorMail: [],
      errorPwd: [],
      email: null,
      password: null,
      rememberMe: false,
      credentionError: [],
      disabled: false,
      captcha: true,
      errorCount: localStorage.getItem("errcon"),
      connectionLimitReached: null,
    };
  },
  computed: {
    isDisabled() {
      if (this.email && this.password && !this.disabled && this.captcha) {
        return false;
      }
      return true;
    },
  },
  methods: {
    clearStorage() {
      localStorage.setItem("token", null);
      localStorage.setItem("adminToken", null);
      localStorage.setItem("errcon", null);
      localStorage.setItem("email", null);
      localStorage.setItem("id", null);
      localStorage.setItem("phone", null);
    },

    encryptValue(val) {
      return this.CryptoJS.AES.encrypt(val, PARAPHRASE).toString();
    },

    decryptValue(val) {
      return this.CryptoJS.AES.decrypt(val, PARAPHRASE).toString(
        this.CryptoJS.enc.Utf8
      );
    },

    autoLogin() {
      const userMail = localStorage.getItem("userMail");
      const userPassword = localStorage.getItem("userPwd");

      this.clearStorage();

      if (userMail !== null && userPassword !== null) {
        const formData = {
          email: this.decryptValue(userMail),
          password: this.decryptValue(userPassword),
        };

        // todo: AUTO LOGIN
        axios
          .post(
            `${API_URL}/api/login?language=${localStorage.getItem("language")}`,
            formData
          )
          .then((response) => {
            if (response.data.token) {
              localStorage.setItem("token", response.data.token);
              this.$router.push(this.action);
            } else {
              localStorage.setItem("adminToken", response.data.adminToken);
              this.$router.push({ name: "ListesDesUtilisateurs" });
            }
          })
          .catch((error) => {
            if (error.response.status === 423) {
              this.credentionError = [];
              this.credentionError.push(
                `${this.$t("accountSuspended")} ${EMAIL}`
              );
            } else {
              this.credentionError = [];
              this.credentionError.push(this.$t("emailOrpasswordInvalid"));
            }
            this.errorCount++;
          });
      }
    },
    checkForm(e) {
      e.preventDefault();
      this.errorMail = [];
      this.errorPwd = [];
      this.buttonDisable = true;

      if (!this.email) {
        this.errorMail.push(this.$t("addEmail"));
      } else if (!this.validEmail(this.email)) {
        this.errorMail.push(this.$t("emailInvalid"));
      }

      if (!this.password) {
        this.errorPwd.push(this.$t("errorAddPwd"));
      }

      if (!this.errorPwd.length && !this.errorMail.length) {
        const formData = {
          email: this.email,
          password: this.password,
        };
        axios
          .post(`${API_URL}/api/login`, formData)
          .then((response) => {
            if (response.data.token) {
              localStorage.setItem("token", response.data.token);
              this.$router.push(this.action);
            } else {
              localStorage.setItem("adminToken", response.data.adminToken);
              this.$router.push("/listes-des-utilisateurs");
            }
            if (this.rememberMe) {
              localStorage.setItem("userMail", this.encryptValue(this.email));
              localStorage.setItem("userPwd", this.encryptValue(this.password));
            }
          })
          .catch((error) => {
            if (error.response.status === 423) {
              this.credentionError = [];
              this.credentionError.push(
                `${this.$t("accountSuspended")} ${EMAIL}`
              );
            } else {
              this.credentionError = [];
              this.credentionError.push(this.$t("emailOrpasswordInvalid"));
            }
            this.errorCount++;
          });
      }
    },
    validEmail(email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    ErrorCount() {
      return this.errorCount === ERROR_COUNT;
    },
    verifyCaptcha(response) {
      if (response) this.captcha = true;
    },
    errorCaptcha() {
      this.captcha = false;
    },
    translate() {
      const cap = document.querySelector("#cap > div > div > div > iframe");
      let src = cap.getAttribute("src");
      const lng = src.includes("hl=fr") ? "hl=fr" : "hl=en";
      const target = this.$i18n.locale;
      src = src.replace(lng, "hl=" + target + "&");
      cap.setAttribute("src", src);
    },
  },
  mounted: () => {
    localStorage.setItem("errcon", 0);
  },
  created() {
    document.title = this.$route.meta.title;
    this.autoLogin();
  },
  watch: {
    errorCount(val) {
      localStorage.setItem("errcon", this.errorCount);
      if (val === ERROR_COUNT) {
        this.connectionLimitReached = true;
        this.translate();
        this.captcha = false;
      }
    },
    "$i18n.locale"() {
      this.translate();
    },
  },
};
</script>

<style>
.captcha-wrapper > div {
  height: 78px;
  overflow: hidden;
}
#connexion .locale-changer {
  margin-bottom: 20px;
  margin-right: 0;
}
.lang {
  margin-bottom: 8px;
  /* margin-left: 80%; */
}
#connexion .switch-langue {
  margin-right: 0;
}
</style>
