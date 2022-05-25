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
          <h1 v-show="!send" class="titre-form-user">
            {{ $t("forgetPassword:titreForm") }}
          </h1>

          <p
            class="description-form-user"
            v-if="!send"
            v-html="$t('forgetPassword:descriptionForm')"
          ></p>
        </div>

        <div class="form-user-wrapper">
          <form
            action=""
            class="form-user"
            novalidate="true"
            @submit.prevent="checkForm"
          >
            <div v-if="!send" class="form-group">
              <md-field>
                <label for="email" :class="errorMail.length && 'error-input'">{{
                  $t("email")
                }}</label>
                <md-input
                  :class="errorMail.length ? 'error-input' : null"
                  type="email"
                  name="email"
                  id="email"
                  autocomplete="email"
                  v-model="email"
                  @keyup="removeError"
                />
              </md-field>
              <span v-if="errorMail.length" class="d-flex flex-column">
                <span class="error" v-for="error in errorMail" :key="error">{{
                  error
                }}</span>
              </span>
            </div>

            <div class="text-center" v-else>
              <svg
                id="account_circle-24px"
                xmlns="http://www.w3.org/2000/svg"
                width="92"
                height="92"
                viewBox="0 0 92 92"
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
              <h1 class="titre-form-user mt-3">
                {{ $t("forgetPassword:titreForm") }}
              </h1>
              <div class="text-center mb-3 mx-auto" style="max-width: 380px;">
                {{ $t("emailSentMessage") }}
              </div>
            </div>

            <PredictSubmit
              v-if="!send"
              v-bind:label="$t('textSubmit')"
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
              <div class="inscription-link-container text-center" v-if="send">
                {{ $t("info:link") }}<br />
                {{ $t("info:link1") }}
                <router-link
                  to="#"
                  @click.native="handleResendMail"
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
                  {{ $t("resendMail") }}
                </router-link>
                <p class="mt-3" v-else>
                  {{ $t("linkMailMessage") }} {{ countDown }}s
                </p>
              </div>

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
import axios from "axios";
import HomeBienvenue from "../HomeBienvenue/HomeBienvenue.vue";
import PredictSubmit from "../Input/PredictSubmit.vue";
import MainLayout from "../language/MainLayout.vue";
import { API_URL, RESEND_WAITING } from "../../utils/Constant";

export default {
  name: "ForgetPassword",
  data: function() {
    return {
      errorMail: [],
      email: null,
      action: "/reinitialisation",
      send: false,
      resend: false,
      success: [],
      countDown: RESEND_WAITING / 1000,
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
  methods: {
    countDownTimer() {
      clearTimeout(this.countdownTimeout);
      if (this.countDown > 0) {
        this.countdownTimeout = setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 1000);
      }
    },
    handleSendEmail() {
      axios
        .post(
          `${API_URL}/api/resetPassword?language=${localStorage.getItem(
            "language"
          )}`,
          {
            email: this.email,
          }
        )
        .then(() => {
          this.send = true;
          this.success.push(this.$t("emailSent"));

          const elements = document.getElementsByClassName("alert");

          setTimeout(() => {
            while (elements.length > 0) elements[0].remove();
          }, 2000);
        })
        .catch(() => {
          this.errorMail.push(this.$t("emailNoAccountAssociated"));
         
        });
      if (this.send)
        setTimeout(() => {
          this.resend = false;
        }, RESEND_WAITING);
    },
    checkForm(e) {
      e.preventDefault();
      if (this.send) {
        this.resend = true;
      }
      this.errorMail = [];
      this.buttonDisable = true;

      if (!this.email) {
        this.errorMail.push(this.$t("addEmail"));
      } else if (!this.validEmail(this.email)) {
        this.errorMail.push(this.$t("emailInvalid"));
      }
      if (!this.errorMail.length) this.handleSendEmail();
    },
    handleResendMail(e) {
      e.preventDefault();
      this.countDown = RESEND_WAITING / 1000;
      if (this.send) this.resend = true;
      this.handleSendEmail();
      this.countDownTimer();
    },
    removeError() {
      this.errorMail = [];
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
