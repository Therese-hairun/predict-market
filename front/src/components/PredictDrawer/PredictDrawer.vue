<template>
  <md-app-drawer md-permanent="full">
    <md-toolbar class="md-transparent" md-elevation="0">
      <router-link to="/" class="d-flex align-items-center">
        <span class="md-title text-white">
          <img src="../../assets/images/logoBlanc.png" alt="Logo Blanc" width="34" height="38" />
          Predictmarket
        </span>
      </router-link>
    </md-toolbar>

    <md-list>
      <md-list-item v-for="(item, index) in items" :key="index"         
      >
        <router-link :to="item.href" class="w-100 d-flex">
        <span class="icon-container" v-html="item.icon"></span>
        <span class="md-list-item-text">{{item.text}}</span>
        </router-link>
      </md-list-item>
    </md-list>
  </md-app-drawer>  
</template>

<script>
export default {
  name: 'PredictDrawer',
}
</script>