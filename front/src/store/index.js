import Vue from "vue";
import Vuex from "vuex";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";
import user from "./modules/user";
import subscription from "./modules/subscription";
import client from "./modules/client";
import reduction from "./modules/reduction";
import payment from "./modules/payment";
import facture from "./modules/facture";
import admin from "./modules/admin";
import ticket from "./modules/ticket";
import paire from "./modules/paire";
import listPaires from "./modules/listPaires";
import parrainage from "./modules/parrainage";
import couple from "./modules/couple";
import dashboard from "./modules/dashboard";
import downgrade from "./modules/downgrade";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {},
  getters,
  mutations,
  actions,
  modules: {
    user,
    subscription,
    client,
    reduction,
    payment,
    facture,
    admin,
    ticket,
    paire,
    parrainage,
    listPaires,
    couple,
    dashboard,
    downgrade,
  },
});

export default store;
