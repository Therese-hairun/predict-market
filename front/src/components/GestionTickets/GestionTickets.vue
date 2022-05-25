<template>
  <div class="dashboard">
    <PermanentFull
      :titre="$t('ticketManagement')"
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
        <div id="gestion-tickets" class="mx-0">
          <div class="d-flex flex-wrap justify-content-between align-items-end">
            <div class="left">
              <h3 class="titre-recherche">{{ $t("ticketList") }}</h3>
              <span class="help-recherche">{{ $t("info:ticketList") }}</span>
            </div>
            <div class="right d-flex align-items-end">
              {{ $t("viewClosedTicket") }}
              <md-switch class="switch-cloture ml-2" v-model="show_cloture">{{
                show_cloture ? $t("display") : $t("hide")
              }}</md-switch>
            </div>

            <div class="table-wrapper flex-grow">
              <md-table
                md-table-fixed-header
                class="mt-3 predict-table ticket-table d-flex w-100"
              >
                <md-table-toolbar class="filter-bloc px-2 mb-3">
                  <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                    <md-input
                      :placeholder="$t('ticket:searchPlaceholder')"
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
                    <md-table-head scope="col" class="user_col">
                      {{ $t("users") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('client')"
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
                          v-on:click="orderBy('-' + 'client')"
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
                    <md-table-head scope="col" class="ticket_col">
                      {{ $t("ticketName") }}
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
                    <md-table-head scope="col" class="date_col">
                      {{ $t("createdAt") }}
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
                    <md-table-head scope="col" class="date_lastexchange_col">
                      {{ $t("lastExchange") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('updated_at')"
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
                          v-on:click="orderBy('-' + 'updated_at')"
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

                  <md-table-row v-for="(item, index) in tickets" :key="index">
                    <md-table-cell :data-label="$t('users')" class="user_col">
                      {{ item.client.firstname }}
                      {{ item.client.lastname }}
                    </md-table-cell>
                    <md-table-cell
                      :data-label="$t('ticketName')"
                      class="ticket_col"
                    >
                      {{ item.name }}
                    </md-table-cell>
                    <md-table-cell
                      :data-label="$t('createdAt')"
                      class="date_col"
                    >
                      {{ formatDate($t("dateFormat"), item.created_at) }}
                    </md-table-cell>
                    <md-table-cell
                      :data-label="$t('lastExchange')"
                      class="date_lastexchange_col"
                    >
                      {{
                        item.last_change
                          ? formatDate($t("dateFormat"), item.last_change)
                          : "-"
                      }}
                    </md-table-cell>
                    <md-table-cell
                      :data-label="$t('status')"
                      class="status_col"
                    >
                      <span
                        class="rond mr-1"
                        :class="item.status ? 'ouvert' : 'cloture'"
                      ></span>
                      {{ item.status ? $t("opened") : $t("closed") }}
                    </md-table-cell>
                    <md-table-cell data-label="" class="action_col">
                      <b-dropdown
                        variant="link"
                        toggle-class="text-decoration-none"
                        no-caret
                        class="table-dropdown"
                      >
                        <template #button-content>
                          <svg
                            id="option_tableau"
                            data-name="option tableau"
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                          >
                            <g id="more_horiz_black_24dp">
                              <path
                                id="Tracé_42169"
                                data-name="Tracé 42169"
                                d="M0,0H24V24H0Z"
                                fill="none"
                              />
                              <path
                                id="Tracé_42170"
                                data-name="Tracé 42170"
                                d="M6,10a2,2,0,1,0,2,2A2.006,2.006,0,0,0,6,10Zm12,0a2,2,0,1,0,2,2A2.006,2.006,0,0,0,18,10Zm-6,0a2,2,0,1,0,2,2A2.006,2.006,0,0,0,12,10Z"
                              />
                            </g>
                          </svg>
                        </template>
                        <b-dropdown-item @click="shareData(item.id)">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="22"
                            height="15"
                            viewBox="0 0 22 15"
                          >
                            <path
                              id="Tracé_988"
                              data-name="Tracé 988"
                              d="M23.637-39c-5,0-9.27,3.61-11,8,1.73,4.39,6,7,11,7s9.27-2.61,11-7C32.907-35.39,28.637-39,23.637-39Zm0,13a5,5,0,0,1-5-5,5,5,0,0,1,5-5,5,5,0,0,1,5,5A5,5,0,0,1,23.637-26Zm0-8a3,3,0,0,0-3,3,3,3,0,0,0,3,3,3,3,0,0,0,3-3A3,3,0,0,0,23.637-34Z"
                              transform="translate(-12.637 39)"
                              fill="#242c36"
                            />
                          </svg>
                          {{ $t("toConsult") }}
                        </b-dropdown-item>
                        <b-dropdown-item
                          href="#"
                          @click="updateStatusTicket(item)"
                        >
                          <svg
                            v-if="!item.status"
                            id="play_circle_outline_black_24dp"
                            xmlns="http://www.w3.org/2000/svg"
                            width="25"
                            height="25"
                            viewBox="0 0 20 20"
                          >
                            <path
                              id="Tracé_42361"
                              data-name="Tracé 42361"
                              d="M8,12.875,12.5,9.5,8,6.125ZM9.5,2A7.5,7.5,0,1,0,17,9.5,7.5,7.5,0,0,0,9.5,2Zm0,13.5a6,6,0,1,1,6-6A6.008,6.008,0,0,1,9.5,15.5Z"
                              transform="translate(-0.5 -0.5)"
                              fill="#242c36"
                            />
                          </svg>
                          <svg
                            v-if="item.status"
                            xmlns="http://www.w3.org/2000/svg"
                            width="20"
                            height="20"
                            viewBox="0 0 20 20"
                          >
                            <path
                              id="Tracé_42174"
                              data-name="Tracé 42174"
                              d="M14.59,8,12,10.59,9.41,8,8,9.41,10.59,12,8,14.59,9.41,16,12,13.41,14.59,16,16,14.59,13.41,12,16,9.41ZM12,2A10,10,0,1,0,22,12,9.991,9.991,0,0,0,12,2Zm0,18a8,8,0,1,1,8-8A8.011,8.011,0,0,1,12,20Z"
                              transform="translate(-2 -2)"
                              fill="#242c36"
                            />
                          </svg>
                          {{ !item.status ? $t("open") : $t("close") }}
                        </b-dropdown-item>
                      </b-dropdown>
                    </md-table-cell>
                  </md-table-row>
                  <md-table-row v-if="this.visible" class="empty-data">
                    <md-table-cell :colspan="5" class="align-text">{{
                      this.error
                    }}</md-table-cell>
                  </md-table-row>

                  <md-table-row class="pagination-row" v-if="!visible">
                    <md-table-cell :colspan="5">
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
              :dialogName="$t('addTicket')"
              @close="showDialogPaire = !showDialogPaire"
            >
              <form
                action=""
                class="form-abonnement w-100 my-4"
                style="max-width: 312px;"
              >
                <div class="form-group">
                  <md-field>
                    <label>{{ $t("ticketName") }}</label>
                    <md-input v-model="name"></md-input>
                  </md-field>
                </div>

                <p style="font-size:12px; color:#A7AAAE">
                  {{ $t("ticket:Instruction") }}
                </p>

                <div class="w-100 text-center mt-4">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-submit h-auto m-0"
                    style="width: 100% !important; max-width: 180px;"
                    :disabled="disableInputName"
                    @click="createTicket()"
                  >
                    {{ $t("createTicket") }}
                  </md-button>
                </div>
              </form>
            </Dialog>
            <Dialog
              :showDialog="showDialogPaireReussi"
              :titreDialog="$t('ticket:dialogSuccess')"
              :iconDialog="iconModifJours"
              @close="showDialogPaireReussi = !showDialogPaireReussi"
            >
              <div class="text-center" style="max-width: 380px;">
                {{ $t("ticket:successMessage1") }}<strong>{{ name }}</strong>
                {{ $t("ticket:successMessage2") }}.
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
        </div>
      </div>
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import Dialog from "../Dialog/Dialog.vue";
import MenuGestion from "../../data/MenuGestion.js";
import { PARAPHRASE, formatDate } from "../../utils/Constant";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
  name: "Support",
  components: {
    Dialog,
    PermanentFull,
    TablePagination,
  },
  props: {},
  methods: {
    formatDate,
    handleChangePageValue(val) {
      this.page = val;
    },
    handleChangeSizeValue(val) {
      this.size = val;
    },
    shareData(item) {
      localStorage.setItem("ticketId", this.encryptValue(item.toString()));
      this.$router.push({ name: "DetailTicket" });
    },
    encryptValue(val) {
      return this.CryptoJS.AES.encrypt(val, PARAPHRASE).toString();
    },
    checkTicketData() {
      if (!this.tickets.length) {
        this.error = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },
    setAllFalse() {
      this.showDialogPaire = false;
      this.showDialogPaireReussi = false;
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
    },
    loadTickets: async function() {
      this.loader = true;
      await this.$store.dispatch("loadTickets", {
        token: localStorage.getItem("adminToken"),
        order: "-created_at",
        page: this.page,
        search: this.search,
        size: this.size,
        show_all: this.show_cloture,
      });
      this.loader = false;
    },
    createTicket: async function() {
      const payload = {
        name: this.name,
      };
      await this.$store.dispatch("createTicket", {
        payload,
        token: localStorage.getItem("adminToken"),
      });
      this.toggleDialogPaireReussi();
      this.loadTickets();
    },
    updateStatusTicket: async function(item) {
      const payload = {
        status: !item.status,
      };
      try {
        await this.$store.dispatch("updateStatusTicketAdmin", {
          id: item.id,
          payload,
          token: localStorage.getItem("adminToken"),
        });
        await this.loadTickets();
      } catch (e) {
        //
      }
    },
    orderBy: async function(field) {
      await this.$store.dispatch("loadTickets", {
        token: localStorage.getItem("adminToken"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
        show_all: this.show_cloture,
      });
    },
  },
  data: () => {
    return {
      icon: `
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                  <path id="Tracé_19689" data-name="Tracé 19689" d="M19,3H4.99A2,2,0,0,0,3,5l.01,14A2,2,0,0,0,5,21H15l6-6V5A2.006,2.006,0,0,0,19,3ZM7,8H17v2H7Zm5,6H7V12h5Zm2,5.5V14h5.5Z" transform="translate(-3 -3)" fill="#5c626a"/>
                </svg>
        `,
      menuItems: MenuGestion,
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
      search: "",
      loader: false,
      page: 1,
      size: 5,
      visible: false,
      show_cloture: true,
      rowsPerPage: 3,
      sur: "",
      showDialogPaire: false,
      showDialogPaireReussi: false,
      disableInputName: true,
      name: "",
    };
  },
  watch: {
    async page() {
      await this.loadTickets();
    },
    async size() {
      await this.loadTickets();
    },
    async search() {
      await this.loadTickets();
      if (!this.tickets.length) {
        this.error = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.error = "";
        this.visible = false;
      }
    },
    name(val) {
      this.disableInputName = val.length > 3 ? false : true;
    },
    async show_cloture() {
      await this.loadTickets();
    },
  },
  async mounted() {
    await this.loadTickets();
    this.checkTicketData();
  },
  computed: {
    tickets() {
      return this.$store.state.ticket.tickets.results;
    },
    dataSize() {
      return this.$store.state.ticket.tickets.count;
    },
    next() {
      return this.$store.state.ticket.tickets.next;
    },
  },
};
</script>

<style>
button:focus:not(:focus-visible) {
  box-shadow: none;
  outline: none !important;
}
.ticket-table .user_col {
  width: 15%;
}
.ticket-table .ticket_col {
  width: 10%;
}
.ticket-table .date_col {
  width: 5%;
}
.ticket-table .date_lastexchange_col {
  width: 5%;
}
.ticket-table .status_col {
  width: 5%;
}
</style>
<style scoped>
.ticket-table .table-container {
  height: auto;
  /* max-height: calc(100vh - 280px); */
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
@media (max-width: 479px) {
  .filter-bloc .md-field .md-input::-webkit-input-placeholder,
  .filter-bloc .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 12px !important;
  }
}
</style>
