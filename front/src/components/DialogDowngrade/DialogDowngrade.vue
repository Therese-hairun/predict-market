<template>
  <div>
    <md-dialog
      :md-active.sync="showDialogData"
      class="predict-dialog"
      :md-click-outside-to-close="false"
    >
      <div
        class="dialog-name px-3 text-white d-flex justify-content-between align-items-center"
        :class="!btnClose && 'py-3'"
      >
        {{ $t("keep:message") }}
        <md-button
          class="btn-close px-0 mx-0"
          v-if="btnClose"
          :md-ripple="false"
          v-on:click="(showDialogData = false), $emit('close')"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="14"
            height="14"
            viewBox="0 0 14 14"
          >
            <path
              id="Tracé_2542"
              data-name="Tracé 2542"
              d="M19,6.41,17.59,5,12,10.59,6.41,5,5,6.41,10.59,12,5,17.59,6.41,19,12,13.41,17.59,19,19,17.59,13.41,12Z"
              transform="translate(-5 -5)"
              fill="#fff"
            />
          </svg>
        </md-button>
      </div>
      <md-content class="content-dialog">
        <slot></slot>
        <span class="error">{{ errorToMuchCouple }}</span>
        <div
          class="text-center pt-4"
          style="width: 312px;"
          v-for="(item, index) in listUserCouple"
          :key="index"
        >
          <div class="d-flex align-items-center justify-content-between mb-2">
            <div
              class="crypto-item-title d-flex flex-column align-items-start justify-content-center"
            >
              {{ item.fullName }}
              <span class="crypto-sigle text-uppercase text-left">{{
                item.symbol
              }}</span>
            </div>
            <md-checkbox
              class="mr-0 ml-1"
              v-model="arraySymbol"
              :value="item.id"
            ></md-checkbox>
          </div>
        </div>
        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="keepCouple()"
            :disabled="disableButton"
          >
            {{ $t("keep") }}
          </md-button>
        </div>
      </md-content>
    </md-dialog>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Dialog",
  props: {
    showDialog: { type: Boolean },
  },
  components: {},
  data: () => ({
    rememberMe: false,
    showDialogData: false,
    btnClose: false,
    listUserCouple: [],
    arraySymbol: [],
    downgradeFinished: null,
    userSubscriptionId: null,
    numberCoupleOffered: null,
    disableButton: true,
    errorToMuchCouple: "",
    iconDialog: `
          <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
            <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
            <g id="Groupe_14044" data-name="Groupe 14044" transform="translate(7.629 7.705)">
              <path id="Tracé_19671" data-name="Tracé 19671" d="M162.639,159.613c-.275.33-.533.678-.829.989q-11.931,12.529-23.869,25.051c-.421.441-.864.832-1.531.57a1.752,1.752,0,0,1-.578-.384q-5.724-5.708-11.435-11.43a1.188,1.188,0,0,1-.324-1.459,1.086,1.086,0,0,1,1.252-.616,1.949,1.949,0,0,1,.833.51q5.108,5.078,10.193,10.179c.129.129.264.251.35.333.38-.348.757-.656,1.091-1.005q11.327-11.852,22.646-23.712a1.218,1.218,0,0,1,1.846-.205,3.765,3.765,0,0,1,.355.474Z" transform="translate(-104.921 -133.831)" fill="#f8bd25"/>
              <path id="Tracé_19672" data-name="Tracé 19672" d="M38.362,76.742q-1.469,0-2.941-.112A38.363,38.363,0,1,1,69.557,60.736a1.5,1.5,0,1,1-2.434-1.75,35.373,35.373,0,1,0-8.136,8.137,1.5,1.5,0,1,1,1.749,2.434A38.365,38.365,0,0,1,38.362,76.742Z" transform="translate(0 0)" fill="#242c36"/>
              <path id="Tracé_19673" data-name="Tracé 19673" d="M411.609,413.108a1.5,1.5,0,1,1,1.06-.439A1.51,1.51,0,0,1,411.609,413.108Z" transform="translate(-347.165 -347.165)" fill="#242c36"/>
            </g>
          </svg>
        `,
  }),
  methods: {
    getSubscriptionById: async function() {
      if (this.userSubscriptionId !== undefined) {
        try {
          await this.$store.dispatch("getSubscriptionById", {
            id: this.userSubscriptionId,
            token: localStorage.getItem("token"),
          });
          this.numberCoupleOffered = this.getSubscription.number_couple_offered;
        } catch (e) {
          //
        }
      }
    },
    getUserCouple: async function() {
      try {
        await this.$store.dispatch("getUserCouple", {
          token: localStorage.getItem("token"),
        });
        this.listUserCouple = this.userCouple.data;
        this.nbrUserCouple = this.listUserCouple.length;
      } catch (e) {
        //
      } finally {
        this.loading = false;
      }
    },
    checkDowngradeStatus: async function() {
      try {
        await this.$store.dispatch("checkDowngrade", {
          token: localStorage.getItem("token"),
        });
        this.showDialogData = this.checkDowngrade.status;
        this.userSubscriptionId = this.checkDowngrade.subscribe;
      } catch (e) {
        //
      }
    },
    async keepCouple() {
      const payload = {
        couple: this.arraySymbol,
      };
      try {
        await this.$store.dispatch("downgrade", {
          payload: payload,
          token: localStorage.getItem("token"),
        });
        this.showDialogData = false;
        this.showDialog(false);
      } catch (e) {
        //
      }
    },
  },
  computed: {
    ...mapGetters(["userCouple", "checkDowngrade"]),
    getSubscription() {
      return this.$store.state.subscription.subscriptionId.data;
    },
  },
  async mounted() {
    await this.checkDowngradeStatus();
    await this.getSubscriptionById();
    await this.getUserCouple();
  },
  watch: {
    arraySymbol(val) {
      this.errorToMuchCouple = "";
      this.disableButton = val.length ? false : true;
      if (val.length > this.numberCoupleOffered) {
        this.disableButton = true;
        this.errorToMuchCouple = `${this.$t("chooseOnly")} ${
          this.numberCoupleOffered
        } ${this.$t("couple")}`;
      }
    },
    showDialog: function(value) {
      this.showDialogData = value;
    },
  },
};
</script>

<style scoped>
.titre-dialog {
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;
  font-size: 24px;
  letter-spacing: 0.075px;
  padding-top: 0;
}
.content-dialog {
  padding: 0px 24px;
  overflow: auto;
}
@media (max-width: 479px) {
  .content-dialog {
    padding: 0 12px;
  }
}
.dialog-name {
  background-color: var(--black);
}
.dialog-name .btn-close {
  min-width: auto;
}
</style>
