import fr from "./i18n/fr";
import en from "./i18n/en";
import Vue from "vue";
import VueI18n from "vue-i18n";

Vue.use(VueI18n);

export default new VueI18n({
  locale: "en",
  messages: {
    fr: fr,
    en: en,
  },
});
