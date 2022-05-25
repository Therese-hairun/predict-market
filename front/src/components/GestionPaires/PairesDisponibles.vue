<template>
  <div class="d-flex flex-wrap justify-content-between align-items-center">
    <div class="left">
      <h3 class="titre-recherche">{{ $t("search") }}</h3>
      <span class="help-recherche">{{ $t("paireDispo:message") }}</span>
    </div>

    <div class="table-wrapper flex-grow">
      <md-table
        md-table-fixed-header
        class="mt-3 predict-table paireDispo-table d-flex w-100"
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
            <md-table-head scope="col" class="paire_col">
              {{ $t("pair") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('name')"
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
                  v-on:click="orderBy('-' + 'name')"
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
            <md-table-head class="vues_col">
              {{ $t("views") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('vues')"
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
                  v-on:click="orderBy('-' + 'vues')"
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
            <md-table-head scope="col" class="dayAdd_col">
              {{ $t("dateAdded") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('created_at')"
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
                  v-on:click="orderBy('-' + 'created_at')"
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
            <md-table-head scope="col" class="precision_col">
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
            <md-table-head scope="col" class="status_col">
              {{ $t("status") }}
              <span class="table-tri d-flex flex-column">
                <md-button
                  class="btn-tri arrow-up"
                  v-on:click="orderBy('status')"
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
                  v-on:click="orderBy('-' + 'status')"
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
          <md-table-row v-for="(item, index) in listPaires" :key="index">
            <md-table-cell data-label="Paire" class="paire_col">
              {{ item.name }}
            </md-table-cell>
            <md-table-cell data-label="Vues" class="vues_col">
              {{ item.vues ? item.vues : "-" }}
            </md-table-cell>
            <md-table-cell data-label="Date d'ajout" class="dayAdd_col">
              {{ formatDate($t("dateFormat"), item.created_at) }}
            </md-table-cell>
            <md-table-cell data-label="Précision moyenne" class="precision_col">
              {{ item.precision ? item.precision : "-" }}
            </md-table-cell>
            <md-table-cell data-label="Statut" class="status_col">
              <md-switch
                class="table-switch"
                v-model="item.status"
                @change="updateStatus(item)"
                >{{ item.status ? $t("active") : $t("desactive") }}</md-switch
              >
            </md-table-cell>
            <md-table-cell data-label="" class="action_col">
              <md-button
                class="text-normal btn-modifier"
                @click="shareData(item.name)"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="22"
                  height="15"
                  viewBox="0 0 22 15"
                  class="mr-2"
                >
                  <path
                    id="Tracé_988"
                    data-name="Tracé 988"
                    d="M23.637-39c-5,0-9.27,3.61-11,8,1.73,4.39,6,7,11,7s9.27-2.61,11-7C32.907-35.39,28.637-39,23.637-39Zm0,13a5,5,0,0,1-5-5,5,5,0,0,1,5-5,5,5,0,0,1,5,5A5,5,0,0,1,23.637-26Zm0-8a3,3,0,0,0-3,3,3,3,0,0,0,3,3,3,3,0,0,0,3-3A3,3,0,0,0,23.637-34Z"
                    transform="translate(-12.637 39)"
                    fill="#242c36"
                  />
                </svg>
                <ins>{{ $t("toConsult") }}</ins>
              </md-button>
            </md-table-cell>
          </md-table-row>
          <md-table-row v-if="this.visible" class="empty-data">
            <md-table-cell :colspan="5" class="align-text">{{
              $t("table:NotFound")
            }}</md-table-cell></md-table-row
          >
          <md-table-row class="pagination-row" v-if="!visible">
            <md-table-cell :colspan="6">
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
  </div>
</template>

<script>
import { PARAPHRASE, formatDate } from "../../utils/Constant";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
  name: "PaireDisponible",
  components: {
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
    shareData(item) {
      localStorage.setItem("coupleSymbol", this.encryptValue(item.toString()));
      this.$router.push({ name: "details-de-couple" });
    },
    encryptValue(val) {
      return this.CryptoJS.AES.encrypt(val, PARAPHRASE).toString();
    },
    checkAvailablePairData() {
      if (!this.listPaires.length) {
        this.error = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
    },

    displayPaires: async function() {
      await this.$store.dispatch("displayPaires", {
        token: localStorage.getItem("adminToken"),
        order: "-created_at",
        page: this.page,
        search: this.search,
        size: this.size,
      });
      this.listPaires = this.getListPaires;
    },
    orderBy: async function(field) {
      await this.$store.dispatch("displayPaires", {
        token: localStorage.getItem("adminToken"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    updateStatus: async function(item) {
      const payload = {
        status: item.status,
      };
      try {
        await this.$store.dispatch("updateStatusCouple", {
          id: item.id,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      }
      await this.displayPaires();
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
      coupleName: [],
      errorSelectedCrypto: [],
      errorSelectedCrypto1: [],
      errorInterval: [],
      errorSymbol1: [],
      errorSymbol2: [],
      listPaires: [],
      loading: false,
      search: "",
      selected: "",
      selected1: "",
      order: "",
      page: 1,
      size: 5,
      image1: null,
      image2: null,
      files: null,
      rowsPerPage: 3,
      visible: false,
      sur: "",
      showDialogPaire: false,
      errorAddCouple: "",
      showDialogPaireReussi: false,
      showDialogError: false,
      symbol1: null,
      symbol2: null,
      interval_checkbox: [],
    };
  },
  watch: {
    async page() {
      await this.displayPaires();
    },
    async size() {
      await this.displayPaires();
    },
    async search() {
      await this.displayPaires();
      if (!this.listPaires.length) {
        this.visible = true;
      } else {
        this.error = "";
        this.visible = false;
      }
    },
  },
  async mounted() {
    await this.displayPaires();
    this.checkAvailablePairData();
  },
  computed: {
    getListPaires() {
      return this.$store.state.paire.paires.results;
    },
    dataSize() {
      return this.$store.state.paire.paires.count;
    },
    next() {
      return this.$store.state.paire.paires.next;
    },
  },
  created() {
    document.title = this.$route.meta.title;
  },
};
</script>

<style>
* .loader-content {
  display: flex;
  align-items: center;
  justify-content: center;
}
.md-progress-spinner {
  margin: 16px;
}
.md-progress-spinner svg {
  height: 40px !important;
  width: 40px !important;
}
.md-progress-spinner .md-progress-spinner-circle {
  stroke: var(--primary) !important;
}
.paireDispo-table .paire_col {
  width: 10%;
}
.paireDispo-table .vues_col {
  width: 10%;
}
.paireDispo-table .dayAdd_col {
  width: 5%;
}
.paireDispo-table .precision_col {
  width: 10%;
}
.paireDispo-table .status_col {
  width: 5%;
}
</style>

<style scoped>
.paireDispo-table .table-container {
  height: auto;
  /* max-height: calc(100vh - 365px); */
}
.titre-recherche {
  color: #5c626a;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
}
.align-text {
  text-align: center;
}
@media (max-width: 639px) {
  .filter-bloc {
    padding-left: 0 !important;
    /* padding-right: 0 !important; */
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

.filter-bloc .md-field.md-has-value:before {
  content: "";
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 100px 100px 0 100px;
  border-color: #ffffff transparent transparent transparent;
  position: absolute;
  bottom: -10px;
  left: 50px;
}
.filter-bloc .md-field.md-has-value:after {
  content: "";
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 100px 100px 0 100px;
  border-color: #ccc transparent transparent transparent;
  position: absolute;
  bottom: -11px;
  left: 50px;
}
.text-error {
  padding: 32px 0;
}
.text-error .material-icons {
  color: var(--red);
  font-size: 4rem;
}
.text-error .md-title {
  font-size: 16px;
}
</style>
