<template lang="">
  <div class="form-group">
    <label
      v-if="label"
      v-html="label"
    ></label>
    <div class="d-flex align-items-center input-number">
      <md-button class="md-icon-button icon-action remove" v-on:click="count--" v-bind:disabled="count<1">
        <md-icon>remove</md-icon>
      </md-button>      
      <div class="input-wrapper flex-grow-1 d-flex align-items-center justify-content-center">
          <input type="number" pattern="/^-?\d+\.?\d*$/" :onKeyPress="handleMaxLength(count, numberLength)" v-model.number="count" class="border-0 rounded-0 text-center px-0" >{{unite}}
      </div>
      <md-button class="md-icon-button icon-action add" v-on:click="count++">
        <md-icon>add</md-icon>
      </md-button>      
    </div>
  </div>
</template>

<script>
export default {
  name: "PredictInputNumber",
  props: ['value', 'unite', 'label', 'numberLength'],
  computed: {
    count: {
      get() { return this.value },
      set(newValue) { this.$emit('input', newValue) }
    }
  },
  methods:{
    handleMaxLength(value, numberLength) {
      if (value.toString().length === parseInt(numberLength)) 
        return `return false`;
      else
        return `return event.charCode >= 48 && event.charCode <= 57`;
    }
  }
};
</script>

<style>
  .input-number{
    border: 1px solid var(--line);
    border-radius: 4px;
  }
  .input-number .input-wrapper{
    border-right: 1px solid var(--line) !important;
    border-left: 1px solid var(--line) !important;
    width: auto !important;
  }
  .input-number input{
    max-width: 50px;
  }
  .input-number input:focus{
    outline: 0;
  }

</style>
