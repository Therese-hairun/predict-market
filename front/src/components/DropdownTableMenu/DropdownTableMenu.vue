<template>
  <md-menu id="usermenu" md-size="small" md-align-trigger>
    <md-button md-menu-trigger>
      <b-list-group class="position-relative">
        <b-list-group-item
          class="d-flex align-items-center bg-transparent border-0 px-0"
        >
          <svg
            id="option_tableau"
            data-name="option tableau"
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <g id="more_horiz_black_24dp">
              <path
                id="Tracé_42169"
                data-name="Tracé 42169"
                d="M0,0H24V24H0Z"
                fill="none"
              />
              <path
                id="Tracé_42170"
                data-name="Tracé 42170"
                d="M6,10a2,2,0,1,0,2,2A2.006,2.006,0,0,0,6,10Zm12,0a2,2,0,1,0,2,2A2.006,2.006,0,0,0,18,10Zm-6,0a2,2,0,1,0,2,2A2.006,2.006,0,0,0,12,10Z"
              />
            </g>
          </svg>
        </b-list-group-item>
      </b-list-group>
    </md-button>

    <md-menu-content id="usermenu-dropdown">
      <router-link to="/mon-compte" class="usermenu-dropdown-item">
        <md-menu-item class="justify-content-start">
          <svg
            class="mr-2"
            xmlns="http://www.w3.org/2000/svg"
            width="18.676"
            height="19.2"
            viewBox="0 0 18.676 19.2"
          >
            <path
              id="Tracé_19685"
              data-name="Tracé 19685"
              d="M19.14,12.94A7.074,7.074,0,0,0,19.2,12a5.777,5.777,0,0,0-.07-.94l2.03-1.58a.491.491,0,0,0,.12-.61L19.36,5.55a.488.488,0,0,0-.59-.22l-2.39.96a7.064,7.064,0,0,0-1.62-.94L14.4,2.81a.484.484,0,0,0-.48-.41H10.08a.474.474,0,0,0-.47.41L9.25,5.35a7.22,7.22,0,0,0-1.62.94L5.24,5.33a.477.477,0,0,0-.59.22L2.74,8.87a.455.455,0,0,0,.12.61l2.03,1.58a5.563,5.563,0,0,0-.02,1.88L2.84,14.52a.491.491,0,0,0-.12.61l1.92,3.32a.488.488,0,0,0,.59.22l2.39-.96a7.064,7.064,0,0,0,1.62.94l.36,2.54a.492.492,0,0,0,.48.41h3.84a.466.466,0,0,0,.47-.41l.36-2.54a6.859,6.859,0,0,0,1.62-.94l2.39.96a.477.477,0,0,0,.59-.22l1.92-3.32a.463.463,0,0,0-.12-.61ZM12,15.6A3.6,3.6,0,1,1,15.6,12,3.611,3.611,0,0,1,12,15.6Z"
              transform="translate(-2.662 -2.4)"
              fill="#242c36"
            />
          </svg>
          {{ $t("myAccount") }}
        </md-menu-item>
      </router-link>
      <div class="usermenu-dropdown-item" @click="logOut">
        <md-menu-item class="justify-content-start">
          <svg
            class="mr-2"
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="18"
            viewBox="0 0 20 18"
          >
            <path
              id="Tracé_19687"
              data-name="Tracé 19687"
              d="M17,7,15.59,8.41,18.17,11H8v2H18.17l-2.58,2.58L17,17l5-5ZM4,5h8V3H4A2.006,2.006,0,0,0,2,5V19a2.006,2.006,0,0,0,2,2h8V19H4Z"
              transform="translate(-2 -3)"
              fill="#242c36"
            />
          </svg>
          {{ $t("logOut") }}
        </md-menu-item>
      </div>
    </md-menu-content>
  </md-menu>
</template>

<script>
export default {
  name: "DropDownTableMenu",
  methods: {
    logOut() {
      localStorage.clear();
      this.$router.push({ name: "Login" });
    },
  },
};
</script>
