<template lang="">
  <div id="couple-crypto" class="flex-grow-1">
    <md-tabs class="h-100">
      <template slot="md-tab" slot-scope="{ tab }">
        <div class="d-flex tab-item text-initial">
          <span v-html="tab.icon" class="mr-1"></span> {{ tab.label }}
        </div>
      </template>
      <md-tab
        class="h-100"
        v-for="(item, index) in data"
        :key="index"
        :md-label="item.titre"
        :md-icon="item.icon"
      >
        <CoupleCryptoItemList
          v-if="item.listing.length"
          v-on:refresh="refresh"
          :listCoupleCrypto="item.listing"
        ></CoupleCryptoItemList>

        <div
          v-else
          class="couple-vide h-100 d-flex flex-column justify-content-center"
        >
          <span v-html="item.iconVide" class="icon-vide text-center"></span>
          <span
            v-html="item.titremessageVide"
            class="titre-message-vide text-center"
          ></span>
          <span
            v-html="item.messageVide"
            class="message-vide text-center"
          ></span>
        </div>
      </md-tab>
    </md-tabs>
  </div>
</template>

<script>
import CoupleCryptoItemList from "../CoupleCryptoItemList/CoupleCryptoItemList.vue";

export default {
  name: "CoupleCrypto",
  data: () => {
    return {};
  },
  methods: {
    refresh() {
      this.$emit("refresh");
    },
  },
  props: {
    data: [],
  },
  components: {
    CoupleCryptoItemList,
  },
};
</script>

<style scoped>
#couple-crypto .tab-item {
  height: auto;
  color: var(--placeholder);
  font-size: 16px;
}
@media (max-width: 560px) {
  #couple-crypto .tab-item {
    font-size: 12px;
  }
}
#couple-crypto .md-tabs-content .couple-vide  {
  max-width: 360px;
  margin: 0 auto;
}
#couple-crypto .md-tabs-content .couple-vide .icon-vide {
  margin-bottom: 36px;
}
#couple-crypto .md-tabs-content .couple-vide .message-vide {
  font-size: 12px;
  line-height: 18px;
  color: #5c626a;
}
#couple-crypto .md-tabs-content .couple-vide .titre-message-vide {
  font-size: 20px;
  line-height: 24px;
  color: var(--black);
  width: 100%;
}
</style>
