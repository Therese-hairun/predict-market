<template>
  <div>
    <md-dialog
      :md-active.sync="showDialogData"
      class="predict-dialog"
      :md-click-outside-to-close="false"
    >
      <div
        v-if="dialogName"
        class="dialog-name px-3 text-white d-flex justify-content-between align-items-center"
        :class="!btnClose && 'py-3'"
      >
        {{ dialogName }}
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
      <md-dialog-title
        v-if="titreDialog"
        class="titre-dialog d-flex flex-column justify-content-center align-items-center"
      >
        <span
          class="mt-3 mb-4"
          :v-if="iconDialog"
          v-html="iconDialog"
          style="margin-bottom: 10px;"
        >
        </span>
        {{ titreDialog }}
      </md-dialog-title>

      <md-content class="content-dialog">
        <slot></slot>
      </md-content>
    </md-dialog>
  </div>
</template>

<script>
export default {
  name: "Dialog",
  props: {
    showDialog: { type: Boolean },
    titreDialog: { type: String },
    iconDialog: { type: String },
    dialogName: { type: String },
    btnClose: { type: Boolean, required: false, default: true }
  },
  components: {},
  data: () => ({
    rememberMe: false,
    showDialogData: false,
  }),
  watch: {
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
@media (max-width: 479px){
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
