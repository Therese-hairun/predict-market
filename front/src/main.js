import Vue from "vue";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "./assets/css/custom-material.css";
import "./assets/css/fonts.css";
import "./assets/css/global.css";
import "./assets/css/responsive.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import VueRouter from "vue-router";
import VueRecaptcha from "vue-recaptcha";
import i18n from "./i18n";
import store from "./store";
import VueTelInput from "vue-tel-input";
import "vue-tel-input/dist/vue-tel-input.css";

import App from "./App.vue";
import VueHtml2pdf from "vue-html2pdf";
import router from "./router";

import JwPagination from "jw-vue-pagination";
Vue.component("jw-pagination", JwPagination);

import VueCryptojs from "vue-cryptojs";
Vue.use(VueCryptojs);

import VueSocialSharing from "vue-social-sharing";
Vue.use(VueSocialSharing);

Vue.use(VueHtml2pdf);
Vue.use(VueRecaptcha);
Vue.use(VueMaterial);

import VueMaterialLocales from "@undecaf/vue-material-locales";
import fr from "@undecaf/vue-material-locales/dist/locale/fr";
import en from "@undecaf/vue-material-locales/dist/locale/en-US";
Vue.use(VueMaterialLocales, [fr, en]);
Vue.material.selectLocale("en-US");

Vue.use(VueRouter);
Vue.use(VueTelInput, {
  mode: "international",
});
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.config.productionTip = false;

new Vue({
  i18n,
  router,
  mode: "history",
  store,
  render: (h) => h(App),
}).$mount("#app");
