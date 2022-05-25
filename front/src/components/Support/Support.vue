<template>
  <div id="support" class="dashboard">
    <PermanentFull :titre="$t('support')" :icon="icon" :menuItems="menuItems">
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div id="support" class="mx-0">
          <div
            class="d-flex flex-wrap justify-content-between align-items-center"
          >
            <div class="left">
              <h3 class="titre-recherche">{{ $t("myTickets") }}</h3>
              <span class="help-recherche">{{ $t("messageSupport") }}</span>
            </div>

            <div class="right">
              <md-button
                class="submit-dialog text-center btn-submit text-normal w-100 py-0 m-0"
                @click="toggleDialogPaire()"
              >
                <md-icon class="text-white">add</md-icon
                >{{ $t("addTicket") }}</md-button
              >
            </div>
          </div>
          <div class="table-wrapper flex-grow">
            <md-table
              md-table-fixed-header
              class="mt-3 predict-table support-table d-flex w-100"
            >
              <md-table-toolbar class="filter-bloc px-2 mb-3">
                <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                  <md-input
                    :placeholder="$t('yourTickets')"
                    class="input-search border-0"
                    v-model="search"
                    autocomplete="off"
                  />
                  <svg
                    class=""
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
              <div v-if="!ticketLength">
                <md-table-empty-state
                  :md-label="$t('emptyTicket')"
                  id="support-table-empty-state"
                  :md-description="$t('emptyMessage')"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="148.453"
                    height="121.888"
                    viewBox="0 0 148.453 121.888"
                    style="order:1; margin-bottom: 0.75rem;"
                  >
                    <g
                      id="Groupe_53078"
                      data-name="Groupe 53078"
                      transform="translate(9259.094 3855.75)"
                    >
                      <g
                        id="Oval"
                        transform="translate(-9259.094 -3855.75)"
                        fill="#fff"
                        stroke="#5c626a"
                        stroke-miterlimit="10"
                        stroke-width="2"
                      >
                        <circle
                          cx="53.131"
                          cy="53.131"
                          r="53.131"
                          stroke="none"
                        />
                        <circle
                          cx="53.131"
                          cy="53.131"
                          r="52.131"
                          fill="none"
                        />
                      </g>
                      <path
                        id="Tracé_42175"
                        data-name="Tracé 42175"
                        d="M717.108,67.788a25.785,25.785,0,1,0,25.785,25.785,25.8,25.8,0,0,0-25.785-25.785Zm0,49.531h0a23.747,23.747,0,1,1,23.747-23.747,23.783,23.783,0,0,1-23.747,23.747ZM704.1,98.117H731.37a14.219,14.219,0,0,1-27.273,0Zm17.87-8.935h0l-1.724-1.722L725.1,82.6l4.86,4.86-1.722,1.722L725.1,85.97Zm-14.656,0h0l-1.645-1.722,4.778-4.86h.082l4.777,4.86-1.722,1.722-3.055-3.212Z"
                        transform="translate(-9922.287 -3896.973)"
                        fill="#5c626a"
                      />
                      <g id="Groupe_53077" data-name="Groupe 53077">
                        <g
                          id="Oval_Copy"
                          data-name="Oval Copy"
                          transform="translate(-9176.272 -3799.494)"
                          fill="#fff"
                          stroke="#a7aaae"
                          stroke-miterlimit="10"
                          stroke-width="1"
                        >
                          <circle
                            cx="32.816"
                            cy="32.816"
                            r="32.816"
                            stroke="none"
                          />
                          <circle
                            cx="32.816"
                            cy="32.816"
                            r="32.316"
                            fill="none"
                          />
                        </g>
                        <path
                          id="Tracé_42176"
                          data-name="Tracé 42176"
                          d="M706.949,67.788a15.626,15.626,0,1,0,15.626,15.626,15.638,15.638,0,0,0-15.626-15.626Zm0,30.017h0A14.391,14.391,0,1,1,721.34,83.414a14.413,14.413,0,0,1-14.391,14.391Zm-7.885-11.637h16.528a8.617,8.617,0,0,1-16.528,0Zm10.83-5.415h0l-1.045-1.044,2.943-2.945,2.945,2.945-1.044,1.044-1.9-1.947Zm-8.882,0h0l-1-1.044,2.9-2.945h.05l2.9,2.945-1.044,1.044-1.852-1.947Z"
                          transform="translate(-9850.406 -3850.093)"
                          fill="#5c626a"
                        />
                      </g>
                    </g>
                  </svg>
                </md-table-empty-state>
              </div>
              <div class="table-container" v-if="ticketLength">
                <md-table-row class="table-header">
                  <md-table-head scope="col" class="ticketName_col">
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
                  <md-table-head scope="col" class="createDate_col">
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
                  <md-table-head scope="col" class="lastDateChange_col">
                    {{ $t("lastExchange") }}
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        v-on:click="orderBy('update_at')"
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
                        v-on:click="orderBy('-' + 'update_at')"
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
                  <md-table-head scope="col"></md-table-head>
                </md-table-row>
                <md-table-row v-for="(item, index) in tickets" :key="index">
                  <md-table-cell :data-label="$t('ticketName')">
                    {{ item.name }}
                  </md-table-cell>
                  <md-table-cell :data-label="$t('createdAt')">
                    {{ formatDate($t("dateFormat"), item.created_at) }}
                  </md-table-cell>
                  <md-table-cell :data-label="$t('lastExchange')">
                    {{
                      item.last_change
                        ? formatDate($t("dateFormat"), item.last_change)
                        : "-"
                    }}
                  </md-table-cell>
                  <md-table-cell :data-label="$t('status')">
                    <span
                      class="rond mr-1"
                      :class="item.status ? 'ouvert' : 'cloture'"
                    ></span>
                    {{ item.status ? $t("opened") : $t("closed") }}
                  </md-table-cell>
                  <md-table-cell data-label="">
                    <div class="d-flex align-items-center justify-content-end">
                      <md-button
                        class="text-center w-auto text-normal btn-modifier btn-cloturer"
                        v-if="item.status"
                        @click="updateStatusTicket(item.id)"
                      >
                        <svg
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
                        <ins>{{ $t("close") }}</ins>
                      </md-button>
                      <md-button
                        class="text-center w-auto text-normal btn-modifier btn-consulter"
                      >
                        <router-link
                          :to="{
                            name: 'DetailsSupport',
                          }"
                          @click.native="shareData(item.id)"
                        >
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
                          <ins>{{ $t("toConsult") }}</ins>
                        </router-link>
                      </md-button>
                    </div>
                  </md-table-cell>
                </md-table-row>
                <md-table-row class="pagination-row">
                  <md-table-cell :colspan="7">
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

                <md-field class="m-0 textareaField">
                  <label>{{ $t("ticketMessage") }}</label>
                  <md-textarea v-model="ticketMessage" maxlength="255">
                  </md-textarea>
                </md-field>
              </div>

              <p style="font-size:12px; color:#A7AAAE">
                {{ $t("ticket:Instruction") }}
              </p>

              <div class="w-100 text-center mt-4">
                <md-button
                  class="submit-dialog bigBtn text-center btn-submit h-auto m-0"
                  style="width: 100% !important; max-width: 180px;"
                  :disabled="disableInputName || disableInputMesssage"
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
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import Dialog from "../Dialog/Dialog.vue";
import MenuUser from "../../data/MenuUser.js";
import { PARAPHRASE, formatDate } from "../../utils/Constant";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
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
      localStorage.setItem("supportId", this.encryptValue(item.toString()));
    },
    setAllFalse() {
      this.showDialogPaire = false;
      this.showDialogPaireReussi = false;
    },
    toggleDialogPaire() {
      this.setAllFalse();
      this.name = "";
      this.showDialogPaire = !this.showDialogPaire;
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
    loadTickets: async function() {
      await this.$store.dispatch("loadUserTickets", {
        token: localStorage.getItem("token"),
        order: "-created_at",
        page: this.page,
        search: this.search,
        size: this.size,
      });
      this.ticketLength = this.tickets.length;
    },
    createTicket: async function() {
      const payload = {
        name: this.name,
        message: this.ticketMessage,
      };
      await this.$store.dispatch("createTicket", {
        payload,
        token: localStorage.getItem("token"),
      });
      this.toggleDialogPaireReussi();
      await this.loadTickets();
      this.$router.push(
        { name: "DetailsSupport" },
        this.shareData(this.tickets[0].id)
      );
    },
    updateStatusTicket: async function(item) {
      const payload = {
        status: false,
      };
      try {
        await this.$store.dispatch("updateStatusTicket", {
          id: item,
          payload,
          token: localStorage.getItem("token"),
        });
        this.loadTickets();
      } catch (e) {
        //
      }
    },
    orderBy: async function(field) {
      await this.$store.dispatch("loadUserTickets", {
        token: localStorage.getItem("token"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    encryptValue(val) {
      return this.CryptoJS.AES.encrypt(val, PARAPHRASE).toString();
    },
  },
  data: () => {
    return {
      titre: "Support",
      icon: `
          <svg class="icon-item" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="5 0 19 24">
            <path id="Tracé_19680" class="to-fill" data-name="Tracé 19680" d="M11.5,2a8.5,8.5,0,0,0,0,17H12v3c4.86-2.34,8-7,8-11.5A8.506,8.506,0,0,0,11.5,2Zm1,14.5h-2v-2h2Zm0-3.5h-2c0-3.25,3-3,3-5a2,2,0,0,0-4,0h-2a4,4,0,0,1,8,0C15.5,10.5,12.5,10.75,12.5,13Z" fill="#5c626a"/>
          </svg>
        `,
      menuItems: MenuUser,
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
      ticketLength: null,
      page: 1,
      size: 5,
      visible: false,
      rowsPerPage: 3,
      sur: "",
      showDialogPaire: false,
      showDialogPaireReussi: false,
      disableInputName: true,
      disableInputMesssage: true,
      name: "",
      ticketMessage: "",
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
    },
    name(val) {
      this.disableInputName = val.length > 3 ? false : true;
    },
    ticketMessage(val) {
      this.disableInputMesssage = val.length > 3 ? false : true;
    },
  },
  async mounted() {
    await this.loadTickets();
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
    user() {
      return this.$store.state.client.clients;
    },
  },
};
</script>

<style>
.support-table .table-container {
  height: auto;
  /* max-height: calc(100vh - 280px); */
}
@media (max-width: 1280px) {
  .dashboard-title {
    padding-left: 16px;
    padding-right: 16px;
  }
}
@media (max-width: 960px) {
  .dashboard-title {
    /* padding-left: 16px;
      padding-right: 16px; */
  }
}
@media (max-width: 600px) {
  .dashboard-title {
    font-size: 24px;
    padding-left: 12px;
    padding-right: 12px;
  }
}
@media (max-width: 479px) {
  .dashboard-title {
    font-size: 18px;
    line-height: 1.15;
  }
}
@media (max-width: 639px) {
  /* #support .md-toolbar {
      padding-left: 0 !important;
    } */
}
@media (max-width: 639px) {
  #support .md-toolbar .md-field {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }
}
@media (max-width: 639px) {
  #support .md-toolbar .md-field input {
    font-size: 14px;
    padding: 6px 0.5rem !important;
    width: calc(100% - 32px);
  }
}
@media (max-width: 479px) {
  #support .md-toolbar .md-field input {
    font-size: 14px;
  }
}
@media (max-width: 639px) {
  #support .md-toolbar .md-field svg {
    margin-right: 0 !important;
    width: 16px;
    min-width: 16px;
  }
}
#support .md-field.md-has-value > svg {
  display: none;
}
@media (max-width: 639px) {
  #support .md-toolbar .md-field .md-input::-webkit-input-placeholder,
  #support .md-toolbar .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 14px !important;
  }
}
@media (max-width: 479px) {
  #support .md-toolbar .md-field .md-input::-webkit-input-placeholder,
  #support .md-toolbar .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 12px !important;
  }
}
@media (max-width: 639px) {
  #support .md-empty-state-description {
    font-size: 14px;
    line-height: 1.4;
  }
}
@media (max-width: 639px) {
  #support .md-table-empty-state {
    padding: 12px;
  }
}

.support-table .ticketName_col {
  width: 25%;
}
.support-table .createDate_col {
  width: 5%;
}
.support-table .lastDateChange_col {
  width: 5%;
}
.predict-dialog .form-abonnement .textareaField .md-count {
  color: var(--black);
  font-weight: 600;
  height: 20px;
  margin-top: 4px;
  position: relative;
  top: auto;
  bottom: auto;
  right: auto;
  text-align: right;
  width: 60px;
}
</style>

<style scoped>
.predict-dialog .form-abonnement .textareaField textarea {
  border: 1px solid var(--line);
  border-radius: 6px;
  height: 100px;
  font-size: 12px;
  margin-top: 15px;
  padding: 15px 0.75rem;
  resize: none;
  min-width: 100%;
}
.predict-dialog
  .form-abonnement
  .textareaField
  textarea::-moz-input-placeholder {
  color: var(--placeholder);
  font-size: 14px;
}
.predict-dialog
  .form-abonnement
  .textareaField
  textarea::-webkit-input-placeholder {
  color: var(--placeholder);
  font-size: 14px;
}
.predict-dialog .form-abonnement .textareaField > label {
  left: 10px;
  line-height: 1.25;
  top: -50px;
}
.predict-dialog .form-abonnement .textareaField.md-has-value > label,
.predict-dialog .form-abonnement .textareaField.md-focused > label {
  background-color: #fff;
  font-size: 10px !important;
  line-height: 20px;
  top: -104px;
}

.titre-recherche {
  color: #5c626a;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
}
.help-recherche {
  display: inline-block;
  margin-bottom: 10px;
}
.btn-modifier svg {
  margin-right: 6px;
}
.btn-submit {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  height: 40px;
}
.btn-submit i {
  font-size: 14px;
  margin-right: 15px;
}
@media (max-width: 479px) {
  #support .right {
    text-align: center;
    width: 100%;
  }
}
@media (max-width: 479px) {
  #support .right .btn-submit {
    max-width: 180px;
  }
}
</style>
