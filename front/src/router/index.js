import Vue from "vue";
import Router from "vue-router";
import { API_URL } from "../utils/Constant";
import axios from "axios";

import Login from "../components/Login/Login.vue";
import Register from "../components/Register/Register.vue";
import VerificationSms from "../components/Register/VerificationSms.vue";
import EnvoiEmail from "../components/Register/EnvoiEmail.vue";
import VerificationEmail from "../components/Register/VerificationEmail.vue";
import Felicitation from "../components/Register/Felicitation.vue";
import ForgetPassword from "../components/Login/ForgetPassword.vue";
import Reinitialisation from "../components/Login/Reinitialisation.vue";
import SuccessPwd from "../components/Login/SuccessPwd.vue";
import Dashboard from "../components/Dashboard/Dashboard.vue";
import TousLesCryptos from "../components/TousLesCryptos/TousLesCryptos.vue";
import VisualiserCrypto from "../components/TousLesCryptos/VisualiserCrypto.vue";
import ListesDesUtilisateurs from "../components/ListesDesUtilisateurs/ListesDesUtilisateurs.vue";
import DetailsUtilisateur from "../components/DetailsUtilisateur/DetailsUtilisateur.vue";
import GestionAbonnement from "../components/GestionAbonnement/GestionAbonnement.vue";
import MonCompte from "../components/MonCompte/MonCompte.vue";
import Abonnement from "../components/Abonnement/Abonnement.vue";
import Commande from "../components/Commande/Commande.vue";
import CodeReduction from "../components/CodeReduction/CodeReduction.vue";
import HelloWorld from "../components/HelloWorld.vue";
import GestionPaires from "../components/GestionPaires/GestionPaires.vue";
import Support from "../components/Support/Support.vue";
import DetailsSupport from "../components/Support/DetailsSupport.vue";
import DetailsCouples from "../components/GestionPaires/DetailsCouples.vue";
import GestionTickets from "../components/GestionTickets/GestionTickets.vue";
import DetailTicket from "../components/GestionTickets/DetailTicket.vue";
import ExpiredSubscription from "../components/ExpiredSubscription/ExpiredSubscription.vue";
import PageNotFound from "../components/PageNotFound/PageNotFound.vue";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: "/404",
      name: "NotFound",
      component: PageNotFound,
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "*",
      redirect: "404",
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "/",
      component: Login,
      name: "Login",
      meta: { requiresAuth: false, title: "Connexion" },
    },
    {
      path: "/register",
      component: Register,
      name: "Register",
      meta: { requiresAuth: false, title: "Inscription" },
    },
    {
      path: "/verification-sms",
      component: VerificationSms,
      name: "VerificationSms",
      meta: { requiresAuth: false, title: "Verification SMS" },
    },
    {
      path: "/envoi-d-email",
      component: EnvoiEmail,
      name: "EnvoiDEmail",
      meta: { requiresAuth: false, title: "Envoi Email" },
    },
    {
      path: "/verification-email",
      component: VerificationEmail,
      name: "VerificationEmail",
      meta: { requiresAuth: false, title: "Verification Email" },
    },
    {
      path: "/felicitation/:id",
      component: Felicitation,
      name: "Felicitation",
      meta: { requiresAuth: false, title: "Felicitation" },
    },
    {
      path: "/mot-de-passe-oublie",
      component: ForgetPassword,
      name: "ForgetPassword",
      meta: { requiresAuth: false, title: "Mot de passe oublié" },
    },
    {
      path: "/reinitialisation/:id",
      component: Reinitialisation,
      name: "Reinitialisation",
      meta: { requiresAuth: false, title: "Réinitialisation mot de passe" },
    },
    {
      path: "/success-pwd",
      component: SuccessPwd,
      name: "SuccessPwd",
      meta: { requiresAuth: false, title: "Mot de passe réinitialisé" },
    },
    {
      path: "/dashboard",
      component: Dashboard,
      name: "Dashboard",
      meta: { requiresAuth: true, title: "Dashboard" },
    },
    {
      path: "/visualiser-crypto/:symbol",
      component: VisualiserCrypto,
      name: "VisualiserCrypto",
      meta: { requiresAuth: true, title: "Visualiser Crypto" },
    },
    {
      path: "/tous-les-couples",
      component: TousLesCryptos,
      name: "TousLesCryptos",
      meta: { requiresAuth: true, title: "Couples" },
    },
    {
      path: "/listes-des-utilisateurs",
      component: ListesDesUtilisateurs,
      name: "ListesDesUtilisateurs",
      meta: { requiresAuth: true, title: "Liste utilisateurs" },
    },
    {
      path: "/listes-des-utilisateurs/detail-user",
      component: DetailsUtilisateur,
      name: "DetailsUtilisateur",
      meta: { requiresAuth: true, title: "Details utilisateur" },
    },
    {
      path: "/gestion-abonnement",
      component: GestionAbonnement,
      name: "GestionAbonnement",
      meta: { requiresAuth: true, title: "Gestion abonnements" },
    },
    {
      path: "/abonnement",
      component: Abonnement,
      name: "Abonnement",
      meta: { requiresAuth: true, title: "Abonnement" },
    },
    {
      path: "/abonnement/commande/:typeId/:status",
      component: Commande,
      name: "Commande",
      meta: { requiresAuth: true, title: "Commande" },
    },
    {
      path: "/mon-compte",
      component: MonCompte,
      name: "Profil",
      meta: { requiresAuth: true, title: "Mon compte" },
    },
    {
      path: "/support",
      component: Support,
      name: "Support",
      props: true,
      meta: { requiresAuth: true, title: "Support" },
    },
    {
      path: "/support/details-ticket",
      component: DetailsSupport,
      name: "DetailsSupport",
      props: true,
      meta: { requiresAuth: true, title: "Details support" },
    },
    {
      path: "/code-de-reduction",
      component: CodeReduction,
      name: "CodeReduction",
      meta: { requiresAuth: true, title: "Code de réduction" },
    },
    {
      path: "/gestion-des-paires",
      component: GestionPaires,
      name: "GestionPaires",
      meta: { requiresAuth: true, title: "Gestion des paires" },
    },
    {
      path: "/gestion-des-paires/details-de-couple",
      component: DetailsCouples,
      name: "details-de-couple",
      meta: { requiresAuth: true, title: "Details de couple" },
    },
    {
      path: "/pdf",
      component: HelloWorld,
      name: "pdf",
      meta: { requiresAuth: true, title: "pdf" },
    },
    {
      path: "/tous-les-tickets",
      component: GestionTickets,
      name: "gestion-tickets",
      meta: { requiresAuth: true, title: "Gestion des tickets" },
    },
    {
      path: "/tous-les-tickets/details-ticket",
      component: DetailTicket,
      name: "DetailTicket",
      meta: { requiresAuth: true, title: "Details tickets" },
    },
    {
      path: "/expired-subscription",
      component: ExpiredSubscription,
      name: "ExpiredSubscription",
      meta: { requiresAuth: true, title: "Abonnement expiré" },
    },
  ],
});

router.beforeEach(async (to, from, next) => {
  let account = false;
  if (localStorage.length !== 0 && localStorage.getItem("token") !== "null") {
    try {
      const response = await axios.post(
        `${API_URL}/api/verify_account`,
        {},
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      account = response.data.status;
    } catch (e) {
      account = false;
    }
  }
  if (to.meta.requiresAuth) {
    if (account) next();
    else {
      // account false
      if (
        (localStorage.getItem("token") &&
          localStorage.getItem("token") !== "null") ||
        (localStorage.getItem("adminToken") &&
          localStorage.getItem("adminToken") !== "null")
      ) {
        next();
      } else
        next({
          name: "Login",
        });
    }
    if (account === false && localStorage.getItem("token") !== "null") {
      next({
        name: "Login",
      });
    }
  } else {
    next();
  }
});
export default router;
