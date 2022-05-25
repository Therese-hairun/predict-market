<template>
  <div class="dashboard">
    <PermanentFull
      :titre="titre"
      :icon="icon"
      :menuItems="menuItems"
      :admin="true"
    >
      <!-- Loader -->
      <div class="loader-content" v-if="loader">
        <p class="msg">{{ $t("loading") }}</p>
        <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
      </div>
      <!-- /Loader -->
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div id="details-couple" class="mx-0">
          <div class="d-flex flex-column justify-content-center">
            <router-link
              to="/gestion-des-paires"
              class="back mb-3 align-self-start"
              ><i class="fa fa-chevron-left" aria-hidden="true"></i>
              {{ $t("back") }}</router-link
            >
            <h3 class="titre-recherche">{{ $t("details") }}</h3>
            <p class="description">
              {{ $t("info:details") }}
            </p>
          </div>
          <div class="md-layout md-gutter column-wrapper">
            <div
              class="md-layout-item dashboard-border bloc-content left d-flex flex-column align-items-center justify-content-center item-wrapper"
            >
              <md-card
                class="crypto-card d-flex flex-column align-items-center m-0 w-100 shadow-none"
              >
                <md-card-media class="cryto-item-md-card-media">
                  <span
                    class="b-avatar cryto-item-b-avatar bg-white cryto-item-big-avatar badge-secondary rounded-circle"
                    style="width: 86px; height: 86px;"
                  >
                    <span class="b-avatar-custom">
                      <span class="b-avatar-img">
                        <img :src="paire.symbol_1_logo" alt="symbol_logo" />
                      </span>
                    </span>
                  </span>
                  <span
                    class="b-avatar cryto-item-b-avatar bg-white cryto-item-avatar badge-secondary rounded-circle"
                    style="width: 53px; height: 53px;"
                  >
                    <span class="b-avatar-custom">
                      <span class="b-avatar-img">
                        <img :src="paire.symbol_2_logo" alt="symbol_logo" />
                      </span>
                    </span>
                  </span>
                </md-card-media>

                <md-card-header class="px-0">
                  <div
                    class="crypto-item-title d-flex flex-column align-items-center justify-content-center"
                  >
                    {{ paire.assetFullName }}
                    <span class="crypto-sigle text-uppercase text-center"
                      >{{ paire.symbol_1 }} / {{ paire.symbol_2 }}</span
                    >
                  </div>
                </md-card-header>
                <md-switch
                  class="table-switch"
                  v-model="paire.status"
                  @change="updateStatus(paire.status)"
                  >{{
                    paire.status ? $t("active") : $t("desactive")
                  }}</md-switch
                >
              </md-card>
            </div>

            <div
              class="md-layout-item dashboard-border bloc-content left d-flex flex-column justify-content-center p-0"
            >
              <div class="p-2 p-md-3 position-relative details-item">
                <md-button
                  :md-ripple="false"
                  class="modifier position-absolute"
                  @click="toggleDialogPaire()"
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

                <h3 class="titre-recherche">{{ $t("predictions") }}</h3>
                <p class="description">
                  {{ $t("info:checkPair") }}
                </p>
                <md-table>
                  <md-table-row class="table-header">
                    <md-table-head scope="col" class="user_col">
                      {{ $t("type") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('type')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'type')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="user_col">
                      {{ $t("averageAccuracy") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('precision')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'precision')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="user_col">
                      {{ $t("status") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('statut')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'statut')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                  </md-table-row>

                  <md-table-row
                    v-for="(item, index) in pageOfItems"
                    :key="index"
                  >
                    <md-table-cell data-label="Type">{{
                      item.interval
                    }}</md-table-cell>
                    <md-table-cell data-label="Précision moyenne">{{
                      item.precision
                    }}</md-table-cell>
                    <md-table-cell data-label="Statut">{{
                      item.status
                    }}</md-table-cell>
                  </md-table-row>
                  <md-table-row v-if="this.visible">
                    <md-table-cell
                      data-label=""
                      :colspan="3"
                      class="align-text"
                      >{{ this.errorEmptyData }}</md-table-cell
                    >
                  </md-table-row>

                  <md-table-row v-if="!visible">
                    <md-table-cell :colspan="3">
                      <PredictPagination
                        v-if="training"
                        :dataToPaginate="training"
                        @onChangePage="onChangePage"
                      />
                    </md-table-cell>
                  </md-table-row>
                </md-table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </PermanentFull>

    <Dialog
      :showDialog="showDialogPaire"
      :dialogName="$t('updatePair')"
      @close="showDialogPaire = !showDialogPaire"
    >
      <form
        action=""
        class="form-abonnement w-100 my-4"
        style="max-width: 589px;"
      >
        <h3 class="titre-recherche">{{ $t("crypto1") }}</h3>
        <p>
          {{ $t("info:uploadImage1") }}
        </p>
        <span class="error">{{ errorSelectedCrypto }}</span>
        <div class="mb-2">
          {{ this.symbol1 }}
          <md-field class="mt-0">
            <label for="symbol1">{{ $t("symbol1") }}</label>
            <md-select v-model="selected" name="symbol1" id="symbol1">
              <md-option
                v-for="(item, index) in paires"
                :key="index"
                v-bind:value="item.assetname"
                >{{ item.assetname }}
              </md-option>
            </md-select>
          </md-field>
        </div>
        <span class="error">{{ errorSymbol1 }}</span>
        <div class="d-flex upload-field mt-3" @click="handleFigure1">
          <div class="avatar avatar_1" v-if="figure1">
            <img v-bind:src="paire.symbol_1_logo" alt="symbol_logo" />
          </div>
          <UploadFile
            :uploadMsg="$t('uploadMsg')"
            :max="1"
            :clearAll="$t('delete')"
            type="file"
            :handleImages="handleImage1"
          />
        </div>

        <h3 class="titre-recherche mt-3">{{ $t("crypto2") }}</h3>
        <p>
          {{ $t("info:uploadImage2") }}
        </p>
        <span class="error">{{ errorSelectedCrypto1 }}</span>
        <div class="mb-2">
          <md-field class="mt-0">
            <label for="symbol2">{{ $t("symbol2") }}</label>
            <md-select v-model="selected1" name="symbol1" id="symbol1">
              <md-option
                v-for="(item, index) in paires"
                :key="index"
                v-bind:value="item.assetname"
                >{{ item.assetname }}
              </md-option>
            </md-select>
          </md-field>
        </div>
        <span class="error">{{ errorSymbol2 }}</span>
        <div class="upload-field mt-3" @click="handleFigure2">
          <figure class="avatar avatar_2" v-if="figure2">
            <img v-bind:src="paire.symbol_2_logo" alt="symbol_logo" />
          </figure>
          <UploadFile
            :uploadMsg="$t('uploadMsg')"
            :max="1"
            :clearAll="$t('delete')"
            type="file"
            :handleImages="handleImage2"
          />
        </div>

        <h3 class="titre-recherche mt-3">{{ $t("predictionIntervals") }}</h3>
        <p>
          {{ $t("info:predictionIntervals") }}
        </p>
        <span class="error">{{ errorInterval }}</span>
        <div class="interval-checkbox custom-checkbox">
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="5m"
            >5m</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="15m"
            >15m</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="30m"
            >30m</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="1h"
            >1h</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="2h"
            >2h</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="4h"
            >4h</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="6h"
            >6h</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="12h"
            >12h</md-checkbox
          >
          <md-checkbox class="mt-0" v-model="interval_checkbox" value="1d"
            >1{{ $t("unitDay") }}</md-checkbox
          >
        </div>

        <div class="w-100 text-center mt-4">
          <div class="loader-content" v-if="loading">
            <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
          </div>
          <md-button
            v-else
            class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
            style="width: 100% !important; max-width: 277px;"
            @click="verifyForm()"
          >
            {{ $t("modify") }}
          </md-button>
        </div>
      </form>
    </Dialog>
    <Dialog
      :dialogName="$t('errorMessage')"
      :showDialog="showDialogError"
      class="dialogError"
      @close="showDialogError = !showDialogError"
    >
      <div class="text-error text-center" style="max-width: 380px;">
        <span class="material-icons text-alert">warning</span>
        <h4 class="md-title">{{ errorUpdateCouple }}</h4>
      </div>
    </Dialog>

    <Dialog
      :showDialog="showDialogPaireReussi"
      :titreDialog="$t('successModification')"
      :iconDialog="iconModifJours"
      @close="showDialogPaireReussi = !showDialogPaireReussi"
    >
      <div class="text-center" style="max-width: 380px;">
        {{ $t("updateCouple:message1") }}
        <strong>{{ coupleName[0] }}</strong> {{ $t("and") }}
        <strong>{{ coupleName[1] }}</strong> {{ $t("updateCouple:message2") }}
      </div>

      <div class="form-group text-center mt-4">
        <md-button
          class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
          @click="showDialogPaireReussi = false"
        >
          {{ $t("continue") }}
        </md-button>
      </div>
    </Dialog>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import Dialog from "../Dialog/Dialog.vue";
import MenuGestion from "../../data/MenuGestion.js";
import UploadFile from "../Input/UploadFile.vue";
import PredictPagination from "../Pagination/PredictPagination.vue";
import { PARAPHRASE } from "../../utils/Constant";

export default {
  name: "DetailsCouples",
  components: {
    PermanentFull,
    Dialog,
    UploadFile,
    PredictPagination,
  },
  methods: {
    onChangePage(dataPageOfItems) {
      this.pageOfItems = dataPageOfItems;
    },
    checkTrainingPairData() {
      if (!this.training.length) {
        this.errorEmptyData = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },
    handleFigure1() {
      this.figure1 = false;
    },
    handleFigure2() {
      this.figure2 = false;
    },
    setAllFalse() {
      this.showDialogPaire = false;
      this.showDialogPaireReussi = false;
      this.showDialogError = false;
    },
    toggleDialogError() {
      this.setAllFalse();
      this.showDialogError = !this.showDialogError;
    },
    toggleDialogPaire() {
      this.setAllFalse();
      this.showDialogPaire = !this.showDialogPaire;
      this.selected = this.paire.symbol_1;
      this.selected1 = this.paire.symbol_2;
    },
    toggleDialogPaireReussi() {
      this.setAllFalse();
      this.showDialogPaireReussi = !this.showDialogPaireReussi;
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
    },
    getCoupleBySymbol: async function() {
      try {
        this.loader = true;
        await this.$store.dispatch("getCoupleBySymbol", {
          symbol: this.coupleSymbol,
          token: localStorage.getItem("adminToken"),
        });
        this.paire = this.getPaire;
        this.interval_checkbox = this.paire.intervals;
        this.loader = false;
      } catch (e) {
        this.loader = false;
      }
    },
    init() {
      this.errorSelectedCrypto = "";
      this.errorSelectedCrypto1 = "";
      this.errorInterval = "";
      this.errorSymbol1 = "";
      this.errorSymbol2 = "";
    },
    verifyForm() {
      this.init();
      if (!this.selected) {
        this.errorSelectedCrypto = this.$t("errorSelectedCrypto");
      }
      if (!this.selected1) {
        this.errorSelectedCrypto1 = this.$t("errorSelectedCrypto1");
      }
      if (!this.interval_checkbox.length) {
        this.errorInterval = this.$t("errorInterval");
      }
      if (this.image1 === undefined) {
        if (this.figure1 === false) {
          this.errorSymbol1 = this.$t("errorSymbol1");
        }
      }
      if (this.image2 === undefined) {
        if (this.figure2 === false) {
          this.errorSymbol2 = this.$t("errorSymbol2");
        }
      }
      if (
        this.selected &&
        this.selected1 &&
        this.interval_checkbox.length &&
        (this.image1 || this.figure1) &&
        (this.figure2 || this.image2)
      )
        this.updateCouple();
    },
    handleImage1(event) {
      this.image1 = event[0];
    },
    handleImage2(event) {
      this.image2 = event[0];
    },
    async updateCouple() {
      this.loading = true;
      let temp = "";
      for (let i = 0; i < this.interval_checkbox.length; i++) {
        temp = temp + `'` + this.interval_checkbox[i] + `'`;
        if (i + 1 != this.interval_checkbox.length) temp = temp + `,`;
      }
      temp = "[" + temp + "]";
      try {
        await this.$store.dispatch("updatePaire", {
          id: this.paire.id,
          symbol_1: this.selected,
          symbol_2: this.selected1,
          image1: this.image1,
          image2: this.image2,
          interval: temp.toString(),
          token: localStorage.getItem("adminToken"),
        });
        this.coupleName = this.$store.state.paire.updateCouple.data.split("/");
        this.toggleDialogPaireReussi();
        await this.getCoupleBySymbol();
        this.loading = false;
      } catch (error) {
        this.loading = false;
        if (error.response.status === 409)
          this.errorUpdateCouple = this.$t("errorCoupleExist");
        else this.errorUpdateCouple = this.$t("errorCombination");
        this.toggleDialogError();
      }
    },
    updateStatus: async function(item) {
      const payload = {
        status: item,
      };
      try {
        await this.$store.dispatch("updateStatusCouple", {
          id: this.paire.id,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      }
      await this.getCoupleBySymbol();
    },
    loadPaires: async function() {
      this.loader = true;
      try {
        await this.$store.dispatch("loadPaires", {
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      } finally {
        this.loader = false;
      }
    },
    decryptValue(val) {
      return this.CryptoJS.AES.decrypt(val, PARAPHRASE).toString(
        this.CryptoJS.enc.Utf8
      );
    },
  },
  async mounted() {
    await this.getCoupleBySymbol();
    await this.loadPaires();
    this.checkTrainingPairData();
  },
  computed: {
    paires() {
      return this.$store.state.listPaires.listPaires;
    },
    getPaire() {
      return this.$store.state.paire.coupleId.data;
    },
    training() {
      return this.$store.state.paire.coupleId.precision_data;
    },
  },
  data: () => {
    return {
      titre: "",
      paire: "",
      coupleSymbol: null,
      loader: false,
      figure1: true,
      figure2: true,
      coupleName: [],
      icon: `
          <svg class="icon-item" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="5 0 19 24">
            <rect id="Rectangle_1874" data-name="Rectangle 1874" width="24" height="24" fill="none"/>
            <path id="Tracé_19677" class="to-fill" data-name="Tracé 19677" d="M2.88,7.88,4.42,9.42A8.158,8.158,0,0,0,4,12a8,8,0,1,0,8-8,8.158,8.158,0,0,0-2.58.42L7.89,2.89A10,10,0,1,1,2,12,10.11,10.11,0,0,1,2.88,7.88ZM6,12a6,6,0,1,1,6,6A6,6,0,0,1,6,12ZM7,5.5A1.5,1.5,0,1,1,5.5,4,1.5,1.5,0,0,1,7,5.5Z" fill="#5c626a"/>
          </svg>
        `,
      iconModifJours: `
            <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
              <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
              <g id="Groupe_14044" data-name="Groupe 14044" transform="translate(7.629 7.705)">
                <path id="Tracé_19671" data-name="Tracé 19671" d="M162.639,159.613c-.275.33-.533.678-.829.989q-11.931,12.529-23.869,25.051c-.421.441-.864.832-1.531.57a1.752,1.752,0,0,1-.578-.384q-5.724-5.708-11.435-11.43a1.188,1.188,0,0,1-.324-1.459,1.086,1.086,0,0,1,1.252-.616,1.949,1.949,0,0,1,.833.51q5.108,5.078,10.193,10.179c.129.129.264.251.35.333.38-.348.757-.656,1.091-1.005q11.327-11.852,22.646-23.712a1.218,1.218,0,0,1,1.846-.205,3.765,3.765,0,0,1,.355.474Z" transform="translate(-104.921 -133.831)" fill="#f8bd25"/>
                <path id="Tracé_19672" data-name="Tracé 19672" d="M38.362,76.742q-1.469,0-2.941-.112A38.363,38.363,0,1,1,69.557,60.736a1.5,1.5,0,1,1-2.434-1.75,35.373,35.373,0,1,0-8.136,8.137,1.5,1.5,0,1,1,1.749,2.434A38.365,38.365,0,0,1,38.362,76.742Z" transform="translate(0 0)" fill="#242c36"/>
                <path id="Tracé_19673" data-name="Tracé 19673" d="M411.609,413.108a1.5,1.5,0,1,1,1.06-.439A1.51,1.51,0,0,1,411.609,413.108Z" transform="translate(-347.165 -347.165)" fill="#242c36"/>
              </g>
            </svg>
        `,
      menuItems: MenuGestion,
      errorSelectedCrypto: "",
      errorSelectedCrypto1: "",
      errorInterval: "",
      errorSymbol1: "",
      errorSymbol2: "",
      listPaires: [],
      selected: "",
      selected1: "",
      loading: false,
      rowsPerPage: 3,
      sur: "",
      errorUpdateCouple: "",
      showDialogPaire: false,
      showDialogPaireReussi: false,
      showDialogError: false,
      symbol1: null,
      symbol2: null,

      errorEmptyData: null,
      visible: false,

      pageOfItems: [],

      interval_checkbox: [],
    };
  },
  async created() {
    this.coupleSymbol = this.decryptValue(localStorage.getItem("coupleSymbol"));

    try {
      await this.$store.dispatch("loadDataCouples", {
        token: localStorage.getItem("adminToken"),
      });
    } catch (e) {
      //
    }
  },
};
</script>

<style scoped>
.upload-field {
  display: flex;
  position: relative;
}
.upload-field .avatar {
  background: #f6f6f7;
  border: 1px dashed #a7aaae;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 100%;
  z-index: 1;
}
.upload-field .avatar.avatar_1 img {
  height: 120px;
  width: 120px;
}
.upload-field .avatar.avatar_2 img {
  height: 110px;
  width: 110px;
}
.crypto-card {
  padding: 33px 12.5px 11px;
  border-radius: 12px;
}
.cryto-item-md-card-media {
  width: 121px;
  height: 99px;
}
.cryto-item-b-avatar {
  position: absolute;
}
.cryto-item-big-avatar {
  top: 0;
  left: 0;
  z-index: 2;
  border: 2px solid #5c626a;
}
.cryto-item-big-avatar .b-avatar-img {
  width: 60px;
  height: 60px;
}
.cryto-item-avatar {
  bottom: 0;
  right: 0;
  border: 1px solid var(--placeholder);
}
.cryto-item-avatar .b-avatar-img img {
  width: 28px;
  height: 28px;
}
.crypto-content {
  padding-bottom: 17.5px;
}
.item-wrapper {
  flex: 1 1 465px;
  max-width: 465px;
  min-width: 180px;
  margin-right: 20px;
}
.column-wrapper {
  flex-wrap: nowrap;
  padding-left: 20px;
  padding-right: 20px;
}
@media (max-width: 1280px) {
  .column-wrapper {
    padding-left: 12px;
    padding-right: 12px;
  }
}
@media (max-width: 780px) {
  .column-wrapper {
    flex-wrap: wrap;
  }
  .column-wrapper > div {
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100%;
  }
  .item-wrapper {
    flex: 1 1 100%;
    margin-right: 0;
    margin-bottom: 20px;
  }
}
.details-item .modifier {
  top: 5px;
  right: 5px;
  min-width: auto;
}
.back i {
  margin-right: 12px;
  vertical-align: middle;
}

.align-text {
  text-align: center;
}
</style>
