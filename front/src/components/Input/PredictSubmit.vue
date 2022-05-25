<template>
  <div>
    <button
      class="btn-submit text-center w-100 py-0"
      type="submit"
      v-bind:disabled="disabled"
    >
    <div class="text-wrapper">
      {{ $t(label) }}
    </div>
    </button>
  </div>
</template>

<script>
export default {
  name: "PredictSubmit",
  props: {
    label: { type: String },
    disabled: { type: Boolean },
  },
};
</script>
