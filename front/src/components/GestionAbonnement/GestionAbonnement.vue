<template lang="">
  <div class="dashboard">
    <PermanentFull
      :titre="$t('subscriptionManagement')"
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
          <div class="liste-des-utilisateurs">
            <div
              class="d-flex flex-wrap justify-content-between align-items-center"
            >
              <div class="left">
                <h3 class="titre-recherche">{{ $t("search") }}</h3>
                <span class="help-recherche">{{
                  $t("searchAvailableSubscription")
                }}</span>
              </div>

              <div class="right">
                <md-button
                  class="submit-dialog text-center btn-submit text-normal w-100 py-0 m-0"
                  @click="toggleDialogAbonnement(), Init(null)"
                >
                  <md-icon class="text-white">add</md-icon>
                  {{ $t("addSubscription") }}
                </md-button>
              </div>
            </div>
            <div class="table-wrapper flex-grow">
              <md-table
                md-table-fixed-header
                class="mt-3 predict-table gestionAbonnement-table d-flex"
              >
                <md-table-toolbar class="filter-bloc px-2 mb-3">
                  <md-field md-clearable class="md-toolbar-section-end m-0 p-0">
                    <md-input
                      :placeholder="$t('subscriptionPlaceholder')"
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
                    <md-table-head scope="col" class="nameSubscribe_col">
                      {{ $t("subscriptionName") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('name')"
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
                          v-on:click="orderBy('-' + 'name')"
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
                    <md-table-head scope="col" class="nbrPaires_col">
                      {{ $t("nbrPairs") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('number_couple_offered')"
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
                          v-on:click="orderBy('-' + 'number_couple_offered')"
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
                    <md-table-head scope="col" class="nbrUsers_col">
                      {{ $t("nbrUsers") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('nbreUsers')"
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
                          v-on:click="orderBy('-' + 'nbreUsers')"
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
                    <md-table-head scope="col" class="monthPrices_col">
                      {{ $t("monthlyPrice") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('price')"
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
                          v-on:click="orderBy('-' + 'price')"
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
                    <md-table-head scope="col" class="discount_col">
                      {{ $t("discountAnnualPrice") }}
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
                    <md-table-head scope="col" class="annualPrice_col">
                      {{ $t("annualPriceAccordingDiscount") }}
                    </md-table-head>
                    <md-table-head scope="col" class="highlighting_col">
                      {{ $t("promote") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('recommanded')"
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
                          v-on:click="orderBy('-' + 'recommanded')"
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
                    <md-table-head scope="col" class="show_col">
                      {{ $t("show") }}
                      <span class="table-tri d-flex flex-column">
                        <md-button
                          class="btn-tri arrow-up"
                          v-on:click="orderBy('is_active')"
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
                          v-on:click="orderBy('-' + 'is_active')"
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

                  <md-table-row
                    v-for="(item, index) in subscriptions"
                    :key="index"
                  >
                    <md-table-cell
                      class="nameSubscribe_col"
                      :data-label="$t('subscriptionName')"
                      >{{ item.name }}</md-table-cell
                    >
                    <md-table-cell
                      class="dateAdd_col"
                      data-label="Date d'ajout"
                      >{{
                        formatDate($t("dateFormat"), item.created_at)
                      }}</md-table-cell
                    >
                    <md-table-cell
                      class="nbrPaires_col"
                      data-label="Nbre paires"
                    >
                      {{
                        item.number_couple_offered
                          ? item.number_couple_offered
                          : $t("unlimited")
                      }}
                    </md-table-cell>
                    <md-table-cell
                      class="nbrUsers_col"
                      data-label="Nbre utilisateurs"
                    >
                      {{ item.nbreUsers }}-
                    </md-table-cell>
                    <md-table-cell
                      class="monthPrices_col"
                      data-label="Prix mensuel"
                    >
                      {{ pointToComma(item.price.toFixed(2)) }} €
                    </md-table-cell>
                    <md-table-cell
                      class="discount_col"
                      data-label="Remise (prix annuel)"
                    >
                      {{
                        item.reduction
                          ? pointToComma(
                              parseFloat(item.reduction).toFixed(2)
                            ) + " %"
                          : "-"
                      }}
                    </md-table-cell>
                    <md-table-cell
                      class="annualPrice_col"
                      data-label="Prix annuel selon la remise"
                    >
                      {{ pointToComma(showTotal(item.price, item.reduction)) }}
                      €
                    </md-table-cell>
                    <md-table-cell
                      class="highlighting_col"
                      data-label="Mise en avant"
                    >
                      <md-radio
                        v-model="radio"
                        :value="item.recommanded == 1 ? false : item.id"
                        >{{ $t("promote") }}</md-radio
                      >
                    </md-table-cell>
                    <md-table-cell class="show_col" data-label="Afficher">
                      <md-switch
                        class="table-switch"
                        v-model="item.is_active"
                        @change="updateStatus(item)"
                        >{{
                          item.is_active ? $t("active") : $t("desactive")
                        }}</md-switch
                      >
                    </md-table-cell>
                    <md-table-cell class="action_col" data-label="">
                      <md-button
                        class="text-center w-100 text-normal btn-modifier"
                        v-on:click="
                          toggleDialogModifAbonnement(), getSubscribeById(item)
                        "
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="18.002"
                          height="18.003"
                          viewBox="0 0 18.002 18.003"
                          class="mr-1"
                        >
                          <path
                            id="Tracé_42500"
                            data-name="Tracé 42500"
                            d="M3,17.25V21H6.75L17.81,9.94,14.06,6.19ZM20.71,7.04a1,1,0,0,0,0-1.41L18.37,3.29a1,1,0,0,0-1.41,0L15.13,5.12l3.75,3.75,1.83-1.83Z"
                            transform="translate(-3 -2.998)"
                            fill="#242c36"
                          />
                        </svg>

                        {{ $t("modify") }}
                      </md-button>
                    </md-table-cell>
                  </md-table-row>
                  <md-table-row v-if="this.visible">
                    <md-table-cell
                      data-label="date d'ajout"
                      :colspan="9"
                      class="align-text"
                      >{{ this.error }}</md-table-cell
                    ></md-table-row
                  >
                  <md-table-row class="pagination-row" v-if="!visible">
                    <md-table-cell :colspan="10">
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
        @close="showDialogAbonnement = !showDialogAbonnement"
        :dialogName="$t('addSubscription')"
      >
        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <div class="form-group">
            <md-field>
              <label>{{ $t("subscriptionName") }}</label>
              <md-input
                v-model="name"
                :class="errorSubscriptionName && 'error-input'"
              ></md-input>
            </md-field>
            <span class="error">{{ errorSubscriptionName }}</span>
          </div>
          <div class="form-group">
            <div>
              <md-radio v-model="addDefinePaire" :value="false">{{
                $t("allPair")
              }}</md-radio>
              <md-radio v-model="addDefinePaire" :value="true">{{
                $t("setNumber")
              }}</md-radio>
            </div>
          </div>
          <div class="form-group">
            <md-field>
              <label>{{ $t("numberPairs") }}</label>
              <md-input
                v-model="number_couple_offered"
                :disabled="!addDefinePaire"
                :class="errorNumberOfPair && 'error-input'"
                type="number"
                @keypress="noNegativeNumber"
              ></md-input>
            </md-field>
            <span class="error">{{ errorNumberOfPair }}</span>
          </div>
          <div class="form-group">
            <md-field class="d-flex align-items-center position-relative">
              <label>{{ $t("monthlyPrice") }}</label>
              <md-input
                v-model="price"
                type="number"
                @keypress="noNegativeNumber"
                :class="errorMonthlyPrice && 'error-input'"
              ></md-input>
              <md-icon class="custom-icon position-absolute">
                €
              </md-icon>
            </md-field>
            <span class="error">{{ errorMonthlyPrice }}</span>
          </div>
          <div class="form-group">
            <md-field class="d-flex align-items-center position-relative">
              <label>{{ $t("discountAnnualPrice") }}</label>
              <md-input
                v-model="reduction"
                type="number"
                @keypress="noNegativeNumber"
                :class="errorReduction && 'error-input'"
              ></md-input>
              <md-icon class="custom-icon position-absolute">
                %
              </md-icon>
            </md-field>
            <span class="error">{{ errorReduction }}</span>
          </div>

          <div class="form-group d-flex flex-column">
            <label>{{ $t("annualPriceAccordingDiscount") }} :</label>
            <div class="table-switch font-weight-bold mt-0">
              {{ pointToComma(this.total.toFixed(2)) }} €
            </div>
          </div>
          <div class="form-group d-flex flex-column">
            <label>{{ $t("subscriptionStatus") }}</label>
            <md-switch
              class="table-switch font-weight-bold mt-0"
              v-model="is_active"
            >
              {{
                is_active === true ? $t("active") : $t("desactive")
              }}</md-switch
            >
          </div>
          <div class="w-100 text-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase"
              v-on:click="checkAddForm()"
            >
              {{ $t("add") }}
            </md-button>
          </div>
        </form>
      </Dialog>
      <Dialog
        :showDialog="showDialogAbonnementReussi"
        :titreDialog="$t('addSuccess')"
        :iconDialog="iconModifJours"
        @close="showDialogAbonnementReussi = !showDialogAbonnementReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("subscription:successMessage1") }}
          <strong>{{ this.name }}</strong>
          {{ $t("subscription:successMessage2") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogAbonnementReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>

      <Dialog
        :showDialog="showDialogModifAbonnement"
        :dialogName="$t('modifySubscription')"
        @close="showDialogModifAbonnement = !showDialogModifAbonnement"
      >
        <form
          action=""
          class="form-abonnement w-100 mt-3"
          style="max-width: 356px;"
        >
          <div class="form-group">
            <md-field>
              <label>{{ $t("subscriptionName") }}</label>
              <md-input
                v-model="name"
                :class="errorSubscriptionName && 'error-input'"
              ></md-input>
            </md-field>
            <span class="error">{{ errorSubscriptionName }}</span>
          </div>
          <div class="form-group">
            <div>
              <md-radio v-model="definePaire" :value="false">{{
                $t("allPair")
              }}</md-radio>
              <md-radio v-model="definePaire" :value="true">{{
                $t("setNumber")
              }}</md-radio>
            </div>
          </div>
          <div class="form-group">
            <md-field>
              <label>{{ $t("numberPairs") }}</label>
              <md-input
                v-model="number_couple_offered"
                :disabled="!definePaire"
                :class="errorNumberOfPair && 'error-input'"
                type="number"
                @keypress="noNegativeNumber"
              ></md-input>
            </md-field>
            <span class="error">{{ errorNumberOfPair }}</span>
          </div>
          <div class="form-group">
            <md-field class="d-flex align-items-center position-relative">
              <label>{{ $t("monthlyPrice") }}</label>
              <md-input
                v-model="price"
                type="number"
                @keypress="noNegativeNumber"
                :class="errorMonthlyPrice && 'error-input'"
              ></md-input>
              <md-icon class="custom-icon position-absolute">
                €
              </md-icon>
            </md-field>
            <span class="error">{{ errorMonthlyPrice }}</span>
          </div>
          <div class="form-group">
            <md-field class="d-flex align-items-center position-relative">
              <label>{{ $t("discountAnnualPrice") }}</label>
              <md-input
                v-model="reduction"
                type="number"
                @keypress="noNegativeNumber"
                :class="errorReduction && 'error-input'"
              ></md-input>
              <md-icon class="custom-icon position-absolute">
                %
              </md-icon>
            </md-field>
            <span class="error">{{ errorReduction }}</span>
          </div>

          <div class="form-group d-flex flex-column">
            <label>{{ $t("annualPriceAccordingDiscount") }} :</label>
            <div class="table-switch font-weight-bold mt-0">
              {{ pointToComma(this.total.toFixed(2)) }} €
            </div>
          </div>
          <div class="form-group d-flex flex-column">
            <label>{{ $t("subscriptionStatus") }}</label>
            <md-switch
              class="table-switch font-weight-bold mt-0"
              v-model="is_active"
            >
              {{
                is_active === true ? $t("active") : $t("desactive")
              }}</md-switch
            >
          </div>
          <div class="w-100 text-center">
            <md-button
              class="submit-dialog text-center btn-submit text-center w-100 text-uppercase"
              @click="checkUpdateForm()"
              >{{ $t("modify") }}
            </md-button>
          </div>
        </form>
      </Dialog>
      <Dialog
        :showDialog="showDialogModifAbonnementReussi"
        :titreDialog="$t('successModification')"
        @close="
          showDialogModifAbonnementReussi = !showDialogModifAbonnementReussi
        "
        :iconDialog="iconModifJours"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("modifSubscription") }} <strong>{{ this.name }}</strong>
          {{ $t("modifCompleted") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogModifAbonnementReussi = false"
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
import MenuGestion from "../../data/MenuGestion.js";
import { formatDate } from "../../utils/Constant";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
  name: "GestionAbonnement",
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
    checkSubscriptionsPairData() {
      if (!this.subscriptions.length) {
        this.error = this.$t("tableNoDataYet");
        this.visible = true;
      }
    },
    noNegativeNumber(e) {
      if (e.charCode >= 48 && e.charCode <= 57) {
        return true;
      }
      return e.preventDefault();
    },
    setAllFalse() {
      this.showDialogModifAbonnement = false;
      this.showDialogAbonnementReussi = false;
      this.showDialogModifAbonnementReussi = false;
      this.showDialogAbonnement = false;
    },
    toggleDialogAbonnement() {
      this.setAllFalse();
      this.initErrorForm();
      this.showDialogAbonnement = !this.showDialogAbonnement;
    },
    toggleDialogAbonnementReussi() {
      this.setAllFalse();
      this.showDialogAbonnementReussi = !this.showDialogAbonnementReussi;
    },
    toggleDialogModifAbonnement() {
      this.setAllFalse();
      this.initErrorForm();
      this.errorReduction = "";
      this.showDialogModifAbonnement = !this.showDialogModifAbonnement;
    },
    toggleDialogModifAbonnementReussi() {
      this.setAllFalse();
      this.showDialogModifAbonnementReussi = !this
        .showDialogModifAbonnementReussi;
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
    },
    orderBy: async function(field) {
      await this.$store.dispatch("loadSubscriptions", {
        token: localStorage.getItem("adminToken"),
        order: field,
        page: this.page,
        search: this.search,
        size: this.size,
      });
    },
    initErrorForm() {
      this.errorSubscriptionName = "";
      this.errorNumberOfPair = "";
      this.errorMonthlyPrice = "";
      this.errorReduction = "";
    },
    checkAddForm() {
      this.initErrorForm();
      if (!this.name) {
        this.errorSubscriptionName = this.$t("errorSubscriptionName");
      }
      if (this.addDefinePaire == true && this.number_couple_offered == "") {
        this.errorNumberOfPair = this.$t("errorNumberOfPair");
      }
      if (!this.price) {
        this.errorMonthlyPrice = this.$t("errorMonthlyPrice");
      }
      if (!this.reduction)
        this.errorReduction = this.$t("errorReductionRequired");
      if (this.reduction > 100)
        this.errorReduction = this.$t("invalidReduction");
      if (
        !this.errorSubscriptionName &&
        !this.errorNumberOfPair &&
        !this.errorMonthlyPrice &&
        !this.errorReduction
      ) {
        this.addSubscription();
      }
    },
    checkUpdateForm() {
      this.initErrorForm();
      if (!this.name) {
        this.errorSubscriptionName = this.$t("errorSubscriptionName");
      }
      if (this.definePaire == true && this.number_couple_offered == "") {
        this.errorNumberOfPair = this.$t("errorNumberOfPair");
      }
      if (!this.price) {
        this.errorMonthlyPrice = this.$t("errorMonthlyPrice");
      }
      if (!this.reduction)
        this.errorReduction = this.$t("errorReductionRequired");
      if (this.reduction > 100)
        this.errorReduction = this.$t("invalidReduction");
      if (
        !this.errorSubscriptionName &&
        !this.errorNumberOfPair &&
        !this.errorMonthlyPrice &&
        !this.errorReduction
      ) {
        this.updateSubscribe();
      }
    },
    addSubscription: async function() {
      const payload = {
        name: this.name,
        price: +this.price,
        reduction: +this.reduction,
        number_couple_offered: +this.number_couple_offered,
        is_active: this.is_active,
      };
      try {
        await this.$store.dispatch("addSubscription", {
          payload,
          token: localStorage.getItem("adminToken"),
        });
        this.toggleDialogAbonnementReussi();
        await this.loadSubscriptions();
      } catch (e) {
        //
      }
    },
    updateSubscribe: async function() {
      this.errorReduction = "";
      if (this.reduction > 100)
        this.errorReduction = this.$t("invalidReduction");

      if (
        !this.errorPaireNegativeNumber &&
        !this.errorReduction &&
        this.price &&
        this.name
      ) {
        const payload = {
          name: this.name,
          price: +this.price,
          reduction: +this.reduction,
          number_couple_offered: +this.number_couple_offered,
          is_active: this.is_active,
        };
        try {
          await this.$store.dispatch("updateSubscription", {
            id: this.id,
            payloadUpdate: payload,
            token: localStorage.getItem("adminToken"),
          });
          await this.loadSubscriptions();
          this.toggleDialogModifAbonnementReussi();
        } catch (e) {
          //
        }
      }
    },
    getSubscribeById: function(item) {
      this.Init(item);
    },
    updateStatus: async function(item) {
      const payload = {
        is_active: item.is_active,
      };
      try {
        await this.$store.dispatch("updateSubscriptionStatus", {
          id: item.id,
          payloadUpdate: payload,
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      }
      await this.loadSubscriptions();
    },
    Init(item) {
      if (item == null) {
        this.id = "";
        this.name = "";
        this.created_at = "";
        this.price = "";
        this.reduction = "";
        this.number_couple_offered = 0;
        this.addDefinePaire = false;
        this.is_active = true;
      } else {
        this.id = +item.id;
        this.name = item.name;
        this.created_at = item.created_at;
        this.price = +item.price;
        this.reduction = +item.reduction;
        this.number_couple_offered = +item.number_couple_offered;
        if (this.number_couple_offered == 0) this.definePaire = false;
        else this.definePaire = true;
        this.is_active = item.is_active;
      }
    },
    getTotal(price, reduction) {
      const pa = +price * 12;
      const r = pa * (reduction / 100);
      this.total = pa - r;
    },
    showTotal(price, reduction) {
      const pa = +price * 12;
      const r = pa * (reduction / 100);
      return (pa - r).toFixed(2);
    },
    loadSubscriptions: async function() {
      this.loader = true;
      await this.$store.dispatch("loadSubscriptions", {
        token: localStorage.getItem("adminToken"),
        order: "-created_at",
        page: this.page,
        search: this.search,
        size: this.size,
      });
      this.loader = false;
    },
  },
  data: () => {
    return {
      search: "",
      id: "",
      name: "",
      price: 0,
      reduction: 0,
      number_couple_offered: null,
      errorReduction: "",
      errorSubscriptionName: "",
      errorNumberOfPair: "",
      errorMonthlyPrice: "",
      is_active: true,
      loader: false,
      created_at: "",
      page: 1,
      size: 5,
      total: 0,
      sur: "",
      order: "",
      error: "",
      visible: false,
      icon: `
        <svg id="space_dashboard_black_24dp" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36">
          <rect id="Rectangle_1872" data-name="Rectangle 1872" width="36" height="36" fill="none"/>
          <path id="Tracé_19674" data-name="Tracé 19674" d="M15,30H6a3.009,3.009,0,0,1-3-3V6A3.009,3.009,0,0,1,6,3h9Zm3,0h9a3.009,3.009,0,0,0,3-3V16.5H18ZM30,13.5V6a3.009,3.009,0,0,0-3-3H18V13.5Z" transform="translate(1.5 1.5)" fill="#242c36"/>
          <path id="Tracé_19683" data-name="Tracé 19683" d="M15,30H6a3.009,3.009,0,0,1-3-3V6A3.009,3.009,0,0,1,6,3h9Zm3,0h9a3.009,3.009,0,0,0,3-3V16.5H18ZM30,13.5V6a3.009,3.009,0,0,0-3-3H18V13.5Z" transform="translate(1.5 1.5)" fill="#242c36"/>
        </svg>
      `,
      menuItems: MenuGestion,
      radio: false,
      rowsPerPage: 3,
      showDialogAbonnement: false,
      showDialogAbonnementReussi: false,
      showDialogModifAbonnement: false,
      showDialogModifAbonnementReussi: false,
      renewAuto: true,
      nomAbonnement: null,
      definePaire: false,
      addDefinePaire: false,
      prixMensuel: null,
      prixAnnuel: null,
      disabled: null,
      dateValidity: null,
      jourGratuit: 10,
      credits: 10,
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
    };
  },
  async mounted() {
    await this.loadSubscriptions();
    this.checkSubscriptionsPairData();
  },

  watch: {
    async page() {
      await this.loadSubscriptions();
    },
    async size() {
      await this.loadSubscriptions();
    },
    async search() {
      await this.loadSubscriptions();
      if (!this.subscriptions.length) {
        this.error = this.$t("table:NotFound");
        this.visible = true;
      } else {
        this.error = "";
        this.visible = false;
      }
    },
    addDefinePaire(val) {
      this.errorNumberOfPair = "";
      val
        ? (this.number_couple_offered = "")
        : (this.number_couple_offered = 0);
    },
    definePaire(val) {
      this.errorNumberOfPair = "";
      val ? this.number_couple_offered : (this.number_couple_offered = 0);
      if (val && this.number_couple_offered === 0)
        this.number_couple_offered = "";
    },
    async radio(val) {
      const payload = {
        recommanded: true,
      };
      try {
        await this.$store.dispatch("setRecommandedSubscription", {
          id: val,
          payload,
          token: localStorage.getItem("adminToken"),
        });
      } catch (e) {
        //
      }
    },
    price(val) {
      if (val > 0) this.getTotal(this.price, this.reduction);
      else this.total = 0;
    },
    reduction() {
      this.price > 0 && this.getTotal(this.price, this.reduction);
    },
  },
  computed: {
    subscriptions() {
      return this.$store.state.subscription.subscriptions.results;
    },
    dataSize() {
      return this.$store.state.subscription.subscriptions.count;
    },
    next() {
      return this.$store.state.subscription.subscriptions.next;
    },
  },
  created() {
    document.title = this.$route.meta.title;
  },
};
</script>

<style>
.gestionAbonnement-table .nameSubscribe_col {
  width: 2.5%;
}
.gestionAbonnement-table .dateAdd_col {
  width: 2.5%;
}
.gestionAbonnement-table .nbrPaires_col {
  width: 2.5%;
}
.gestionAbonnement-table .nbrUsers_col {
  width: 2.5%;
}
.gestionAbonnement-table .monthPrices_col {
  width: 5%;
}
.gestionAbonnement-table .discount_col {
  width: 5%;
}
.gestionAbonnement-table .annualPrice_col {
  width: 5%;
}
.gestionAbonnement-table .highlighting_col {
  width: 5%;
}
.gestionAbonnement-table .show_col {
  width: 5%;
}
.gestionAbonnement-table .action_col {
  width: 2.5%;
}
#content-dashboard-wrapper .gestionAbonnement-table .md-table-head-container {
  line-height: normal;
  white-space: normal;
}
</style>

<style scoped>
#content-dashboard-wrapper .gestionAbonnement-table .md-table-head {
  font-size: 12px;
}

.gestionAbonnement-table .table-container {
  height: auto;
  /* max-height: calc(100vh - 320px); */
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
