<template lang="">
  <div
    v-bind:class="
      type === 'checkbox' || type === 'radio'
        ? 'form-group form-check mb-sm-0'
        : 'form-group'
    "
  >
    <label
      v-if="label && type != 'checkbox' && type != 'radio'"
      v-bind:for="id"
      v-html="label"
      :class="errors.length && 'error-input'"
    ></label>
    <span v-if="errors.length">
      <span class="error" v-for="error in errors" :key="error">{{
        error
      }}</span>
    </span>
    <div class="input-group">
      <input
        v-bind:class="
          type === 'checkbox' || type === 'radio'
            ? 'form-check-input'
            : 'form-control'
        "
        v-if="type != 'password'"
        v-bind:id="id"
        v-bind:type="type"
        v-bind:required="required"
        v-bind:name="name"
        v-bind:placeholder="placeholder"
        v-on:input="$emit('input', $event.target.value)"
      />
      <input
        class="form-control"
        v-if="type === 'password'"
        v-bind:id="id"
        :type="togglePassword ? 'password' : 'text'"
        v-bind:required="required"
        v-bind:name="name"
        v-bind:placeholder="placeholder"
        v-on:input="$emit('input', $event.target.value)"
      />
      <label
        v-if="label && (type === 'checkbox' || type === 'radio')"
        class="form-check-label"
        v-bind:for="id"
        v-html="label"
      ></label>
      <div v-if="type === 'password'" class="input-group-append">
        <span
          class="input-group-text bg-transparent"
          id="oeil-svg"
          v-on:click="toggleVisible(togglePassword)"
        >
          <svg
            v-if="togglePassword"
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="15"
            viewBox="0 0 22 15"
          >
            <path
              id="Tracé_988"
              data-name="Tracé 988"
              d="M23.637-39c-5,0-9.27,3.61-11,8,1.73,4.39,6,7,11,7s9.27-2.61,11-7C32.907-35.39,28.637-39,23.637-39Zm0,13a5,5,0,0,1-5-5,5,5,0,0,1,5-5,5,5,0,0,1,5,5A5,5,0,0,1,23.637-26Zm0-8a3,3,0,0,0-3,3,3,3,0,0,0,3,3,3,3,0,0,0,3-3A3,3,0,0,0,23.637-34Z"
              transform="translate(-12.637 39)"
              fill="#242c36"
            />
          </svg>
          <svg
            v-if="!togglePassword"
            xmlns="http://www.w3.org/2000/svg"
            height="24px"
            viewBox="0 0 24 24"
            width="24px"
          >
            <path
              d="M0 0h24v24H0zm0 0h24v24H0zm0 0h24v24H0zm0 0h24v24H0z"
              fill="none"
            />
            <path
              d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z"
            />
          </svg>
        </span>
      </div>
    </div>
    <div v-if="help" class="help_input" v-html="help"></div>
  </div>
</template>

<script>
export default {
  name: "PredictInput",
  props: {
    id: { type: String },
    type: { type: String, required: true },
    name: { type: String, required: true },
    placeholder: { type: String },
    label: { type: String },
    required: { type: String },
    model: { type: String },
    errors: {
      type: Array,
      default: function() {
        return [""];
      }
    },
    help: { type: String }
  },
  data: () => {
    return {
      togglePassword: true
    };
  },
  methods: {
    toggleVisible(togglePassword) {
      return (this.togglePassword == !togglePassword);
    }
  }
};
</script>
