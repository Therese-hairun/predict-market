<template lang="">
  <md-menu class="switch-langue" id="usermenu" md-size="small" md-align-trigger>
    <md-button md-menu-trigger>
      <b-list-group class="list-group">
        <b-list-group-item
          class="list-group-item align-items-center bg-transparent "
        >
          <div
            v-if="this.$i18n.locale == 'en'"
            class="tooltip-item"
            v-on:click="selectLanguage()"
            id="tooltip-target-1"
          >
            <img width="30" src="../../../public/fr.jpg" alt="En" />
          </div>

          <div
            v-if="this.$i18n.locale == 'fr'"
            class="tooltip-item"
            v-on:click="selectLanguage()"
            id="tooltip-target-1"
          >
            <img width="30" src="../../../public/en.jpg" alt="Fr" />
          </div>
        </b-list-group-item>
        <b-tooltip
          target="tooltip-target-1"
          triggers="hover"
          placement="bottom"
        >
          {{ $t("changeLang") }}
        </b-tooltip>
      </b-list-group>
    </md-button>
  </md-menu>
</template>

<script>
export default {
  data() {
    return { langs: ["fr", "en"], langue: "fr" };
  },
  methods: {
    selectLanguage() {
      if (this.$i18n.locale == "fr") {
        this.$i18n.locale = "en";
        localStorage.setItem("language", this.$i18n.locale);
        //vm.$material.selectLocale
        this.$material.selectLocale("en-US");
      } else {
        this.$i18n.locale = "fr";
        localStorage.setItem("language", this.$i18n.locale);
        this.$material.selectLocale("fr");
      }
    },
  },
};
</script>

<style>
.switch-langue {
  display: flex;
  justify-content: flex-end;
  margin-right: 8px;
}
.switch-langue .md-button {
  border: none;
  justify-content: flex-start;
  margin-left: auto;
  min-width: 50px;
  padding: 0;
}
.switch-langue .list-group {
  position: relative;
}
.switch-langue .list-group {
  height: 100%;
}
.switch-langue .list-group .list-group-item {
  height: 100%;
  padding: 0;
  border: none;
}
.switch-langue .md-button-content {
  height: 36px;
}
.switch-langue .tooltip-item {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}

.locale-changer {
  margin-right: 20px;
}
@media (max-width: 639px) {
  .locale-changer {
    margin-right: 10px;
  }
}

.locale-changer .md-field {
  margin-bottom: 0;
  margin-top: 0;
  min-height: 36px;
  max-width: 80px;
  padding-top: 0;
}
.locale-changer .md-field input {
  padding-bottom: 8px !important;
  padding-top: 8px !important;
  text-transform: uppercase;
}
.selectLangue-field-item {
  text-transform: uppercase;
}
.md-select-menu .language-item .md-list-item-container {
  text-transform: uppercase;
  font-weight: 500;
}
.md-select-menu .language-item .md-list-item-content {
  min-height: 30px;
}
</style>
