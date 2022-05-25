<template lang="">
  <div class="crypto-list d-flex flex-wrap">
    <div
      class="crypto-item w-100 position-relative"
      v-for="(item, index) in listCoupleCrypto"
      :key="index"
    >
      <CoupleCryptoItem :item="item" v-on:refresh="refresh"></CoupleCryptoItem>
    </div>
  </div>
</template>

<script>
import CoupleCryptoItem from "../CoupleCryptoItem/CoupleCryptoItem.vue";

export default {
  name: "CoupleCryptoItemList",
  props: {
    listCoupleCrypto: [],
  },
  data: () => {
    return {
      isActive: false,
    };
  },
  methods: {
    toggleActive() {
      this.isActive = !this.isActive;
    },
    refresh() {
      this.$emit("refresh");
    },
  },
  components: {
    CoupleCryptoItem,
  },
};
</script>

<style scoped>
.crypto-list {
  margin-left: -6.5px;
  margin-right: -6.5px;
}
.crypto-item {
  margin-top: 10px;
  margin-bottom: 10px;
  padding-left: 6.5px;
  padding-right: 6.5px;
  flex: 1 0 33.3%;
  max-width: 33.3%;
}
@media (max-width: 639px) {
  .crypto-item {
    flex: 1 0 100%;
    max-width: 100%;
  }
}

@media (min-width: 640px) and (max-width: 960px) {
  .crypto-item {
    flex: 1 0 50%;
    max-width: 50%;
  }
}
@media (min-width: 1200px) {
  .crypto-item {
    flex: 1 0 33%;
    max-width: 33%;
    min-width: 157px;
  }
}
@media (min-width: 1401px) {
  .crypto-item {
    flex: 1 0 50%;
    max-width: 50%;
  }
}
@media (min-width: 1200px) and (max-width: 1401px) {
  .crypto-item {
    flex: 1 0 50%;
    max-width: 50%;
  }
}
@media (max-width: 639px) {
  .crypto-item:last-child {
    
  }
}
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
}
.crypto-btn-ajouter:hover {
  background-color: #f6f6f7;
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
