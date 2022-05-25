<template lang="">
  <md-menu id="usermenu" md-size="small" md-align-trigger>
    <md-button md-menu-trigger>
      <b-list-group class="position-relative">
        <b-list-group-item
          class="d-flex align-items-center bg-transparent border-0 px-0"
        >
          <b-avatar
            variant="info"
            :src="profil"
            class="mr-2"
            v-if="avatar"
          ></b-avatar>

          <svg
            v-else
            id="account_circle_black_24dp"
            class="mr-1"
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 36 36"
          >
            <path
              id="Tracé_1"
              data-name="Tracé 1"
              d="M0,0H36V36H0Z"
              fill="none"
            />
            <path
              id="Tracé_2"
              data-name="Tracé 2"
              d="M18,2A16,16,0,1,0,34,18,16.006,16.006,0,0,0,18,2Zm0,4.8a4.8,4.8,0,1,1-4.8,4.8A4.794,4.794,0,0,1,18,6.8Zm0,22.72a11.521,11.521,0,0,1-9.6-5.152c.048-3.184,6.4-4.928,9.6-4.928,3.184,0,9.552,1.744,9.6,4.928A11.521,11.521,0,0,1,18,29.52Z"
              fill="#242c36"
            />
          </svg>

          <div class="mr-auto d-flex flex-column align-items-start">
            <span class="username">{{ username }}</span>
            <span class="usertype">{{ usertype }}</span>
          </div>

          <svg
            id="dropdown_compte"
            class="ml-1"
            data-name="dropdown compte"
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <g id="arrow_drop_down-24px">
              <path
                id="Tracé_2864"
                data-name="Tracé 2864"
                d="M0,0H24V24H0Z"
                fill="none"
              />
              <path
                id="Tracé_2865"
                data-name="Tracé 2865"
                d="M7,10l5,5,5-5Z"
                fill="#242c36"
              />
            </g>
          </svg>
        </b-list-group-item>
      </b-list-group>
    </md-button>

    <md-menu-content id="usermenu-dropdown">
      <router-link
        to="/mon-compte"
        class="usermenu-dropdown-item"
        v-if="!admin"
      >
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
  name: "UserMenu",
  props: {
    username: String,
    usertype: String,
    avatar: String,
    admin: {
      type: Boolean,
      required: false,
    },
  },
  data: function() {
    return {
      profil: null,
    };
  },
  methods: {
    async loadUser() {
      try {
        if (localStorage.getItem("token") !== "null") {
          await this.$store.dispatch("loadClients", {
            token: localStorage.getItem("token"),
          });
          this.profil = this.client.profil;
        } else this.profil = null;
      } catch (e) {
        //
      }
    },
    async refresh() {
      await this.loadUser();
    },
    logOut() {
      localStorage.clear();
      this.$router.push({ name: "Login" });
    },
  },
  async mounted() {
    this.loadUser();
  },
  computed: {
    client() {
      return this.$store.state.client.clients;
    },
  },
};
</script>

<style>
#usermenu .md-button .md-ripple {
  justify-content: flex-start;
  padding: 0;
}
.usermenu-dropdown-item .md-list-item-content {
  justify-content: flex-start;
}
#usermenu .md-button .md-ripple .md-button-content {
  width: inherit;
}
</style>

<style scoped>
#usermenu .md-button {
  text-transform: initial;
  width: 100%;
}

#usermenu .username {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  line-height: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}
@media (max-width: 479px) {
  #usermenu .username {
    font-size: 12px;
  }
}
#usermenu .usertype {
  font-size: 12px;
  line-height: 18px;
}
#usermenu .b-avatar {
  height: 32px;
  width: 32px;
}
#usermenu-dropdown .md-menu-content-container .md-list {
  padding: 0;
}
.usermenu-dropdown-item .md-list-item-content {
  font-size: 12px;
  font-family: "Poppins-Regular", Arial, Helvetica, sans-serif;
}
.usermenu-dropdown-item {
  cursor: pointer;
}
.usermenu-dropdown-item:hover {
  background-color: #f6f6f7;
}
.usermenu-dropdown-item:hover svg path {
  fill: var(--black) !important;
}
.md-menu-content {
  min-width: 143px;
  box-shadow: none;
}
.list-group .list-group-item {
  padding: 0;
}
</style>
