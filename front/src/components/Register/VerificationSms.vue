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
        <router-link
          to="/register"
          class="back position-absolute mb-5 align-self-start"
          ><i class="fa fa-chevron-left" aria-hidden="true"></i>
          {{ $t("back") }}</router-link
        >
        <div class="content-right text-center">
          <h1 class="titre-form-user">{{ $t("smsVerification") }}</h1>
          <p class="description-form-user">
            {{ $t("verificationSms:descriptionForm") }}
            <strong>{{ phone }}</strong>
          </p>
        </div>

        <div class="form-user-wrapper">
          <form class="form-user" novalidate="true" @submit.prevent="checkForm">
            <div
              class="
                form-group
                code-activation
                d-flex
                flex-nowrap
                justify-content-between
              "
            >
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number1"
                  id="number1"
                  autocomplete="off"
                  v-model="number1"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number2"
                  id="number2"
                  autocomplete="off"
                  v-model="number2"
                  ref="n2"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number3"
                  id="number3"
                  autocomplete="off"
                  v-model="number3"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number4"
                  id="number4"
                  autocomplete="off"
                  v-model="number4"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number5"
                  id="number5"
                  autocomplete="off"
                  v-model="number5"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number6"
                  id="number6"
                  autocomplete="off"
                  v-model="number6"
                  @keypress="numericOnly"
                />
              </md-field>
            </div>
            <span v-if="errors.length" class="d-flex flex-column text-center">
              <span class="error" v-for="error in errors" :key="error">{{
                error
              }}</span>
            </span>

            <PredictSubmit
              v-bind:label="$t('verify')"
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
              <div class="inscription-link-container text-center">
                <p v-if="!resend">
                  {{ $t("codeNotSentMessage") }}
                </p>
                <router-link
                  to="#"
                  @click.native="resendCode"
                  class="mt-2 d-block"
                  v-if="!resend"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="22"
                    viewBox="0 0 16 22"
                  >
                    <path
                      id="Tracé_19663"
                      data-name="Tracé 19663"
                      d="M12,6V9l4-4L12,1V4A7.986,7.986,0,0,0,5.24,16.26L6.7,14.8A5.87,5.87,0,0,1,6,12,6,6,0,0,1,12,6Zm6.76,1.74L17.3,9.2A5.99,5.99,0,0,1,12,18V15L8,19l4,4V20A7.986,7.986,0,0,0,18.76,7.74Z"
                      transform="translate(-4 -1)"
                      fill="#242C36"
                    />
                  </svg>
                  {{ $t("resendCode") }}
                </router-link>
                <p v-else>
                  {{ $t("codeSent") }}
                  {{ countDown }}s
                </p>
              </div>

              <hr />
              <div class="inscription-link-container text-center">
                {{ $t("haveAccount") }}
                <router-link to="/">{{ $t(logIn) }}</router-link>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import HomeBienvenue from "../HomeBienvenue/HomeBienvenue.vue";
import PredictSubmit from "../Input/PredictSubmit.vue";
import MainLayout from "../language/MainLayout.vue";
import { API_URL, RESEND_WAITING, SMS_CODE } from "../../utils/Constant";

export default {
  name: "VerificationSms",
  data: () => {
    return {
      errors: [],
      phone: null,
      number1: null,
      number2: null,
      number3: null,
      number4: null,
      number5: null,
      number6: null,
      correctCode: "",
      codeValidation: null,
      action: "/envoi-d-email",
      resend: false,
      countDown: RESEND_WAITING / 1000,
    };
  },
  computed: {
    isDisabled() {
      if (
        this.number1 &&
        this.number2 &&
        this.number3 &&
        this.number4 &&
        this.number5 &&
        this.number6
      ) {
        return false;
      }
      return true;
    },
  },
  methods: {
    countDownTimer() {
      if (this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 1000);
      }
      if (this.countDown === 0) this.resend = false;
    },
    async resendCode() {
      this.countDown = RESEND_WAITING / 1000;
      this.resend = true;
      const SMS = {
        From: "PredictM",
        To: localStorage.getItem("phone").replaceAll(" ", ""),
        Text: `${this.$t("smsCode")} ${SMS_CODE}`,
      };
      axios.post(`${API_URL}/api/sendSMS`, SMS);
      this.countDownTimer();

      setTimeout(() => {
        this.resend = false;
      }, RESEND_WAITING);
    },
    async checkForm(e) {
      e.preventDefault();
      this.errors = [];

      if (
        this.number1 &&
        this.number2 &&
        this.number3 &&
        this.number4 &&
        this.number5 &&
        this.number6
      ) {
        this.codeValidation =
          this.number1 +
          this.number2 +
          this.number3 +
          this.number4 +
          this.number5 +
          this.number6;

        await axios
          .patch(`${API_URL}/api/activate_phone`, {
            phone: localStorage.getItem("phone"),
            code: this.codeValidation,
          })
          .catch(() => {
            this.errors.push(this.$t("errorCode"));
          });
      }

      if (!this.errors.length) {
        this.$router.push(this.action);
      }
    },
    numericOnly(e) {
      if (e.charCode >= 48 && e.charCode <= 57) {
        document.getElementById("number2").focus();
        return true;
      }
      return e.preventDefault();
    },
  },
  components: {
    HomeBienvenue,
    PredictSubmit,
    MainLayout,
  },
  watch: {
    number1(val) {
      if (val) {
        document.getElementById("number2").focus();
      }
    },
    number2(val) {
      if (val) {
        document.getElementById("number3").focus();
      }
    },
    number3(val) {
      if (val) {
        document.getElementById("number4").focus();
      }
    },
    number4(val) {
      if (val) {
        document.getElementById("number5").focus();
      }
    },
    number5(val) {
      if (val) {
        document.getElementById("number6").focus();
      }
    },
  },
  created() {
    document.title = this.$route.meta.title;
    this.phone = localStorage.getItem("phone");
  },
};
</script>
