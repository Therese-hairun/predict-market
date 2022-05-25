<template>
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
        <div id="detail-ticket" class="mx-0">
          <div class="d-flex flex-column justify-content-center">
            <router-link
              to="/tous-les-tickets"
              class="back mb-3 align-self-start"
              ><i class="fa fa-chevron-left" aria-hidden="true"></i
              >{{ $t("back") }}</router-link
            >
            <div class="titre-recherche">{{ $t("ticketDetail") }}</div>
            <p class="description">
              {{ $t("info:ticketDetail") }}
            </p>
          </div>
        </div>
        <div
          class="messagebox dashboard-border overflow-hidden flex-grow-1 d-flex flex-column"
        >
          <div class="titre-wrapper">
            <p>{{ ticketName }}</p>
            <div
              class="statut d-flex align-items-baseline"
              style="font-size: 12px; color: #fff;"
            >
              <span style="font-size: 8px; color: #a7aaae;">{{
                $t("status")
              }}</span>
              <span
                class="rond ml-2 mr-2"
                :class="status ? 'ouvert' : 'cloture'"
              ></span>
              {{ status ? $t("opened") : $t("closed") }}
              <md-button
                class="ml-auto btn-cloture"
                @click="updateStatusTicket()"
              >
                <svg
                  v-if="status"
                  xmlns="http://www.w3.org/2000/svg"
                  width="15"
                  height="15"
                  viewBox="0 0 20 20"
                >
                  <path
                    id="Tracé_42174"
                    data-name="Tracé 42174"
                    d="M14.59,8,12,10.59,9.41,8,8,9.41,10.59,12,8,14.59,9.41,16,12,13.41,14.59,16,16,14.59,13.41,12,16,9.41ZM12,2A10,10,0,1,0,22,12,9.991,9.991,0,0,0,12,2Zm0,18a8,8,0,1,1,8-8A8.011,8.011,0,0,1,12,20Z"
                    transform="translate(-2 -2)"
                    fill="#fdca40"
                  />
                </svg>
                <svg
                  v-if="!status"
                  id="play_circle_outline_black_24dp"
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 20 20"
                >
                  <path
                    id="Tracé_42361"
                    data-name="Tracé 42361"
                    d="M8,12.875,12.5,9.5,8,6.125ZM9.5,2A7.5,7.5,0,1,0,17,9.5,7.5,7.5,0,0,0,9.5,2Zm0,13.5a6,6,0,1,1,6-6A6.008,6.008,0,0,1,9.5,15.5Z"
                    transform="translate(-0.5 -0.5)"
                    fill="#fdca40"
                  />
                </svg>
                {{ !status ? $t("open") : $t("close") }}
              </md-button>
            </div>
          </div>

          <div
            class="message-wrapper flex-grow-1 p-2 p-md-3"
            id="messageWrapper"
          >
            <div class="message-list">
              <div
                class="message-content"
                v-for="(date, index) in messages"
                :key="index"
              >
                <div class="day_separator">
                  <div>
                    <div class="border-dashed"></div>
                    <div
                      :data-text-as-pseudo-element="
                        formatDate(date[0].message_date)
                      "
                      dir="auto"
                      style='position: relative; display: inline; flex-grow: 0; flex-shrink: 0; overflow: hidden; white-space: nowrap; overflow-wrap: break-word; font-size: 12px; color: rgb(138, 141, 145); font-family: "SF Regular", "Segoe System UI Regular", "Segoe UI Regular", sans-serif; font-weight: 400; align-self: center; padding: 5px 10px; cursor: inherit;'
                    ></div>
                    <div class="border-dashed"></div>
                  </div>
                </div>
                <div
                  v-for="(item, index) in date"
                  :key="index"
                  :class="
                    !item.is_admin ? 'sender-wrapper' : 'receiver-wrapper'
                  "
                >
                  <div>
                    <div class="profil-wrapper">
                      <div class="profil-bloc">
                        <button class="profil" v-if="!item.is_admin">
                          <b-avatar
                            size="40px"
                            v-if="profil"
                            v-bind:src="profil"
                          ></b-avatar>
                          <div v-else>
                            {{ userInitial }}
                          </div>
                        </button>
                        <div
                          :class="
                            !item.is_admin ? 'sender-name' : 'receiver-name'
                          "
                        >
                          <span v-if="!item.is_admin"> </span>
                          <time>{{ getHour(item.message_time) }}</time>
                        </div>
                      </div>
                      <div class="message-bloc">
                        <div>
                          <div>
                            <div class="message-bloc-wrapper">
                              <div
                                :class="
                                  !item.is_admin
                                    ? 'sender-message'
                                    : 'receiver-message'
                                "
                              >
                                {{ item.message }}
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="form-wrapper d-flex p-2 p-md-3 d-flex">
            <md-field class="new_message_wrapper m-0">
              <!-- ticket ouvert : fond blanc | ticket cloturé : fond grisé -->
              <md-textarea
                v-model="new_message"
                md-autogrow
                :placeholder="$t('yourMessageHere')"
                :class="status ? 'open' : 'closed'"
                :disabled="!status"
                maxlength="255"
              ></md-textarea>
            </md-field>
            <button
              class="btn-send-message bgColor-primary"
              :disabled="sendButton"
              @click="sendMessage()"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20.77"
                height="18.002"
                viewBox="0 0 20.77 18.002"
              >
                <path
                  id="send"
                  d="M35.932,55.761l-.007,0L17.443,48.092a1.02,1.02,0,0,0-.961.093,1.067,1.067,0,0,0-.482.891v4.9A1.039,1.039,0,0,0,16.845,55l10.08,1.864a.173.173,0,0,1,0,.34l-10.08,1.864A1.039,1.039,0,0,0,16,60.086v4.9a1.02,1.02,0,0,0,.458.852,1.036,1.036,0,0,0,.572.173,1.063,1.063,0,0,0,.412-.084l18.481-7.622.008,0a1.385,1.385,0,0,0,0-2.545Z"
                  transform="translate(-16 -48.013)"
                  fill="#fff"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </PermanentFull>
  </div>
</template>
<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import MenuGestion from "../../data/MenuGestion.js";
import moment from "moment";
import * as _ from "lodash";
import { PARAPHRASE } from "../../utils/Constant";

export default {
  name: "DetailsSupport",
  components: {
    PermanentFull,
  },
  data: () => {
    return {
      titre: "",
      ticketName: "",
      userTicket: null,
      sendButton: true,
      profil: null,
      userInitial: "",
      icon: `
          <svg class="icon-item" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="5 0 19 24">
            <path id="Tracé_19680" class="to-fill" data-name="Tracé 19680" d="M11.5,2a8.5,8.5,0,0,0,0,17H12v3c4.86-2.34,8-7,8-11.5A8.506,8.506,0,0,0,11.5,2Zm1,14.5h-2v-2h2Zm0-3.5h-2c0-3.25,3-3,3-5a2,2,0,0,0-4,0h-2a4,4,0,0,1,8,0C15.5,10.5,12.5,10.75,12.5,13Z" fill="#5c626a"/>
          </svg>
        `,
      menuItems: MenuGestion,
      status: null,
      new_message: "",
    };
  },
  methods: {
    handleDefaultScrollPosition() {
      const container = this.$el.querySelector("#messageWrapper .message-list");
      container.scrollTop = container.scrollHeight;
    },
    getHour(item) {
      return moment(item, "HH:mm:ss").format("HH:mm");
    },
    getTicketById: async function() {
      await this.$store.dispatch("getTicketByIdAdmin", {
        id: this.userTicket,
        token: localStorage.getItem("adminToken"),
      });
      this.profil = this.$store.state.ticket.ticketAdmin.profil;
      this.userInitial =
        this.ticket.client.lastname[0].toUpperCase() +
        "" +
        this.ticket.client.firstname[0].toUpperCase();
      this.status = this.ticket.status;
      this.ticketName = this.ticket.name;
    },
    sendMessage: async function() {
      this.sendButton = true;
      const payload = {
        message: this.new_message,
      };
      try {
        await this.$store.dispatch("sendMessageAdmin", {
          id: this.userTicket,
          payload,
          token: localStorage.getItem("adminToken"),
        });
        await this.getTicketById();
        this.new_message = "";
        this.handleDefaultScrollPosition();
      } catch (e) {
        // 
      }
    },
    updateStatusTicket: async function() {
      const payload = {
        status: !this.status,
      };
      try {
        await this.$store.dispatch("updateStatusTicketAdmin", {
          id: this.ticket.id,
          payload,
          token: localStorage.getItem("adminToken"),
        });
        this.getTicketById();
      } catch (e) {
        // 
      }
    },
    formatDate(item) {
      return moment().format("YYYY-MM-DD") == item
        ? this.$t("today")
        : moment(item).format(this.$t("dateFormat"));
    },
    decryptValue(val) {
      return this.CryptoJS.AES.decrypt(val, PARAPHRASE).toString(
        this.CryptoJS.enc.Utf8
      );
    },
  },
  async mounted() {
    await this.getTicketById();
    this.handleDefaultScrollPosition();
  },
  computed: {
    ticket() {
      return this.$store.state.ticket.ticketAdmin.ticket;
    },
    messages() {
      const groupby = _.groupBy(
        this.$store.state.ticket.ticketAdmin.messages,
        "message_date"
      );
      return groupby;
    },
  },
  watch: {
    new_message(val) {
      this.sendButton = val.length > 0 ? false : true;
    },
  },
  created() {
    this.userTicket = +this.decryptValue(localStorage.getItem("ticketId"));
  },
};
</script>

<style>
.form-wrapper .md-count {
  color: var(--black);
  display: inline-block;
  font-weight: 600;
  left: 0;
  right: auto;
  text-align: right;
  width: 60px;
}
</style>

<style scoped>
#content-dashboard-wrapper {
  max-height: calc(100vh - 80px);
  overflow: hidden;
}
@media (max-width: 960px) {
  #content-dashboard-wrapper {
    max-height: calc(100vh - 60px);
  }
}
@media (max-width: 600px) {
  #content-dashboard-wrapper {
    max-height: calc(100vh - 70px);
  }
}
@media (max-width: 639px) {
  .messagebox.dashboard-border {
    padding: 0 !important;
  }
}
.messagebox {
  justify-content: space-between;
}
.messagebox .titre-wrapper {
  background-color: var(--black);
  color: var(--placeholder);
  padding: 10px 16px;
  position: relative;
}
.messagebox .titre-wrapper > p {
  max-width: calc(100% - 125px);
}
@media (max-width: 479px) {
  .messagebox .titre-wrapper > p {
    margin: 0;
  }
}
.sender-wrapper {
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: visible;
  align-items: stretch;
  width: 100%;
}
.sender-wrapper > div {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: hidden;
  align-items: stretch;
  align-self: stretch;
  padding-top: 10px;
}
.sender-wrapper > div > div {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  flex-shrink: 1;
  overflow: hidden;
  align-items: stretch;
  justify-content: flex-start;
  padding-right: 36px;
}
.receiver-wrapper .profil-wrapper,
.sender-wrapper .profil-wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 1;
  overflow: hidden;
  align-items: stretch;
  background-color: rgba(0, 0, 0, 0);
  min-height: 30px;
}
.receiver-wrapper .profil-bloc,
.sender-wrapper .profil-bloc {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: hidden;
  align-items: flex-start;
}
.sender-wrapper .profil {
  position: relative;
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: visible;
  align-items: stretch;
  justify-content: center;
  background-color: transparent;
  border-color: transparent;
  text-align: left;
  border-width: 0px;
  width: 40px;
  height: 42px;
  margin-right: 10px;
  cursor: pointer;
  padding: 0px;
  border-style: solid;
}
.sender-wrapper .profil > div {
  position: relative;
  overflow: visible;
  flex-grow: 0;
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  background-color: var(--black);
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  border-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--placeholder);
}

.receiver-name {
  text-align: right;
}
.receiver-wrapper time,
.sender-wrapper time {
  color: var(--line);
  font-size: 12px;
  /* font-size: 10px; */
}
.receiver-wrapper .message-bloc,
.sender-wrapper .message-bloc {
  position: relative;
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: hidden;
  align-items: stretch;
  margin-left: 50px;
  margin-top: -23px;
}
.receiver-wrapper .message-bloc > div,
.sender-wrapper .message-bloc > div {
  position: relative;
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 1;
  overflow: hidden;
  align-items: stretch;
  border-radius: 8px 8px 8px 0px;
  background-color: var(--black);
  transform: translateX(0px);
}
.receiver-wrapper .message-bloc > div {
  background-color: #f6f6f7;
}
.receiver-wrapper .message-bloc > div > div,
.sender-wrapper .message-bloc > div > div {
  position: relative;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  flex-shrink: 1;
  overflow: hidden;
  align-items: stretch;
  padding: 8px;
}
.receiver-message,
.sender-message {
  position: relative;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: visible;
  white-space: pre-wrap;
  overflow-wrap: break-word;
  font-size: 12px;
  line-height: 18px;
  letter-spacing: 0.12px;
  color: var(--placeholder);
  align-self: stretch;
  background-color: rgba(0, 0, 0, 0);
  font-weight: 400;
  user-select: text;
  cursor: text;
}
.receiver-message {
  color: var(--black);
}

.receiver-wrapper {
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: visible;
  align-items: stretch;
  width: 100%;
}
.receiver-name,
.sender-name {
  position: relative;
  display: inline;
  flex-grow: 1;
  flex-shrink: 1;
  overflow: hidden;
  white-space: pre;
  text-overflow: ellipsis;
  background-color: rgba(0, 0, 0, 0);
  align-self: center;
  padding-bottom: 25px;
  font-size: 12px;
  color: var(--black);
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-weight: 400;
  user-select: text;
  cursor: text;
}
.receiver-wrapper > div {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: hidden;
  align-items: stretch;
  align-self: stretch;
  justify-content: flex-end;
  padding-top: 10px;
}
.receiver-wrapper > div > div {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  flex-shrink: 1;
  overflow: hidden;
  align-items: stretch;
  justify-content: flex-end;
  /* padding-left: 130px; */
  padding-left: 30px;
  transform: translateX(0px);
}
.day_separator {
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: visible;
  align-items: stretch;
  will-change: transform;
  width: 100%;
}
.day_separator > div {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  flex-shrink: 1;
  overflow: hidden;
  align-items: center;
  align-self: stretch;
  justify-content: center;
  margin-left: 50px;
  margin-right: 50px;
  padding: 10px 0px 0px;
}
.day_separator .border-dashed {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  flex-shrink: 1;
  overflow: hidden;
  align-items: stretch;
  margin: 5px 5px 5px 0px;
  height: 1px;
  opacity: 0.4;
  border: 0.5px dashed var(--line);
}
[data-text-as-pseudo-element]::before {
  content: attr(data-text-as-pseudo-element);
  position: relative;
  display: inline;
  flex-grow: 0;
  flex-shrink: 0;
  overflow: hidden;
  white-space: nowrap;
  overflow-wrap: break-word;
  font-size: 10px;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  color: var(--line);
  font-weight: 400;
  align-self: center;
  padding: 5px 10px;
  cursor: inherit;
}
.messagebox .new_message_wrapper {
  border-radius: 6px;
  width: calc(100% - 64px);
  /* background-color: #d3d4d6;
    si le ticket est ouvert, background-color: #fff */
}

.messagebox .new_message_wrapper input,
.messagebox .new_message_wrapper textarea {
  padding-top: 0;
  padding-bottom: 0;
  font-size: 12px !important;
  min-width: 100%;
}

.messagebox .new_message_wrapper input {
  padding-top: 0;
  padding-bottom: 0;
  height: 46px !important;
  font-size: 12px !important;
}
.messagebox .new_message_wrapper textarea {
  border: 1px solid var(--line) !important;
  border-radius: 6px;
  min-height: 46px !important;
  font-size: 12px !important;
  padding: 13px 0.75rem !important;
}
@media (max-width: 479px) {
  .messagebox .new_message_wrapper textarea {
    padding: 13px 0.5rem !important;
  }
}
.messagebox .new_message_wrapper input::-webkit-input-placeholder,
.messagebox .new_message_wrapper textarea::-webkit-input-placeholder {
  /* Chrome/Opera/Safari */
  color: var(--placeholder);
  font-size: 12px;
}
.messagebox .new_message_wrapper input::-moz-placeholder,
.messagebox .new_message_wrapper textarea::-moz-placeholder {
  /* Firefox 19+ */
  color: var(--placeholder);
  font-size: 12px;
}
.messagebox .new_message_wrapper input:-ms-input-placeholder,
.messagebox .new_message_wrapper textarea:-ms-input-placeholder {
  /* IE 10+ */
  color: var(--placeholder);
  font-size: 12px;
}
.messagebox .new_message_wrapper input:-moz-placeholder,
.messagebox .new_message_wrapper textarea:-moz-placeholder {
  /* Firefox 18- */
  color: var(--placeholder);
  font-size: 12px;
}
.messagebox .btn-send-message {
  position: relative;
  display: flex;
  overflow: hidden;
  align-items: center;
  justify-content: center;
  border-width: 0px;
  padding: 8px;
  border-radius: 6px;
  min-width: 46px;
  width: 46px;
  height: 46px;
  margin-left: 16px;
  cursor: pointer;
  border-style: solid;
}
@media (max-width: 479px) {
  .messagebox .btn-send-message {
    margin-left: 8px;
  }
}
.form-wrapper {
  padding-bottom: 20px;
}
.btn-cloture {
  font-size: 12px;
  font-weight: 500;
  line-height: 16px;
  border: 1px solid var(--primary);
  color: var(--primary);
  text-transform: inherit;
  border-radius: 16px;
  height: 32px;
  margin: 0;
  min-width: 104px;
  padding: 2px 3px;
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}
@media (max-width: 479px) {
  .btn-cloture {
    right: 8px;
    min-width: 84px;
  }
}
.btn-cloture svg {
  margin-right: 3px;
}
.open {
  background-color: #f6f6f7;
}
.closed {
  background-color: #d3d4d9;
}
.back i {
  margin-right: 12px;
  vertical-align: middle;
}
</style>
