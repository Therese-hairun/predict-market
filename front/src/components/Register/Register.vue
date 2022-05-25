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

          <h1 class="titre-form-user">{{ $t("register") }}</h1>

          <p class="description-form-user">{{ $t("info") }}</p>
        </div>

        <div class="form-user-wrapper">
          <form
            action=""
            class="form-user"
            @submit="checkForm"
            novalidate="true"
          >
            <div class="row-fluid d-flex flex-wrap flex-xl-row">
              <div class="col-12 col-xl-6 p-0 inscription-prenom">
                <div class="form-group">
                  <md-field>
                    <label
                      for="prenom"
                      :class="errorPrenomRequired.length && 'error-input'"
                      >{{ $t("firstname") }}</label
                    >
                    <md-input
                      name="prenom"
                      id="prenom"
                      autocomplete="prenom"
                      v-model="prenom"
                      :class="errorPrenomRequired.length && 'error-input'"
                    />
                  </md-field>

                  <span
                    v-if="errorPrenomRequired.length"
                    class="d-flex flex-column"
                  >
                    <span
                      class="error"
                      v-for="error in errorPrenomRequired"
                      :key="error"
                      >{{ error }}</span
                    >
                  </span>
                </div>
              </div>
              <div class="col-12 col-xl-6 p-0 inscription-nom">
                <div class="form-group">
                  <md-field>
                    <label
                      for="nom"
                      :class="errorNomRequired.length && 'error-input'"
                      >{{ $t("lastname") }}</label
                    >
                    <md-input
                      name="nom"
                      id="nom"
                      autocomplete="nom"
                      v-model="nom"
                      :class="errorNomRequired.length && 'error-input'"
                    />
                  </md-field>
                  <span
                    v-if="errorNomRequired.length"
                    class="d-flex flex-column"
                  >
                    <span
                      class="error"
                      v-for="error in errorNomRequired"
                      :key="error"
                      >{{ error }}</span
                    >
                  </span>
                </div>
              </div>
            </div>

            <div class="form-group">
              <vue-tel-input
                v-model="telephone"
                class="border-0"
                :inputOptions="tel_options"
                :class="errorTelephoneRequired.length && 'error-input'"
              ></vue-tel-input>
              <span
                v-if="errorTelephoneRequired.length"
                class="d-flex flex-column"
              >
                <span
                  class="error"
                  v-for="error in errorTelephoneRequired"
                  :key="error"
                  >{{ error }}</span
                >
              </span>
            </div>

            <div class="form-group">
              <md-field>
                <label for="code" :class="errorCode.length && 'error-input'">{{
                  $t("referral-code")
                }}</label>
                <md-input
                  type="text"
                  name="code"
                  id="code"
                  autocomplete="code"
                  v-model="code"
                  :class="errorCode.length && 'error-input'"
                />
              </md-field>
              <span v-if="errorCode.length" class="d-flex flex-column">
                <span class="error" v-for="error in errorCode" :key="error">{{
                  error
                }}</span>
              </span>
              <div class="help_input">{{ $t("referral-label") }}</div>
            </div>

            <div class="form-group">
              <md-field>
                <label
                  for="password"
                  :class="invalidPassword ? 'error-input' : null"
                  >{{ $t("password") }}</label
                >
                <md-input
                  type="password"
                  name="password"
                  id="password"
                  autocomplete="password"
                  v-model="password"
                  @keyup="handlePassword"
                  :class="invalidPassword ? 'error-input' : null"
                />
              </md-field>
              <span v-if="invalidPassword" class="d-flex flex-column">
                <span class="error">{{ $t("errorPwdInvalid") }}</span>
              </span>
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
            </div>

            <div class="form-group">
              <md-field>
                <label
                  for="password"
                  :class="disabled && incoherentPassword && 'error-input'"
                  >{{ $t("confirm-password") }}</label
                >
                <md-input
                  type="password"
                  name="confirmPassword"
                  id="confirmPassword"
                  autocomplete="confirmPassword"
                  v-model="confirmPassword"
                  @keyup="handleConfirmPassword"
                  :class="disabled && incoherentPassword && 'error-input'"
                />
              </md-field>
              <span v-if="incoherentPassword" class="d-flex flex-column">
                <span class="error">{{ $t("errorConfirmPwdConfirm") }}</span>
              </span>
            </div>

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
                  align-items-start
                  justify-content-between
                  rememberMe-wrapper
                "
              >
                <md-checkbox
                  id="acceptCGU"
                  name="acceptCGU"
                  v-model="acceptCGU"
                  class="mt-0"
                  ><span>
                    {{ $t("left-accept-cgu") }}
                    <a href="#" title="CGU" target="_blank">CGU</a>
                    {{ $t("right-accept-cgu") }}
                  </span></md-checkbox
                >

                <div id="cap" class="captcha-wrapper overflow-hidden">
                  <vue-recaptcha
                    sitekey="6Lc0FGccAAAAAKbydlgQekIURGrgF-bo2E-Etfp_"
                    @verify="verifyCaptcha"
                    @error="errorCaptcha"
                  >
                  </vue-recaptcha>
                </div>
              </div>
            </div>
            <PredictSubmit
              v-bind:label="label"
              :disabled="isDisabled"
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
              {{ $t("already-have-account") }}
              <router-link to="/">{{ $t("login") }}</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import HomeBienvenue from "../HomeBienvenue/HomeBienvenue.vue";
import PredictSubmit from "../Input/PredictSubmit.vue";
import MainLayout from "../language/MainLayout.vue";
import VueRecaptcha from "vue-recaptcha";
import axios from "axios";
import { API_URL, SMS_CODE } from "../../utils/Constant";

import moment from "moment";
export default {
  name: "Register",
  data() {
    return {
      tel_options: {
        placeholder: this.$t("phone:placeholder"),
      },
      label: "signin",
      action: "/verification-sms",
      errorMail: [],
      errorPwd: [],
      errorCode: [],
      errorConfirmPwd: [],
      errorRequired: [],
      errorNomRequired: [],
      errorPrenomRequired: [],
      errorTelephoneRequired: [],
      errorConf: "",
      nom: null,
      prenom: null,
      telephone: null,
      phone: null,
      code: null,
      email: null,
      password: null,
      confirmPassword: "",
      acceptCGU: null,
      togglePassword: true,
      disabled: true,
      invalidPassword: false,
      incoherentPassword: false,
      captcha: null,
    };
  },
  computed: {
    isDisabled() {
      if (
        this.nom &&
        this.prenom &&
        this.telephone &&
        this.password &&
        this.confirmPassword &&
        this.acceptCGU &&
        !this.invalidPassword &&
        !this.disabled &&
        this.captcha
      ) {
        return false;
      }
      return true;
    },
  },
  methods: {
    translate() {
      const cap = document.querySelector("#cap > div > div > div > iframe");
      let src = cap.getAttribute("src");
      const lng = src.includes("hl=fr") ? "hl=fr" : "hl=en";
      const target = this.$i18n.locale;
      src = src.replace(lng, "hl=" + target + "&");
      cap.setAttribute("src", src);
    },
    handleConfirmPassword() {
      if (
        this.password != this.confirmPassword &&
        this.confirmPassword.length
      ) {
        this.disabled = true;
        this.incoherentPassword = true;
      } else {
        this.disabled = false;
        this.incoherentPassword = false;
      }
    },
    handlePassword() {
      if (this.confirmPassword.length) {
        if (!this.validPassword(this.password)) {
          this.disabled = true;
          this.invalidPassword = true;
        } else {
          this.disabled = false;
          this.invalidPassword = false;
          if (this.password != this.confirmPassword) {
            this.incoherentPassword = true;
            this.disabled = true;
          } else {
            this.incoherentPassword = false;
            this.disabled = false;
          }
        }
      } else {
        if (!this.validPassword(this.password)) {
          this.disabled = true;
          this.invalidPassword = true;
        } else {
          this.disabled = false;
          this.invalidPassword = false;
        }
      }
    },
    generateCode() {
      return (Math.random() + 1)
        .toString(36)
        .substr(2, 7)
        .toUpperCase();
    },
    removeError() {
      this.errorTelephoneRequired = [];
      this.errorPwd = [];
    },
    async verifyCodeParrainage(payload) {
      try {
        const res = await axios.post(`${API_URL}/api/check_code`, payload);
        if (!res.data.Status) this.errorCode.push(this.$t("codeDoesntExist"));
      } catch (e) {
        //
      }
    },
    async checkForm(e) {
      e.preventDefault();
      this.errorMail = [];
      this.errorPwd = [];
      this.errorCode = [];
      this.errorConfirmPwd = [];
      this.errorRequired = [];
      this.errorNomRequired = [];
      this.errorPrenomRequired = [];
      this.errorTelephoneRequired = [];

      if (this.code) {
        //VERIFICATION CODE PARRAINAGE
        const payload = {
          code: this.code,
        };
        await this.verifyCodeParrainage(payload);
      }
      if (!this.password) {
        this.errorPwd.push(this.$t("errorAddPwd"));
      }

      if (!this.confirmPassword) {
        this.errorConfirmPwd.push(this.$t("errorConfirmPwd"));
      }

      if (!this.prenom) {
        this.errorPrenomRequired.push(this.$t("errorNomRequired"));
      }
      if (!this.nom) {
        this.errorNomRequired.push(this.$t("errorPrenomRequired"));
      }
      if (!this.telephone) {
        this.errorTelephoneRequired.push(this.$t("errorTelephoneRequired"));
      }
      if (!this.validPhone(this.telephone.replaceAll(" ", ""))) {
        this.errorTelephoneRequired.push(this.$t("errorTelephoneInvalid"));
      }

      if (
        !this.errorCode.length &&
        !this.errorPwd.length &&
        !this.errorRequired.length &&
        !this.errorNomRequired.length &&
        !this.errorPrenomRequired.length &&
        !this.errorTelephoneRequired.length
      ) {
        const smsCode = SMS_CODE;
        const SMS = {
          From: "PredictM",
          To: this.telephone.replaceAll(" ", ""),
          Text: `${this.$t("smsCode")} ${smsCode}`,
        };
        const formData = {
          firstname: this.prenom,
          lastname: this.nom,
          password: this.password,
          email: this.nom + "@default.com",
          phone: this.telephone.replaceAll(" ", ""),
          created_at: moment(Date.now())
            .utcOffset(0, false)
            .toISOString(),
          sms_validation_code: smsCode,
          relationship_code: this.code,
          storage_code_client: this.generateCode(),
        };
        axios
          .post(`${API_URL}/api/create_client`, formData)
          .then((response) => {
            if (response) {
              axios.post(`${API_URL}/api/sendSMS`, SMS);
              localStorage.setItem("id", response.data.id);
              localStorage.setItem("phone", this.telephone.replaceAll(" ", ""));
              this.$router.push(this.action);
            }
          })
          .catch((error) => {
            this.errorTelephoneRequired.push(error.response.data.Message);
          });
      }
    },
    validEmail(email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    validPassword(pwd) {
      var re = /^(?=.*[a-z].*[A-Z]|[A-Z].*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
      return re.test(pwd);
    },
    validPhone(phoneNumber) {
      var re = /^\+(?:[0-9] ?){6,14}[0-9]$/;
      return re.test(phoneNumber);
    },
    onVerify: function(response) {
      if (response) this.form.robot = true;
    },
    verifyCaptcha(response) {
      if (response) this.captcha = true;
    },
    errorCaptcha() {
      this.captcha = false;
    },
  },
  components: {
    HomeBienvenue,
    PredictSubmit,
    MainLayout,
    "vue-recaptcha": VueRecaptcha,
  },
  created() {
    document.title = this.$route.meta.title;
  },
  watch: {
    "$i18n.locale"() {
      this.tel_options = {
        placeholder: this.$t("phone:placeholder"),
      };
      this.translate();
    },
  },
};
</script>
