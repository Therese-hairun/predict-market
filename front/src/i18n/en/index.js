import LoginComponent from "./LoginComponent.json";
import SignInComponent from "./SignInComponent.json";
import dashboard from "./dashboard.json";
import global from "./global.json";
import ticket from "./ticket.json";
import permanentfull from "./permanentfull.json";
import tousLesCouples from "./tousLesCouples.json";
import subscription from "./subscription.json";
import commande from "./commande.json";
import detailSupport from "./detailSupport.json";
import myAccount from "./myAccount.json";
import listUsers from "./listUsers.json";
import codeReduction from "./codeReduction.json";
import detailsCouple from "./detailsCouple.json";
import couple from "./couple.json";
import lang from "./langswitch.json";
import visualiserCouple from "./visualiserCouple.json";
import sidebar from "./sidebar.json";
import expiredSubscription from "./expiredSubscription.json";
import gestionAbonnement from "./gestionAbonnement.json";

export default {
  ...global,
  ...LoginComponent,
  ...SignInComponent,
  ...dashboard,
  ...ticket,
  ...permanentfull,
  ...tousLesCouples,
  ...subscription,
  ...detailSupport,
  ...myAccount,
  ...listUsers,
  ...codeReduction,
  ...commande,
  ...detailsCouple,
  ...couple,
  ...lang,
  ...visualiserCouple,
  ...sidebar,
  ...expiredSubscription,
  ...gestionAbonnement,
};
