<template lang="">
  <div class="dashboard">
    <PermanentFull
      :titre="$t('codeReduction')"
      :icon="icon"
      :menuItems="menuItems"
      :admin="true"
    >
      <!-- Loader -->
      <div class="loader-content" v-if="loader">
        <p class="msg">{{ $t("loading") }}</p>
        <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
      </div>
      <!-- /Loader -->
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div class="pt-4 flex-grow-1 d-flex flex-column">
          <div class="liste-des-reductions">
            <div
              class="d-flex flex-wrap justify-content-between align-items-center"
            >
              <div class="left mb-2 mb-md-0">
                <h3 class="titre-recherche">{{ $t("search") }}</h3>
                <span class="help-recherche">{{ $t("searchCodeText") }}</span>
              </div>

              <div class="right">
                <md-button
                  class="submit-dialog text-center btn-submit text-normal w-100 py-0 m-0"
                  @click="toggleDialogAddReduction()"
                >
                  <md-icon class="text-white">add</md-icon>
                  {{ $t("addCodeReduction") }}
                </md-button>
              </div>
            </div>
            <div class="table-wrapper flex-grow">
              <md-table
                md-table-fixed-header
                class="mt-3 predict-table codeReduce-table d-flex"
              >
                <md-table-toolbar class="filter-bloc px-2 mb-3">
                  <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                    <md-input
                      :placeholder="$t('discount:searchCode')"
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
                        id="Search"
                        d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                        transform="translate(-570 -2016)"
                        fill="#242c36"
                      />
                    </svg>
                  </md-field>
                </md-table-toolbar>

                <div class="table-container">
                  <md-table-row class="table-header">
                    <md-table-head scope="col" class="reductionName_col">
                      {{ $t("codeReductionName") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('code_name')"
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
                          v-on:click="orderBy('-' + 'code_name')"
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
                    <md-table-head scope="col" class="code_col">
                      {{ $t("code") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('code')"
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
                          v-on:click="orderBy('-' + 'code')"
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
                    <md-table-head scope="col" class="dateAdd_col">
                      {{ $t("dateAdded") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('created_at')"
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
                          v-on:click="orderBy('-' + 'created_at')"
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
                    <md-table-head scope="col" class="dateExpiry_col">
                      {{ $t("expirationDate") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('expiry_at')"
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
                          v-on:click="orderBy('-' + 'expiry_at')"
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
                    <md-table-head scope="col" class="reduce_col">
                      {{ $t("reduction") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('reduction')"
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
                          v-on:click="orderBy('-' + 'reduction')"
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
                          v-on:click="orderBy('client_is_subscribed')"
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
                          v-on:click="orderBy('-' + 'client_is_subscribed')"
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
                    <md-table-head scope="col" class="user_col">
                      {{ $t("users") }}
                      <span class="table-tri d-flex flex-column"> </span>
                    </md-table-head>
                    <md-table-head
                      scope="col"
                      class="action_col"
                    ></md-table-head>
                  </md-table-row>
                  <md-table-row
                    v-for="(item, index) in reductions"
                    :key="index"
                  >
                    <md-table-cell
                      class="reductionName_col"
                      :data-label="$t('codeReductionName')"
                    >
                      {{ item.code_name }}
                    </md-table-cell>
                    <md-table-cell class="code_col" :data-label="$t('code')">
                      {{ item.code }}
                    </md-table-cell>
                    <md-table-cell
                      class="dateAdd_col"
                      :data-label="$t('dateAdded')"
                    >
                      {{ formatDate($t("dateFormat"), item.created_at) }}
                    </md-table-cell>
                    <md-table-cell
                      class="dateExpiry_col"
                      :data-label="$t('expirationDate')"
                    >
                      {{ formatDate($t("dateFormat"), item.expiry_at) }}
                    </md-table-cell>
                    <md-table-cell class="reduce_col" data-label="Réduction">
                      {{ pointToComma(item.reduction) }} %
                    </md-table-cell>
                    <md-table-cell
                      class="subscribe_col"
                      :data-label="$t('users')"
                    >
                      {{
                        !item.subscribes.length
                          ? $t("allSubscriptions")
                          : displayArraySubscribe(item.subscribes)
                      }}
                    </md-table-cell>
                    <md-table-cell
                      class="user_col"
                      :data-label="$t('subscription')"
                    >
                      {{
                        !item.clients.length
                          ? $t("allUsers")
                          : displayArrayUser(item.clients)
                      }}
                    </md-table-cell>
                    <md-table-cell class="action_col" data-label="">
                      <div class="d-flex align-items-center">
                        <md-button
                          class="text-center w-100 text-normal btn-modifier"
                          :md-ripple="false"
                          @click="toggleDialogConfirm(item)"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="14"
                            height="14"
                            viewBox="0 0 14 14"
                            class="mr-2"
                          >
                            <path
                              id="Tracé_2542"
                              data-name="Tracé 2542"
                              d="M19,6.41,17.59,5,12,10.59,6.41,5,5,6.41,10.59,12,5,17.59,6.41,19,12,13.41,17.59,19,19,17.59,13.41,12Z"
                              transform="translate(-5 -5)"
                              fill="#242c36"
                            /></svg
                          >{{ $t("delete") }}
                        </md-button>
                        <md-button
                          class="text-center w-100 text-normal btn-modifier"
                          v-on:click="toggleDialogModifReduction(item)"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="18.002"
                            height="18.003"
                            viewBox="0 0 18.002 18.003"
                            class="mr-2"
                          >
                            <path
                              id="Tracé_42500"
                              data-name="Tracé 42500"
                              d="M3,17.25V21H6.75L17.81,9.94,14.06,6.19ZM20.71,7.04a1,1,0,0,0,0-1.41L18.37,3.29a1,1,0,0,0-1.41,0L15.13,5.12l3.75,3.75,1.83-1.83Z"
                              transform="translate(-3 -2.998)"
                              fill="#242c36"
                            /></svg
                          >{{ $t("modify") }}
                        </md-button>
                      </div>
                    </md-table-cell>
                  </md-table-row>
                  <md-table-row v-if="this.visible" class="empty-data">
                    <md-table-cell :colspan="9" class="align-text">{{
                      this.error
                    }}</md-table-cell></md-table-row
                  >
                  <md-table-row class="pagination-row" v-if="!visible">
                    <md-table-cell :colspan="9">
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
        :showDialog="showDialogAddReduction"
        :dialogName="$t('addDiscount')"
        @close="showDialogAddReduction = !showDialogAddReduction"
      >
        <md-steppers :md-active-step.sync="active" class="pt-3 pb-4">
          <md-step
            id="first"
            :md-label="$t('definition')"
            :md-done.sync="first"
          >
            <form
              action=""
              class="form-abonnement step-1 w-100 mt-3"
              style="max-width: 501px;"
            >
              <div class="form-group">
                <md-field>
                  <label>{{ $t("codeReductionName") }}</label>
                  <md-input
                    v-model="code_name"
                    :class="errorCodeNameRequired.length && 'error-input'"
                  ></md-input>
                </md-field>
                <span
                  class="error"
                  v-for="error in errorCodeNameRequired"
                  :key="error"
                  >{{ error }}</span
                >
              </div>
              <p>
                {{ $t("personalizeCode") }}
              </p>
              <div class="form-group">
                <md-field class="d-flex align-items-center position-relative">
                  <label>{{ $t("form:codeReduction") }}</label>
                  <md-input
                    v-model="code"
                    :class="errorCodeRequired.length && 'error-input'"
                  ></md-input>
                  <md-icon class="custom-icon position-absolute">
                    <md-button @click="generateCode()">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="22"
                        viewBox="0 0 16 22"
                      >
                        <path
                          id="Tracé_42557"
                          data-name="Tracé 42557"
                          d="M12,6V9l4-4L12,1V4A7.986,7.986,0,0,0,5.24,16.26L6.7,14.8A5.87,5.87,0,0,1,6,12,6,6,0,0,1,12,6Zm6.76,1.74L17.3,9.2A5.99,5.99,0,0,1,12,18V15L8,19l4,4V20A7.986,7.986,0,0,0,18.76,7.74Z"
                          transform="translate(-4 -1)"
                          fill="#242c36"
                        />
                      </svg> </md-button
                  ></md-icon>
                </md-field>
                <span
                  class="error"
                  v-for="error in errorCodeRequired"
                  :key="error"
                  >{{ error }}</span
                >
              </div>
              <div class="form-group">
                <md-datepicker
                  v-model="expiry_at"
                  class="d-flex date-picker align-items-center"
                  :md-disabled-dates="isPreviousDate"
                >
                  <label>{{ $t("expirationDate") }}</label>
                </md-datepicker>
                <span class="error">{{ errorExpiryAtRequired }}</span>
              </div>
              <div class="form-group">
                <md-field class="d-flex align-items-center position-relative">
                  <label>{{ $t("reduction") }}</label>
                  <md-input
                    v-model="reduction"
                    type="number"
                    :class="errorReductionRequired.length && 'error-input'"
                    @keypress="handleNegativeNumber"
                  ></md-input>
                  <md-icon class="custom-icon position-absolute">
                    %
                  </md-icon>
                </md-field>
                <span class="error">{{ errorReductionRequired }}</span>
              </div>

              <div class="w-100 text-center">
                <md-button
                  class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
                  @click="checkForm()"
                >
                  {{ $t("next") }}
                </md-button>
              </div>
            </form>
          </md-step>

          <md-step
            id="second"
            :md-label="$t('subscription')"
            :md-done.sync="second"
          >
            <form
              action=""
              class="form-abonnement step-2 w-100 mt-3"
              style="max-width: 501px;"
            >
              <div class="form-group">
                <div class="d-flex flex-wrap align-items-center">
                  <md-radio v-model="definePaire" :value="false">{{
                    $t("allSubscriptions")
                  }}</md-radio>
                  <md-radio v-model="definePaire" :value="true">{{
                    $t("selectOneOrMore")
                  }}</md-radio>
                </div>
              </div>
              <div
                v-if="definePaire === false"
                class="form-group toutAbobloc d-flex align-items-center justify-content-center"
                style="min-height:302px"
              >
                <p class="text-center" style="max-width: 409px">
                  {{ $t("discountAppliedTo") }}
                  <strong>{{ $t("allSubscriptions") }}</strong
                  >.
                </p>
              </div>
              <div v-else class="form-group search-wrapper">
                <span class="error">{{ errorSubscriptionList }}</span>
                <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                  <md-input
                    :placeholder="$t('discount:searchSubscription')"
                    class="input-search border-0 mb-2"
                    v-model="searchSubscribption"
                  />
                  <svg
                    class="mr-2 position-absolute"
                    xmlns="http://www.w3.org/2000/svg"
                    width="16.395"
                    height="16.395"
                    viewBox="0 0 16.395 16.395"
                  >
                    <path
                      id="Search"
                      d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                      transform="translate(-570 -2016)"
                      fill="#242c36"
                    />
                  </svg>
                </md-field>
                <span class="error">{{ this.checkErrorSubscription }}</span>
                <div
                  class="w-100 mt-1"
                  v-for="(item, index) in subscriptionsList"
                  :key="index"
                >
                  <md-checkbox
                    :value="item.id"
                    v-model="array"
                    class="d-flex flex-row-reverse justify-content-between w-100 my-1"
                    >{{ item.name }}</md-checkbox
                  >
                </div>
              </div>
              <div class="w-100 text-center d-flex align-items-center">
                <div class="w-50 mr-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-return text-uppercase h-auto m-0"
                    @click="setDone('second', 'first')"
                  >
                    {{ $t("back") }}
                  </md-button>
                </div>
                <div class="w-50 ml-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
                    @click="checkSubscription()"
                  >
                    {{ $t("next") }}
                  </md-button>
                </div>
              </div>
            </form>
          </md-step>

          <md-step id="third" :md-label="$t('user')" :md-done.sync="third">
            <form
              action=""
              class="form-abonnement step-2 w-100 mt-3"
              style="max-width: 501px;"
            >
              <div class="form-group">
                <div class="d-flex flex-wrap align-items-center">
                  <md-radio v-model="defineUsers" :value="false">{{
                    $t("allUsers")
                  }}</md-radio>
                  <md-radio v-model="defineUsers" :value="true">{{
                    $t("selectOneOrMore")
                  }}</md-radio>
                </div>
              </div>
              <div
                v-if="defineUsers === false"
                class="form-group toutAbobloc d-flex align-items-center justify-content-center"
                style="min-height:302px"
              >
                <p class="text-center" style="max-width: 409px">
                  {{ $t("discountAppliedTo") }}
                  <strong>{{ $t("allUsers") }}</strong
                  >.
                </p>
              </div>
              <div v-else class="form-group search-wrapper">
                <span class="error">{{ errorUserList }}</span>
                <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                  <md-input
                    :placeholder="$t('discount:searchUser')"
                    class="input-search border-0 mb-2"
                    v-model="searchUser"
                  />
                  <svg
                    class="mr-2 position-absolute"
                    xmlns="http://www.w3.org/2000/svg"
                    width="16.395"
                    height="16.395"
                    viewBox="0 0 16.395 16.395"
                  >
                    <path
                      id="Search"
                      d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                      transform="translate(-570 -2016)"
                      fill="#242c36"
                    />
                  </svg>
                </md-field>
                <span class="error">{{ this.checkErrorUser }}</span>
                <div
                  class="w-100 mt-1"
                  v-for="(item, index) in this.userList"
                  :key="index"
                >
                  <md-checkbox
                    v-model="arrayUser"
                    :value="item.client.id"
                    class="d-flex flex-row-reverse justify-content-between w-100 my-1"
                    >{{ item.client.firstname }} {{ item.client.lastname }}
                  </md-checkbox>
                </div>
              </div>
              <div class="w-100 text-center d-flex align-items-center">
                <div class="w-50 mr-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-return text-uppercase h-auto m-0"
                    @click="setDone('second', 'first')"
                  >
                    {{ $t("back") }}
                  </md-button>
                </div>
                <div class="w-50 ml-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
                    @click="checkUser()"
                  >
                    {{ $t("add") }}
                  </md-button>
                </div>
              </div>
            </form>
          </md-step>
        </md-steppers>
      </Dialog>
      <Dialog
        :showDialog="showDialogAjoutReussi"
        :titreDialog="$t('addSuccess')"
        :iconDialog="iconModifJours"
        @close="showDialogAjoutReussi = !showDialogAjoutReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("addDiscountSuccess") }}
          <strong>{{ this.code_name }}</strong> {{ $t("addDiscountSuccess1") }}
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
        :showDialog="showDialogModifReduction"
        :dialogName="$t('updateDiscountDialog')"
        @close="showDialogModifReduction = !showDialogModifReduction"
      >
        <md-steppers :md-active-step.sync="active" class="pt-3 pb-4">
          <md-step
            id="first"
            :md-label="$t('definition')"
            :md-done.sync="first"
          >
            <form
              action=""
              class="form-abonnement step-1 w-100 mt-3"
              style="max-width: 501px;"
            >
              <div class="form-group">
                <md-field>
                  <label>{{ $t("codeReductionName") }}</label>
                  <md-input
                    v-model="code_name"
                    :class="errorCodeNameRequired.length && 'error-input'"
                  ></md-input>
                </md-field>
                <span
                  class="error"
                  v-for="error in errorCodeNameRequired"
                  :key="error"
                  >{{ error }}</span
                >
              </div>
              <p>
                {{ $t("personalizeCode") }}
              </p>
              <div class="form-group">
                <md-field class="d-flex align-items-center position-relative">
                  <label>{{ $t("form:codeReduction") }}</label>
                  <md-input
                    v-model="code"
                    :class="errorCodeRequired.length && 'error-input'"
                  ></md-input>
                  <md-icon class="custom-icon position-absolute">
                    <md-button @click="generateCode()">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="22"
                        viewBox="0 0 16 22"
                      >
                        <path
                          id="Tracé_42557"
                          data-name="Tracé 42557"
                          d="M12,6V9l4-4L12,1V4A7.986,7.986,0,0,0,5.24,16.26L6.7,14.8A5.87,5.87,0,0,1,6,12,6,6,0,0,1,12,6Zm6.76,1.74L17.3,9.2A5.99,5.99,0,0,1,12,18V15L8,19l4,4V20A7.986,7.986,0,0,0,18.76,7.74Z"
                          transform="translate(-4 -1)"
                          fill="#242c36"
                        />
                      </svg>
                    </md-button>
                  </md-icon>
                </md-field>
                <span
                  class="error"
                  v-for="error in errorCodeRequired"
                  :key="error"
                  >{{ error }}</span
                >
              </div>
              <div class="form-group">
                <md-datepicker
                  v-model="expiry_at"
                  :class="'d-flex date-picker align-items-center'"
                  :md-disabled-dates="isPreviousDate"
                >
                  <label>{{ $t("expirationDate") }}</label>
                </md-datepicker>
                <span class="error">{{ errorExpiryAtRequired }}</span>
              </div>
              <div class="form-group">
                <md-field class="d-flex align-items-center position-relative">
                  <label>{{ $t("reduction") }}</label>
                  <md-input
                    v-model="reduction"
                    type="number"
                    :class="errorReductionRequired.length && 'error-input'"
                    @keypress="handleNegativeNumber"
                  ></md-input>
                  <md-icon class="custom-icon position-absolute">
                    %
                  </md-icon>
                </md-field>
                <span class="error">{{ errorReductionRequired }}</span>
              </div>

              <div class="w-100 text-center">
                <md-button
                  class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
                  @click="checkForm()"
                >
                  {{ $t("next") }}
                </md-button>
              </div>
            </form>
          </md-step>

          <md-step
            id="second"
            :md-label="$t('subscription')"
            :md-done.sync="second"
          >
            <form
              action=""
              class="form-abonnement step-2 w-100 mt-3"
              style="max-width: 501px;"
            >
              <div class="form-group">
                <div class="d-flex flex-wrap align-items-center">
                  <md-radio v-model="definePaire" :value="false">{{
                    $t("allSubscriptions")
                  }}</md-radio>
                  <md-radio v-model="definePaire" :value="true">{{
                    $t("selectOneOrMore")
                  }}</md-radio>
                </div>
              </div>
              <div
                v-if="definePaire === false"
                class="form-group toutAbobloc d-flex align-items-center justify-content-center"
                style="min-height:302px"
              >
                <p class="text-center" style="max-width: 409px">
                  {{ $t("discountAppliedTo") }}
                  <strong>{{ $t("allSubscriptions") }}</strong>
                </p>
              </div>
              <div v-else class="form-group search-wrapper">
                <span class="error">{{ errorSubscriptionList }}</span>
                <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                  <md-input
                    :placeholder="$t('discount:searchSubscription')"
                    class="input-search border-0 mb-2"
                    v-model="searchSubscribption"
                  />
                  <svg
                    class="mr-2 position-absolute"
                    xmlns="http://www.w3.org/2000/svg"
                    width="16.395"
                    height="16.395"
                    viewBox="0 0 16.395 16.395"
                  >
                    <path
                      id="Search"
                      d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                      transform="translate(-570 -2016)"
                      fill="#242c36"
                    />
                  </svg>
                </md-field>
                <span class="error">{{ this.checkErrorSubscription }}</span>
                <div
                  class="w-100 mt-1"
                  v-for="(item, index) in subscriptionsList"
                  :key="index"
                >
                  <md-checkbox
                    :value="item.id"
                    v-model="array"
                    class="d-flex flex-row-reverse justify-content-between w-100 my-1"
                    >{{ item.name }}</md-checkbox
                  >
                </div>
              </div>
              <div class="w-100 text-center d-flex align-items-center">
                <div class="w-50 mr-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-return text-uppercase h-auto m-0"
                    @click="setDone('second', 'first')"
                  >
                    {{ $t("back") }}
                  </md-button>
                </div>
                <div class="w-50 ml-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
                    @click="checkSubscription()"
                  >
                    {{ $t("next") }}
                  </md-button>
                </div>
              </div>
            </form>
          </md-step>

          <md-step id="third" :md-label="$t('user')">
            <form
              action=""
              class="form-abonnement step-2 w-100 mt-3"
              style="max-width: 501px;"
            >
              <div class="form-group">
                <div class="d-flex flex-wrap align-items-center">
                  <md-radio v-model="defineUsers" :value="false">{{
                    $t("allUsers")
                  }}</md-radio>
                  <md-radio v-model="defineUsers" :value="true">{{
                    $t("selectOneOrMore")
                  }}</md-radio>
                </div>
              </div>
              <div
                v-if="defineUsers === false"
                class="form-group toutAbobloc d-flex align-items-center justify-content-center"
                style="min-height:302px"
              >
                <p class="text-center" style="max-width: 409px">
                  {{ $t("discountAppliedTo") }}
                  <strong>{{ $t("allUsers") }}</strong
                  >.
                </p>
              </div>
              <div v-else class="form-group search-wrapper">
                <span class="error">{{ errorUserList }}</span>
                <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                  <md-input
                    :placeholder="$t('discount:searchUser')"
                    class="input-search border-0 mb-2"
                    v-model="searchUser"
                  />
                  <svg
                    class="mr-2 position-absolute"
                    xmlns="http://www.w3.org/2000/svg"
                    width="16.395"
                    height="16.395"
                    viewBox="0 0 16.395 16.395"
                  >
                    <path
                      id="Search"
                      d="M586.1,2032.1a1.025,1.025,0,0,1-1.448,0l-3.221-3.222a7.16,7.16,0,1,1,1.446-1.447l3.222,3.222a1.024,1.024,0,0,1,0,1.446m-5.319-12.552a5.114,5.114,0,1,0,0,7.233,5.113,5.113,0,0,0,0-7.233"
                      transform="translate(-570 -2016)"
                      fill="#242c36"
                    />
                  </svg>
                </md-field>
                <span class="error">{{ this.checkErrorUser }}</span>
                <div
                  class="w-100 mt-1"
                  v-for="(item, index) in userList"
                  :key="index"
                >
                  <md-checkbox
                    :value="item.client.id"
                    v-model="arrayUser"
                    class="d-flex flex-row-reverse justify-content-between w-100 my-1"
                    >{{ item.client.firstname }}
                    {{ item.client.lastname }}</md-checkbox
                  >
                </div>
              </div>
              <div class="w-100 text-center d-flex align-items-center">
                <div class="w-50 mr-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-return text-uppercase h-auto m-0"
                    @click="setDone('second', 'first')"
                  >
                    {{ $t("back") }}
                  </md-button>
                </div>
                <div class="w-50 ml-1">
                  <md-button
                    class="submit-dialog bigBtn text-center btn-submit text-uppercase h-auto m-0"
                    @click="checkUserUpdate()"
                  >
                    {{ $t("modify") }}
                  </md-button>
                </div>
              </div>
            </form>
          </md-step>
        </md-steppers>
      </Dialog>
      <Dialog
        :showDialog="showDialogModifReussi"
        :titreDialog="$t('successModification')"
        :iconDialog="iconModifJours"
        @close="showDialogModifReussi = !showDialogModifReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("discount:successMessage1") }}
          <strong>{{ this.code_name }}</strong>
          {{ $t("discount:successMessage2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogModifReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>
      <Dialog
        :showDialog="showDialogConfirm"
        :titreDialog="$t('confirmChoice')"
        :iconDialog="iconModifJours"
        @close="showDialogConfirm = !showDialogConfirm"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("confirmMessage") }}
          <strong>{{ this.codeToDelete }} ?</strong>
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-1"
            @click="deleteReduction(codeId)"
          >
            {{ $t("confirm") }}
          </md-button>
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-1"
            @click="showDialogConfirm = !showDialogConfirm"
          >
            {{ $t("cancel") }}
          </md-button>
        </div>
      </Dialog>
    </PermanentFull>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import Dialog from "../Dialog/Dialog.vue";
import MenuGestion from "../../data/MenuGestion.js";
import moment from "moment";
import { formatDate } from "../../utils/Constant";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
  name: "CodeReduction",
  components: {
    PermanentFull,
    Dialog,
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
    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
    checkReductionsPairData() {
      if (!this.reductions.length) {
        this.error = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },
    handleNegativeNumber(e) {
      if (e.charCode >= 48 && e.charCode <= 57) {
        return true;
      }
      return e.preventDefault();
    },
    checkSubscription() {
      if (this.definePaire) {
        if (this.array.length == 0) {
          this.checkErrorSubscription = this.$t("checkSubscription");
        } else {
          this.checkErrorSubscription = "";
          this.setDone("second", "third");
        }
      } else this.setDone("second", "third");
    },
    checkUser() {
      if (this.defineUsers) {
        if (this.arrayUser.length == 0) {
          this.checkErrorUser = this.$t("checkUser");
        } else {
          this.checkErrorUser = "";
          this.addReduction();
        }
      } else this.addReduction();
    },
    checkUserUpdate() {
      if (this.defineUsers) {
        if (this.arrayUser.length == 0) {
          this.checkErrorUser = this.$t("checkUser");
        } else {
          this.checkErrorUser = "";
          this.updateReduction();
        }
      } else this.updateReduction();
    },
    setAllFalse() {
      this.showDialogAddReduction = false;
      this.showDialogAjoutReussi = false;
      this.showDialogModifReduction = false;
      this.showDialogModifReussi = false;
      this.showDialogConfirm = false;
    },
    toggleDialogAddReduction() {
      this.setAllFalse();
      this.setDone("first", "first");
      this.initForm();
      this.showDialogAddReduction = !this.showDialogAddReduction;
    },
    toogleDialogAjoutReussi() {
      this.setAllFalse();
      this.showDialogAjoutReussi = !this.showDialogAjoutReussi;
    },
    toggleDialogModifReduction(item) {
      this.setAllFalse();
      this.setDone("first", "first");
      this.initModif(item);
      this.showDialogModifReduction = !this.showDialogModifReduction;
    },
    toogleDialogModifReussi() {
      this.setAllFalse();
      this.showDialogModifReussi = !this.showDialogModifReussi;
    },

    toggleDialogConfirm(item) {
      this.setAllFalse();
      this.codeToDelete = item.code_name;
      this.codeId = item.id;
      this.showDialogConfirm = !this.showDialogConfirm;
    },
    setDone(id, index) {
      this[id] = true;

      if (index) {
        this.active = index;
      }
    },

    setError() {
      this.secondStepError = "This is an error!";
    },
    orderBy: async function(field) {
      await this.$store.dispatch("loadReductions", {
        token: localStorage.getItem("adminToken"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    loadReductions: async function() {
      this.loader = true;
      await this.$store.dispatch("loadReductions", {
        token: localStorage.getItem("adminToken"),
        order: "-created_at",
        page: this.page,
        search: this.search,
        size: this.size,
      });
      this.loader = false;
    },
    deleteReduction: async function(item) {
      try {
        await this.$store.dispatch("deleteReduction", {
          id: +item,
          token: localStorage.getItem("adminToken"),
        });
        this.loadReductions();
        this.showDialogConfirm = !this.showDialogConfirm;
      } catch (e) {
        //
      }
    },
    addReduction: async function() {
      const payload = {
        code_name: this.code_name,
        code: this.code,
        clients: this.arrayUser,
        subscribes: this.array,
        reduction: +this.reduction,
        expiry: this.formatDateUpdate(this.expiry_at),
      };
      try {
        await this.$store.dispatch("addReduction", {
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
        this.toogleDialogAjoutReussi();
      } catch (e) {
        //
      }
      this.loadReductions();
    },
    updateReduction: async function() {
      const payload = {
        code_name: this.code_name,
        code: this.code,
        clients: this.arrayUser,
        subscribes: this.array,
        reduction: +this.reduction,
        expiry: this.formatDateUpdate(this.expiry_at),
      };
      try {
        await this.$store.dispatch("updateReduction", {
          id: this.id,
          payload: payload,
          token: localStorage.getItem("adminToken"),
        });
        this.toogleDialogModifReussi();
      } catch (e) {
        //
      }
      this.loadReductions();
    },
    displayArraySubscribe: function(item) {
      return item.map((a) => a.name).join(", ");
    },
    displayArrayUser: function(item) {
      return item.map((a) => a.full_name).join(", ");
    },
    formatDateUpdate(item) {
      return moment(item, this.$t("dateFormat")).format("YYYY-MM-DD HH:mm:ss");
    },
    initForm: function() {
      this.code_name = "";
      this.code = "";
      this.arrayUser = [];
      this.array = [];
      this.reduction = "";
      this.expiry_at = null;
      this.errorCodeNameRequired = [];
      this.errorCodeRequired = [];
      this.errorExpiryAtRequired = "";
      this.errorReductionRequired = "";
    },
    initModif(item) {
      this.id = item?.id;
      this.code_name = item.code_name;
      this.code = item.code;
      this.reduction = item.reduction;
      this.expiry_at = moment(item.expiry_at).format(this.$t("dateFormat"));
      this.array = item.subscribes.map((subscribe) => subscribe.id);
      this.arrayUser = item.clients.map((user) => user.id);
      this.definePaire = this.array.length ? true : false;
      this.defineUsers = this.arrayUser.length ? true : false;
      this.searchUser = "";
      this.searchSubscribption = "";
      this.errorCodeNameRequired = [];
      this.errorCodeRequired = [];
      this.errorExpiryAtRequired = "";
      this.errorReductionRequired = "";
    },
    generateCode() {
      this.code = (Math.random() + 1).toString(36).substr(2, 7);
    },
    loadSubscriptionList: async function() {
      await this.$store.dispatch("loadSubscriptions", {
        token: localStorage.getItem("adminToken"),
        order: "",
        page: "",
        search: this.searchSubscribption,
        size: "",
      });
    },
    loadUserList: async function() {
      await this.$store.dispatch("loadUsers", {
        token: localStorage.getItem("adminToken"),
        order: "",
        page: "",
        search: this.searchUser,
        size: "",
      });
    },
    checkForm() {
      this.errorCodeNameRequired = [];
      this.errorCodeRequired = [];
      this.errorExpiryAtRequired = "";
      this.errorReductionRequired = "";
      if (!this.code_name) {
        this.errorCodeNameRequired.push(this.$t("errorCodeNameRequired"));
      }
      if (!this.code) {
        this.errorCodeRequired.push(this.$t("errorCodeRequired"));
      }
      if (this.expiry_at == null) {
        this.errorExpiryAtRequired = this.$t("errorExpiryAtRequired");
      }
      if (!this.reduction) {
        this.errorReductionRequired = this.$t("errorReductionRequired");
      }
      if (100 < this.reduction) {
        this.errorReductionRequired = this.$t("errorInvalid");
      }
      if (
        this.code_name &&
        this.code &&
        this.expiry_at != null &&
        this.reduction &&
        100 > this.reduction
      )
        this.setDone("first", "second");
    },
    isPreviousDate(date) {
      const dateNow = new Date();
      dateNow.setDate(dateNow.getDate() - 1);
      return date < dateNow;
    },
  },
  data: () => {
    return {
      checkErrorSubscription: "",
      checkErrorUser: "",
      search: "",
      id: "",
      name: "",
      code_name: "",
      price: 0,
      reduction: 0,
      array: [],
      arrayUser: [],
      is_active: true,
      created_at: "",
      code: null,
      expiry_at: null,
      codeToDelete: "",
      codeId: 0,
      page: 1,
      size: 5,
      total: 0,
      loader: false,
      visible: false,
      discover: false,
      petitTrader: true,
      pro: false,
      trader: true,
      definePaire: false,
      defineUsers: false,
      dre: true,
      douglas: false,
      subscriptions: [],
      users: [],
      searchUser: "",
      searchSubscribption: "",
      errorSubscriptionList: "",
      errorUserList: "",
      error: "",
      errorCodeNameRequired: [],
      errorCodeRequired: [],
      errorInvalid: "",
      errorExpiryAtRequired: "",
      errorReductionRequired: "",
      icon: `
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 17.272 18">
        <path id="Tracé_42553" data-name="Tracé 42553" d="M26.8,9.231a.527.527,0,0,1,0-.466l.671-1.373a1.563,1.563,0,0,0-.674-2.075L25.445,4.6a.528.528,0,0,1-.274-.377l-.264-1.506a1.563,1.563,0,0,0-1.765-1.282l-1.514.214a.527.527,0,0,1-.443-.144L20.086.442a1.562,1.562,0,0,0-2.182,0L16.805,1.5a.528.528,0,0,1-.443.144l-1.514-.214a1.562,1.562,0,0,0-1.765,1.282l-.264,1.506a.528.528,0,0,1-.274.377l-1.35.716a1.563,1.563,0,0,0-.674,2.075l.671,1.373a.527.527,0,0,1,0,.466L10.52,10.6a1.563,1.563,0,0,0,.674,2.075l1.35.716a.527.527,0,0,1,.274.377l.264,1.506a1.562,1.562,0,0,0,1.54,1.3,1.606,1.606,0,0,0,.225-.016l1.514-.214a.527.527,0,0,1,.443.144l1.1,1.063a1.563,1.563,0,0,0,2.182,0l1.1-1.063a.528.528,0,0,1,.443-.144l1.514.214a1.562,1.562,0,0,0,1.765-1.282l.264-1.506a.528.528,0,0,1,.274-.377l1.35-.716a1.563,1.563,0,0,0,.674-2.075Zm-9.879-4.9a1.9,1.9,0,1,1-1.9,1.9A1.905,1.905,0,0,1,16.918,4.326Zm-.982,8.464a.519.519,0,1,1-.734-.734l6.851-6.851a.519.519,0,1,1,.734.734Zm5.135.879a1.9,1.9,0,1,1,1.9-1.9A1.905,1.905,0,0,1,21.071,13.67Z" transform="translate(-10.359 0.002)" fill="#5c626a"/>
      </svg>
      `,
      menuItems: MenuGestion,
      rowsPerPage: 3,
      showDialogAddReduction: false,
      showDialogAjoutReussi: false,
      showDialogModifReduction: false,
      showDialogModifReussi: false,
      showDialogConfirm: false,
      abonnement: false,
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
      active: "first",
      first: false,
      second: false,
      third: false,
    };
  },
  async mounted() {
    await this.loadReductions();
    await this.loadUserList();
    await this.loadSubscriptionList();
    this.checkReductionsPairData();
  },

  watch: {
    async page() {
      await this.loadReductions();
    },
    async size() {
      await this.loadReductions();
    },
    async search() {
      await this.loadReductions();
      if (!this.reductions.length) {
        this.error = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.error = "";
        this.visible = false;
      }
    },
    async searchSubscribption() {
      await this.loadSubscriptionList();
      if (!this.subscriptionsList.length) {
        this.errorSubscriptionList = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.errorSubscriptionList = "";
        this.visible = false;
      }
    },
    async searchUser() {
      await this.loadUserList();
      if (!this.userList.length) {
        this.errorUserList = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.errorUserList = "";
        this.visible = false;
      }
    },
    definePaire(val) {
      if (!val) this.array = [];
    },
    defineUsers(val) {
      if (!val) this.arrayUser = [];
    },
  },
  computed: {
    reductions() {
      return this.$store.state.reduction.reductions.results;
    },
    dataSize() {
      return this.$store.state.reduction.reductions.count;
    },
    subscriptionsList() {
      return this.$store.state.subscription.subscriptions;
    },
    userList() {
      return this.$store.state.user.users;
    },
    next() {
      return this.$store.state.reduction.reductions.next;
    },
  },
  created() {
    document.title = this.$route.meta.title;
  },
};
</script>

<style>
#app .dashboard .md-datepicker-header {
  background: red;
}
.predict-table .reductionName_col {
  width: 10%;
}
.predict-table .code_col {
  width: 5%;
}
.predict-table .dateAdd_col {
  width: 5%;
}
.predict-table .dateExpiry_col {
  width: 5%;
}
.predict-table .reduce_col {
  width: 5%;
}
.codeReduce-table .action_col {
  width: 10%;
}
</style>

<style scoped>
.codeReduce-table .table-container {
  height: auto;
  /* max-height: calc(100vh - 310px); */
}
.liste-des-reductions {
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
.btn-modifier:hover svg path,
.btn-modifier:hover {
  fill: var(--primary);
  color: var(--primary);
  transition: none;
}
.btn-modifier {
  text-decoration: underline;
}
/* input:disabled {
    background-color: rgb(235, 235, 228);
  } */
.align-text {
  text-align: center;
}
.toutAbobloc {
  border-radius: 4px;
  background-color: #f6f6f7;
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
    font-size: 14px;
    padding: 6px 0.5rem !important;
    width: calc(100% - 32px);
  }
}
@media (max-width: 479px) {
  .filter-bloc .md-field input {
    font-size: 12px;
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
</style>
