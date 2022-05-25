<template lang="">
  <div class="dashboard">
    <PermanentFull
      :titre="$t('userManagement')"
      :icon="icon"
      :menuItems="menuItems"
      :admin="true"
    >
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <!-- Loader -->
        <div class="loader-content" v-if="loading">
          <p class="msg">{{ $t("loading") }}</p>
          <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
        </div>
        <!-- /Loader -->
        <div class="pt-4 flex-grow-1 d-flex flex-column">
          <div class="liste-des-utilisateurs">
            <h3 class="titre-recherche">{{ $t("search") }}</h3>
            <span class="help-recherche">{{ $t("searchUserText") }}</span>
            <br />
            <div class="table-wrapper flex-grow">
              <md-table
                md-table-fixed-header
                class="mt-3 predict-table user_list-table d-flex h-100"
              >
                <md-table-toolbar class="filter-bloc px-2 mb-3">
                  <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                    <md-input
                      :placeholder="$t('searchByName')"
                      class="input-search border-0"
                      v-model="search"
                    />
                    <svg
                      class="mr-2"
                      xmlns="http://www.w3.org/2000/svg"
                      width="16.395"
                      height="16.395"
                      viewBox="0 0 16.395 16.395"
                    >
                      <path
                        d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                        transform="translate(-570 -2016)"
                        fill="#242c36"
                      />
                    </svg>
                  </md-field>
                </md-table-toolbar>
                <div class="table-container">
                  <md-table-row class="table-header">
                    <md-table-head scope="col" class="user_col">
                      {{ $t("users") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('client')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'client')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="subscribe_col">
                      {{ $t("subscription") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('subscribe')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'subscribe')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="date_col">
                      {{ $t("validityDate") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('end')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'end')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="credits_col">
                      {{ $t("credits") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('sum')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'sum')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="freeDays_col">
                      {{ $t("freeDays") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('free_day')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'free_day')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head scope="col" class="suspend_col">
                      {{ $t("suspend") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('account_is_active')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42155"
                              data-name="Tracé 42155"
                              d="M7,13.75,10.75,10l3.75,3.75Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                        <md-button
                          class="btn-tri arrow-down"
                          v-on:click="orderBy('-' + 'account_is_active')"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="7.5"
                            height="3.75"
                            viewBox="0 0 7.5 3.75"
                          >
                            <path
                              id="Tracé_42154"
                              data-name="Tracé 42154"
                              d="M7,10l3.75,3.75L14.5,10Z"
                              transform="translate(-7 -10)"
                              fill="#5c626a"
                            />
                          </svg>
                        </md-button>
                      </span>
                    </md-table-head>
                    <md-table-head
                      scope="col"
                      class="action_col"
                    ></md-table-head>
                  </md-table-row>
                  <md-table-row v-for="(item, index) in users" :key="index">
                    <md-table-cell class="user_col" :data-label="$t('users')">
                      {{ item.client.firstname }}
                      {{ item.client.lastname }}</md-table-cell
                    >
                    <md-table-cell
                      class="subscribe_col"
                      :data-label="$t('subscription')"
                    >
                      {{ splitData(item.subscribe, 1) }}
                    </md-table-cell>
                    <md-table-cell
                      class="date_col"
                      :data-label="$t('validityDate')"
                    >
                      {{ formatDate($t("dateFormat"), item.end) }}
                    </md-table-cell>
                    <md-table-cell
                      class="credits_col"
                      :data-label="$t('credits')"
                    >
                      {{ pointToComma(item.client.reward.sum.toFixed(2)) }} €
                    </md-table-cell>
                    <md-table-cell
                      class="freeDays_col"
                      :data-label="$t('freeDays')"
                    >
                      {{ pointToComma(item.client.reward.free_day.toFixed(2)) }}
                      {{ $t("unitDay") }}
                    </md-table-cell>
                    <md-table-cell
                      class="suspend_col"
                      :data-label="$t('suspend')"
                    >
                      <md-switch
                        class="table-switch"
                        v-model="item.client.account_status"
                        @change="updateUserStatus(item)"
                        >{{
                          item.client.account_status
                            ? $t("active")
                            : $t("desactive")
                        }}</md-switch
                      >
                    </md-table-cell>
                    <md-table-cell class="action_col" data-label="">
                      <b-dropdown
                        variant="link"
                        toggle-class="text-decoration-none"
                        no-caret
                        class="table-dropdown"
                      >
                        <template #button-content>
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
                        </template>
                        <b-dropdown-item @click="shareData(item.client.id)">
                          <svg
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
                          {{ $t("seeDetails") }}
                        </b-dropdown-item>
                        <b-dropdown-item
                          href="#"
                          @click="getData(item), toggleDialogAbonnement()"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="18.132"
                            height="15"
                            viewBox="0 0 18.132 15"
                          >
                            <path
                              id="Tracé_42490"
                              data-name="Tracé 42490"
                              d="M3,10H14v2H3ZM3,8H14V6H3Zm0,8h7V14H3Zm15.01-3.13.71-.71a1,1,0,0,1,1.41,0l.71.71a1,1,0,0,1,0,1.41l-.71.71Zm-.71.71L12,18.88V21h2.12l5.3-5.3Z"
                              transform="translate(-3 -6)"
                              fill="#242c36"
                            />
                          </svg>
                          {{ $t("modifySubscription") }}
                        </b-dropdown-item>
                        <b-dropdown-item
                          href="#"
                          @click="toggleDialogCredit(), getData(item)"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="17.999"
                            height="17.099"
                            viewBox="0 0 17.999 17.099"
                          >
                            <path
                              id="Tracé_42201"
                              data-name="Tracé 42201"
                              d="M18.046,6.95,16,4.907a4.818,4.818,0,0,1,.288-1.035A1.261,1.261,0,0,0,16.4,3.35,1.348,1.348,0,0,0,15.049,2a4.5,4.5,0,0,0-3.6,1.8H6.95A4.947,4.947,0,0,0,2,8.75C2,11.486,4.25,19.1,4.25,19.1H9.2V17.3H11v1.8h4.95l1.512-5.031L20,13.222V6.95ZM11.9,8.3H7.4V6.5h4.5Zm2.7,1.8a.9.9,0,1,1,.9-.9A.9.9,0,0,1,14.6,10.1Z"
                              transform="translate(-2 -2)"
                              fill="#242c36"
                            />
                          </svg>
                          {{ $t("modifyCredits") }}
                        </b-dropdown-item>
                        <b-dropdown-item
                          href="#"
                          @click="toggleDialogJour(), getData(item)"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="20"
                            height="22"
                            viewBox="0 0 20 22"
                          >
                            <path
                              id="Tracé_42544"
                              data-name="Tracé 42544"
                              d="M20,3H19V1H17V3H7V1H5V3H4A2.006,2.006,0,0,0,2,5V21a2.006,2.006,0,0,0,2,2H20a2.006,2.006,0,0,0,2-2V5A2.006,2.006,0,0,0,20,3Zm0,18H4V8H20Z"
                              transform="translate(-2 -1)"
                              fill="#242c36"
                            />
                          </svg>
                          {{ $t("modifyFreeDays") }}
                        </b-dropdown-item>
                      </b-dropdown>
                    </md-table-cell>
                  </md-table-row>
                  <md-table-row v-if="this.visible">
                    <md-table-cell :colspan="7" class="align-text">{{
                      this.error
                    }}</md-table-cell></md-table-row
                  >
                  <md-table-row class="pagination-row" v-if="!visible">
                    <md-table-cell :colspan="7">
                      <TablePagination
                        @pageVal="handleChangePageValue"
                        @pageSize="handleChangeSizeValue"
                        :dataSize="dataSize"
                        :next="next"
                      />
                    </md-table-cell>
                  </md-table-row>
                </div>
              </md-table>
            </div>
          </div>
        </div>
      </div>

      <Dialog
        :showDialog="showDialogAbonnement"
        :dialogName="$t('modifySubscription')"
        :titreDialog="this.dialogName"
        @close="showDialogAbonnement = !showDialogAbonnement"
      >
        <div class="text-center" style="max-width: 356px;">
          {{ $t("info:modifySubscription") }}
        </div>

        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <div class="form-group">
            <md-field>
              <label for="type_abonnement"></label>
              <md-select v-model="selected">
                <md-option
                  v-for="(type, index) in subscriptions"
                  :key="index"
                  :value="type.id + ':' + type.name"
                  >{{ type.name }}
                </md-option>
              </md-select>
            </md-field>
          </div>

          <div class="form-group">
            <md-datepicker
              v-model="dateValidity"
              class="d-flex date-picker align-items-center"
              :md-disabled-dates="isPreviousDate"
            >
              <label>{{ $t("validityDate") }}</label>
            </md-datepicker>
          </div>

          <div class="form-group d-flex flex-column">
            <label>{{ $t("renew") }}</label>
            <md-switch
              class="table-switch font-weight-bold mt-0"
              v-model="renewAuto"
              >{{ renewAuto ? $t("active") : $t("desactive") }}</md-switch
            >
          </div>

          <div class="w-100 text-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase"
              @click="updateSubscription()"
              :disabled="!dateValidity"
            >
              {{ $t("modify") }}
            </md-button>
          </div>
        </form>
      </Dialog>

      <Dialog
        :showDialog="showDialogCredit"
        :dialogName="$t('modifyCredits')"
        @close="showDialogCredit = !showDialogCredit"
        :titreDialog="this.dialogName"
      >
        <div class="text-center" style="max-width: 356px;">
          {{ $t("info:modifyCredits") }}
        </div>

        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <span v-if="errorCredits" class="d-flex flex-column">
            <span class="error">{{ errorCredits }}</span>
          </span>
          <PredictInputNumber
            :value="credits"
            v-model="credits"
            numberLength="5"
            unite="€"
          ></PredictInputNumber>

          <div class="w-100 text-center d-flex align-items-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              @click="subCredits()"
              style="border-top-right-radius: 0;border-bottom-right-radius: 0;border-right: 0.5px solid #fff"
            >
              {{ $t("back:remove") }}
            </md-button>
            <md-button
              type="submit"
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              @click="addCredits()"
              style="border-top-left-radius: 0;border-bottom-left-radius: 0;border-left: 0.5px solid #fff"
            >
              {{ $t("add") }}
            </md-button>
          </div>
        </form>
      </Dialog>

      <Dialog
        :showDialog="showDialogAjoutReussi"
        :titreDialog="this.dialogName"
        :iconDialog="iconModifJours"
        @close="showDialogAjoutReussi = !showDialogAjoutReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("creditAddOf") }} <strong>{{ credits }} €</strong>
          {{ $t("for") }} <strong>{{ this.dialogName }}</strong>
          {{ $t("modifCompleted") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAjoutReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogEnlevementReussi"
        :titreDialog="$t('removeSuccess')"
        @close="showDialogEnlevementReussi = !showDialogEnlevementReussi"
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("removeCreditSuccess") }} <strong>{{ credits }} €</strong>
          {{ $t("for") }} <strong>{{ this.dialogName }}</strong>
          {{ $t("modifCompleted") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogEnlevementReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogAboModifie"
        titreDialog="Abonnement modifié"
        @close="showDialogAboModifie = !showDialogAboModifie"
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("subscriptionFor") }} <strong>{{ this.dialogName }}</strong>
          {{ $t("modifiedSuccessSubscription") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAboModifie = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogJour"
        :dialogName="$t('modifyCredits')"
        @close="showDialogJour = !showDialogJour"
        :titreDialog="this.dialogName"
      >
        <div class="text-center" style="max-width: 356px;">
          {{ $t("modifyCreditsMessage") }}
        </div>

        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <span v-if="errorFreeDay" class="d-flex flex-column">
            <span class="error">{{ errorFreeDay }}</span>
          </span>
          <PredictInputNumber
            :value="joursGratuits"
            v-model="joursGratuits"
            numberLength="3"
            :unite="$t('unitDay')"
          ></PredictInputNumber>

          <div class="w-100 text-center d-flex align-items-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              @click="subFreeDay()"
              style="border-top-right-radius: 0;border-bottom-right-radius: 0;border-right: 0.5px solid #fff"
            >
              {{ $t("back:remove") }}
            </md-button>
            <md-button
              type="submit"
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase px-0 mx-0"
              @click="addFreeDay()"
              style="border-top-left-radius: 0;border-bottom-left-radius: 0;border-left: 0.5px solid #fff"
            >
              {{ $t("add") }}
            </md-button>
          </div>
        </form>
      </Dialog>

      <Dialog
        :showDialog="showDialogAjoutJourReussi"
        titreDialog="Ajout réussi"
        @close="showDialogAjoutJourReussi = !showDialogAjoutJourReussi"
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("addFreeDaysSuccess1") }}
          <strong>{{ joursGratuits }} {{ $t("unitDay") }}</strong> pour
          <strong>{{ this.dialogName }}</strong> {{ $t("addFreeDaysSuccess2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAjoutJourReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogEnlevementJourReussi"
        :titreDialog="$t('removeSuccess')"
        @close="
          showDialogEnlevementJourReussi = !showDialogEnlevementJourReussi
        "
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("removeDaysSuccess") }}
          <strong>{{ joursGratuits }} j</strong> {{ $t("for") }}
          <strong>{{ this.dialogName }}</strong> {{ $t("modifCompleted") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogEnlevementJourReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import Dialog from "../Dialog/Dialog.vue";
import PredictInputNumber from "../Input/PredictInputNumber.vue";
import MenuGestion from "../../data/MenuGestion.js";
import moment from "moment";
import { PARAPHRASE, formatDate } from "../../utils/Constant";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
  name: "ListesDesUtilisateurs",
  components: {
    PermanentFull,
    Dialog,
    PredictInputNumber,
    TablePagination,
  },
  methods: {
    formatDate,
    handleChangePageValue(val) {
      this.page = val;
    },
    handleChangeSizeValue(val) {
      this.size = val;
    },
    shareData(item) {
      localStorage.setItem("userDetailId", this.encryptValue(item.toString()));
      this.$router.push({ name: "DetailsUtilisateur" });
    },
    encryptValue(val) {
      return this.CryptoJS.AES.encrypt(val, PARAPHRASE).toString();
    },
    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
    checkUsersData() {
      if (this.users && !this.users.length) {
        this.error = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },

    setAllFalse() {
      this.showDialogCredit = false;
      this.showDialogAjoutReussi = false;
      this.showDialogEnlevementReussi = false;
      this.showDialogEnlevementReussi = false;
      this.showDialogAj = false;
      this.showDialogEnlevementJourReussi = false;
      this.showDialogJour = false;
      this.showDialogAbonnement = false;
    },
    toggleDialogAbonnement() {
      this.setAllFalse();
      this.showDialogAbonnement = !this.showDialogAbonnement;
    },
    toggleDialogCredit() {
      this.setAllFalse();
      this.showDialogCredit = !this.showDialogCredit;
    },
    toogleDialogAjoutReussi() {
      this.setAllFalse();
      this.showDialogAjoutReussi = !this.showDialogAjoutReussi;
    },
    toogleDialogEnlevementReussi() {
      this.credits = -this.credits;
      this.setAllFalse();
      this.showDialogEnlevementReussi = !this.showDialogEnlevementReussi;
    },
    toogleDialogAboModifie() {
      this.setAllFalse();
      this.showDialogAboModifie = !this.showDialogAboModifie;
    },
    toogleDialogAjoutJourReussi() {
      this.setAllFalse();
      this.showDialogAjoutJourReussi = !this.showDialogAjoutJourReussi;
    },
    toogleDialogEnlevementJourReussi() {
      this.setAllFalse();
      this.joursGratuits = -this.joursGratuits;
      this.showDialogEnlevementJourReussi = !this
        .showDialogEnlevementJourReussi;
    },
    toggleDialogJour() {
      this.setAllFalse();
      this.showDialogJour = !this.showDialogJour;
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
      this.find();
    },
    loadUsers: async function() {
      await this.$store.dispatch("loadUsers", {
        token: localStorage.getItem("adminToken"),
        order: this.order,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    orderBy: async function(field) {
      await this.$store.dispatch("loadUsers", {
        token: localStorage.getItem("adminToken"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    updateUserStatus: async function(item) {
      const payload = {
        account_is_active: item.client.account_status ? true : false,
      };
      try {
        await this.$store.dispatch("updateUserStatus", {
          id: item.client.id,
          payload,
          token: localStorage.getItem("adminToken"),
        });
        await this.loadUsers();
      } catch (e) {
        //
      }
    },
    updateSubscription: async function() {
      const payload = {
        subscribe: +this.selected[0],
        end: this.formatDateUpdate(this.dateValidity),
        renew: this.renewAuto ? 1 : 0,
      };
      try {
        await this.$store.dispatch("updateSubscriptionUser", {
          id: this.getId,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
        await this.loadUsers();
        this.toogleDialogAboModifie();
        this.dateValidity = "";
        this.selected = "";
        this.renewAuto = "";
      } catch (e) {
        //
      }
    },
    updateCredit: async function() {
      const payload = {
        sum: +this.credits + this.previousCredits,
      };
      try {
        await this.$store.dispatch("updateCredit", {
          id: this.getId,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
        await this.loadUsers();
      } catch (e) {
        //
      }
    },
    updateFreeDay: async function() {
      const payload = {
        free_day: +this.joursGratuits + this.previousJoursGratuits,
      };
      try {
        await this.$store.dispatch("updateFreeDay", {
          id: this.getId,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
        this.loadUsers();
      } catch (e) {
        //
      }
    },
    getData: function(item) {
      this.renewAuto = item?.renew_status ? true : false;
      this.getId = +item.client.id;
      this.dialogName = item.client.firstname + " " + item.client.lastname;
      this.dateValidity = this.validityDate = this.formatDate(
        this.$t("dateFormat"),
        item.end
      );
      this.previousCredits = item.client.reward.sum;
      this.credits = 0;
      this.previousJoursGratuits = item.client.reward.free_day;
      this.joursGratuits = 0;
      this.selected = item?.subscribe;
    },
    splitData: function(data, index) {
      return data?.split(":")[index];
    },

    addCredits: function() {
      this.updateCredit();
      this.toogleDialogAjoutReussi();
    },
    subCredits: function() {
      this.errorCredits = "";
      if (this.previousCredits < this.credits)
        this.errorCredits = this.$t("errorCredits");
      else {
        this.credits = -this.credits;
        this.updateCredit();
        this.toogleDialogEnlevementReussi();
      }
    },
    addFreeDay: function() {
      this.updateFreeDay();
      this.toogleDialogAjoutJourReussi();
    },
    subFreeDay: function() {
      this.errorFreeDay = "";
      if (this.previousJoursGratuits < this.joursGratuits)
        this.errorFreeDay = this.$t("errorFreeDay");
      else {
        this.joursGratuits = -this.joursGratuits;
        this.updateFreeDay();
        this.toogleDialogEnlevementJourReussi();
      }
    },
    loadCouples: async function() {
      try {
        this.loading = true;
        await this.$store.dispatch("loadDataCouples", {
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      } finally {
        this.loading = false;
      }
    },
    formatDateUpdate(item) {
      return moment(item, this.$t("dateFormat")).format("YYYY-MM-DD HH:mm:ss");
    },
    loadSubscriptions: async function() {
      await this.$store.dispatch("loadSubscriptions", {
        token: localStorage.getItem("adminToken"),
        order: "",
        page: "",
        search: "",
        size: "",
      });
    },
    isPreviousDate(date) {
      const dateNow = new Date();
      dateNow.setDate(dateNow.getDate() - 1);
      return date < dateNow;
    },
  },
  data: () => {
    return {
      search: "",
      order: "",
      error: "",
      errorFreeDay: "",
      errorCredits: "",
      visible: false,
      userId: "",
      userName: "",
      credits: "",
      freeDays: "",
      joursGratuits: "",
      selected: "",
      previousJoursGratuits: 0,
      previousCredits: 0,
      is_account_active: true,

      icon: `
          <svg id="groups_black_24dp" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36">
            <rect id="Rectangle_1884" data-name="Rectangle 1884" width="36" height="36" fill="none"/>
            <g id="Groupe_14074" data-name="Groupe 14074" transform="translate(0 9)">
              <path id="Tracé_19688" data-name="Tracé 19688" d="M18,16.125a15.916,15.916,0,0,1,6.36,1.35A4.477,4.477,0,0,1,27,21.57V24H9V21.585a4.445,4.445,0,0,1,2.64-4.1A15.661,15.661,0,0,1,18,16.125ZM6,16.5a3,3,0,1,0-3-3A3.009,3.009,0,0,0,6,16.5Zm1.7,1.65A10.474,10.474,0,0,0,6,18a10.426,10.426,0,0,0-4.17.87A3.016,3.016,0,0,0,0,21.645V24H6.75V21.585A6.748,6.748,0,0,1,7.7,18.15ZM30,16.5a3,3,0,1,0-3-3A3.009,3.009,0,0,0,30,16.5Zm6,5.145a3.016,3.016,0,0,0-1.83-2.775,10.2,10.2,0,0,0-5.865-.72,6.748,6.748,0,0,1,.945,3.435V24H36ZM18,6a4.5,4.5,0,1,1-4.5,4.5A4.494,4.494,0,0,1,18,6Z" transform="translate(0 -6)" fill="#242c36"/>
            </g>
          </svg>
        `,
      menuItems: MenuGestion,

      rowsPerPage: 3,
      showDialogAboModifie: false,
      showDialogCredit: false,
      showDialogAbonnement: false,
      dialogName: "",
      getId: "",
      loading: false,
      showDialogAjoutReussi: false,
      showDialogEnlevementReussi: false,
      showDialogAjoutJourReussi: false,
      showDialogEnlevementJourReussi: false,
      showDialogJour: false,
      renewAuto: true,
      dateValidity: null,
      iconModifJours: `
            <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
              <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
              <g id="Groupe_14044" data-name="Groupe 14044" transform="translate(7.629 7.705)">
                <path id="Tracé_19671" data-name="Tracé 19671" d="M162.639,159.613c-.275.33-.533.678-.829.989q-11.931,12.529-23.869,25.051c-.421.441-.864.832-1.531.57a1.752,1.752,0,0,1-.578-.384q-5.724-5.708-11.435-11.43a1.188,1.188,0,0,1-.324-1.459,1.086,1.086,0,0,1,1.252-.616,1.949,1.949,0,0,1,.833.51q5.108,5.078,10.193,10.179c.129.129.264.251.35.333.38-.348.757-.656,1.091-1.005q11.327-11.852,22.646-23.712a1.218,1.218,0,0,1,1.846-.205,3.765,3.765,0,0,1,.355.474Z" transform="translate(-104.921 -133.831)" fill="#f8bd25"/>
                <path id="Tracé_19672" data-name="Tracé 19672" d="M38.362,76.742q-1.469,0-2.941-.112A38.363,38.363,0,1,1,69.557,60.736a1.5,1.5,0,1,1-2.434-1.75,35.373,35.373,0,1,0-8.136,8.137,1.5,1.5,0,1,1,1.749,2.434A38.365,38.365,0,0,1,38.362,76.742Z" transform="translate(0 0)" fill="#242c36"/>
                <path id="Tracé_19673" data-name="Tracé 19673" d="M411.609,413.108a1.5,1.5,0,1,1,1.06-.439A1.51,1.51,0,0,1,411.609,413.108Z" transform="translate(-347.165 -347.165)" fill="#242c36"/>
              </g>
            </svg>


        `,
      page: 1,
      size: 5,
    };
  },
  async mounted() {
    await this.loadUsers();
    await this.loadSubscriptions();
    await this.loadCouples();
    this.checkUsersData();
  },
  watch: {
    async page() {
      await this.loadUsers();
    },
    async size() {
      await this.loadUsers();
    },
    async search() {
      await this.loadUsers();
      if (!this.users.length) {
        this.error = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.error = "";
        this.visible = false;
      }
    },
  },
  computed: {
    users() {
      return this.$store.state.user.users.results;
    },
    dataSize() {
      return this.$store.state.user.users.count;
    },
    next() {
      return this.$store.state.user.users.next;
    },
    subscriptions() {
      return this.$store.state.subscription.subscriptions;
    },
  },
  created() {
    document.title = this.$route.meta.title;
  },
};
</script>

<style></style>
<style scoped>
.user_list-table .table-container {
  height: auto;
  /* max-height: calc(100vh - 305px); */
}
a {
  text-decoration: underline;
}
.liste-des-utilisateurs {
  padding: 0;
}
.table-toolbar {
  background-color: #f6f6f7 !important;
  border-radius: 4px;
  min-height: 42px;
}
.titre-search {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0.15px;
  color: #5c626a;
}
.table-wrapper {
  /* border-radius: 8px;
    border: 1px solid #d3d4d6 !important; */
  overflow: hidden;
}
.input-search {
  background-color: #f6f6f7;
  border-radius: 4px;
  color: var(--placeholder);
}
.predict-table .increase,
.predict-table .increase path {
  color: #21a179;
  fill: #21a179;
}
.predict-table .decrease,
.predict-table .decrease path {
  color: var(--rouge);
  fill: var(--rouge);
}
.predict-table {
  border-radius: 8px;
}
.table-header {
  background-color: var(--black) !important;
}
.jaune {
  color: var(--primary);
  fill: var(--primary);
}
.vert {
  fill: #21a179;
  color: #21a179;
}
.predict-table .status-badge {
  margin-top: -10px;
}
.predict-table .status-badge,
.grise {
  color: var(--placeholder);
  fill: var(--placeholder);
}
.table-tri {
  width: 15.5px;
  height: 100%;
  margin: 5px;
}
.table-tri button {
  width: 100%;
  min-width: auto;
  margin: 0;
  height: auto;
}
.table-tri button.arrow-down svg {
  transform: translate(0, -2px);
}
.table-tri button.arrow-up svg {
  transform: translate(0, 2px);
}
.table-tri button.active path,
.table-tri button:hover path {
  fill: var(--primary);
}
.titre-recherche {
  color: #5c626a;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
}
.help-recherche {
  color: var(--black);
  font-size: 14px;
}
.form-abonnement .submit-dialog {
  width: 100% !important;
}
.align-text {
  text-align: center;
}
@media (max-width: 639px) {
  .filter-bloc {
    padding-left: 0 !important;
    /* padding-right: 0 !important; */
  }
}
@media (max-width: 639px) {
  .filter-bloc .md-field {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }
}
@media (max-width: 639px) {
  .filter-bloc .md-field input {
    font-size: 14px !important;
    padding: 6px 0.5rem !important;
    width: calc(100% - 32px);
  }
}
@media (max-width: 479px) {
  .filter-bloc .md-field input {
    font-size: 12px !important;
  }
}
@media (max-width: 639px) {
  .filter-bloc .md-field svg {
    margin-right: 0 !important;
    width: 16px;
    min-width: 16px;
  }
}
.filter-bloc .md-field.md-has-value svg {
  display: none;
}
@media (max-width: 639px) {
  .filter-bloc .md-field .md-input::-webkit-input-placeholder,
  .filter-bloc .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 14px !important;
  }
}
@media (max-width: 479px) {
  .filter-bloc .md-field .md-input::-webkit-input-placeholder,
  .filter-bloc .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 12px !important;
  }
}

.user_list-table .user_col {
  max-width: 10%;
}
.user_list-table .subscribe_col {
  width: 5%;
}
.user_list-table .date_col {
  width: 5%;
}
.user_list-table .credits_col {
  width: 5%;
}
.user_list-table .freeDays_col {
  width: 5%;
}
.user_list-table .suspend_col {
  text-align: center;
  width: 15%;
}
</style>
