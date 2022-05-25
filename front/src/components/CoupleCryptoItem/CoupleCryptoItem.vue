<template lang="">
  <div class="h-100">
    <md-card
      class="crypto-card d-flex flex-column align-items-center m-0 w-100 h-100"
    >
      <md-card-media class="cryto-item-md-card-media">
        <span
          class="b-avatar cryto-item-b-avatar bg-white cryto-item-big-avatar badge-secondary rounded-circle"
          style="width: 86px; height: 86px;"
        >
          <span class="b-avatar-custom">
            <span class="b-avatar-img">
              <img
                :src="item.symbol_1_logo ? item.symbol_1_logo : null"
                alt="logo_1"
              />
            </span>
          </span>
        </span>
        <span
          class="b-avatar cryto-item-b-avatar bg-white cryto-item-avatar badge-secondary rounded-circle"
          style="width: 53px; height: 53px;"
        >
          <span class="b-avatar-custom">
            <span class="b-avatar-img">
              <img
                :src="item.symbol_2_logo ? item.symbol_2_logo : null"
                alt="logo_2"
              />
            </span>
          </span>
        </span>
      </md-card-media>

      <md-card-header class="px-0">
        <div
          class="crypto-item-title d-flex flex-column align-items-center justify-content-center"
        >
          {{ item.couple ? item.couple : item.symbol }}
          <span class="crypto-sigle text-uppercase text-center">{{
            item.fullName
          }}</span>
        </div>
      </md-card-header>

      <md-card-content class="crypto-content">
        <div class="crypto-status">
          <span class="increase" v-if="item.h24 >= 0">
            <svg class="Trac_19695" width="20" height="12" viewBox="2 6 20 12">
              <path
                id="Trac_19695"
                d="M 16 6 L 18.29000091552734 8.289999961853027 L 13.41000080108643 13.17000007629395 L 9.410000801086426 9.170000076293945 L 2 16.59000015258789 L 3.410000085830688 18 L 9.409999847412109 12 L 13.40999984741211 16 L 19.70999908447266 9.710000038146973 L 22 12 L 22 6 L 16 6 Z"
              ></path>
            </svg>
            {{ pointToComma(item.h24) }}%
            <b-badge class="status-badge bg-transparent position-absolute">{{
              $t("now")
            }}</b-badge>
          </span>
          <span class="decrease" v-if="item.h24 < 0">
            <svg class="Trac_19693" width="20" height="12" viewBox="2 6 20 12">
              <path
                id="Trac_19693"
                d="M 16 18 L 18.29000091552734 15.71000003814697 L 13.41000080108643 10.82999992370605 L 9.410000801086426 14.82999992370605 L 2 7.409999847412109 L 3.410000085830688 6 L 9.409999847412109 12 L 13.40999984741211 8 L 19.70999908447266 14.28999996185303 L 22 12 L 22 18 L 16 18 Z"
              ></path>
            </svg>
            {{ pointToComma(item.h24) }}%
            <b-badge class="status-badge bg-transparent position-absolute">{{
              $t("now")
            }}</b-badge>
          </span>
        </div>
      </md-card-content>
      <div v-if="activateSubscription" class="w-100">
        <md-card-actions class="w-100 p-0 mt-auto " v-if="!item.owned">
          <md-button
            class="crypto-btn-ajouter d-flex align-items-center justify-content-center w-100"
            @click="getACouple(item.coupleId ? item.coupleId : item.id)"
            >{{ $t("add") }}</md-button
          >
        </md-card-actions>
        <md-card-actions class="w-100 p-0" v-else>
          <md-button
            class="crypto-btn-ajouter d-flex align-items-center justify-content-center w-100"
            @click="removeCouple(item.coupleId ? item.coupleId : item.id)"
            >{{ $t("remove") }}</md-button
          >
          <md-button
            class="crypto-btn-ajouter d-flex align-items-center justify-content-center w-100 added"
            @click="shareData(item.symbol)"
          >
            {{ $t("visualize") }}
          </md-button>
        </md-card-actions>

        <md-card-actions class="add-favoris-wrapper position-absolute">
          <md-button
            class="add-favoris w-100"
            v-bind:class="{ active: false }"
            v-if="!item.favorite"
            @click="addFavorite(item.symbol)"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="13.75"
              height="11.634"
              viewBox="0 0 13.75 11.634"
            >
              <path
                id="Path"
                d="M6.375,10.5,6.2,10.362C5.861,10.1,5.4,9.81,4.877,9.478,2.818,8.183,0,6.41,0,3.387A3.5,3.5,0,0,1,3.6,0,3.69,3.69,0,0,1,6.375,1.224,3.69,3.69,0,0,1,9.147,0a3.5,3.5,0,0,1,3.6,3.387c0,3.023-2.818,4.8-4.877,6.091-.528.332-.984.619-1.321.883Z"
                transform="translate(0.5 0.5)"
                fill="none"
                stroke="#242c36"
                stroke-width="1"
              />
            </svg>
          </md-button>
          <md-button
            class="add-favoris w-100"
            v-bind:class="{ active: true }"
            @click="deleteFavorite(item.symbol)"
            v-else
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="13.75"
              height="11.634"
              viewBox="0 0 13.75 11.634"
            >
              <path
                id="Path"
                d="M6.375,10.5,6.2,10.362C5.861,10.1,5.4,9.81,4.877,9.478,2.818,8.183,0,6.41,0,3.387A3.5,3.5,0,0,1,3.6,0,3.69,3.69,0,0,1,6.375,1.224,3.69,3.69,0,0,1,9.147,0a3.5,3.5,0,0,1,3.6,3.387c0,3.023-2.818,4.8-4.877,6.091-.528.332-.984.619-1.321.883Z"
                transform="translate(0.5 0.5)"
                fill="none"
                stroke="#242c36"
                stroke-width="1"
              />
            </svg>
          </md-button>
        </md-card-actions>
      </div>
    </md-card>
    <Dialog
      :showDialog="showDialog"
      :titreDialog="$t('warning')"
      :iconDialog="iconDialog"
      @close="showDialog = !showDialog"
    >
      <p class="text-center" v-html="errorCouplePopUp">
        {{ errorCouplePopUp }}
      </p>

      <div
        class="w-100 row-fluid d-flex flex-column flex-sm-row align-items-center justify-content-between rememberMe-wrapper"
      >
        <form action="" class="w-100">
          <!-- <md-checkbox id="show" name="show" v-model="rememberMe"
            >Ne plus faire apparaître ce message.</md-checkbox
          > -->
          <div class="w-100 text-center">
            <md-button
              type="submit"
              class="submit-dialog text-center btn-submit text-center w-100"
              @click="showDialog = false"
            >
              {{ $t("continue") }}
            </md-button>
          </div>
        </form>
      </div>
    </Dialog>
  </div>
</template>

<script>
import Dialog from "../../components/Dialog/Dialog.vue";

export default {
  name: "CoupleCryptoItem",
  props: {
    item: [],
  },
  data: () => {
    return {
      isActive: false,
      isAdded: false,
      showDialog: false,
      rememberMe: false,
      iconDialog: `
          <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
            <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
            <g id="Groupe_53071" data-name="Groupe 53071" transform="translate(-37.371 -57.653)">
              <g id="Groupe_53075" data-name="Groupe 53075">
                <path id="Tracé_42545" data-name="Tracé 42545" d="M45,129.664q7.829-13.7,15.662-27.4,8.411-14.638,16.884-29.241A6.476,6.476,0,0,1,86.3,70.229a6.342,6.342,0,0,1,2.615,2.514q6.548,11.339,13.1,22.677a1.557,1.557,0,0,1-.374,2.3c-.79.479-1.646.167-2.241-.822-.116-.193-.224-.391-.337-.586Q92.982,85.789,86.9,75.263a12.637,12.637,0,0,0-.886-1.39,3.385,3.385,0,0,0-5.428,0,8.441,8.441,0,0,0-.613.942q-15.686,27.16-31.368,54.323c-1.158,2.007-.912,3.953.791,5.02a4.717,4.717,0,0,0,2.332.61c3.78.063,7.561.033,11.342.033q25.8,0,51.6.008a3.836,3.836,0,0,0,3.189-1.172,3.479,3.479,0,0,0,.213-4.378q-3.35-5.821-6.714-11.633-2.833-4.906-5.665-9.812a3.649,3.649,0,0,1-.332-.75,1.462,1.462,0,0,1,2.447-1.444,3.4,3.4,0,0,1,.478.669q6.248,10.818,12.484,21.644a6.46,6.46,0,0,1-2.037,8.9,6.658,6.658,0,0,1-3.716.982c-3.706-.014-7.411,0-11.117,0q-26.027,0-52.054.008a6.538,6.538,0,0,1-6.022-3.1,15.884,15.884,0,0,1-.83-1.752Z" fill="#242c36"/>
                <path id="Tracé_42546" data-name="Tracé 42546" d="M232.582,199.652c0,2.227.037,4.454-.008,6.68a4.769,4.769,0,0,1-7.27,4.148,4.473,4.473,0,0,1-2.311-3.967c-.046-4.628-.069-9.257.006-13.884a4.707,4.707,0,0,1,4.8-4.586,4.8,4.8,0,0,1,4.781,4.78c.036,1.15.011,2.3.011,3.452q0,1.689,0,3.377Zm-3-.042c0-2.2.016-4.4-.007-6.607a1.8,1.8,0,1,0-3.591.005c-.017,4.4-.028,8.809.023,13.213a2.606,2.606,0,0,0,.663,1.507,1.486,1.486,0,0,0,1.8.294,1.822,1.822,0,0,0,1.105-1.806C229.584,204.014,229.579,201.812,229.579,199.61Z" transform="translate(-144.468 -96.251)" fill="#f8bd25"/>
                <path id="Tracé_42547" data-name="Tracé 42547" d="M227.891,339.875a4.8,4.8,0,1,1,4.778-4.784A4.853,4.853,0,0,1,227.891,339.875Zm-.025-3.011a1.791,1.791,0,1,0-1.789-1.773A1.851,1.851,0,0,0,227.866,336.864Z" transform="translate(-144.558 -211.717)" fill="#f8bd25"/>
                <path id="Tracé_42548" data-name="Tracé 42548" d="M352.943,235.021a1.474,1.474,0,1,1-.026,2.948,1.474,1.474,0,0,1,.026-2.948Z" transform="translate(-248.795 -134.391)" fill="#242c36"/>
              </g>
            </g>
          </svg>
        `,
      errorCouplePopUp: "",
      activateSubscription: false,
    };
  },
  computed: {
    client() {
      return this.$store.state.client.clients;
    },
  },
  async mounted() {
    await this.getUserSubscription();
  },
  methods: {
    getUserSubscription: async function() {
      try {
        await this.$store.dispatch("loadClients", {
          token: localStorage.getItem("token"),
        });
        this.activateSubscription = this.$store.state.client.clients.subscription.activate;
      } catch (e) {
       //
      }
    },
    shareData(symbol) {
      this.countViewCouple(symbol);
      this.$router.push({
        name: "VisualiserCrypto",
        params: { symbol: symbol.replace("/", "_") },
      });
    },
    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
    toggleAdded() {
      this.isAdded = true;
      this.showDialog = !this.showDialog;
    },
    toReplace(item) {
      return item.replace("/", "_");
    },
    countViewCouple: async function(symbol) {
      try {
        await this.$store.dispatch("countViewCouple", {
          symbol,
          token: localStorage.getItem("token"),
        });
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
      }
    },
    deleteFavorite: async function(symbol) {
      this.loader = true;
      try {
        await this.$store.dispatch("deleteFavorite", {
          token: localStorage.getItem("token"),
          symbol,
        });
        this.$emit("refresh");
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
      } finally {
        this.loader = false;
      }
    },
    addFavorite: async function(item) {
      this.loader = true;
      const payload = {
        couple: item,
      };
      try {
        await this.$store.dispatch("addFavorite", {
          token: localStorage.getItem("token"),
          payload,
        });
        this.$emit("refresh");
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
      } finally {
        this.loader = false;
      }
    },
    removeCouple: async function(item) {
      const payload = {
        couple: item,
      };
      try {
        await this.$store.dispatch("removeCouple", {
          token: localStorage.getItem("token"),
          payload,
        });
        this.$emit("refresh");
      } catch (e) {
        this.errorCouplePopUp = this.$t("removeCoupleMessage");
        this.toggleAdded();
      }
    },
    getACouple: async function(item) {
      let temp = [];
      temp.push(item);
      const payload = {
        couple: temp,
      };
      try {
        this.loader = true;
        await this.$store.dispatch("getACouple", {
          token: localStorage.getItem("token"),
          payload,
        });
        this.$emit("refresh");
      } catch (e) {
        this.errorCouplePopUp = this.$t("errorExceeded");
        this.toggleAdded();
      } finally {
        this.loader = false;
      }
    },
  },
  components: {
    Dialog,
  },
};
</script>

<style scoped>
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
.crypto-status {
  font-size: 16px;
}
.crypto-status .increase,
.crypto-status .increase path {
  color: #21a179;
  fill: #21a179;
}
.crypto-status .decrease,
.crypto-status .decrease path {
  color: var(--rouge);
  fill: var(--rouge);
}
.crypto-status .status-badge {
  color: var(--placeholder);
  font-size: 8px;
}
.crypto-item-title {
  font-size: 14px;
  color: var(--black);
}
.crypto-sigle {
  color: #5c626a;
  font-size: 12px;
  letter-spacing: 0.1px;
  line-height: 18px;
  width: 100%;
}
.crypto-btn-ajouter {
  border: 1px solid #5c626a;
  border-radius: 16px;
  color: #5c626a !important;
  font-size: 12px;
  line-height: 16px;
  text-transform: inherit;
  height: 32px;
  min-width: auto;
}
.crypto-btn-ajouter.added {
  border: 1px solid var(--primary);
  background-color: var(--primary);
  color: #fff !important;
}
.crypto-btn-ajouter:hover {
  background-color: #f6f6f7;
}
.crypto-btn-ajouter.added:hover {
  background-color: #f8bd25;
}
.crypto-btn-ajouter.added a {
  color: #fff !important;
  text-decoration: none !important;
}

.add-favoris-wrapper {
  width: fit-content !important;
  right: 0;
  top: 0;
  padding: 0;
}
.add-favoris {
  min-width: 36px;
}
.add-favoris::before {
  display: none;
}
.add-favoris:hover path {
  fill: #d3d4d6;
}
.add-favoris.active path {
  fill: #242c36;
}
</style>
