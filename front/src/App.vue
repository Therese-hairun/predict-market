<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "App",
  components: {},
  created() {
    document.title = "Predict Market";
  },
};
</script>
<style>
.pdf-preview > iframe {
  height: 100% !important;
}
</style>
