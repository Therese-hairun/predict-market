<template lang="">
  <div class="dashboard">
    <PermanentFull
      :titre="titre"
      :icon="icon"
      :menuItems="menuItems"
      :admin="true"
    >
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div class="py-4 flex-grow-1 d-flex flex-column">
          <div id="details-utilisateur">
            <div class="d-flex flex-column justify-content-center">
              <router-link
                :to="{
                  name: 'ListesDesUtilisateurs',
                }"
                class="back mb-3 align-self-start"
                ><i class="fa fa-chevron-left" aria-hidden="true"></i>
                {{ $t("back") }}</router-link
              >
              <div class="titre-page">{{ $t("details") }}</div>
              <p class="description">
                {{ $t("info:userDetail") }}
              </p>
            </div>
            <div class="md-layout md-gutter column-wrapper">
              <div class="md-layout-item dashboard-border bloc-content">
                <div
                  class="avatar-wrapper d-flex flex-column align-items-center mt-3 mb-5"
                >
                  <b-avatar
                    v-if="imgAvatar"
                    class="mb-4"
                    size="146px"
                    :src="imgAvatar"
                  ></b-avatar>
                  <div
                    class="fake-avatar mb-4 rounded-circle "
                    v-else
                    style="width:146px; height:146px;"
                  >
                    <div
                      class="text-wrapper text-uppercase rounded-circle d-flex align-items-center justify-content-center w-100 h-100 text-center"
                    >
                      {{ userInitial }}
                    </div>
                  </div>
                  <div class="nom-utilisateur">
                    {{ userFirstname }} {{ userLastname }}
                  </div>
                  <a class="mail-utilisateur">{{ userEmail }}</a>
                </div>
                <BlocAbonnement
                  :typeAbonnement="userSubscribeName"
                  :emplacementDispo="emplacementDispo"
                  :emplacementUtilise="emplacementUtilise"
                  :titreAbonnement="$t('subscription')"
                  :iconAbonnement="iconAbonnement"
                ></BlocAbonnement>
                <div class="d-flex flex-wrap justify-content-between">
                  <span class="pseudo-label">{{ $t("suspendUser") }}</span>
                  <p class="d-flex align-items-center">
                    <strong class="mr-1">{{
                      userAccountStatus ? $t("active") : $t("desactive")
                    }}</strong
                    ><md-switch
                      class="table-switch my-0"
                      v-model="userAccountStatus"
                      @change="updateUserStatus()"
                    ></md-switch>
                  </p>
                </div>
                <div class="d-flex flex-column">
                  <span class="pseudo-label">{{ $t("registrationDate") }}</span>
                  <p>{{ formatDate($t("dateFormat"), user.start) }}</p>
                </div>
                <div class="d-flex flex-column">
                  <span class="pseudo-label">{{ $t("totalExpenses") }}</span>
                  <p>{{ pointToComma(user.total_discount) }} €</p>
                </div>
                <div class="d-flex flex-column">
                  <span class="pseudo-label">{{ $t("nbrAffilie") }}</span>
                  <p>{{ user.number_of_affiliated }}</p>
                </div>
                <div class="d-flex flex-column">
                  <span class="pseudo-label">{{ $t("cumul:credits") }}</span>
                  <p>{{ pointToComma(previousCredits) }} €</p>
                </div>
                <div class="d-flex flex-column">
                  <span class="pseudo-label">{{ $t("cumul:days") }}</span>
                  <p>{{ previousJoursGratuits }} {{ $t("unitDay") }}</p>
                </div>
              </div>
              <div
                class="md-layout-item dashboard-border bloc-content position-relative"
              >
                <md-button
                  :md-ripple="false"
                  class="modifier position-absolute"
                  @click="toggleDialogAbonnement"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="18.002"
                    height="18.003"
                    viewBox="0 0 18.002 18.003"
                  >
                    <path
                      id="Tracé_42500"
                      data-name="Tracé 42500"
                      d="M3,17.25V21H6.75L17.81,9.94,14.06,6.19ZM20.71,7.04a1,1,0,0,0,0-1.41L18.37,3.29a1,1,0,0,0-1.41,0L15.13,5.12l3.75,3.75,1.83-1.83Z"
                      transform="translate(-3 -2.998)"
                      fill="#242c36"
                    />
                  </svg>
                </md-button>
                <div class="titre-page">{{ $t("subscription") }}</div>
                <p>{{ $t("user:subscriptionInfo") }}</p>
                <div class="d-flex flex-column">
                  <span class="pseudo-label">{{ $t("renew") }}</span>
                  <p>{{ user.renew_status ? $t("yes") : $t("no") }}</p>
                </div>
                <div class="d-flex mb-3">
                  <div class="d-flex flex-column debut-abonnement">
                    <span class="pseudo-label">{{
                      $t("subscription:startDate")
                    }}</span>
                    <p class="mb-0">
                      {{ formatDate($t("dateFormat"), user.start) }}
                    </p>
                  </div>
                  <div class="d-flex flex-column fin-abonnement">
                    <span class="pseudo-label">{{
                      $t("subscription:endDate")
                    }}</span>
                    <p class="mb-0">
                      {{ formatDate($t("dateFormat"), user.end) }}
                    </p>
                  </div>
                </div>
                <div class="d-flex flex-column">
                  <div class="loader-content" v-if="loading">
                    <md-progress-spinner
                      md-mode="indeterminate"
                    ></md-progress-spinner>
                  </div>
                  <span class="pseudo-label">{{ $t("includePair") }}</span>
                  <ul class="liste-paire list-unstyled d-flex flex-wrap">
                    <li
                      class="item-paire text-uppercase"
                      v-for="(item, index) in userCouples"
                      :key="index"
                    >
                      {{ item.symbol }}
                    </li>
                  </ul>
                </div>
              </div>
              <div class="md-layout-item px-0 bloc-content p-0 m-0">
                <div
                  class="md-layout-item bloc-content dashboard-border mx-0 position-relative"
                >
                  <md-button
                    :md-ripple="false"
                    class="modifier position-absolute"
                    @click="toggleDialogCredit"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="18.002"
                      height="18.003"
                      viewBox="0 0 18.002 18.003"
                    >
                      <path
                        id="Tracé_42500"
                        data-name="Tracé 42500"
                        d="M3,17.25V21H6.75L17.81,9.94,14.06,6.19ZM20.71,7.04a1,1,0,0,0,0-1.41L18.37,3.29a1,1,0,0,0-1.41,0L15.13,5.12l3.75,3.75,1.83-1.83Z"
                        transform="translate(-3 -2.998)"
                        fill="#242c36"
                      />
                    </svg>
                  </md-button>
                  <div class="titre-page">{{ $t("credits") }}</div>
                  <p>{{ $t("detail:credits") }}</p>
                  <div class="d-flex details">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="50.526"
                      height="48"
                      viewBox="0 0 50.526 48"
                    >
                      <path
                        id="Tracé_42201"
                        data-name="Tracé 42201"
                        d="M47.044,15.895,41.309,10.16a13.524,13.524,0,0,1,.808-2.905,3.538,3.538,0,0,0,.3-1.465A3.784,3.784,0,0,0,38.632,2,12.619,12.619,0,0,0,28.526,7.053H15.895A13.887,13.887,0,0,0,2,20.947C2,28.627,8.316,50,8.316,50H22.211V44.947h5.053V50H41.158L45.4,35.878,52.526,33.5V15.895ZM29.789,19.684H17.158V14.632H29.789Zm7.579,5.053a2.526,2.526,0,1,1,2.526-2.526A2.534,2.534,0,0,1,37.368,24.737Z"
                        transform="translate(-2 -2)"
                        fill="#5c626a"
                      />
                    </svg>
                    <div class="d-flex flex-column ml-2">
                      {{ $t("credits") }} :
                      <span class="text"
                        >{{ pointToComma(previousCredits) }} €</span
                      >
                    </div>
                  </div>
                </div>
                <div
                  class="md-layout-item bloc-content dashboard-border mx-0 position-relative"
                >
                  <md-button
                    :md-ripple="false"
                    class="modifier position-absolute"
                    @click="toggleDialogJour"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="18.002"
                      height="18.003"
                      viewBox="0 0 18.002 18.003"
                    >
                      <path
                        id="Tracé_42500"
                        data-name="Tracé 42500"
                        d="M3,17.25V21H6.75L17.81,9.94,14.06,6.19ZM20.71,7.04a1,1,0,0,0,0-1.41L18.37,3.29a1,1,0,0,0-1.41,0L15.13,5.12l3.75,3.75,1.83-1.83Z"
                        transform="translate(-3 -2.998)"
                        fill="#242c36"
                      />
                    </svg>
                  </md-button>
                  <div class="titre-page">{{ $t("freeDays") }}</div>
                  <p>{{ $t("detail:days") }}</p>
                  <div class="d-flex details">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="41.667"
                      height="45.833"
                      viewBox="0 0 41.667 45.833"
                    >
                      <path
                        id="Tracé_19699"
                        data-name="Tracé 19699"
                        d="M39.5,5.167H37.417V1H33.25V5.167H12.417V1H8.25V5.167H6.167A4.179,4.179,0,0,0,2,9.333V42.667a4.179,4.179,0,0,0,4.167,4.167H39.5a4.179,4.179,0,0,0,4.167-4.167V9.333A4.179,4.179,0,0,0,39.5,5.167Zm0,37.5H6.167V15.583H39.5Z"
                        transform="translate(-2 -1)"
                        fill="#5c626a"
                      />
                    </svg>
                    <div class="d-flex flex-column ml-2">
                      {{ $t("freeDays") }} :
                      <span class="text"
                        >{{ previousJoursGratuits }} {{ $t("unitDay") }}</span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Dialog
        :showDialog="showDialogAbonnement"
        :dialogName="$t('modifySubscription')"
        :titreDialog="userFirstname + ' ' + userLastname"
        @close="showDialogAbonnement = !showDialogAbonnement"
      >
        <div class="text-center" style="max-width: 356px;">
          {{ $t("info:modifySubscription") }}
        </div>

        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <div class="form-group">
            <md-field>
              <label for="type_abonnement">{{ $t("type:subscription") }}</label>
              <md-select v-model="selected">
                <md-option
                  v-for="(subscription, index) in subscriptionList"
                  :key="index"
                  v-bind:value="subscription.id"
                  >{{ subscription.name }}
                </md-option>
              </md-select>
            </md-field>
          </div>

          <div class="form-group">
            <md-datepicker
              v-model="dateValidity"
              class="d-flex date-picker align-items-center"
              :md-disabled-dates="isPreviousDate"
            >
              <label>{{ $t("validityDate") }}</label>
            </md-datepicker>
          </div>

          <div class="form-group d-flex flex-column">
            <label>{{ $t("renew") }}</label>
            <md-switch
              class="table-switch font-weight-bold mt-0"
              v-model="renewAuto"
              >{{ renewAuto ? $t("active") : $t("desactive") }}</md-switch
            >
          </div>

          <div class="w-100 text-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase"
              @click="updateSubscription()"
              :disabled="!dateValidity"
            >
              {{ $t("modify") }}
            </md-button>
          </div>
        </form>
      </Dialog>

      <Dialog
        :showDialog="showDialogCredit"
        :dialogName="$t('modifyCredits')"
        :titreDialog="userFirstname + ' ' + userLastname"
        @close="showDialogCredit = !showDialogCredit"
      >
        <div class="text-center" style="max-width: 356px;">
          {{ $t("info:modifyCredits") }}
        </div>

        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <span v-if="errorCredits" class="d-flex flex-column">
            <span class="error">{{ errorCredits }}</span>
          </span>
          <PredictInputNumber
            v-model="credits"
            unite="€"
            numberLength="5"
          ></PredictInputNumber>

          <div class="w-100 text-center d-flex align-items-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              style="border-top-right-radius: 0;border-bottom-right-radius: 0;border-right: 0.5px solid #fff; flex:1"
              @click="subCredits()"
            >
              {{ $t("back:remove") }}
            </md-button>
            <md-button
              type="submit"
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              style="border-top-left-radius: 0;border-bottom-left-radius: 0;border-left: 0.5px solid #fff; flex:1"
              @click="addCredits()"
            >
              {{ $t("add") }}
            </md-button>
          </div>
        </form>
      </Dialog>

      <Dialog
        :showDialog="showDialogAjoutReussi"
        :titreDialog="$t('addSuccess')"
        :iconDialog="iconModifJours"
        @close="showDialogAjoutReussi = !showDialogAjoutReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("creditAddOf") }} <strong>{{ credits }} €</strong>
          {{ $t("for") }}
          <strong>{{ userFirstname }} {{ userLastname }}</strong>
          {{ $t("addFreeDaysSuccess2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAjoutReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogEnlevementReussi"
        :titreDialog="$t('removeSuccess')"
        :iconDialog="iconModifJours"
        @close="showDialogEnlevementReussi = !showDialogEnlevementReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("removeCreditSuccess") }} <strong>{{ -credits }} €</strong>
          {{ $t("for") }}
          <strong>{{ userFirstname }} {{ userLastname }}</strong>
          {{ $t("addFreeDaysSuccess2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogEnlevementReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogAboModifie"
        :titreDialog="$t('updateSubscription')"
        @close="showDialogAboModifie = !showDialogAboModifie"
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("subscriptionFor") }}
          <strong>{{ userFirstname }} {{ userLastname }}</strong>
          {{ $t("modifiedSuccessSubscription") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAboModifie = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogJour"
        :dialogName="$t('modifyFreeDays')"
        @close="showDialogJour = !showDialogJour"
        :titreDialog="userFirstname + ' ' + userLastname"
      >
        <div class="text-center" style="max-width: 356px;">
          {{ $t("info:modifyDays") }}
        </div>

        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <span v-if="errorFreeDay" class="d-flex flex-column">
            <span class="error">{{ errorFreeDay }}</span>
          </span>
          <PredictInputNumber
            :value="joursGratuits"
            v-model="joursGratuits"
            numberLength="3"
            :unite="$t('unitDay')"
          ></PredictInputNumber>

          <div class="w-100 text-center d-flex align-items-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              @click="subFreeDay()"
              style="border-top-right-radius: 0;border-bottom-right-radius: 0;border-right: 0.5px solid #fff; flex:1"
            >
              {{ $t("back:remove") }}
            </md-button>
            <md-button
              type="submit"
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              @click="addFreeDay()"
              style="border-top-left-radius: 0;border-bottom-left-radius: 0;border-left: 0.5px solid #fff; flex:1"
            >
              {{ $t("add") }}
            </md-button>
          </div>
        </form>
      </Dialog>

      <Dialog
        :showDialog="showDialogAjoutJourReussi"
        :titreDialog="$t('addSuccess')"
        @close="showDialogAjoutJourReussi = !showDialogAjoutJourReussi"
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("addFreeDaysSuccess1") }}
          <strong>{{ joursGratuits }} j</strong> {{ $t("for") }}
          <strong>{{ userFirstname }} {{ userLastname }}</strong>
          {{ $t("addFreeDaysSuccess2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAjoutJourReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogEnlevementJourReussi"
        :titreDialog="$t('removeSuccess')"
        @close="
          showDialogEnlevementJourReussi = !showDialogEnlevementJourReussi
        "
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("removeDaysSuccess") }}
          <strong>{{ -joursGratuits }} j</strong> {{ $t("for") }}
          <strong>{{ userFirstname }} {{ userLastname }}</strong>
          {{ $t("addFreeDaysSuccess2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogEnlevementJourReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>
    </PermanentFull>
  </div>
</template>

<script>
import MenuGestion from "../../data/MenuGestion.js";
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import BlocAbonnement from "../BlocAbonnement/BlocAbonnement.vue";
import Dialog from "../Dialog/Dialog.vue";
import PredictInputNumber from "../Input/PredictInputNumber.vue";
import moment from "moment";
import { PARAPHRASE, formatDate } from "../../utils/Constant";

export default {
  name: "DetailsUtilisateur",
  components: {
    PermanentFull,
    BlocAbonnement,
    Dialog,
    PredictInputNumber,
  },
  methods: {
    formatDate,
    pointToComma(val) {
      if (val)
        return val
          .toFixed(2)
          .toString()
          .replace(".", ",");
      return val;
    },
    setAllFalse() {
      this.showDialogCredit = false;
      this.showDialogAjoutReussi = false;
      this.showDialogEnlevementReussi = false;
      this.showDialogAjoutJourReussi = false;
      this.showDialogEnlevementJourReussi = false;
      this.showDialogJour = false;
      this.showDialogAbonnement = false;
    },
    toggleDialogAbonnement() {
      this.setAllFalse();
      this.renewAuto = this.user.renew_status ? true : false;
      this.selected = this.user.subscribe.id;
      this.showDialogAbonnement = !this.showDialogAbonnement;
    },
    toggleDialogCredit() {
      this.setAllFalse();
      this.credits = 0;
      this.errorCredits = "";
      this.showDialogCredit = !this.showDialogCredit;
    },
    toogleDialogAjoutReussi() {
      this.setAllFalse();
      this.showDialogAjoutReussi = !this.showDialogAjoutReussi;
    },
    toogleDialogEnlevementReussi() {
      this.setAllFalse();
      this.showDialogEnlevementReussi = !this.showDialogEnlevementReussi;
    },
    toogleDialogAboModifie() {
      this.setAllFalse();

      this.showDialogAboModifie = !this.showDialogAboModifie;
    },
    toogleDialogAjoutJourReussi() {
      this.setAllFalse();
      this.showDialogAjoutJourReussi = !this.showDialogAjoutJourReussi;
    },
    toogleDialogEnlevementJourReussi() {
      this.setAllFalse();
      this.showDialogEnlevementJourReussi = !this
        .showDialogEnlevementJourReussi;
    },
    toggleDialogJour() {
      this.setAllFalse();
      this.errorFreeDay = "";
      this.joursGratuits = 0;
      this.showDialogJour = !this.showDialogJour;
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
      this.find();
    },
    getUserCouple: async function() {
      this.loading = true;
      try {
        await this.$store.dispatch("getUserCouples", {
          id: +this.userDetailId,
          token: localStorage.getItem("adminToken"),
        });
        this.userCouples = await this.$store.state.user.userCouples.data;
        this.loading = false;
      } catch (e) {
        this.loading = false;
      }
    },
    loadUser: async function() {
      try {
        await this.$store.dispatch("loadUserById", {
          id: this.userDetailId,
          token: localStorage.getItem("adminToken"),
        });
        this.user = this.$store.state.user.userList;
        this.userInitial =
          this.user.client.lastname[0].toUpperCase() +
          "" +
          this.user.client.firstname[0].toUpperCase();
        this.imgAvatar = this.user.profil;
        this.getData(this.$store.state.user.userList);
      } catch (e) {
        //
      }
    },
    loadSubscriptions: async function() {
      await this.$store.dispatch("listSubscriptions", {
        token: localStorage.getItem("adminToken"),
      });
    },
    splitData: function(data, index) {
      return data?.split(":")[index];
    },
    updateCredit: async function() {
      const payload = {
        sum: +this.credits + this.previousCredits,
      };
      await this.$store.dispatch("updateCredit", {
        id: +this.user.client.id,
        payload: payload,
        token: localStorage.getItem("adminToken"),
      });
      this.loadUser();
    },
    addCredits: function() {
      this.updateCredit();
      this.toogleDialogAjoutReussi();
    },
    subCredits: function() {
      this.errorCredits = "";
      if (this.previousCredits < this.credits)
        this.errorCredits = this.$t("errorCredits");
      else {
        this.credits = -this.credits;
        this.updateCredit();
        this.toogleDialogEnlevementReussi();
      }
    },
    updateFreeDay: async function() {
      const payload = {
        free_day: +this.joursGratuits + this.previousJoursGratuits,
      };
      await this.$store.dispatch("updateFreeDay", {
        id: +this.user.client.id,
        payload: payload,
        token: localStorage.getItem("adminToken"),
      });
      this.loadUser();
    },
    addFreeDay: function() {
      this.updateFreeDay();
      this.toogleDialogAjoutJourReussi();
    },
    subFreeDay: function() {
      this.errorFreeDay = "";
      if (this.previousJoursGratuits < this.joursGratuits)
        this.errorFreeDay = this.$t("errorFreeDay");
      else {
        this.joursGratuits = -this.joursGratuits;
        this.updateFreeDay();
        this.toogleDialogEnlevementJourReussi();
      }
    },

    updateSubscription: async function() {
      const payload = {
        subscribe: +this.selected,
        end: this.formatDateUpdate(this.dateValidity),
        renew: this.renewAuto ? 1 : 0,
      };
      try {
        await this.$store.dispatch("updateSubscriptionUser", {
          id: +this.user.client.id,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
        this.loadUser();
        this.toogleDialogAboModifie();
      } catch (e) {
        //
      }
    },
    updateUserStatus: async function() {
      const payload = {
        account_is_active: this.userAccountStatus ? true : false,
      };
      try {
        await this.$store.dispatch("updateUserStatus", {
          id: this.userDetailId,
          payload,
          token: localStorage.getItem("adminToken"),
        });
        this.loadUser();
      } catch (e) {
        //
      }
    },
    getData: function(item) {
      this.previousCredits = item.client.reward.sum;
      this.previousJoursGratuits = item.client.reward.free_day;
      this.userLastname = this.user.client.lastname;
      this.userFirstname = this.user.client.firstname;
      this.dateValidity = this.formatDate(this.$t("dateFormat"), this.user.end);
      this.userEmail = this.user.client.email;
      this.userAccountStatus = this.user.client.account_status;
      this.userSubscribeName = this.user.subscribe.name;
      this.emplacementUtilise = this.user.number_couple.toString();
      this.emplacementDispo = this.user.subscribe.number_couple_offered.toString();
    },
    formatDateUpdate(item) {
      return moment(item, this.$t("dateFormat")).format("YYYY-MM-DD HH:mm:ss");
    },
    isPreviousDate(date) {
      const dateNow = new Date();
      dateNow.setDate(dateNow.getDate() - 1);
      return date < dateNow;
    },
    decryptValue(val) {
      return this.CryptoJS.AES.decrypt(val, PARAPHRASE).toString(
        this.CryptoJS.enc.Utf8
      );
    },
  },
  data() {
    return {
      titre: "",
      icon: "",
      userDetailId: null,
      userInitial: null,
      loading: false,
      menuItems: MenuGestion,
      isActive: true,
      selected: "",
      user: "",
      previousJoursGratuits: 0,
      previousCredits: 0,
      joursGratuits: 0,
      userCouples: [],
      subscriptions: [],
      credits: 0,
      errorCredits: "",
      errorFreeDay: "",
      userLastname: "",
      userFirstname: "",
      userSubscribeName: "",
      userEmail: "",
      userAccountStatus: false,
      iconAbonnement: `
        <svg xmlns="http://www.w3.org/2000/svg" width="55.169" height="48" viewBox="0 0 55.169 48" class="mr-2">
          <g id="Groupe_53079" data-name="Groupe 53079" transform="translate(0 0)">
            <path id="Tracé_42431" data-name="Tracé 42431" d="M-86.252-73.489a3.833,3.833,0,0,1-2.03,2.692,4.622,4.622,0,0,1-1.333.376.6.6,0,0,0-.605.523q-1.5,5.525-3.038,11.043c-.53,1.918-1.073,3.832-1.584,5.754a.5.5,0,0,1-.584.453q-18.422-.012-36.844,0c-.37,0-.477-.149-.566-.474-1.524-5.548-3.068-11.09-4.582-16.641a.768.768,0,0,0-.77-.675,3.629,3.629,0,0,1-3.233-3.63,3.7,3.7,0,0,1,3.153-3.612,3.62,3.62,0,0,1,4.087,2.847,8.892,8.892,0,0,1,.023,1.544c.006.168.039.422.149.486,2.852,1.691,5.715,3.361,8.62,5.061l9.523-15.781a3.636,3.636,0,0,1-1.608-3.467,3.549,3.549,0,0,1,1.287-2.405,3.668,3.668,0,0,1,5.015.287c1.521,1.641,1.309,3.663-.618,5.606l9.5,15.759,1.707-1q3.368-1.968,6.739-3.932c.279-.162.41-.3.331-.668a3.637,3.637,0,0,1,2.764-4.282,3.647,3.647,0,0,1,4.294,2.446c.065.2.133.406.2.609Z" transform="translate(141.421 90.25)" fill="#5c626a"/>
            <path id="Tracé_42432" data-name="Tracé 42432" d="M-24.083,509.6q-8.674,0-17.348,0a3.149,3.149,0,0,1-3.359-2.432A3.1,3.1,0,0,1-41.7,503.4c.107-.005.215,0,.323,0q17.295,0,34.589,0a3.25,3.25,0,0,1,3.033,1.493A3.092,3.092,0,0,1-6.52,509.59c-1.256.031-2.514.006-3.771.006Z" transform="translate(51.667 -461.605)" fill="#5c626a"/>
          </g>
        </svg>
      `,
      emplacementDispo: "",
      emplacementUtilise: "",
      imgAvatar: null,
      showDialogAboModifie: false,
      showDialogCredit: false,
      showDialogAbonnement: false,
      showDialogAjoutReussi: false,
      showDialogEnlevementReussi: false,
      showDialogAjoutJourReussi: false,
      showDialogEnlevementJourReussi: false,
      showDialogJour: false,
      renewAuto: "",
      dateValidity: null,
      iconModifJours: `
          <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
            <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
            <g id="Groupe_14044" data-name="Groupe 14044" transform="translate(7.629 7.705)">
              <path id="Tracé_19671" data-name="Tracé 19671" d="M162.639,159.613c-.275.33-.533.678-.829.989q-11.931,12.529-23.869,25.051c-.421.441-.864.832-1.531.57a1.752,1.752,0,0,1-.578-.384q-5.724-5.708-11.435-11.43a1.188,1.188,0,0,1-.324-1.459,1.086,1.086,0,0,1,1.252-.616,1.949,1.949,0,0,1,.833.51q5.108,5.078,10.193,10.179c.129.129.264.251.35.333.38-.348.757-.656,1.091-1.005q11.327-11.852,22.646-23.712a1.218,1.218,0,0,1,1.846-.205,3.765,3.765,0,0,1,.355.474Z" transform="translate(-104.921 -133.831)" fill="#f8bd25"/>
              <path id="Tracé_19672" data-name="Tracé 19672" d="M38.362,76.742q-1.469,0-2.941-.112A38.363,38.363,0,1,1,69.557,60.736a1.5,1.5,0,1,1-2.434-1.75,35.373,35.373,0,1,0-8.136,8.137,1.5,1.5,0,1,1,1.749,2.434A38.
              ,38.365,0,0,1,38.362,76.742Z" transform="translate(0 0)" fill="#242c36"/>
              <path id="Tracé_19673" data-name="Tracé 19673" d="M411.609,413.108a1.5,1.5,0,1,1,1.06-.439A1.51,1.51,0,0,1,411.609,413.108Z" transform="translate(-347.165 -347.165)" fill="#242c36"/>
            </g>
          </svg>
      `,
    };
  },
  async mounted() {
    await this.loadUser();
    await this.loadSubscriptions();
    await this.getUserCouple();
  },
  watch: {
    "$i18n.locale"() {
      this.dateValidity = this.formatDate(this.$t("dateFormat"), this.user.end);
    },
  },
  computed: {
    subscriptionList() {
      return this.$store.state.subscription.listSubscriptions;
    },
  },
  created() {
    document.title = this.$route.meta.title;
    this.userDetailId = +this.decryptValue(
      localStorage.getItem("userDetailId")
    );
  },
};
</script>

<style scoped>
#details-utilisateur > .md-layout {
  margin-left: -10px;
  margin-right: -10px;
}
#details-utilisateur .titre-page {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0.15px;
  color: #5c626a;
}
#details-utilisateur .nom-utilisateur,
#details-utilisateur .pseudo-label {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.25px;
  color: var(--black);
  white-space: nowrap;
}
#details-utilisateur .description {
  letter-spacing: 0.25px;
  color: var(--black);
  font-size: 14px;
  line-height: 20px;
}

#details-utilisateur .mail-utilisateur {
  text-decoration: none !important;
  font-family: "Poppins-Regular", Arial, Helvetica, sans-serif;
}
#details-utilisateur .mail-utilisateur,
#details-utilisateur p {
  font-size: 12px;
  letter-spacing: 0.12px;
  color: var(--black);
}

#details-utilisateur .liste-paire {
  margin: 0 -13px;
}
#details-utilisateur .liste-paire li {
  border: 1px solid #707070;
  border-radius: 18px;
  padding: 6.5px 10px;
  margin: 13px;
}
#details-utilisateur .bloc-content {
  padding: 20px;
  margin: 10px;
}
#details-utilisateur .avatar-wrapper span.b-avatar {
  border: 1px dashed var(--placeholder);
  background-color: transparent;
  padding: 9px;
}
#details-utilisateur .fake-avatar {
  border: 1px dashed var(--placeholder);
  padding: 9px;
}
#details-utilisateur .fake-avatar .text-wrapper {
  font-size: 34px;
  line-height: 36px;
  color: var(--placeholder);
  background-color: #f6f6f7;
}
#details-utilisateur .column-wrapper > div {
  /* flex: 1 0 534px;
    max-width: 534px; */
  margin-left: 0 !important;
  margin-right: 24px !important;
}
#details-utilisateur .column-wrapper > div:first-child {
  flex: 0 0 473px;
  max-width: 473px;
}
#details-utilisateur .debut-abonnement {
  padding-right: 41.5px;
}
#details-utilisateur .fin-abonnement {
  padding-left: 29.5px;
  border-left: 1px solid var(--placeholder);
}
#details-utilisateur .details {
  color: var(--placeholder);
  font-size: 12px;
}
#details-utilisateur .details .text {
  font-size: 24px;
  color: var(--primary);
}
#details-utilisateur .modifier {
  top: 5px;
  right: 5px;
  min-width: auto;
}
.back i {
  margin-right: 12px;
  vertical-align: middle;
}
</style>
