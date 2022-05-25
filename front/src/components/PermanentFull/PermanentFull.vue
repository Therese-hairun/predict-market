<template>
  <div class="page-container md-layout-row">
    <md-app id="permanentfull">
      <md-app-toolbar class="header-bar shadow-none d-flex align-items-center">
        <md-button
          class="permanentfull-icon-button md-icon-button"
          @click="toggleMenu"
          v-if="!menuVisible"
        >
          <svg
            id="sort_black_24dp"
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <path
              id="Tracé_19697"
              data-name="Tracé 19697"
              d="M3,18H9V16H3ZM3,6V8H21V6Zm0,7H15V11H3Z"
              fill="#242c36"
            />
          </svg>
        </md-button>
        <md-button
          class="permanentfull-icon-button md-icon-button"
          @click="toggleMenu"
          v-else
        >
          <i
            data-v-ba6df2ea=""
            aria-hidden="true"
            class="fa fa-chevron-left"
          ></i>
        </md-button>
        <span class="md-title ml-0">{{ $t("menu") }}</span>
        <span class="fxFlex"></span>
        <MainLayout></MainLayout>
        <DialogDowngrade v-if="!admin" :showDialog="showDialogListeCouples">
        </DialogDowngrade>
        <UserMenu
          ref="UserMenu"
          :username="
            admin
              ? adminUser.username
              : client.firstname + ' ' + client.lastname
          "
          :usertype="admin ? 'Admin' : $t('user')"
          :avatar="imgAvatar"
          :admin="admin"
          class="user_menu_container"
        ></UserMenu>
      </md-app-toolbar>

      <md-app-drawer
        md-permanent="full"
        :md-active.sync="menuVisible"
        md-persistent="mini"
      >
        <md-toolbar
          class="md-transparent d-flex flex-nowrap align-items-center "
          md-elevation="0"
        >
          <router-link
            :to="admin ? '/listes-des-utilisateurs' : '/dashboard'"
            class="d-flex align-items-center mx-auto"
          >
            <span class="md-title text-white ml-0">
              <img
                src="../../assets/images/logoJaune.png"
                alt="Logo Jaune"
                width="34"
                height="38"
                class=""
              />
              <span class="pl-2" :class="{ hidden: !menuVisible }">
                Predictmarket
              </span>
            </span>
          </router-link>
        </md-toolbar>

        <md-list>
          <md-list-item v-for="(item, index) in menuItems" :key="index">
            <router-link
              @click.native="resetUpgrade(item)"
              :to="item.href"
              class="w-100 d-flex"
            >
              <span class="icon-container" v-html="item.icon"></span>
              <span class="md-list-item-text">{{ $t(item.text) }}</span>
            </router-link>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content
        id="test-conten"
        class="d-flex flex-column  overflow-hidden p-0"
        :class="appContentClass"
      >
        <h1 class="dashboard-title d-flex align-items-center" v-if="titre">
          <span class="d-flex align-items-center mr-2" v-html="icon"></span
          >{{ titre }}
        </h1>

        <div
          class="md-layout md-gutter flex-grow-1 permanentfull-layout mx-0 column-wrapper"
        >
          <slot></slot>
        </div>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>
import UserMenu from "../UserMenu/UserMenu.vue";
DialogDowngrade;
import MainLayout from "../language/MainLayout.vue";
import DialogDowngrade from "../DialogDowngrade/DialogDowngrade.vue";

export default {
  name: "PermanentFull",
  methods: {
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    toggle() {
      this.toggleCard = !this.toggleCard;
    },
    refresh() {
      this.$refs.UserMenu.loadUser();
    },
    resetUpgrade(item) {
      if (item.text === "subscription") localStorage.setItem("upgrade", 0);
      this.$emit("refresh");
    },
  },
  data: () => {
    return {
      username: "",
      imgAvatar: "https://jlg.ro/wp-content/uploads/2020/09/empty-avatar.png",
      showDialogListeCouples: false,
      toggleCard: false,
      menuVisible: false,
    };
  },
  props: {
    iconColor: {
      type: String,
    },
    titre: String,
    icon: String,
    menuItems: Array,
    typeAbonnement: String,
    dateExpiration: String,
    emplacementDispo: String,
    appContentClass: String,
    admin: {
      type: Boolean,
      required: false,
    },
  },
  components: {
    UserMenu,
    MainLayout,
    DialogDowngrade,
  },
  async mounted() {
    try {
      if (localStorage.getItem("token") !== "null") {
        await this.$store.dispatch("loadClients", {
          token: localStorage.getItem("token"),
        });
        if (this.client == []) this.$router.push({ name: "login" });
      } else {
        await this.$store.dispatch("loadAdmin", {
          token: localStorage.getItem("adminToken"),
        });
        if (this.adminUser == []) this.$router.push({ name: "login" });
      }
    } catch (e) {
      //
    }
  },
  computed: {
    client() {
      return this.$store.state.client.clients;
    },
    adminUser() {
      return this.$store.state.admin.admins;
    },
  },
};
</script>

<style>
@media (max-width: 1200px) {
  #content-sidebar-wrapper {
    flex: 0 0 100%;
  }
}
#permanentfull .md-app-toolbar > .permanentfull-icon-button {
  margin-left: -8px;
}
@media (max-width: 960px) {
  #permanentfull .md-app-toolbar > .permanentfull-icon-button {
    margin-left: 0;
  }
}
@media (max-width: 600px) {
  #permanentfull .md-app-toolbar > .permanentfull-icon-button {
    margin-left: -5px;
  }
}
</style>

<style scoped>
.md-app {
  min-height: 100vh;
}
/* .permanentfull-icon-button:hover i::before,
.permanentfull-icon-button:hover path {
  color: var(--primary);
  fill: var(--primary);
} */
#permanentfull .hidden {
  display: none;
}

#permanentfull .md-drawer {
  background-color: var(--black);
  width: 245px;
  max-width: calc(100vw - 125px);
}
.header-bar {
  background: #fff;
  padding-top: 5px;
  flex-wrap: nowrap;
  position: sticky;
  left: 0;
  width: 100%;
  z-index: 10;
}

@media (max-width: 600px) {
  #permanentfull .md-drawer {
    width: 100%;
    max-width: 100%;
  }
}
.md-drawer .md-title img {
  margin-right: 0;
}

#permanentfull .md-drawer.md-persistent-mini:not(.md-active) {
  width: 60px !important;
  position: relative;
  transform: translate3D(0, 0, 0);
}
@media (max-width: 599px) {
  #permanentfull .md-toolbar .md-button {
    margin-right: 0;
  }
}
#permanentfull .md-toolbar .md-title {
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;
  font-size: 16px;
  color: #fff;
}
@media (max-width: 599px) {
  #permanentfull .header-bar .md-title {
    display: none;
  }
}
#permanentfull .md-drawer .md-toolbar a:hover {
  text-decoration: none !important;
}
#permanentfull .md-drawer .md-toolbar a:hover .md-title {
  color: var(--primary) !important;
}
#permanentfull .md-list {
  background-color: transparent;
}
#permanentfull .md-list-item {
  border-left: 2px solid transparent;
  margin-top: 12px;
  margin-bottom: 12px;
}
#permanentfull .md-list-item:hover {
  cursor: pointer;
  border-left: 2px solid var(--primary);
}
#permanentfull .md-list-item a {
  color: #5c626a !important;
  text-decoration: none !important;
  padding: 10px 16px;
}
#permanentfull .md-list-item a.router-link-active,
#permanentfull .md-list-item a:hover {
  background-color: #323b46;
}
#permanentfull .md-list-item-text {
  line-height: 24px;
}
#permanentfull .md-list-item a.router-link-active .md-list-item-text,
#permanentfull .md-list-item a:hover .md-list-item-text {
  color: #fff !important;
}
#permanentfull .md-list-item-container .icon-container {
  margin-right: 8px;
  width: 24px;
  height: auto;
}
#permanentfull .md-list-item-container .icon-container .icon-item {
  fill: red;
}
#permanentfull .md-app-toolbar > * {
  color: var(--black) !important;
  font-size: 14px !important;
  font-family: "Poppins-Regular", Arial, Helvetica, sans-serif !important;
}

#permanentfull .user_menu_container {
  margin-left: auto;
}
@media (max-width: 479px) {
  #permanentfull .user_menu_container {
    margin-left: 0;
    /* width: calc(100% - 50px); */
  }
}
#content-dashboard-wrapper {
  width: 100%;
}
#content-sidebar-wrapper {
  width: 100%;
}

@media (min-width: 1200px) {
  .permanentfull-content {
    padding-left: 36px;
    padding-right: 36px;
  }
}

.permanentfull-layout.column-wrapper {
  /* flex-direction: column; */
  /* margin-bottom: 20px; */
}

@media (min-width: 1200px) and (max-width: 1400px) {
  .permanentfull-layout.column-wrapper > div {
    width: 50%;
  }
}

@media (min-width: 1400px) {
  #content-dashboard-wrapper {
    padding-right: 0;
  }
}
@media (max-width: 1400px) {
  #content-dashboard-wrapper,
  #content-sidebar-wrapper {
    flex: 0 1 100%;
    max-width: 100%;
  }
  #content-sidebar-wrapper {
    margin-top: 20px;
  }
}

.fxFlex {
  flex: 1 0 auto;
}
</style>
