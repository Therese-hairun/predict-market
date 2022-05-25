<template>
  <div class="d-flex flex-wrap justify-content-between align-items-center">
    <div class="left">
      <h3 class="titre-recherche">{{ $t("search") }}</h3>
      <span class="help-recherche">{{ $t("demandePaire:message") }}.</span>
    </div>
    <div class="table-wrapper flex-grow">
      <md-table
        md-table-fixed-header
        class="mt-3 predict-table paireDemande-table d-flex w-100"
      >
        <md-table-toolbar class="filter-bloc px-2 mb-3">
          <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
            <md-input
              :placeholder="$t('exampleCouple')"
              class="input-search border-0"
              v-model="search"
            />
            <svg
              class="mr-2"
              xmlns="http://www.w3.org/2000/svg"
              width="16.395"
              height="16.395"
              viewBox="0 0 16.395 16.395"
            >
              <path
                id="Search"
                d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                transform="translate(-570 -2016)"
                fill="#242c36"
              />
            </svg>
          </md-field>
        </md-table-toolbar>

        <div class="table-container">
          <md-table-row class="table-header">
            <md-table-head scope="col" class="coupleRequest_col">
              {{ $t("requestedCouple") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('couple_demande')"
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
                  v-on:click="orderBy('-' + 'couple_demande')"
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
            <md-table-head class="nbrRequest_col">
              {{ $t("numberRequests") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('nbre_demande')"
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
                  v-on:click="orderBy('-' + 'nbre_demande')"
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
            <md-table-head scope="col" class="lastDateRequest_col">
              {{ $t("lastRequestDate") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('date_demande')"
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
                  v-on:click="orderBy('-' + 'date_demande')"
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
            <md-table-head class="action_col"></md-table-head>
          </md-table-row>

          <md-table-row v-for="(item, index) in requested" :key="index">
            <md-table-cell
              data-label="Couple demandé"
              class="coupleRequest_col"
              >{{ item.couple }}</md-table-cell
            >
            <md-table-cell
              data-label="Nombre de demandes"
              class="nbrRequest_col"
              >{{ item.count }}</md-table-cell
            >
            <md-table-cell
              data-label="Dernière date de demande"
              class="lastDateRequest_col"
              >{{ formatDate($t("dateFormat"), item.last_date) }}</md-table-cell
            >
            <md-table-cell data-label="" class="action_col">
              <md-button
                class="text-normal btn-modifier"
                @click="toggleDialogPaire(item)"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 20 20"
                  class="mr-2"
                >
                  <path
                    id="Tracé_42539"
                    data-name="Tracé 42539"
                    d="M12,2A10,10,0,1,0,22,12,10,10,0,0,0,12,2ZM10,17,5,12l1.41-1.41L10,14.17l7.59-7.59L19,8Z"
                    transform="translate(-2 -2)"
                    fill="#242c36"
                  />
                </svg>
                <ins>{{ $t("validate") }}</ins>
              </md-button>
            </md-table-cell>
          </md-table-row>
          <md-table-row v-if="this.visible">
            <md-table-cell :colspan="4" class="align-text">{{
              $t("table:NotFound")
            }}</md-table-cell></md-table-row
          >
          <md-table-row class="pagination-row" v-if="!visible">
            <md-table-cell :colspan="4">
              <TablePagination
                @pageVal="handleChangePageValue"
                @pageSize="handleChangeSizeValue"
                :dataSize="dataSize"
                :next="next"
              />
            </md-table-cell>
          </md-table-row>
        </div>
      </md-table>
    </div>
    <Dialog
      :showDialog="showDialogPaire"
      :dialogName="$t('validatePair')"
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
        <span class="error" v-for="error in errorSelectedCrypto" :key="error">{{
          error
        }}</span>
        <div class="mb-2">
          {{ this.symbol1 }}
          <md-field class="mt-0">
            <label for="symbol1">{{ couple_1 }}</label>
          </md-field>
        </div>
        <span class="error">{{ errorSymbol1 }}</span>
        <div class="d-flex mt-3">
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
        <span
          class="error"
          v-for="error in errorSelectedCrypto1"
          :key="error"
          >{{ error }}</span
        >
        <div class="mb-2">
          <md-field class="mt-0">
            <label for="symbol2">{{ couple_2 }}</label>
          </md-field>
        </div>
        <span class="error">{{ errorSymbol2 }}</span>
        <div class="d-flex mt-3">
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
        <span class="error" v-for="error in errorInterval" :key="error">{{
          error
        }}</span>
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
            {{ $t("add") }}
          </md-button>
        </div>
      </form>
    </Dialog>
    <Dialog
      :showDialog="showDialogPaireReussi"
      :titreDialog="$t('addSuccess')"
      :iconDialog="iconModifJours"
      @close="showDialogPaireReussi = !showDialogPaireReussi"
    >
      <div class="text-center" style="max-width: 380px;">
        {{ $t("coupleValidation") }} <strong>{{ coupleName[0] }}</strong>
        {{ $t("and") }} <strong>{{ coupleName[1] }}</strong>
        {{ $t("modifCompleted") }}
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
    <Dialog
      :showDialog="showDialogError"
      :titreDialog="$t('errorMessage')"
      :iconDialog="iconWarning"
      @close="showDialogError = !showDialogError"
    >
      <div
        class="form-group dialogError-content text-center mb-4 mt-2"
        style="max-width: 380px;"
      >
        <p class="text-error mb-4">{{ errorAddCouple }}</p>
        <md-button
          class="submit-dialog btn-submit text-center w-100 px-0 m-0"
          @click="showDialogError = false"
        >
          {{ $t("ok") }}
        </md-button>
      </div>
    </Dialog>
  </div>
</template>

<script>
import Dialog from "../Dialog/Dialog.vue";
import UploadFile from "../Input/UploadFile.vue";
import TablePagination from "../Pagination/TablePagination.vue";
import { formatDate } from "../../utils/Constant";

export default {
  name: "DemandesPaires",
  components: {
    Dialog,
    UploadFile,
    TablePagination,
  },

  methods: {
    formatDate,
    handleChangePageValue(val) {
      this.page = val;
    },
    handleChangeSizeValue(val) {
      this.size = val;
    },
    checkRequestedPairData() {
      if (!this.requested.length) {
        this.error = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },
    setAllFalse() {
      this.showDialogPaire = false;
      this.showDialogPaireReussi = false;
    },
    toggleDialogPaire(item) {
      const temp = item.couple.split("/");
      this.coupleToPop = item.couple;
      this.couple_1 = temp[0];
      this.couple_2 = temp[1];
      this.setAllFalse();
      this.showDialogPaire = !this.showDialogPaire;
    },
    toggleDialogPaireReussi() {
      this.setAllFalse();
      this.showDialogPaireReussi = !this.showDialogPaireReussi;
    },
    toggleDialogError() {
      this.setAllFalse();
      this.showDialogError = !this.showDialogError;
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
    },
    init() {
      this.errorInterval = [];
      this.errorSymbol1 = "";
      this.errorSymbol2 = "";
    },
    async finalizeRequest() {
      try {
        await this.$store.dispatch("finalizeRequest", {
          symbol1: this.couple_1,
          symbol2: this.couple_2,
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      }
    },
    verifyForm() {
      this.init();
      if (!this.interval_checkbox.length) {
        this.errorInterval.push(this.$t("errorInterval"));
      }
      if (this.image1 == undefined) {
        this.errorSymbol1 = this.$t("errorSymbol1");
      }
      if (this.image2 == undefined) {
        this.errorSymbol2 = this.$t("errorSymbol2");
      }
      if (this.interval_checkbox.length && this.image1 && this.image2)
        this.validateRequest();
    },
    handleImage1(event) {
      this.image1 = event[0];
    },
    handleImage2(event) {
      this.image2 = event[0];
    },
    async validateRequest() {
      this.loading = true;
      let temp = "";
      for (let i = 0; i < this.interval_checkbox.length; i++) {
        temp = temp + `'` + this.interval_checkbox[i] + `'`;
        if (i + 1 != this.interval_checkbox.length) temp = temp + `,`;
      }
      temp = "[" + temp + "]";
      try {
        await this.$store.dispatch("addPaire", {
          symbol_1: this.couple_1,
          symbol_2: this.couple_2,
          image1: this.image1,
          image2: this.image2,
          interval: temp.toString(),
          token: localStorage.getItem("adminToken"),
        });
        await this.finalizeRequest();
        this.coupleName = this.$store.state.paire.assets.assetName.split("/");
        this.toggleDialogPaireReussi();
        this.displayRequestedCouples();
        this.$emit("refresh");
        this.loading = false;
      } catch (error) {
        if (error.response.status === 409)
          this.errorAddCouple = this.$t("errorCoupleExist");
        else this.errorAddCouple = this.$t("errorCombination");
        this.loading = false;
        this.toggleDialogError();
      }
    },
    orderBy: async function(field) {
      await this.$store.dispatch("requestedCouple", {
        token: localStorage.getItem("adminToken"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    loadPaires: async function() {
      try {
        await this.$store.dispatch("loadPaires", {
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      }
    },
    displayRequestedCouples: async function() {
      try {
        await this.$store.dispatch("requestedCouple", {
          token: localStorage.getItem("adminToken"),
          order: "",
          page: this.page,
          search: this.search,
          size: this.size,
        });
      } catch (e) {
        //
      }
    },
  },
  data: () => {
    return {
      iconCheck: `
            <svg id="done_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <path id="Tracé_42162" data-name="Tracé 42162" d="M0,0H24V24H0Z" fill="none"/>
              <path id="Tracé_42163" data-name="Tracé 42163" d="M9,16.2,4.8,12,3.4,13.4,9,19,21,7,19.6,5.6Z" fill="#21a179"/>
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
      iconWarning: `
        <svg id="warning-icon" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
          <path id="Tracé_12109" data-name="Tracé 12109" d="M1,74.833H85.333L43.167,2Zm46-11.5H39.333V55.667H47ZM47,48H39.333V32.667H47Z" transform="translate(2.833 5.667)"/>
        </svg>
      `,
      errorAddCouple: "",
      showDialogError: false,
      coupleName: [],
      visible: false,
      errorSelectedCrypto: [],
      errorSelectedCrypto1: [],
      errorInterval: [],
      errorSymbol1: "",
      errorSymbol2: "",
      listPaires: [],
      coupleToPop: "",
      couple_1: "",
      couple_2: "",
      loading: false,
      search: "",
      selected: "",
      selected1: "",
      order: "",
      page: 1,
      size: 5,
      error: "",
      rowsPerPage: 3,
      sur: "",
      showDialogDemandePaire: false,
      showDialogDemandePaireReussi: false,
      showDialogPaire: false,
      showDialogPaireReussi: false,
      symbol1: null,
      symbol2: null,
      interval_checkbox: [],
    };
  },
  watch: {
    async page() {
      await this.displayRequestedCouples();
    },
    async size() {
      await this.displayRequestedCouples();
    },
    async search() {
      await this.displayRequestedCouples();
      if (!this.requested.length) {
        //this.error = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.error = "";
        this.visible = false;
      }
    },
  },
  async mounted() {
    await this.displayRequestedCouples();
    await this.loadPaires();
    this.checkRequestedPairData();
  },
  computed: {
    requested() {
      return this.$store.state.paire.requests.results;
    },
    dataSize() {
      return this.$store.state.paire.requests.count;
    },
    next() {
      return this.$store.state.paire.requests.next;
    },
    paires() {
      return this.$store.state.listPaires.listPaires;
    },
  },
};
</script>

<style>
.paireDemande-table .coupleRequest_col {
  width: 10%;
}
.paireDemande-table .vues_col {
  width: 10%;
}
.paireDemande-table .nbrRequest_col {
  width: 5%;
}
.paireDemande-table .lastDateRequest_col {
  width: 5%;
}
.paireDemande-table .status_col {
  width: 5%;
}
.predict-dialog #warning-icon {
  fill: #d32f2f;
}
</style>

<style scoped>
.paireDemande-table .table-container {
  height: auto;
}
.align-text {
  text-align: center;
}
.titre-recherche {
  color: #5c626a;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
}
@media (max-width: 639px) {
  .filter-bloc {
    padding-left: 0 !important;
  }
}
@media (max-width: 639px) {
  .filter-bloc .md-field {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }
}
@media (max-width: 639px) {
  .filter-bloc .md-field input {
    font-size: 14px;
    padding: 6px 0.5rem !important;
    width: calc(100% - 32px);
  }
}
@media (max-width: 479px) {
  .filter-bloc .md-field input {
    font-size: 12px;
  }
}
@media (max-width: 639px) {
  .filter-bloc .md-field svg {
    margin-right: 0 !important;
    width: 16px;
    min-width: 16px;
  }
}
.filter-bloc .md-field.md-has-value svg {
  display: none;
}
@media (max-width: 639px) {
  .filter-bloc .md-field .md-input::-webkit-input-placeholder,
  .filter-bloc .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 14px !important;
  }
}

.dialogError-content {
  width: 380px;
}
@media (max-width: 414px) {
  .dialogError-content {
    width: auto;
  }
}
</style>
