<template>
  <div class="dashboard">
    <PermanentFull
      :titre="$t('pairManagement')"
      :icon="icon"
      :menuItems="menuItems"
      :admin="true"
    >
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div class="add-paire-btn_wrap">
          <md-button
            class="submit-dialog text-center btn-submit text-normal w-100 py-0 m-0"
            @click="toggleDialogPaire()"
          >
            <md-icon class="text-white">add</md-icon>
            {{ $t("addPair") }}
          </md-button>
        </div>
        <!-- Loader -->
        <div class="loader-content" v-if="loader">
          <p class="msg">{{ $t("loading") }}</p>
          <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
        </div>
        <!-- /Loader -->
        <div id="paires" class="paire_tab_content mx-0">
          <md-tabs class="">
            <template slot="md-tab" slot-scope="{ tab }">
              <div class="d-flex tab-item text-initial">
                <span v-html="tab.icon" class="mr-2"></span> {{ tab.label }}
              </div>
            </template>
            <md-tab
              id="tab-paires-dispo"
              :md-label="$t('pairsAvailable')"
              :md-icon="iconTabs1"
            >
              <PairesDisponibles ref="B" />
            </md-tab>
            <md-tab
              id="tab-demande-paire"
              :md-label="$t('pairRequests')"
              :md-icon="iconTabs2"
            >
              <DemandesPaires v-on:refresh="refresh" />
            </md-tab>
          </md-tabs>
        </div>

        <Dialog
          :showDialog="showDialogPaire"
          :dialogName="$t('addPair')"
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
                    v-for="(paire, index) in paires"
                    :key="index"
                    v-bind:value="paire.assetname"
                    >{{ paire.assetname }}
                  </md-option>
                </md-select>
              </md-field>
            </div>
            <span class="error mt-3">{{ errorSymbol1 }}</span>
            <div class="d-flex">
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
                <md-select v-model="selected1" name="symbol2" id="symbol2">
                  <md-option
                    v-for="(paire, index) in paires"
                    :key="index"
                    v-bind:value="paire.assetname"
                    >{{ paire.assetname }}
                  </md-option>
                </md-select>
              </md-field>
            </div>
            <span class="error mt-3">{{ errorSymbol2 }}</span>
            <div class="d-flex ">
              <UploadFile
                :uploadMsg="$t('uploadMsg')"
                :max="1"
                :clearAll="$t('delete')"
                type="file"
                :handleImages="handleImage2"
              />
            </div>

            <h3 class="titre-recherche mt-3">
              {{ $t("predictionIntervals") }}
            </h3>
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
                <md-progress-spinner
                  md-mode="indeterminate"
                ></md-progress-spinner>
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
          :showDialog="showDialogError"
          :titreDialog="$t('errorMessage')"
          :iconDialog="iconWarning"
          class= "errorMsg"
          @close="showDialogError = !showDialogError"
        >
          <div class="form-group dialogError-content text-center mb-4 mt-2" style="max-width: 380px;">
            <p class="text-error mb-4">{{ errorAddCouple }}</p>
            <md-button
              class="submit-dialog btn-submit text-center w-100 px-0 m-0"
              @click="showDialogError = false"
            >
              {{ $t("ok") }}
            </md-button>
          </div>
        </Dialog>

        <Dialog
          :showDialog="showDialogPaireReussi"
          :titreDialog="$t('addSuccess')"
          :iconDialog="iconModifJours"
          @close="showDialogPaireReussi = !showDialogPaireReussi"
        >
          <div class="text-center" style="max-width: 380px;">
            {{ $t("success:addCouple1") }}
            <strong>{{ coupleName[0] }}</strong> et
            <strong>{{ coupleName[1] }}</strong>
            {{ $t("success:addCouple2") }}
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
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import MenuGestion from "../../data/MenuGestion.js";
import PairesDisponibles from "./PairesDisponibles.vue";
import DemandesPaires from "./DemandesPaires.vue";
import Dialog from "../Dialog/Dialog.vue";
import UploadFile from "../Input/UploadFile.vue";

export default {
  name: "GestionPaires",
  components: {
    PermanentFull,
    PairesDisponibles,
    DemandesPaires,
    Dialog,
    UploadFile,
  },
  props: {},
  methods: {
    setAllFalse() {
      this.showDialogPaire = false;
      this.showDialogPaireReussi = false;
    },
    toggleDialogPaire() {
      this.init();
      this.setAllFalse();
      this.showDialogPaire = !this.showDialogPaire;
    },
    toggleDialogError() {
      this.setAllFalse();
      this.showDialogError = !this.showDialogError;
    },
    toggleDialogPaireReussi() {
      this.setAllFalse();
      this.showDialogPaireReussi = !this.showDialogPaireReussi;
    },
    handleImage1(event) {
      this.image1 = event[0];
    },
    handleImage2(event) {
      this.image2 = event[0];
    },
    refresh() {
      this.loader = true;
      this.$refs.B.displayPaires();
      this.loader = false;
    },
    init() {
      this.errorSelectedCrypto = "";
      this.errorSelectedCrypto1 = "";
      this.errorInterval = "";
      this.errorSymbol1 = "";
      this.errorSymbol2 = "";
      this.interval_checkbox = [];
      this.selected = "";
      this.selected1 = "";
    },
    verifyForm() {
      if (!this.selected) {
        this.errorSelectedCrypto = this.$t("errorSelectedCrypto");
      }
      if (!this.selected1) {
        this.errorSelectedCrypto1 = this.$t("errorSelectedCrypto1");
      }
      if (!this.interval_checkbox.length) {
        this.errorInterval = this.$t("errorInterval");
      }
      if (this.image1 == undefined) {
        this.errorSymbol1 = this.$t("errorSymbol1");
      }
      if (this.image2 == undefined) {
        this.errorSymbol2 = this.$t("errorSymbol2");
      }
      if (
        this.selected &&
        this.selected1 &&
        this.interval_checkbox.length &&
        this.image1 &&
        this.image2
      )
        this.addNewPaire();
    },
    loadPaires: async function() {
      try {
        await this.$store.dispatch("loadPaires", {
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        await this.$store.dispatch("loadDataCouples", {
          token: localStorage.getItem("token"),
        });
        window.location.reload();
      }
    },
    async addNewPaire() {
      this.loading = true;
      let temp = "";
      for (let i = 0; i < this.interval_checkbox.length; i++) {
        temp = temp + `'` + this.interval_checkbox[i] + `'`;
        if (i + 1 != this.interval_checkbox.length) temp = temp + `,`;
      }
      temp = "[" + temp + "]";
      try {
        await this.$store.dispatch("addPaire", {
          symbol_1: this.selected,
          symbol_2: this.selected1,
          image1: this.image1,
          image2: this.image2,
          interval: temp.toString(),
          token: localStorage.getItem("adminToken"),
        });
        this.coupleName = this.$store.state.paire.assets.assetName.split("/");
        this.toggleDialogPaireReussi();
        this.refresh();
        this.init();
        this.loading = false;
      } catch (error) {
        if (error.response.status === 409)
          this.errorAddCouple = this.$t("errorCoupleExist");
        else this.errorAddCouple = this.$t("errorCombination");
        this.loading = false;
        this.toggleDialogError();
      }
    },
  },
  data: () => {
    return {
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
      iconWarning: `
        <svg id="warning-icon" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
          <path id="Tracé_12109" data-name="Tracé 12109" d="M1,74.833H85.333L43.167,2Zm46-11.5H39.333V55.667H47ZM47,48H39.333V32.667H47Z" transform="translate(2.833 5.667)"/>
        </svg>
      `,
      menuItems: MenuGestion,
      showDialogPaire: false,
      showDialogPaireReussi: false,
      selected: "",
      selected1: "",
      symbol1: null,
      symbol2: null,
      interval_checkbox: [],
      errorSelectedCrypto: "",
      errorSelectedCrypto1: "",
      errorInterval: "",
      coupleName: [],
      loading: false,
      errorSymbol1: "",
      errorSymbol2: "",
      listPaires: [],
      image1: null,
      image2: null,
      files: null,
      rowsPerPage: 3,
      visible: false,
      sur: "",
      errorAddCouple: "",
      showDialogError: false,
      iconTabs1: `
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
            <path id="Tracé_42047" data-name="Tracé 42047" d="M19,3H5A2.006,2.006,0,0,0,3,5V19a2.006,2.006,0,0,0,2,2H19a2.006,2.006,0,0,0,2-2V5A2.006,2.006,0,0,0,19,3ZM14,17H7V15h7Zm3-4H7V11H17Zm0-4H7V7H17Z" transform="translate(-3 -3)" fill="#a7aaae"/>
          </svg>
        `,
      iconTabs2: `
          <svg xmlns="http://www.w3.org/2000/svg" width="15.998" height="16" viewBox="0 0 15.998 16">
            <path id="Tracé_42501" data-name="Tracé 42501" d="M19.8,18.4,14,10.67V6.5l1.35-1.69A.5.5,0,0,0,14.96,4H9.04a.5.5,0,0,0-.39.81L10,6.5v4.17L4.2,18.4A1,1,0,0,0,5,20H19A1,1,0,0,0,19.8,18.4Z" transform="translate(-4.001 -4)" fill="#a7aaae"/>
          </svg>      
        `,
      loader: false,
    };
  },
  async mounted() {
    await this.loadPaires();
  },
  computed: {
    paires() {
      return this.$store.state.listPaires.listPaires;
    },
  },
};
</script>

<style>
.dashboard-title {
  line-height: 1.4;
}
@media (max-width: 479px) {
  .dashboard-title {
    line-height: 1.15;
  }
}

@media (max-width: 480px) {
  .paire_tab_content .md-tabs-navigation {
    justify-content: center !important;
    margin-bottom: 5px;
    width: 100%;
  }
}
@media (max-width: 479px) {
  .paire_tab_content .md-tabs-navigation .md-button {
    position: relative;
  }
}
@media (max-width: 479px) {
  .paire_tab_content .md-tabs-navigation .md-button .md-ripple {
    justify-content: center;
    position: relative;
  }
}
@media (max-width: 479px) {
  .paire_tab_content .md-tabs-navigation .md-button .md-ripple:after {
    background-color: #fdca40;
    content: "";
    height: 2px;
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    transition: all 0.25s ease-in-out;
    width: 0;
  }
}
@media (max-width: 479px) {
  .paire_tab_content .md-tabs-navigation .md-button.md-active .md-ripple:after {
    width: 50%;
  }
}
@media (max-width: 479px) {
  .paire_tab_content .md-tabs-navigation .md-tabs-indicator {
    display: none;
  }
}
.predict-dialog #warning-icon {
  fill: #d32f2f;
}

</style>
<style scoped>
#paires {
  padding: 20px 0 0;
}
#paires .titre-wrapper .titre {
  color: var(--black);
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;
  font-size: 24px;
  letter-spacing: 0.18px;
  line-height: 24px;
}
#paires .content-wrapper {
  max-width: 1027.5px;
}
#paires .select-choice {
  letter-spacing: 0.25px;
  line-height: 20px;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 14px;
  color: var(--placeholder);
  max-width: fit-content;
}
#paires .select-choice .active {
  color: var(--black);
}

#paires .liste-paires {
  width: calc(100% + 21px);
  margin-left: -21px;
}
#paires .liste-paires .item {
  margin-left: 21px;
  display: inline-block;
  vertical-align: middle;
  width: calc(25% - 21px);
  min-width: 241px;
}
.rond {
  display: inline-block;
  content: "";
  width: 11px;
  height: 11px;
  background-color: #fd406d;
  border-radius: 50%;
}
.rond.cloture {
  background-color: #21a179;
}
#content-dashboard-wrapper {
  position: relative;
}
#content-dashboard-wrapper .add-paire-btn_wrap {
  position: absolute;
  right: 20px;
  top: -45px;
}
@media (max-width: 767px) {
  #content-dashboard-wrapper .add-paire-btn_wrap {
    margin-top: 10px;
    position: relative;
    text-align: center;
    right: auto;
    top: auto;
  }
  #content-dashboard-wrapper .add-paire-btn_wrap .md-button {
    max-width: 200px;
  }
}
.bigBtn {
  max-width: 277px;
  width: 100% !important;
}
@media (max-width: 639px) {
  .bigBtn {
    font-size: 14px;
  }
}
@media (max-width: 639px) {
  .bigBtn .md-ripple {
    padding: 0;
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
