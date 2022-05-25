<template>
  <div class="dashboard">
    <PermanentFull
      :titre="$t('subscription')"
      :icon="icon"
      :menuItems="menuItems"
    >
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div id="abonnement" class="dashboard-border bloc-content mx-0">
          <div
            class="titre-wrapper d-flex flex-column justify-content-center align-items-center"
          >
            <h2 class="titre">{{ $t("subscribe:Plan") }}</h2>
            <p class="description">
              {{ $t("subscribe:Intro") }}
            </p>
          </div>
          <div class="content-wrapper text-center mx-auto">
            <div
              class="select-choice d-flex align-items-center dashboard-border px-3 m-auto"
            >
              <span :class="{ active: !isActive }">{{ $t("monthly") }}</span>
              <md-switch
                class="table-switch mx-3"
                v-model="isActive"
              ></md-switch>
              <span :class="{ active: isActive }">{{ $t("annual") }}</span>
            </div>
            <div class="content mt-4">
              <ul class="liste-abonnement list-unstyled">
                <li
                  class="item"
                  v-for="(item, index) in subscriptionSorted"
                  :key="index"
                >
                  <AbonnementItem
                    :nom="item.name"
                    :discountPrix="item.discountPrice"
                    :discountSaved="item.discountSaved"
                    :pourcentage="item.reduction"
                    :price="item.price"
                    :recommande="item.recommanded"
                    :mensuelAnnuel="isActive"
                    :is_active="isActive"
                    :typeId="item.id"
                    :idUserSubscription="idSubscribe ? idSubscribe : 0"
                  >
                    <div class="d-flex">
                      <span class="mr-1" v-html="iconCheck"></span>
                      {{
                        !item.number_couple_offered
                          ? $t("allPair")
                          : item.number_couple_offered + $t("pairChoice")
                      }}
                    </div>
                    <div class="d-flex">
                      <span class="mr-1" v-html="iconCheck"></span>
                      {{
                        !isActive ? $t("noEngagement") : $t("withEngagement")
                      }}
                    </div>
                  </AbonnementItem>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import MenuUser from "../../data/MenuUser.js";
import AbonnementItem from "../Abonnement/AbonnementItem.vue";

export default {
  components: {
    PermanentFull,
    AbonnementItem,
  },
  props: {
    typeAbonnement: String,
    dateExpiration: String,
    emplacementDispo: String,
    titreAbonnement: String,
    iconAbonnement: String,
  },
  watch: {
    isActive() {
      this.subscriptionSorted = this.handleSortSubscription();
    },
  },
  methods: {
    loadSubscriptions: async function() {
      await this.$store.dispatch("loadSubscriptions", {
        token: localStorage.getItem("token"),
        order: "price",
        page: "",
        search: "",
        size: "",
      });
      this.subscriptions = this.$store.state.subscription.subscriptions;
      this.subscriptionsFilter = this.subscriptions.filter(
        (data) => data.is_active
      );
      this.subscriptionSorted = this.handleSortSubscription();
    },
    upgradeListSubscription: async function() {
      await this.$store.dispatch("upgradeListSubscription", {
        token: localStorage.getItem("token"),
        id: this.idSubscribe,
      });
      this.subscriptions = this.$store.state.subscription.upgradeSubscriptions;

      this.subscriptionsFilter = this.subscriptions.filter(
        (data) => data.is_active
      );
      this.subscriptionSorted = this.handleSortSubscription();
    },

    handleSortSubscription() {
      const subscriptionPriceYear = JSON.parse(
        JSON.stringify(this.subscriptionsFilter)
      );
      subscriptionPriceYear.map((item) => {
        item.discountPrice = item.price;
        item.price = this.getMonthlyPrice(item.price, item.reduction);
        item.discountSaved = this.getSavedMoney(item.price, item.reduction);
      });
      subscriptionPriceYear.sort((item1, item2) => item1.price - item2.price);

      const subscriptionPriceMonth = JSON.parse(
        JSON.stringify(this.subscriptionsFilter)
      );
      subscriptionPriceMonth.map((item) => {
        item.discountPrice = item.price;
        item.discountSaved = this.getSavedMoney(item.price, item.reduction);
      });

      return this.isActive ? subscriptionPriceYear : subscriptionPriceMonth;
    },
    getMonthlyPrice: function(price, reduction) {
      const pa = +price * 12;
      const r = pa * (+reduction / 100);
      return +((pa - r) / 12).toFixed(2);
    },
    getSavedMoney: function(price, reduction) {
      price = price / (1 - reduction / 100);
      const pa = +price * 12;
      const r = (price - (price * reduction) / 100) * 12;
      return +(pa - r).toFixed(2);
    },
    loadClient: async function() {
      try {
        await this.$store.dispatch("loadClients", {
          token: localStorage.getItem("token"),
        });
        this.clientId = this.$store.state.client.clients.id;
        this.idSubscribe = +this.$store.state.client.clients.subscription.id;
      } catch (e) {
        //
      }
    },
  },
  data: () => {
    return {
      subscriptionsFilter: null,
      subscriptionSorted: null,
      clientId: 0,
      subscriptions: {},
      icon: `
        <svg id="space_dashboard_black_24dp" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36">
          <rect id="Rectangle_1872" data-name="Rectangle 1872" width="36" height="36" fill="none"/>
          <path id="Tracé_19674" data-name="Tracé 19674" d="M15,30H6a3.009,3.009,0,0,1-3-3V6A3.009,3.009,0,0,1,6,3h9Zm3,0h9a3.009,3.009,0,0,0,3-3V16.5H18ZM30,13.5V6a3.009,3.009,0,0,0-3-3H18V13.5Z" transform="translate(1.5 1.5)" fill="#242c36"/>
          <path id="Tracé_19683" data-name="Tracé 19683" d="M15,30H6a3.009,3.009,0,0,1-3-3V6A3.009,3.009,0,0,1,6,3h9Zm3,0h9a3.009,3.009,0,0,0,3-3V16.5H18ZM30,13.5V6a3.009,3.009,0,0,0-3-3H18V13.5Z" transform="translate(1.5 1.5)" fill="#242c36"/>
        </svg>
      `,
      menuItems: MenuUser,
      isActive: true,
      iconCheck: `
        <svg id="done_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <path id="Tracé_42162" data-name="Tracé 42162" d="M0,0H24V24H0Z" fill="none"/>
          <path id="Tracé_42163" data-name="Tracé 42163" d="M9,16.2,4.8,12,3.4,13.4,9,19,21,7,19.6,5.6Z" fill="#21a179"/>
        </svg>
      `,
      idSubscribe: "",
      client: Object,
    };
  },
  async mounted() {
    await this.loadClient();
    if (localStorage.getItem("upgrade") == "1")
      await this.upgradeListSubscription();
    else await this.loadSubscriptions();
  },
};
</script>

<style scoped>
#abonnement {
  padding: 20px;
}
#abonnement .titre-wrapper .titre {
  color: var(--black);
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;
  font-size: 24px;
  letter-spacing: 0.18px;
  line-height: 24px;
}
#abonnement .content-wrapper {
  max-width: 1027.5px;
}
#abonnement .select-choice {
  letter-spacing: 0.25px;
  line-height: 20px;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 14px;
  color: var(--placeholder);
  max-width: fit-content;
}
#abonnement .select-choice .active {
  color: var(--black);
}

#abonnement .liste-abonnement {
  width: calc(100% + 20px);
  margin-left: -20px;
  margin-bottom: 0;
}
#abonnement .liste-abonnement .item {
  padding-left: 20px;
  display: inline-block;
  vertical-align: middle;
  width: calc(25% - 20px);
  min-width: 220px;
}
@media (min-width: 480px) {
  #abonnement .liste-abonnement .item {
    min-width: 241px;
  }
}
</style>
