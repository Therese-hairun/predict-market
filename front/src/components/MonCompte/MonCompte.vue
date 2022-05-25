<template lang="">
  <div class="dashboard">
    <PermanentFull
      :titre="$t('myAccount')"
      :icon="icon"
      :menuItems="menuItems"
      ref="PermanentFull"
    >
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column"
      >
        <div class="pt-4 flex-grow-1 d-flex flex-column h-100">
          <div id="mon-compte">
            <md-tabs class="tabs-monCompte">
              <template class="test" slot="md-tab" slot-scope="{ tab }">
                <div class="d-flex tab-item text-initial text">
                  <span v-html="tab.icon" class="mr-1"></span> {{ tab.label }}
                </div>
              </template>

              <md-tab
                id="tab-general"
                :md-label="$t('general')"
                :md-icon="iconTabs1"
              >
                <div class="md-layout md-gutter column-wrapper mx-0">
                  <div class="md-layout-item dashboard-border bloc-content">
                    <div
                      class="avatar-wrapper d-flex flex-column align-items-center mb-3 mb-md-4"
                    >
                      <div class="avatar-innerwrapper">
                        <div
                          class="avatar_loaded"
                          v-if="userPhoto"
                          @click="handleUserphoto"
                        >
                          <img v-bind:src="client.profil" alt="photo user" />
                          <span class="fake_btn">{{ $t("remove") }}</span>
                        </div>
                        <UploadFile
                          uploadMsg=" "
                          :max="1"
                          :clearAll="$t('remove')"
                          :handleImages="handleImage"
                        />
                      </div>

                      <md-button
                        class="submit-dialog text-center btn-submit text-center w-100 text-normal mt-3 py-0 m-0 w-auto"
                        @click="onUpload"
                        v-if="showButton"
                      >
                        {{ $t("update") }}
                      </md-button>
                      <p v-if="showMessage">{{ $t("uploadImageSuccess") }}</p>

                      <!-- UPLOAD IMAGE -->
                      <div class="info-utilisateur text-center mt-3">
                        <p class="nom-utilisateur mb-0">
                          {{ client.firstname }} {{ client.lastname }}
                        </p>
                        <p class="mail-utilisateur mb-0">{{ client.email }}</p>
                      </div>
                    </div>
                    <BlocAbonnement
                      :typeAbonnement="subscription"
                      :emplacementDispo="emplacementDispo"
                      :emplacementUtilise="emplacementUtilise"
                      :titreAbonnement="$t('subscription')"
                      :iconAbonnement="iconAbonnement"
                    ></BlocAbonnement>
                    <div class="d-flex flex-wrap justify-content-between mb-3">
                      <span class="pseudo-label">{{ $t("credits") }}</span>
                      <p class="d-flex align-items-center">
                        {{ $t("info:credits") }}
                      </p>
                      <div class="d-flex details w-100 flex-column">
                        <div class="d-flex align-items-center mb-2">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="50.526"
                            height="48"
                            viewBox="0 0 50.526 48"
                            style="max-width: 16px; max-height: 15.2px"
                          >
                            <path
                              id="Tracé_42201"
                              data-name="Tracé 42201"
                              d="M47.044,15.895,41.309,10.16a13.524,13.524,0,0,1,.808-2.905,3.538,3.538,0,0,0,.3-1.465A3.784,3.784,0,0,0,38.632,2,12.619,12.619,0,0,0,28.526,7.053H15.895A13.887,13.887,0,0,0,2,20.947C2,28.627,8.316,50,8.316,50H22.211V44.947h5.053V50H41.158L45.4,35.878,52.526,33.5V15.895ZM29.789,19.684H17.158V14.632H29.789Zm7.579,5.053a2.526,2.526,0,1,1,2.526-2.526A2.534,2.534,0,0,1,37.368,24.737Z"
                              transform="translate(-2 -2)"
                              fill="#5c626a"
                            />
                          </svg>
                          <div class="d-flex flex-column ml-2">
                            <span class="text"
                              >{{ pointToComma(sum.toFixed(2)) }} €</span
                            >
                          </div>
                        </div>
                        <div class="d-flex w-100 flex-grow-1">
                          <form
                            class="d-flex flex-wrap align-items-center w-100"
                          >
                            <PredictInputNumber
                              :value="credits"
                              v-model="credits"
                              unite=""
                              numberLength="5"
                              class="mb-2 custom-input-number flex-grow-1 mr-3"
                            ></PredictInputNumber>
                            <md-button
                              :disabled="disableCredit"
                              type="submit"
                              class="submit-dialog text-center btn-submit text-center w-100 text-normal py-0 mx-auto mx-sm-0 mt-0 mb-2"
                              style="flex:1"
                              @click="addCredits(credits)"
                            >
                              {{ $t("use") }}
                              <md-icon>
                                <svg
                                  xmlns="http://www.w3.org/2000/svg"
                                  width="16"
                                  height="8"
                                  viewBox="0 0 16 8"
                                >
                                  <path
                                    id="Tracé_42198"
                                    data-name="Tracé 42198"
                                    d="M16.01,11H4v2H16.01v3L20,12,16.01,8Z"
                                    transform="translate(-4 -8)"
                                    fill="#fff"
                                  />
                                </svg>
                              </md-icon>
                            </md-button>
                          </form>
                        </div>
                      </div>
                    </div>
                    <div class="d-flex flex-wrap justify-content-between mb-3">
                      <span class="pseudo-label">{{ $t("freeDays") }}</span>
                      <p class="d-flex align-items-center">
                        {{ $t("info:freedays") }}
                      </p>
                      <div class="d-flex details w-100 flex-column">
                        <div class="d-flex align-items-center mb-2">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="41.667"
                            height="45.833"
                            viewBox="0 0 41.667 45.833"
                            style="max-width: 15px; max-height: 16.5px"
                          >
                            <path
                              id="Tracé_19699"
                              data-name="Tracé 19699"
                              d="M39.5,5.167H37.417V1H33.25V5.167H12.417V1H8.25V5.167H6.167A4.179,4.179,0,0,0,2,9.333V42.667a4.179,4.179,0,0,0,4.167,4.167H39.5a4.179,4.179,0,0,0,4.167-4.167V9.333A4.179,4.179,0,0,0,39.5,5.167Zm0,37.5H6.167V15.583H39.5Z"
                              transform="translate(-2 -1)"
                              fill="#5c626a"
                            />
                          </svg>
                          <div class="d-flex flex-column ml-2">
                            <span class="text"
                              >{{ free_day }} {{ $t("days") }}</span
                            >
                          </div>
                        </div>
                        <div class="d-flex w-100 flex-grow-1">
                          <form
                            class="d-flex flex-wrap align-items-center w-100"
                          >
                            <PredictInputNumber
                              :value="jourGratuit"
                              v-model="jourGratuit"
                              unite=""
                              numberLength="3"
                              class="mb-2 custom-input-number flex-grow-1 mr-3"
                            ></PredictInputNumber>
                            <md-button
                              :disabled="disableDay"
                              type="submit"
                              class="submit-dialog text-center btn-submit text-center w-100 text-normal py-0 mx-auto mx-sm-0 mt-0 mb-2"
                              style="flex:1"
                              @click="addDays(jourGratuit)"
                            >
                              {{ $t("use") }}
                              <md-icon>
                                <svg
                                  xmlns="http://www.w3.org/2000/svg"
                                  width="16"
                                  height="8"
                                  viewBox="0 0 16 8"
                                >
                                  <path
                                    id="Tracé_42198"
                                    data-name="Tracé 42198"
                                    d="M16.01,11H4v2H16.01v3L20,12,16.01,8Z"
                                    transform="translate(-4 -8)"
                                    fill="#fff"
                                  />
                                </svg>
                              </md-icon>
                            </md-button>
                          </form>
                        </div>
                      </div>
                    </div>
                    <div
                      class="d-flex flex-wrap justify-content-between pt-md-3 mb-3"
                    >
                      <span class="">{{ $t("renew") }}</span>
                      <p class="d-flex align-items-center">
                        <strong class="mr-1">{{
                          renew ? $t("active") : $t("desactive")
                        }}</strong
                        ><md-switch
                          class="table-switch my-0"
                          v-model="renew"
                          @change="updateRenewStatus"
                        ></md-switch>
                      </p>
                      <Dialog
                        :showDialog="showDialogRenewAuto"
                        :titreDialog="$t('dialog:renewSuccess')"
                        :iconDialog="iconModifJours"
                        @close="showDialogRenewAuto = !showDialogRenewAuto"
                      >
                        <div class="text-center" style="max-width: 380px;">
                          {{ $t("info:renew") }}
                        </div>

                        <div class="form-group text-center mt-4">
                          <md-button
                            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
                            @click="showDialogRenewAuto = false"
                          >
                            {{ $t("continue") }}
                          </md-button>
                        </div>
                      </Dialog>
                    </div>
                    <div class="d-flex flex-wrap justify-content-between">
                      <div class="d-flex flex-column mr-sm-3">
                        <span class="">{{ $t("expire:message") }}</span>
                        <p class="d-flex align-items-center">
                          <strong class="mr-1">{{
                            formatDate(subscribeExpiration)
                          }}</strong>
                        </p>
                      </div>
                      <md-button
                        type="submit"
                        class="submit-compte submit-dialog btn-upgrade text-center btn-submit text-center w-100 text-normal py-1 m-0 mx-auto mx-sm-0 ml-sm-1"
                        style="flex:1"
                        @click="upgradeSubscription()"
                      >
                        <md-icon>
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="8"
                            height="16"
                            viewBox="0 0 8 16"
                          >
                            <path
                              id="Tracé_42472"
                              data-name="Tracé 42472"
                              d="M16,18v2H8V18ZM11,7.99V16h2V7.99h3L12,4,8,7.99Z"
                              transform="translate(-8 -4)"
                              fill="#fff"
                            />
                          </svg>
                        </md-icon>
                        {{ $t("upgrade") }}
                      </md-button>
                    </div>
                  </div>
                  <div class="md-layout-item position-relative p-0">
                    <div class="dashboard-border bloc-content mx-0">
                      <div class="titre-page mb-1">{{ $t("myInfo") }}</div>
                      <p>
                        {{ $t("info:message") }}
                      </p>
                      <form
                        class="form-user d-flex flex-column align-items-end"
                        action=""
                        novalidate="true"
                      >
                        <div class="form-group w-100">
                          <md-field>
                            <label for="nom">{{ $t("lastName") }}</label>
                            <md-input
                              name="nom"
                              id="nom"
                              autocomplete="off"
                              v-model="nom"
                              :class="errorNomRequired.length && 'error-input'"
                            />
                          </md-field>
                          <span
                            v-if="errorNomRequired.length"
                            class="d-flex flex-column"
                          >
                            <span
                              class="error"
                              v-for="error in errorNomRequired"
                              :key="error"
                              >{{ error }}</span
                            >
                          </span>
                        </div>
                        <div class="form-group w-100">
                          <md-field>
                            <label for="prenom">{{ $t("firstName") }}</label>
                            <md-input
                              name="prenom"
                              id="prenom"
                              autocomplete="off"
                              v-model="prenom"
                              :class="
                                errorPrenomRequired.length && 'error-input'
                              "
                            />
                          </md-field>

                          <span
                            v-if="errorPrenomRequired.length"
                            class="d-flex flex-column"
                          >
                            <span
                              class="error"
                              v-for="error in errorPrenomRequired"
                              :key="error"
                              >{{ error }}</span
                            >
                          </span>
                        </div>

                        <div class="form-group w-100">
                          <md-field>
                            <label for="email">{{ $t("email") }}</label>
                            <md-input
                              type="email"
                              name="email"
                              id="email"
                              autocomplete="off"
                              v-model="email"
                              disabled
                            />
                          </md-field>
                        </div>

                        <md-button
                          type="submit"
                          class="submit-dialog text-center btn-submit text-center w-100 text-normal py-0 m-0 w-auto"
                          @click="infoCheck"
                        >
                          {{ $t("save") }}
                        </md-button>
                      </form>
                    </div>
                    <div class="dashboard-border bloc-content mx-0">
                      <div class="titre-page mb-1">{{ $t("phoneNumber") }}</div>
                      <p>
                        {{ $t("phoneMessage") }}
                      </p>
                      <form
                        class="form-user d-flex flex-column align-items-end"
                        action=""
                        novalidate="true"
                      >
                        <div class="form-group w-100">
                          <md-field>
                            <vue-tel-input
                              class="border-0"
                              autocomplete="off"
                              :autoDefaultCountry="false"
                              v-model="telephone"
                              :inputOptions="tel_options"
                              :class="
                                errorTelephoneRequired.length && 'error-input'
                              "
                              @keyup="removeError"
                            ></vue-tel-input>
                          </md-field>
                          <span
                            v-if="errorTelephoneRequired.length"
                            class="d-flex flex-column"
                          >
                            <span
                              class="error"
                              v-for="error in errorTelephoneRequired"
                              :key="error"
                              >{{ error }}</span
                            >
                          </span>
                        </div>

                        <md-button
                          class="submit-dialog text-center btn-submit text-center w-100 text-normal py-0 m-0 w-auto"
                          @click="phoneCheck"
                        >
                          {{ $t("save") }}
                        </md-button>
                      </form>
                    </div>
                  </div>
                  <div
                    class="md-layout-item px-0 bloc-content password-wrapper p-0 m-0"
                  >
                    <div
                      class="md-layout-item bloc-content dashboard-border mx-0 position-relative"
                    >
                      <div class="titre-page mb-1">{{ $t("password") }}</div>
                      <p>
                        {{ $t("password:info") }}
                      </p>
                      <form
                        class="form-user d-flex flex-column align-items-end"
                        action=""
                        novalidate="true"
                      >
                        <div class="form-group w-100">
                          <md-field>
                            <label for="password">{{
                              $t("oldPassword")
                            }}</label>
                            <md-input
                              type="password"
                              name="password"
                              id="password"
                              autocomplete="off"
                              v-model="password"
                              @keyup="handlePassword"
                              :class="errorOldPwd.length ? 'error-input' : null"
                            />
                          </md-field>
                          <span
                            v-if="errorOldPwd.length"
                            class="d-flex flex-column"
                          >
                            <span
                              class="error"
                              v-for="error in errorOldPwd"
                              :key="error"
                              >{{ error }}</span
                            >
                          </span>
                        </div>
                        <div class="form-group w-100">
                          <md-field>
                            <label for="newPassword">{{
                              $t("newPassword")
                            }}</label>
                            <md-input
                              type="password"
                              name="newPassword"
                              id="newPassword"
                              autocomplete="off"
                              v-model="newPassword"
                              :class="errorPwd.length ? 'error-input' : null"
                            />
                          </md-field>
                          <span
                            v-if="errorPwd.length"
                            class="d-flex flex-column"
                          >
                            <span
                              class="error"
                              v-for="error in errorPwd"
                              :key="error"
                              >{{ error }}</span
                            >
                          </span>
                          <div class="help_input">
                            {{ $t("password-help-label") }}
                            <ul>
                              <li>
                                {{ $t("contain-a") }}
                                <strong>{{ $t("lowercase") }}</strong
                                >, {{ $tc("a", 2) }}
                                <strong>{{ $t("uppercase") }}</strong
                                >, {{ $tc("a", 1) }}
                                <strong>{{ $t("number") }}</strong>
                                {{ $t("and-a") }}

                                <strong>{{ $t("special-character") }}</strong
                                >.
                              </li>
                              <li>
                                {{ $t("at-least") }}
                                <strong>{{ $t("8-characters") }}</strong
                                >.
                              </li>
                            </ul>
                          </div>
                        </div>

                        <div class="form-group w-100">
                          <md-field>
                            <label for="password">{{
                              $t("confirmPassword")
                            }}</label>
                            <md-input
                              type="password"
                              name="confirmPassword"
                              id="confirmPassword"
                              autocomplete="off"
                              v-model="confirmPassword"
                              :class="
                                errorConfirmPwd.length ? 'error-input' : null
                              "
                            />
                          </md-field>
                          <span
                            v-if="errorConfirmPwd.length"
                            class="d-flex flex-column"
                          >
                            <span
                              class="error"
                              v-for="error in errorConfirmPwd"
                              :key="error"
                              >{{ error }}</span
                            >
                          </span>
                        </div>
                        <md-button
                          type="submit"
                          class="submit-dialog text-center btn-submit text-center w-100 text-normal py-0 m-0 btn-100"
                          @click="checkPasswordForm"
                        >
                          {{ $t("save") }}
                        </md-button>
                      </form>
                    </div>
                  </div>
                </div>
              </md-tab>
              <md-tab
                id="tab-factures"
                :md-label="$t('mybills')"
                :md-icon="iconTabs2"
              >
                <div class="md-layout md-gutter column-wrapper mx-0">
                  <div
                    class="md-layout-item dashboard-border bloc-content mt-0"
                  >
                    <BlocAbonnement
                      :typeAbonnement="subscription"
                      :emplacementDispo="emplacementDispo"
                      :emplacementUtilise="emplacementUtilise"
                      :titreAbonnement="$t('subscription')"
                      :iconAbonnement="iconAbonnement"
                    ></BlocAbonnement>

                    <div class="d-flex flex-wrap justify-content-between mb-3">
                      <span class="pseudo-label">{{ $t("toPay") }}</span>
                      <div class="pseudo-label future-cost w-100 my-2">
                        {{ pointToComma(subscriptionPrice.toFixed(2)) }}€
                      </div>
                      <p class="d-flex align-items-center my-2">
                        {{ $t("toPayMessage") }}
                      </p>
                    </div>
                    <hr />
                    <div
                      class="d-flex flex-wrap justify-content-between pt-3 mb-3"
                    >
                      <span class="">{{ $t("renew") }}</span>
                      <p class="d-flex align-items-center">
                        <strong class="mr-1">{{
                          renew ? $t("active") : $t("desactive")
                        }}</strong
                        ><md-switch
                          class="table-switch my-0"
                          v-model="renew"
                          @change="updateRenewStatus"
                        ></md-switch>
                      </p>
                    </div>
                    <div class="d-flex flex-wrap justify-content-between">
                      <div class="d-flex flex-column mr-3">
                        <span class="">{{ $t("expire:message") }}</span>
                        <p class="d-flex align-items-center">
                          <strong class="mr-1">{{
                            formatDate(subscribeExpiration)
                          }}</strong>
                        </p>
                      </div>
                      <md-button
                        type="submit"
                        class="submit-compte submit-dialog text-center btn-submit text-center w-100 text-normal py-1 m-0"
                        style="flex:1"
                        @click="upgradeSubscription()"
                      >
                        <md-icon>
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="8"
                            height="16"
                            viewBox="0 0 8 16"
                          >
                            <path
                              id="Tracé_42472"
                              data-name="Tracé 42472"
                              d="M16,18v2H8V18ZM11,7.99V16h2V7.99h3L12,4,8,7.99Z"
                              transform="translate(-8 -4)"
                              fill="#fff"
                            />
                          </svg>
                        </md-icon>
                        {{ $t("upgrade") }}
                      </md-button>
                    </div>
                  </div>
                  <div
                    class="md-layout-item dashboard-border historique-wrapper"
                  >
                    <div
                      class="pt-3 py-md-4 flex-grow-1 d-flex flex-column h-100"
                    >
                      <div class="liste-des-factures h-100 d-flex flex-column">
                        <h3 class="titre-recherche">
                          {{ $t("historyBills") }}
                        </h3>
                        <span class="help-recherche">{{
                          $t("checkBills")
                        }}</span>

                        <div class="table-wrapper flex-grow">
                          <md-table
                            md-table-fixed-header
                            class="mt-3 predict-table monCompte-table d-flex flex-grow-1"
                          >
                            <md-table-toolbar class="search-code-field mb-3">
                              <md-field
                                md-clearable
                                class="md-toolbar-section-end m-0 p-0"
                              >
                                <md-input
                                  :placeholder="$t('codeNumber')"
                                  pla
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
                                <md-table-head class="date_col" scope="col">
                                  {{ $t("date") }}
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
                                <md-table-head
                                  class="codeNumber_col"
                                  scope="col"
                                >
                                  {{ $t("codeNumber") }}
                                  <span class="table-tri d-flex flex-column">
                                    <md-button
                                      class="btn-tri arrow-up"
                                      v-on:click="orderBy('payment__reference')"
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
                                      v-on:click="
                                        orderBy('-' + 'payment__reference')
                                      "
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
                                  class="subscription_col"
                                  scope="col"
                                >
                                  {{ $t("subscription") }}
                                  <span class="table-tri d-flex flex-column">
                                    <md-button
                                      class="btn-tri arrow-up"
                                      v-on:click="
                                        orderBy(
                                          'payment__subscription__subscribe__name'
                                        )
                                      "
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
                                      v-on:click="
                                        orderBy(
                                          '-' +
                                            'payment__subscription__subscribe__name'
                                        )
                                      "
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
                                <md-table-head class="amount_col" scope="col">
                                  {{ $t("amount") }}
                                  <span class="table-tri d-flex flex-column">
                                    <md-button
                                      class="btn-tri arrow-up"
                                      v-on:click="orderBy('initial_price')"
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
                                      v-on:click="
                                        orderBy('-' + 'initial_price')
                                      "
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
                                <md-table-head class="actions_col" scope="col">
                                </md-table-head>
                              </md-table-row>
                              <md-table-row
                                v-for="(item, index) in factures"
                                :key="index"
                              >
                                <md-table-cell :data-label="$t('date')">{{
                                  formatDate(item.created_at)
                                }}</md-table-cell>
                                <md-table-cell :data-label="$t('codeNumber')">{{
                                  item.payment.reference
                                }}</md-table-cell>
                                <md-table-cell
                                  :data-label="$t('subscription')"
                                  >{{
                                    item.payment.subscribe.name
                                  }}</md-table-cell
                                >
                                <md-table-cell :data-label="$t('amount')"
                                  >{{
                                    pointToComma(item.final_price.toFixed(2))
                                  }}
                                  €</md-table-cell
                                >
                                <md-table-cell data-label="">
                                  <div class="d-flex align-items-center">
                                    <md-button
                                      class="text-center w-100 text-normal btn-modifier"
                                      :md-ripple="false"
                                    >
                                      <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        width="22"
                                        height="15"
                                        viewBox="0 0 22 15"
                                        class="mr-1"
                                      >
                                        <path
                                          id="Tracé_988"
                                          data-name="Tracé 988"
                                          d="M23.637-39c-5,0-9.27,3.61-11,8,1.73,4.39,6,7,11,7s9.27-2.61,11-7C32.907-35.39,28.637-39,23.637-39Zm0,13a5,5,0,0,1-5-5,5,5,0,0,1,5-5,5,5,0,0,1,5,5A5,5,0,0,1,23.637-26Zm0-8a3,3,0,0,0-3,3,3,3,0,0,0,3,3,3,3,0,0,0,3-3A3,3,0,0,0,23.637-34Z"
                                          transform="translate(-12.637 39)"
                                          fill="#242c36"
                                        /></svg
                                      ><ins
                                        @click="generateReport(item, false)"
                                        >{{ $t("toConsult") }}</ins
                                      >
                                    </md-button>
                                    <md-button
                                      class="text-center w-100 text-normal btn-modifier"
                                    >
                                      <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        width="24"
                                        height="16"
                                        viewBox="0 0 24 16"
                                        class="mr-1"
                                      >
                                        <path
                                          id="Tracé_42478"
                                          data-name="Trace_42478"
                                          d="M19.35,10.04a7.492,7.492,0,0,0-14-2A6,6,0,0,0,6,20H19a4.986,4.986,0,0,0,.35-9.96ZM17,13l-5,5L7,13h3V9h4v4Z"
                                          transform="translate(0 -4)"
                                          fill="#242c36"
                                        /></svg
                                      ><ins
                                        @click="generateReport(item, true)"
                                        >{{ $t("download") }}</ins
                                      >
                                    </md-button>
                                  </div>
                                </md-table-cell>
                              </md-table-row>
                              <md-table-row
                                v-if="visibleFatures"
                                class="empty-data"
                              >
                                <md-table-cell
                                  :colspan="7"
                                  class="align-text"
                                  >{{ errorFactures }}</md-table-cell
                                >
                              </md-table-row>

                              <md-table-row
                                class="pagination-row"
                                v-if="!visibleFatures"
                              >
                                <md-table-cell :colspan="7">
                                  <TablePagination
                                    @pageVal="handleChangeBillPageValue"
                                    @pageSize="handleChangeBillSizeValue"
                                    :dataSize="dataBillSize"
                                    :next="nextBill"
                                  />
                                </md-table-cell>
                              </md-table-row>
                            </div>
                          </md-table>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </md-tab>
              <md-tab
                id="tab-parrainage"
                :md-label="$t('sponsorship')"
                :md-icon="iconTabs3"
              >
                <div class="md-layout md-gutter column-wrapper mx-0">
                  <div
                    class="md-layout-item dashboard-border bloc-content w-50"
                  >
                    <div
                      class="partage-wrapper d-flex flex-column align-items-center justify-content-center"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="36"
                        height="39.84"
                        viewBox="0 0 36 39.84"
                        class="m-3"
                      >
                        <path
                          id="Tracé_42480"
                          data-name="Tracé 42480"
                          d="M33,30.16a5.824,5.824,0,0,0-3.92,1.54L14.82,23.4A6.547,6.547,0,0,0,15,22a6.547,6.547,0,0,0-.18-1.4l14.1-8.22A5.987,5.987,0,1,0,27,8a6.547,6.547,0,0,0,.18,1.4l-14.1,8.22a6,6,0,1,0,0,8.76L27.32,34.7a5.642,5.642,0,0,0-.16,1.3A5.84,5.84,0,1,0,33,30.16Z"
                          transform="translate(-3 -2)"
                        />
                      </svg>
                      <h3 class="titre-recherche">{{ $t("share") }}</h3>
                      <p class="text-center" style="max-width: 528px">
                        {{ $t("shareMessage") }}
                      </p>
                    </div>

                    <div
                      class="d-flex flex-column justify-content-between mb-3"
                    >
                      <span class="pseudo-label">
                        {{ $t("mySponsorshipCode") }}
                      </span>
                      <p class="d-flex align-items-center">
                        {{ $t("copyMessage") }}
                      </p>

                      <div class="form-group w-100">
                        <md-field class="position-relative code-wrapper">
                          <md-input
                            v-model="client.storage_code_client"
                            value="KLJ08DJ23"
                            :disabled="true"
                          ></md-input>

                          <span
                            @click="copyTextToClipboard()"
                            class="md-suffix copy-wrapper position-absolute"
                          >
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              width="19"
                              height="22"
                              viewBox="0 0 19 22"
                            >
                              <path
                                id="Tracé_42482"
                                data-name="Tracé 42482"
                                d="M16,1H4A2.006,2.006,0,0,0,2,3V17H4V3H16Zm3,4H8A2.006,2.006,0,0,0,6,7V21a2.006,2.006,0,0,0,2,2H19a2.006,2.006,0,0,0,2-2V7A2.006,2.006,0,0,0,19,5Zm0,16H8V7H19Z"
                                transform="translate(-2 -1)"
                                fill="#fdca40"
                              />
                            </svg>
                            {{ $t("copy") }}
                          </span>
                        </md-field>
                      </div>
                    </div>

                    <div
                      class="d-flex flex-column justify-content-between mb-3"
                    >
                      <span class="pseudo-label">
                        {{ $t("socialMedia") }}
                      </span>
                      <p class="d-flex align-items-center">
                        {{ $t("socialMediaMessage") }}
                      </p>

                      <div class="partage-item">
                        <p class="text_content">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            class="mr-2"
                          >
                            <g
                              id="Twitter_Social_Icon_Circle_Color"
                              transform="translate(0 0)"
                            >
                              <g id="Dark_Blue" transform="translate(0 0)">
                                <circle
                                  id="Ellipse_923"
                                  data-name="Ellipse 923"
                                  cx="12"
                                  cy="12"
                                  r="12"
                                  fill="#1da1f2"
                                />
                              </g>
                              <g
                                id="Logo__x2014__FIXED"
                                transform="translate(5.382 6.87)"
                              >
                                <path
                                  id="Tracé_42483"
                                  data-name="Tracé 42483"
                                  d="M94.122,125.96a8.176,8.176,0,0,0,8.232-8.232c0-.126,0-.252-.006-.372a5.927,5.927,0,0,0,1.446-1.5,5.872,5.872,0,0,1-1.662.456,2.891,2.891,0,0,0,1.272-1.6,5.859,5.859,0,0,1-1.836.7,2.895,2.895,0,0,0-5,1.98,2.651,2.651,0,0,0,.078.66,8.208,8.208,0,0,1-5.964-3.024,2.892,2.892,0,0,0,.9,3.858,2.842,2.842,0,0,1-1.308-.36v.036a2.9,2.9,0,0,0,2.322,2.838,2.884,2.884,0,0,1-.762.1,2.763,2.763,0,0,1-.546-.054,2.889,2.889,0,0,0,2.7,2.01,5.816,5.816,0,0,1-3.594,1.236,5.261,5.261,0,0,1-.69-.042,8.061,8.061,0,0,0,4.422,1.308"
                                  transform="translate(-89.7 -114.5)"
                                  fill="#fff"
                                />
                              </g>
                            </g>
                          </svg>

                          <span
                            >{{ $t("shareCode") }}
                            <strong class="ml-md-1">Twitter</strong></span
                          >
                        </p>
                        <div class="btn_content">
                          <md-button
                            type="submit"
                            class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                          >
                            <ShareNetwork
                              network="twitter"
                              :title="titleSocialMedia()"
                              :url="sharingURL()"
                              class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                            >
                              {{ $t("share") }}
                            </ShareNetwork>
                          </md-button>
                        </div>
                      </div>

                      <div class="partage-item">
                        <p class="text_content">
                          <svg
                            id="Groupe_52939"
                            data-name="Groupe 52939"
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            class="mr-2"
                          >
                            <path
                              id="Tracé_42484"
                              data-name="Tracé 42484"
                              d="M24,12A12,12,0,1,0,10.125,23.854V15.469H7.078V12h3.047V9.356c0-3.008,1.792-4.669,4.533-4.669a18.453,18.453,0,0,1,2.686.234V7.875H15.831a1.734,1.734,0,0,0-1.956,1.874V12H17.2l-.532,3.469h-2.8v8.385A12,12,0,0,0,24,12Z"
                              fill="#1877f2"
                            />
                            <path
                              id="Tracé_42485"
                              data-name="Tracé 42485"
                              d="M311.593,210.781l.532-3.469H308.8v-2.251a1.734,1.734,0,0,1,1.956-1.874h1.513v-2.953a18.453,18.453,0,0,0-2.686-.234c-2.741,0-4.533,1.661-4.533,4.669v2.644H302v3.469h3.047v8.385a12.127,12.127,0,0,0,3.75,0v-8.385Z"
                              transform="translate(-294.922 -195.313)"
                              fill="#fff"
                            />
                          </svg>
                          <span
                            >{{ $t("shareCode") }}
                            <strong class="ml-md-1">Facebook</strong></span
                          >
                        </p>
                        <div class="btn_content">
                          <md-button
                            type="submit"
                            class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                          >
                            <ShareNetwork
                              network="facebook"
                              :url="sharingURL()"
                              title=""
                              :quote="titleSocialMedia()"
                              hashtags="predictMarket"
                              class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                            >
                              {{ $t("share") }}
                            </ShareNetwork>
                          </md-button>
                        </div>
                      </div>

                      <div class="partage-item">
                        <p class="text_content">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            class="mr-2"
                          >
                            <path
                              id="Tracé_42489"
                              data-name="Tracé 42489"
                              d="M720.78,1006.28a12,12,0,1,0,12,12A12,12,0,0,0,720.78,1006.28Zm-3.189,17.577h-2.5v-7.526h2.5Zm-.214-8.923a1.449,1.449,0,0,1-1.036.372h-.011a1.379,1.379,0,0,1-1-.372,1.249,1.249,0,0,1-.383-.935,1.213,1.213,0,0,1,.394-.93,1.447,1.447,0,0,1,1.025-.366,1.4,1.4,0,0,1,1,.36,1.271,1.271,0,0,1,.394.969A1.186,1.186,0,0,1,717.377,1014.934Zm9.239,8.923h-2.5v-4.022q0-1.7-1.262-1.7a1.224,1.224,0,0,0-.806.265,1.467,1.467,0,0,0-.569,1.256v4.2h-2.5q.023-3.4.023-5.284t-.023-2.242h2.5v1.07a2.557,2.557,0,0,1,2.265-1.251,2.69,2.69,0,0,1,2.084.862,3.626,3.626,0,0,1,.789,2.529Zm-5.138-6.433v-.023l-.011.023Z"
                              transform="translate(-708.78 -1006.28)"
                              fill="#2867b2"
                            />
                          </svg>
                          <span
                            >{{ $t("shareCode") }}
                            <strong class="ml-md-1">Linkedin</strong></span
                          >
                        </p>
                        <div class="btn_content">
                          <md-button
                            type="submit"
                            class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                            @click="shareLinkedin()"
                          >
                            {{ $t("share") }}
                          </md-button>
                        </div>
                      </div>

                      <div class="partage-item">
                        <p class="text_content">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            class="mr-2"
                          >
                            <defs>
                              <linearGradient
                                id="linear-gradient"
                                x1="0.665"
                                y1="0.159"
                                x2="0.419"
                                y2="0.751"
                                gradientUnits="objectBoundingBox"
                              >
                                <stop offset="0" stop-color="#2aabee" />
                                <stop offset="1" stop-color="#229ed9" />
                              </linearGradient>
                            </defs>
                            <g id="Telegram_2019_Logo" transform="translate(0)">
                              <circle
                                id="Ellipse_924"
                                data-name="Ellipse 924"
                                cx="12"
                                cy="12"
                                r="12"
                                transform="translate(0 0)"
                                fill="url(#linear-gradient)"
                              />
                              <path
                                id="Tracé_42488"
                                data-name="Tracé 42488"
                                d="M54.687,70.243s1.249-.486,1.145.694c-.035.486-.347,2.185-.59,4.023l-.832,5.445s-.069.8-.694.936a2.767,2.767,0,0,1-1.734-.624c-.139-.1-2.6-1.665-3.468-2.428a.657.657,0,0,1,.035-1.11l3.642-3.468c.416-.416.832-1.387-.9-.208L46.432,76.8a2.038,2.038,0,0,1-1.6.035l-2.254-.694s-.832-.52.59-1.04C46.641,73.469,50.906,71.8,54.687,70.243Z"
                                transform="translate(-38.109 -63.133)"
                                fill="#fff"
                              />
                            </g>
                          </svg>
                          <span
                            >{{ $t("shareCode") }}
                            <strong class="ml-md-1"> Telegram</strong></span
                          >
                        </p>
                        <div class="btn_content">
                          <md-button
                            type="submit"
                            class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                          >
                            <ShareNetwork
                              network="telegram"
                              :url="sharingURL()"
                              :title="titleSocialMedia()"
                              hashtags="predictMarket"
                              class="submit-dialog text-center btn-submit text-normal w-auto py-0 my-0 mr-0"
                            >
                              {{ $t("share") }}
                            </ShareNetwork>
                          </md-button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="md-layout-item w-50 px-0">
                    <div
                      class="dashboard-border bloc-content mx-0 d-flex flex-wrap align-items-center"
                    >
                      <div class="d-flex flex-column total-wrapper ">
                        <span class="pseudo-label">{{ $t("total") }}</span>
                        <p>
                          {{ $t("totalMessage") }}
                        </p>
                      </div>
                      <div class="details-total bloc-content">
                        <div class="content_item">
                          <span>{{ $t("affiliates") }}</span>
                          <span class="value">{{ userAffiliated }}</span>
                        </div>
                        <div class="content_item">
                          <span>{{ $t("storedDays") }}</span>
                          <span class="value"
                            >{{ totalDays }} {{ $t("unitDay") }}</span
                          >
                        </div>
                        <div class="content_item">
                          <span>{{ $t("storedCredits") }}</span>
                          <span class="value"
                            >{{ pointToComma(totalCredits.toFixed(2)) }} €</span
                          >
                        </div>
                      </div>
                    </div>
                    <div class="d-flex flex-column">
                      <h3 class="titre-recherche">
                        {{ $t("tableAffiliates") }}
                      </h3>
                      <p>{{ $t("consultListAffiliates") }}</p>

                      <md-table
                        md-table-fixed-header
                        class="mt-3 predict-table d-flex flex-grow-1"
                      >
                        <md-table-row class="table-header">
                          <md-table-head scope="col">
                            {{ $t("affiliate") }}
                            <span class="table-tri d-flex flex-column">
                              <md-button
                                class="btn-tri arrow-up"
                                v-on:click="orderBy('client_child_name')"
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
                                v-on:click="orderBy('-' + 'client_child_name')"
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
                          <md-table-head scope="col">
                            {{ $t("days") }}
                            <span class="table-tri d-flex flex-column">
                              <md-button
                                class="btn-tri arrow-up"
                                v-on:click="orderBy('reward_day_by_child')"
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
                                v-on:click="
                                  orderBy('-' + 'reward_day_by_child')
                                "
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
                          <md-table-head scope="col">
                            {{ $t("credits") }}
                            <span class="table-tri d-flex flex-column">
                              <md-button
                                class="btn-tri arrow-up"
                                v-on:click="orderBy('reward_credit_by_child')"
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
                                v-on:click="
                                  orderBy('-' + 'reward_credit_by_child')
                                "
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
                        </md-table-row>
                        <md-table-row
                          v-for="(item, index) in affiliated"
                          :key="index"
                        >
                          <md-table-cell data-label="Affilié">{{
                            item.client_child_name
                          }}</md-table-cell>
                          <md-table-cell data-label="Jours"
                            >{{ item.reward_day_by_child }}
                            {{ $t("unitDay") }}</md-table-cell
                          >
                          <md-table-cell data-label="Crédits"
                            >{{
                              pointToComma(
                                item.reward_credit_by_child.toFixed(2)
                              )
                            }}
                            €</md-table-cell
                          >
                        </md-table-row>

                        <md-table-row v-if="visibleAffiliated">
                          <md-table-cell
                            data-label=""
                            :colspan="3"
                            class="align-text"
                            >{{ errorAffiliated }}</md-table-cell
                          >
                        </md-table-row>

                        <md-table-row
                          class="pagination-row"
                          v-if="!visibleAffiliated"
                        >
                          <md-table-cell :colspan="3">
                            <TablePagination
                              @pageVal="handleChangeAffiliatedPageValue"
                              @pageSize="handleChangeAffiliatedSizeValue"
                              :dataSize="dataAffiliatedSize"
                              :next="nextAffiliated"
                            />
                          </md-table-cell>
                        </md-table-row>
                      </md-table>
                    </div>
                  </div>
                </div>
              </md-tab>
            </md-tabs>
          </div>
        </div>
      </div>
      <Dialog
        :showDialog="showDialogActivation"
        :titreDialog="$t('smsVerification')"
        :dialogName="`Activation`"
        @close="closeModalSMSAcvtivation"
      >
        <div class="text-center mx-auto mb-4" style="max-width: 409px;">
          {{ $t("enterCodeMessage") }} <strong>{{ telephone }}</strong
          >.
        </div>

        <div class="form-user-wrapper">
          <form class="form-user form-sms " novalidate="true">
            <div
              class="form-group code-activation d-flex flex-nowrap justify-content-between"
            >
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number1"
                  id="number1"
                  autocomplete="off"
                  v-model="number1"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number2"
                  id="number2"
                  autocomplete="off"
                  v-model="number2"
                  ref="n2"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number3"
                  id="number3"
                  autocomplete="off"
                  v-model="number3"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number4"
                  id="number4"
                  autocomplete="off"
                  v-model="number4"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number5"
                  id="number5"
                  autocomplete="off"
                  v-model="number5"
                  @keypress="numericOnly"
                />
              </md-field>
              <md-field :md-counter="false">
                <md-input
                  maxlength="1"
                  name="number6"
                  id="number6"
                  autocomplete="off"
                  v-model="number6"
                  @keypress="numericOnly"
                />
              </md-field>
            </div>
            <span
              v-if="errorCode.length"
              class="d-flex flex-column text-center"
            >
              <span class="error" v-for="error in errorCode" :key="error">{{
                error
              }}</span>
            </span>

            <md-button
              :md-ripple="false"
              class="text-uppercase mx-0 py-3 h-auto w-100 text-uppercase btn-submit"
              @click="verificationPhone()"
              :disabled="
                !(
                  number1 &&
                  number2 &&
                  number3 &&
                  number4 &&
                  number5 &&
                  number6
                )
              "
            >
              {{ $t("verify") }}
            </md-button>

            <div
              class="form-additionnel row-fluid d-flex flex-column w-100 justify-content-center mb-4 pb-2"
            >
              <div class="inscription-link-container text-center">
                <p v-if="!resend">
                  {{ $t("codeNotSentMessage") }}
                </p>
                <router-link
                  to="#"
                  @click.native="resendCode"
                  class="mt-2 d-block"
                  v-if="!resend"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="22"
                    viewBox="0 0 16 22"
                  >
                    <path
                      id="Tracé_19663"
                      data-name="Tracé 19663"
                      d="M12,6V9l4-4L12,1V4A7.986,7.986,0,0,0,5.24,16.26L6.7,14.8A5.87,5.87,0,0,1,6,12,6,6,0,0,1,12,6Zm6.76,1.74L17.3,9.2A5.99,5.99,0,0,1,12,18V15L8,19l4,4V20A7.986,7.986,0,0,0,18.76,7.74Z"
                      transform="translate(-4 -1)"
                      fill="#242C36"
                    />
                  </svg>
                  {{ $t("resendCode") }}
                </router-link>
                <p v-else>
                  {{ $t("codeSent") }}
                  {{ countDown }}s
                </p>
              </div>
            </div>
          </form>
        </div>
      </Dialog>
      <Dialog
        :showDialog="showDialogModificationReussi"
        :titreDialog="$t('successModification')"
        :iconDialog="iconModif"
        @close="showDialogModificationReussi = !showDialogModificationReussi"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("success:phoneModification") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogModificationReussi = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>
      <Dialog
        :showDialog="showDialogModificationInfo"
        :titreDialog="$t('successModification')"
        :iconDialog="iconModif"
        @close="showDialogModificationInfo = !showDialogModificationInfo"
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("success:infoModification") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogModificationInfo = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>
      <Dialog
        :showDialog="showDialogModificationPassword"
        :titreDialog="$t('successModification')"
        :iconDialog="iconModif"
        @close="
          showDialogModificationPassword = !showDialogModificationPassword
        "
      >
        <div class="text-center" style="max-width: 380px;">
          {{ $t("success:passwordModification") }}
        </div>

        <div class="form-group text-center mt-4">
          <md-button
            class="submit-dialog text-center btn-submit text-center w-100 px-0 mx-0"
            @click="showDialogModificationPassword = false"
          >
            {{ $t("continue") }}
          </md-button>
        </div>
      </Dialog>
    </PermanentFull>

    <div class="wrapperPdf">
      <vue-html2pdf
        id="html2pdf"
        :show-layout="false"
        :float-layout="true"
        :enable-download="downloadLayout"
        :preview-modal="true"
        :paginate-elements-by-height="1400"
        filename="Facture"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a4"
        pdf-content-width="800px"
        @hasStartedGeneration="hasStartedGeneration()"
        @hasGenerated="hasGenerated($event)"
        ref="html2Pdf"
      >
        <section slot="pdf-content" style="height: 100%">
          <div
            class="mui-container wrapper"
            style="max-width: 620px; margin-left: auto; margin-right: auto; min-height: 100vh; display: flex; flex-direction: column;
            font-family: Arial, sans-serif"
          >
            <div
              style="display: block; height: 8px; margin-top: 10px; background-color: #fdca40;"
            ></div>

            <div
              style="margin-top: 35px; padding-left: 40px; padding-right: 40px;"
            >
              <img
                data-v-ba6df2ea=""
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABaCAYAAAAvitHLAAAABHNCSVQICAgIfAhkiAAABJ5JREFUeF7tnUtoE1EUhs+ZKCpU3SnUgvh2YVOw1QQXbZOI4gMVVz4QFXx1I4JgwYVtFyIVRXAjRUHxUV35QvGBTaob22qFpgWtL1xY0Z3agoqduZ4bTai1JpmcMWaSczdZzPx35nz574OZM/ciJCnTyxdPLPKYqwGNtQBqLiAUI+D4ZBq3H1Og+imGPlT4jGK+3D9oXH/dee/T3+LCkQ7M84UmGwD7AdUOAjbW7VA4909Av4KCJgvwUE97y4fhdf0BcN7CwAoPGs3ktgmcC+edVsFnhdamaFvk+tDYhgJErz9YR7QPIJW8A+BAQEoXhAPdbeGDVJ3SVSZAlfpDG6nZnnfgOnlfhQVqK0E8kwBY5gsFqL+7SzxH5X30TgSo1HcLcXl3W8u9mAO9vtBVarSrnai7UOpQCq5F21vWoHfRkklgDr6Xfs/eX6+7w0HLKsayhcFdYOAJe3I5O0bAUjV65G2luV6VILFPgJrxHaQB5CONxRPty0VBE5lP5MDQVxpJxggO+wRoIvgNy/yh2IRQSmYEBGBm3BIqASgAmQSYcnGgAGQSYMrFgQKQSYApFwcKQCYBplwcKACZBJhycaAAZBJgysWBApBJgCkXBwpAJgGmXBwoAJkEmHJxoABkEmDKxYECkEmAKRcHCkAmAaZcHCgAmQSYcnGgAGQSYMrFgQKQSYApFwcKQCYBplwcWKgAq70K5kwBKJ9JvyUKxo+zR6L/C0DvW4TOlwi9fQCt0cw+D3SdAzWs+o0anrOp3b19CPUXCCZBtVNcBXDnMgU7l1l24rN9btMtA5pupQ/RNQA1OA0wG+XIFQOaI+lBdAVA3Wwv7vu3zhv+x6w/bKTVnF0B8GKt5Xifl8rJuk9c30hfUKcoOQ8wQKPt0W3ZdV+c2d5TBkRSjM45DzCbfd9ws+nBRA8qyUrOAzy526S5XqqG9G+Od74E2H7c426A9xtN25Nkp3DqyXZVrcsBPjluOsUjo3rm7xaAGYGLiwQgCx+AABSA0geyPCCDCAsfgAAUgEwCTLk4UAAyCTDl4kAByCTAlIsDBSCTAFMuDmQCfEDPA4tsvjRnXjIhH6DngZVufx4oT6SZdpB3IkyA8laOCVDLL+0zYXaJAxXZqOL5W4B1h5M/ztfV5fxbOX2TOZ2Z4JYlQLPZF6adG6PXUC3zB9+QEafacPd/OzUbENOGRxRoKeledNsq5ro5N2ywHO8TdZ9X15xeQlHcQXo1cwIY3EOrmB/7b7bK8MJ6dJ5NSZYVs35mqtqdbOtJss5MffwC4TklEqXKgRnxNvVC3KXl1XON0Z6nGcZR0DIEc1p8M4LbtBnB0oKmYTP4xGYEWuetCMyBUUaXLMidHsXYAtyoZnQ9DFPj/1VK/cEtBuDp9Koo7LOUZW2OdkTOxibSQ1HQxgT1tDFBXWHjSR49bVLVEG0L18fP+iOT2usPrEJlnJNNqYaBpE2pTGVt6OmI3Bx6ZMRUdK+vugTRo/cYWSlujBG4oZRZE21vpdni7yVpLn/pgmAleiBAEh9t/TCdXDmFmnhRPkOlJjpAm/K9U6heUZwdyoRw96Pwg7/F/AMoXdyj+SH4EAAAAABJRU5ErkJggg=="
                class="logo mr-2"
                alt="Logo Jaune"
                width="26"
                height="26"
              />
            </div>

            <div
              style="margin-top: 20px; padding-left: 40px; padding-right: 40px;"
            >
              <div
                style="float: left; background-color: #f3f3f3; padding: 10px; width: 290px; color: rgb(102, 102, 102);"
              >
                <div>
                  <span style="font-size: 11px;">{{ $t("refInvoice") }}</span
                  ><strong style="font-size: 11px; color: #242c36;">
                    :&nbsp;{{ referenceFacture }}</strong
                  >
                </div>
                <div>
                  <span style="font-size: 11px;">{{ $t("typeInvoice") }}</span
                  ><strong style="font-size: 11px; color: #242c36;">
                    :&nbsp;{{ $t("subscription") }}</strong
                  >
                </div>
                <div>
                  <span style="font-size: 11px;">{{ $t("emissionDate") }}</span
                  ><strong style="font-size: 11px; color: #242c36;">
                    :&nbsp;{{ dateEmission }}</strong
                  >
                </div>
                <div>
                  <span style="font-size: 11px;">{{ $t("expiryDate") }}</span
                  ><strong style="font-size: 11px; color: #242c36;">
                    :&nbsp;{{ dateEcheance }}</strong
                  >
                </div>
              </div>
              <div style="padding: 20px; float: right; color: #242c36;">
                <div>
                  <div style="width: 100%; font-size: 11px;">
                    <strong>{{ fullName }}</strong>
                  </div>
                  <div style="width: 100%;">
                    <strong style="font-size: 11px;">{{ client.email }}</strong>
                  </div>
                  <div style="width: 100%;">
                    <strong style="font-size: 11px;">{{ client.phone }}</strong>
                  </div>
                </div>
              </div>
            </div>

            <div
              style="
                padding-left: 40px; padding-right: 40px;
                padding-top: 10px;
                padding-bottom: 50px;
                max-width: 640px;
                clear: both"
            >
              <div
                style="
                  margin-left: auto; margin-right: auto;
                  padding-top: 50px;
                  padding-bottom: 50px;"
              >
                <div>
                  <div
                    style="margin-left: auto; margin-right: auto; text-align:center;"
                  >
                    <div
                      style="margin-left: auto; margin-bottom: 5px; margin-right: auto; font-size: 18px; text-align:left;"
                    >
                      <strong style="font-size: 14px;">{{
                        $t("subscriptionSection")
                      }}</strong>
                    </div>
                    <table
                      style="margin-left: 0; margin-right: auto;"
                      aria-describedby="Rubrique Abonnement"
                    >
                      <tbody style="margin-left: auto; margin-right: auto;">
                        <tr
                          class="md-table-row table-header"
                          style="margin-left: auto; margin-right: auto;"
                        >
                          <th
                            id="th1"
                            style="
                              padding: 8px 11px;
                              text-align: center;
                              background-color: #fdca40;
                              font-size: 11px;
                              font-weight: bold;
                              width: 250px;"
                            class="md-table-head col-desc"
                            scope="col"
                          >
                            <div class="">
                              <div class="">{{ $t("description") }}</div>
                            </div>
                          </th>

                          <th
                            id="th2"
                            style="
                              padding: 8px 11px;
                              text-align: center;
                              background-color: #fdca40;
                              font-size: 11px;
                              font-weight: bold;"
                            class="md-table-head col-ref"
                            scope="col"
                          >
                            <div class="">
                              <div class="">{{ $t("reference") }}</div>
                            </div>
                          </th>
                          <th
                            id="th3"
                            style="
                              padding: 8px 11px;
                              text-align: center;
                              background-color: #fdca40;
                              font-size: 11px;
                              font-weight: bold;
                              width: 58px;"
                            class="md-table-head col-qte"
                            scope="col"
                          >
                            <div class="">
                              <div class="">{{ $t("quantity") }}</div>
                            </div>
                          </th>
                          <th
                            id="th4"
                            style="
                              padding: 8px 11px;
                              text-align: center;
                              background-color: #fdca40;
                              font-size: 12px;
                              width: 100px;
                              font-weight: bold;"
                            class="md-table-head col-pu"
                            scope="col"
                          >
                            <div class="">
                              <div class="">{{ $t("priceUnit") }}</div>
                            </div>
                          </th>
                          <th
                            id="th5"
                            style="
                              padding: 8px 11px;
                              text-align: center;
                              height: 40px;
                              background-color: #fdca40;
                              font-size: 11px;
                              width: 95px;
                              font-weight: bold;"
                            class="md-table-head col-pht"
                            scope="col"
                          >
                            <div class="">
                              <div class="">{{ $t("priceHT") }}</div>
                            </div>
                          </th>
                        </tr>
                        <tr>
                          <td
                            style="
                              border-bottom: 1px solid #999999;
                              text-align: left;
                              padding: 8px 0;
                              font-size: 11px;"
                          >
                            {{ abonnementFacture }}
                          </td>
                          <td
                            style="
                              border-bottom: 1px solid #999999;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;"
                            class="col-ref border_bottom"
                          >
                            {{ referenceAbonnement }}
                          </td>
                          <td
                            style="
                              border-bottom: 1px solid #999999; 
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;"
                            class="col-qte border_bottom"
                          >
                            1
                          </td>
                          <td
                            style="
                              border-bottom: 1px solid #999999;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;"
                            class="col-pu border_bottom"
                          >
                            {{ prixFacture }} €
                          </td>
                          <td
                            style="
                              border-bottom: 1px solid #999999;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;"
                            class="col-pht border_bottom"
                          >
                            {{ prixFacture }} €
                          </td>
                        </tr>
                        <tr>
                          <td colspan="3"></td>
                          <td
                            style="
                              color: #666666;
                              font-weight: 700;
                              font-size: 11px;
                              text-align: center;
                              padding: 8  px 11px;"
                          >
                            {{ $t("subTotal") }}
                          </td>
                          <td
                            style="
                              color: #666666;
                              font-weight: 700;
                              font-size: 11px;
                              text-align: center;
                              padding: 8px 11px;"
                          >
                            {{ prixFacture }} €
                          </td>
                        </tr>
                        <tr>
                          <td colspan="2" rowspan="4">
                            <div
                              style="
                                background-color: #f3f3f3;
                                padding: 16px 10px;
                                text-align: left;"
                            >
                              <div
                                style="
                                  color: #242c36;
                                  font-weight: 700;
                                  margin-bottom: 3px;
                                  font-size: 11px;"
                              >
                                {{ $t("payInfo") }} :
                              </div>
                              <p
                                style="
                                  color: #666666;
                                  font-size: 10.5px;
                                  line-height: 12px;
                                  margin: 0;"
                              >
                                {{ $t("amountOf") }}
                                <strong
                                  >{{ pointToComma(totalPrice) }} €</strong
                                >
                                {{ $t("chargedOnDefaultPayement") }}. <br />
                                {{ $t("invoiceOnReceipt") }}.
                              </p>
                              <br />
                              <p
                                style="
                                  color: #666666;
                                  font-size: 10.5px;
                                  line-height: 12px;
                                  margin: 0;"
                              >
                                {{ $t("managePaymentMethods") }} : <br />{{
                                  $t("goToCustomerArea")
                                }}.
                              </p>
                            </div>
                          </td>
                          <td></td>
                          <td></td>
                          <td></td>
                        </tr>
                        <tr>
                          <td></td>
                          <td
                            style="
                              color: #666666;
                              font-weight: 700;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;
                              border-bottom: 1px solid #999999;"
                          >
                            {{ $t("priceHT") }}
                          </td>
                          <td
                            style="
                              color: #666666;
                              font-weight: 700;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;
                              border-bottom: 1px solid #999999;"
                          >
                            {{ prixFacture }} €
                          </td>
                        </tr>
                        <tr>
                          <td></td>
                          <td
                            style="
                              color: #666666;
                              font-weight: 700;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;
                              border-bottom: 1px solid #999999;"
                          >
                            {{ $t("tva") }} (20%)
                          </td>
                          <td
                            style="
                              color: #666666;
                              font-weight: 700;
                              text-align: center;
                              padding: 8px 11px;
                              font-size: 11px;
                              border-bottom: 1px solid #999999;"
                          >
                            {{ pointToComma(priceWithTVA) }} €
                          </td>
                        </tr>
                        <tr>
                          <td></td>
                          <td
                            style="
                              padding: 8px 11px;
                              color: #434343;
                              font-weight: 700;
                              border-bottom: 2px solid #999999;
                              text-align: center;
                              font-size: 11px;"
                          >
                            {{ $t("totalTTC") }}
                          </td>
                          <td
                            style="
                              padding: 8px 11px;
                              color: #434343;
                              font-weight: 700;
                              border-bottom: 2px solid #999999;
                              text-align: center;
                              font-size: 11px;"
                          >
                            {{ pointToComma(totalPrice) }} €
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              <div style="margin-left: auto; margin-right: auto;">
                <div
                  style="margin-left: auto; margin-right: auto; font-size: 11px; color: rgb(102, 102, 102);"
                >
                  {{ $t("noDiscount") }}.
                  <br />
                  {{ $t("paymentIncident") }}.
                </div>
                <div
                  style="margin-left: auto; margin-right: auto; margin-top: 15px; color: rgb(102, 102, 102);"
                >
                  <div style="font-size:11px;margin-bottom: 0;">
                    {{ $t("bankDetails") }}
                  </div>
                  <div style="font-size:11px;margin-bottom: 0;">
                    CAISSE EPARGNE
                  </div>
                  <div style="font-size:11px;margin-bottom: 0;">
                    BIC : CEPAFRPP382
                  </div>
                  <div style="font-size:11px;margin-bottom: 0;">
                    IBAN : FR76 1382 5002 0008 0119 7588 662
                  </div>
                </div>
              </div>
            </div>
            <div
              style="margin-top: 15%; margin-right: auto; margin-left: auto; padding-left: 40px; padding-right: 40px; color: rgb(102, 102, 102);"
            >
              <hr
                style="margin-top: auto; margin-right: auto; margin-left: auto; width: 550px; border-style: solid; border-width:thin"
              />
              <div style="text-align:center; max-width: 600px; font-size: 10px">
                <strong
                  >LEVIATAN - 725 boulevard Robert Barrier 73100 Aix-les-Bains -
                  France</strong
                ><br />
                SAS au capital de 4 000,00 € - RCS CHAMBÉRY 828 562 785 - Code
                APE 6312Z<br />
                N°TVA FR26828562785
              </div>
            </div>
          </div>
        </section>
      </vue-html2pdf>
    </div>
  </div>
</template>

<script>
import MenuUser from "../../data/MenuUser.js";
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import BlocAbonnement from "../BlocAbonnement/BlocAbonnement.vue";
import PredictInputNumber from "../Input/PredictInputNumber.vue";
import {
  RESEND_WAITING,
  SMS_CODE,
  API_URL,
  SHARE_URL,
} from "../../utils/Constant";
import Dialog from "../Dialog/Dialog.vue";
import moment from "moment";
import axios from "axios";
import VueHtml2pdf from "vue-html2pdf";
import UploadFile from "../Input/UploadFile.vue";
import TablePagination from "../Pagination/TablePagination.vue";
import queryString from "query-string";

export default {
  name: "MonCompte",
  components: {
    PermanentFull,
    BlocAbonnement,
    PredictInputNumber,
    VueHtml2pdf,
    //PredictSubmit,
    Dialog,
    UploadFile,
    TablePagination,
  },
  props: {
    msg: String,
  },
  computed: {
    isDisabled() {
      if (
        this.number1 &&
        this.number2 &&
        this.number3 &&
        this.number4 &&
        this.number5 &&
        this.number6
      ) {
        return false;
      }
      return true;
    },
    client() {
      return this.$store.state.client.clients;
    },
    factures() {
      return this.$store.state.facture.factures.results;
    },
    dataBillSize() {
      return this.$store.state.facture.factures.count;
    },
    nextBill() {
      return this.$store.state.facture.factures.next;
    },
    affiliated() {
      return this.$store.state.parrainage.parrainages.results;
    },
    dataAffiliatedSize() {
      return this.$store.state.parrainage.parrainages.count;
    },
    nextAffiliated() {
      return this.$store.state.parrainage.parrainages.next;
    },
  },
  async mounted() {
    await this.loadClient();
    await this.loadAffiliated();
    await this.loadFactures();
    await this.checkAffiliatedData();
    await this.checkFacturesData();

    this.closePdfViewer = this.$refs.html2Pdf.closePreview;
    this.$refs.html2Pdf.closePreview = () => {
      this.closePdfViewer();
      document.getElementById("html2pdf").classList.remove("open-pdf");
    };
  },
  watch: {
    image(val) {
      if (val) this.showButton = true;
      if (!val) this.showButton = false;
    },
    async pageBill() {
      await this.loadFactures();
    },
    async sizeBill() {
      await this.loadFactures();
    },
    async pageAffiliated() {
      await this.loadAffiliated();
    },
    async sizeAffiliated() {
      await this.loadAffiliated();
    },
    "$i18n.locale"() {
      this.errorFactures = this.$t("tableNoDataYet");
      this.tel_options = {
        placeholder: this.$t("phone:placeholder"),
      };
    },
    number1(val) {
      if (val) {
        document.getElementById("number2").focus();
      }
    },
    number2(val) {
      if (val) {
        document.getElementById("number3").focus();
      }
    },
    number3(val) {
      if (val) {
        document.getElementById("number4").focus();
      }
    },
    number4(val) {
      if (val) {
        document.getElementById("number5").focus();
      }
    },
    number5(val) {
      if (val) {
        document.getElementById("number6").focus();
      }
    },
    async search() {
      await this.loadFactures();
      if (!this.factures.length) {
        this.errorFactures = this.$t("noDataFound");
        this.visibleFatures = true;
      } else {
        this.errorFactures = "";
        this.visibleFatures = false;
      }
    },
    jourGratuit(val) {
      this.disableDay = !val ? true : false;
      this.disableDay = this.free_day < val ? true : false;
    },
    credits(val) {
      this.disableCredit = !val ? true : false;
      this.disableCredit = this.sum < val ? true : false;
    },
  },
  methods: {
    handleUserphoto() {
      this.userPhoto = false;
    },
    async shareLinkedin() {
      const popUp = window.open(
        `https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=78v3ljq07zd626&redirect_uri=${SHARE_URL}&scope=r_liteprofile%20r_emailaddress%20w_member_social`,
        "popup",
        "width=600,height=600"
      );
      let href = "";
      const interval = setInterval(() => {
        try {
          href = popUp.location.href;
        } catch (error) {
          //
        }
        if (href) {
          popUp.close();
          clearInterval(interval);

          const parsed = queryString.parse(new URL(href).search);

          if (parsed.code) {
            const payload = {
              code: this.client.storage_code_client,
              parsed_code: parsed.code,
            };
            try {
              this.$store.dispatch("shareLinkedin", {
                token: localStorage.getItem("token"),
                payload,
                language: this.$i18n.locale,
              });
            } catch (e) {
              //
            }
          }
        }
      }, 1000);
    },
    handleChangeBillPageValue(val) {
      this.pageBill = val;
    },
    handleChangeBillSizeValue(val) {
      this.sizeBill = val;
    },
    handleChangeAffiliatedPageValue(val) {
      this.pageAffiliated = val;
    },
    handleChangeAffiliatedSizeValue(val) {
      this.sizeAffiliated = val;
    },
    handleImage(event) {
      this.image = event[0];
    },
    async onUpload() {
      if (this.image) {
        try {
          await this.$store.dispatch("uploadUserProfile", {
            image: this.image,
            token: localStorage.getItem("token"),
          });
          this.$refs.PermanentFull.refresh();
          this.showButton = false;
          await this.loadClient();
          this.showMessage = true;
          setInterval(() => {
            this.showMessage = false;
          }, 7200);
        } catch (e) {
          //
        }
      }
    },
    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
    upgradeSubscription() {
      localStorage.setItem("upgrade", 1);
      this.$router.push({
        name: "Abonnement",
      });
    },
    async copyTextToClipboard() {
      try {
        await navigator.clipboard.writeText(this.client.storage_code_client);
      } catch ($e) {
        //
      }
    },
    sharingURL() {
      return SHARE_URL;
    },
    addDays: async function(item) {
      const payload = {
        days: +item,
      };
      try {
        await this.$store.dispatch("addDays", {
          token: localStorage.getItem("token"),
          payload: payload,
        });
        this.loadClient();
      } catch (e) {
        //
      }
    },
    addCredits: async function(item) {
      const payload = {
        credits: +item,
      };
      try {
        await this.$store.dispatch("addCredits", {
          token: localStorage.getItem("token"),
          payload: payload,
        });
        this.loadClient();
      } catch (e) {
        //
      }
    },
    titleSocialMedia() {
      return `${this.$t("useMyCode")} "${
        this.client.storage_code_client
      }" ${this.$t("useMyCode1")}`;
    },
    async pdf() {
      const data = {
        amount: 10,
      };
      await axios
        .post(`${API_URL}/api/pdf`, data, {
          responseType: "blob",
        })
        .then((res) => {
          let blob = new Blob([res.data], {
            type: "application/pdf",
          });

          let fileURL = window.URL.createObjectURL(blob);
          window.open(fileURL);
        });
    },
    generateReport(item, download) {
      this.downloadLayout = download;
      this.getDataForFacturation(item);
      this.$refs.html2Pdf.generatePdf();
      setTimeout(function() {
        document.getElementById("html2pdf").classList.add("open-pdf");
      }, 1000);
    },
    setFormFacture(item) {
      return ("" + item).replace(".", ",");
    },
    orderBy: async function(field) {
      await this.$store.dispatch("loadFactures", {
        token: localStorage.getItem("token"),
        order: field,
        search: this.search,
        page: this.pageBill,
        size: this.sizeBill,
      });
    },
    getDataForFacturation(item) {
      this.fullName =
        this.client.firstname.charAt(0).toUpperCase() +
        this.client.firstname.substr(1) +
        " " +
        this.client.lastname.toUpperCase();
      this.referenceFacture = item.payment.reference;
      this.referenceAbonnement = "ABO000" + item.id;
      this.abonnementFacture = item.payment.subscribe.name;
      this.prixFacture = this.setFormFacture(
        (item.final_price - item.TVA).toFixed(2)
      );
      this.priceWithTVA = this.setFormFacture(item.TVA.toFixed(2));
      this.totalPrice = this.setFormFacture(+item.final_price.toFixed(2));
      this.dateEmission = this.formatDateFacture(item.created_at);
      this.dateEcheance = this.formatDateFacture(item.payment.echeance);
    },
    init: function() {
      this.idUser = this.client.id;
      this.nom = this.client.lastname;
      this.prenom = this.client.firstname;
      this.email = this.client.email;
      this.telephone = this.client.phone;
      // this.password = this.client.password;
      this.profil = this.client.profil;
      this.sum = this.client.reward.sum;
      this.free_day = this.client.reward.free_day;
    },
    initDigit: function() {
      this.number1 = "";
      this.number2 = "";
      this.number3 = "";
      this.number4 = "";
      this.number5 = "";
      this.number6 = "";
    },
    loadClient: async function() {
      try {
        await this.$store.dispatch("loadClients", {
          token: localStorage.getItem("token"),
        });
        this.userProfile = this.client.profil;
        this.emplacementUtilise = this.$store.state.client.clients.subscription.number_couple.toString();
        this.emplacementDispo = this.$store.state.client.clients.subscription.number_couple_offered.toString();
        this.subscribeExpiration = this.$store.state.client.clients.subscription.end;
        this.renew = this.$store.state.client.clients.subscription.renew_status;
        this.subscription = this.$store.state.client.clients.subscription.name;
        this.idSubscribe = this.$store.state.client.clients.subscription.id;
        this.subscriptionPrice = this.$store.state.client.clients.subscription.price;
        this.init();
      } catch (e) {
        //
      }
    },
    loadFactures: async function() {
      try {
        await this.$store.dispatch("loadFactures", {
          token: localStorage.getItem("token"),
          search: this.search,
          page: this.pageBill,
          size: this.sizeBill,
        });
      } catch (e) {
        //
      }
    },
    checkFacturesData: async function() {
      if (!this.factures.length) {
        this.errorFactures = this.$t("tableNoDataYet");
        this.visibleFatures = true;
      }
    },
    checkAffiliatedData: async function() {
      if (!this.affiliated.length) {
        this.errorAffiliated = this.$t("tableNoDataYet");
        this.visibleAffiliated = true;
      }
    },
    updateInfo: async function() {
      const payload = {
        lastname: this.nom,
        firstname: this.prenom,
      };
      await this.$store.dispatch("updateClientInfo", {
        token: localStorage.getItem("token"),
        payload,
      });
      this.loadClient();
    },
    updatePassword: async function() {
      const payload = {
        password: this.confirmPassword,
      };
      try {
        await this.$store.dispatch("updatePassword", {
          token: localStorage.getItem("token"),
          payload,
        });
      } catch (e) {
        //
      }
      this.loadClient();

      this.toggleDialogModificationPassword();
      // this.password = this.client.password;
      this.newPassword = "";
      this.confirmPassword = "";
    },
    showDialogRenew: async function() {
      if (this.renew) {
        this.showDialogRenewAuto = this.renew;
      }
    },
    updateRenewStatus: async function() {
      this.showDialogRenew();
      const payload = {
        renew: this.renew,
      };
      try {
        await this.$store.dispatch("updateRenewStatus", {
          token: localStorage.getItem("token"),
          payload,
        });
      } catch (e) {
        //
      }
    },
    confirmPhone: async function() {
      //this.client.phone
      const payload = {
        smsCode: this.smsCode,
        phone: this.telephone.replaceAll(" ", ""),
      };
      try {
        await this.$store.dispatch("updateClientPhone", {
          payload,
          token: localStorage.getItem("token"),
        });
        this.loadClient();
      } catch (e) {
        //
      }
    },
    toggleDialogModification() {
      this.showDialogActivation = false;
      this.showDialogModificationReussi = false;
      this.showDialogModificationPassword = false;
      this.showDialogModificationReussi = !this.showDialogModificationReussi;
    },
    toggleDialogModificationInfo() {
      this.showDialogActivation = false;
      this.showDialogModificationReussi = false;
      this.showDialogModificationPassword = false;
      this.showDialogModificationInfo = !this.showDialogModificationInfo;
    },
    toggleDialogModificationPassword() {
      this.showDialogActivation = false;
      this.showDialogModificationReussi = false;
      this.showDialogModificationInfo = false;
      this.showDialogModificationPassword = !this
        .showDialogModificationPassword;
    },
    toggleDialogActivation() {
      this.showDialogModificationReussi = false;
      this.showDialogModificationInfo = false;
      this.showDialogModificationPassword = false;
      this.showDialogActivation = !this.showDialogActivation;
    },
    resendCode: async function() {
      this.resend = true;
      this.countDown = RESEND_WAITING / 1000;
      this.smsCode = SMS_CODE;
      const SMS = {
        From: "PredictM",
        To: this.telephone.replaceAll(" ", ""),
        Text: `${this.$t("smsCode")} ${this.smsCode}`,
      };
      await this.$store.dispatch("resendCode", { smsPayload: SMS });
      this.countDownTimer();
      setTimeout(() => {
        this.resend = false;
      }, RESEND_WAITING);
    },
    removeError() {
      this.errorTelephoneRequired = [];
      this.errorPwd = [];
      this.newPassword = [];
      this.confirmPassword = [];
    },
    formatDate(item) {
      return moment(item)
        .lang(localStorage.getItem("language"))
        .format("DD MMMM YYYY");
    },
    formatDateFacture(item) {
      return moment(item).format(this.$t("dateFormat"));
    },
    handleConfirmPassword() {
      if (
        this.password != this.confirmPassword &&
        this.confirmPassword.length
      ) {
        this.disabled = true;
        this.incoherentPassword = true;
      } else {
        this.disabled = false;
        this.incoherentPassword = false;
      }
    },
    handlePassword() {
      if (this.confirmPassword.length) {
        if (!this.validPassword(this.password)) {
          this.disabled = true;
          this.invalidPassword = true;
        } else {
          this.disabled = false;
          this.invalidPassword = false;
          if (this.password != this.confirmPassword) {
            this.incoherentPassword = true;
            this.disabled = true;
          } else {
            this.incoherentPassword = false;
            this.disabled = false;
          }
        }
      } else {
        if (!this.validPassword(this.password)) {
          this.disabled = true;
          this.invalidPassword = true;
        } else {
          this.disabled = false;
          this.invalidPassword = false;
        }
      }
    },
    checkOldPassword: async function(item) {
      const payload = {
        password: item,
      };
      await this.$store.dispatch("verifyPassword", {
        token: localStorage.getItem("token"),
        payload,
      });
      return this.$store.state.client.password.verify;
    },
    async checkPasswordForm(e) {
      e.preventDefault();
      this.errorOldPwd = [];
      this.errorPwd = [];
      this.errorConfirmPwd = [];
      if (!this.newPassword) {
        this.errorPwd = [];
        this.errorPwd.push(this.$t("errorAddPwd"));
      }

      if (!this.confirmPassword) {
        this.errorConfirmPwd = [];
        this.errorConfirmPwd.push(this.$t("errorConfirmPwd"));
      }

      if (this.newPassword && !this.validPassword(this.newPassword)) {
        this.errorPwd = [];
        this.errorPwd.push(this.$t("errorPwdInvalid"));
      }

      if (
        this.validPassword(this.newPassword) &&
        this.confirmPassword &&
        this.confirmPassword != this.newPassword
      ) {
        this.errorConfirmPwd = [];
        this.errorConfirmPwd.push(this.$t("errorConfirmPwdConfirm"));
      }

      if (!(await this.checkOldPassword(this.password))) {
        this.errorOldPwd = [];
        this.errorOldPwd.push(this.$t("errorOldPwd"));
      }

      if (await this.checkOldPassword(this.newPassword)) {
        this.errorPwd = [];
        this.errorPwd.push(this.$t("errorPwd"));
      }

      if (
        this.errorOldPwd &&
        !this.invalidPassword &&
        !this.errorPwd.length &&
        !this.errorConfirmPwd.length &&
        !this.errorOldPwd.length &&
        !this.confirmPassword == !this.newPassword &&
        !this.errorOldPassword.length
      ) {
        this.updatePassword();
        return true;
      }
    },
    infoCheck(e) {
      e.preventDefault();
      this.errorNomRequired = [];
      this.errorPrenomRequired = [];
      if (!this.nom) {
        this.errorNomRequired.push(this.$t("errorNomRequired"));
      }
      if (!this.prenom) {
        this.errorPrenomRequired.push(this.$t("errorPrenomRequired"));
      }
      if (
        this.nom === this.client.lastname &&
        this.prenom === this.client.firstname &&
        this.profil === this.client.profil
      ) {
        this.errorPrenomRequired.push(this.$t("errorPrenomChange"));
        this.errorNomRequired.push(this.$t("errorNomChange"));
      }
      if (!this.errorNomRequired.length && !this.errorPrenomRequired.length) {
        this.updateInfo();
        this.toggleDialogModificationInfo();
        return true;
      }
    },
    countDownTimer() {
      clearTimeout(this.countdownTimeout);
      if (this.countDown > 0) {
        this.countdownTimeout = setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 1000);
      }
      if (this.countDown === 0) this.resend = false;
    },
    checkUsersPhone: async function(phoneNumber) {
      const payload = {
        phone: phoneNumber.replaceAll(" ", ""),
      };
      await this.$store.dispatch("isPhoneUsed", {
        payload,
        token: localStorage.getItem("token"),
      });
      return this.$store.state.client.phone.used;
    },
    phoneCheck: async function(e) {
      e.preventDefault();
      this.errorTelephoneRequired = [];

      if (!this.telephone) {
        this.errorTelephoneRequired.push(this.$t("errorTelephoneRequired"));
      }

      if (
        this.telephone &&
        !this.validPhone(this.telephone.replaceAll(" ", ""))
      ) {
        this.errorTelephoneRequired.push(this.$t("errorTelephoneInvalid"));
      }

      if (await this.checkUsersPhone(this.telephone)) {
        this.errorTelephoneRequired.push(this.$t("errorTelephoneUsed"));
      }

      if (!this.errorTelephoneRequired.length) {
        this.smsCode = SMS_CODE;
        const SMS = {
          From: "PredictM",
          To: this.telephone.replaceAll(" ", ""),
          Text: `${this.$t("smsCode")} ${this.smsCode}`,
        };
        try {
          await this.$store.dispatch("getSMS", {
            smsPayload: SMS,
          });
        } catch (e) {
          //
        }
        this.toggleDialogActivation();
        return true;
      }
    },
    verificationPhone: async function() {
      this.errorCode = [];
      const code =
        this.number1 +
        this.number2 +
        this.number3 +
        this.number4 +
        this.number5 +
        this.number6;
      if (code == this.smsCode) {
        await this.confirmPhone(this.smsCode);
        this.toggleDialogModification();
        this.initDigit();
      } else {
        this.errorCode.push(this.$t("errorCode"));
      }
    },
    validPhone(phoneNumber) {
      var re = /^\+(?:[0-9] ?){6,14}[0-9]$/;
      return re.test(phoneNumber);
    },
    validPassword(pwd) {
      var re = /^(?=.*[a-z].*[A-Z]|[A-Z].*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
      return re.test(pwd);
    },
    numericOnly(e) {
      if (e.charCode >= 48 && e.charCode <= 57) {
        document.getElementById("number2").focus();
        return true;
      }
      return e.preventDefault();
    },
    loadAffiliated: async function() {
      try {
        await this.$store.dispatch("loadAffiliated", {
          code: this.client.storage_code_client,
          token: localStorage.getItem("token"),
          page: this.pageAffiliated,
          size: this.sizeAffiliated,
        });
        this.getTotal();
      } catch (e) {
        //
      }
    },
    orderAffiliated: async function(field) {
      await this.$store.dispatch("loadAffiliated", {
        code: this.client.storage_code_client,
        order: field,
        token: localStorage.getItem("token"),
        page: this.pageAffiliated,
        size: this.sizeAffiliated,
      });
    },
    getTotal() {
      this.userAffiliated = this.affiliated.length;
      this.totalDays = this.affiliated
        .map(function(e) {
          return e.reward_day_by_child;
        })
        .reduce((a, b) => a + b, 0);
      this.totalCredits = this.affiliated
        .map(function(e) {
          return e.reward_credit_by_child;
        })
        .reduce((a, b) => a + b, 0);
    },
    closeModalSMSAcvtivation() {
      this.showDialogActivation = !this.showDialogActivation;
      clearTimeout(this.countdownTimeout);
      this.resend = false;
    },
  },
  data() {
    return {
      icon: `
          <svg class="mr-2" xmlns="http://www.w3.org/2000/svg" width="28.01" height="28.8" viewBox="0 0 18.676 19.2">
            <path id="Tracé_19685" data-name="Tracé 19685" d="M19.14,12.94A7.074,7.074,0,0,0,19.2,12a5.777,5.777,0,0,0-.07-.94l2.03-1.58a.491.491,0,0,0,.12-.61L19.36,5.55a.488.488,0,0,0-.59-.22l-2.39.96a7.064,7.064,0,0,0-1.62-.94L14.4,2.81a.484.484,0,0,0-.48-.41H10.08a.474.474,0,0,0-.47.41L9.25,5.35a7.22,7.22,0,0,0-1.62.94L5.24,5.33a.477.477,0,0,0-.59.22L2.74,8.87a.455.455,0,0,0,.12.61l2.03,1.58a5.563,5.563,0,0,0-.02,1.88L2.84,14.52a.491.491,0,0,0-.12.61l1.92,3.32a.488.488,0,0,0,.59.22l2.39-.96a7.064,7.064,0,0,0,1.62.94l.36,2.54a.492.492,0,0,0,.48.41h3.84a.466.466,0,0,0,.47-.41l.36-2.54a6.859,6.859,0,0,0,1.62-.94l2.39.96a.477.477,0,0,0,.59-.22l1.92-3.32a.463.463,0,0,0-.12-.61ZM12,15.6A3.6,3.6,0,1,1,15.6,12,3.611,3.611,0,0,1,12,15.6Z" transform="translate(-2.662 -2.4)" fill="#242c36"/>
          </svg>
      `,
      tel_options: {
        placeholder: this.$t("phone:placeholder"),
      },
      showPdfPreview: false,
      userProfile: null,
      password: "",
      downloadLayout: false,
      disableDay: true,
      disableCredit: true,
      visible: false,
      subscriptionPrice: 0,
      menuItems: MenuUser,
      fullName: "",
      isActive: true,
      jourGratuit: 0,
      subscription: "",
      userAffiliated: 0,
      totalDays: 0,
      totalCredits: 0,
      dateEmission: null,
      dateEcheance: null,
      referenceAbonnement: "",
      credits: 0,
      sum: 0,
      free_day: 0,
      referenceFacture: "",
      showMessage: "",
      abonnementFacture: 0,
      prixFacture: 0,
      priceWithTVA: 0,
      totalPrice: 0,
      idSubscribe: null,
      subscribeExpiration: null,
      renew: null,
      idUser: null,
      nom: null,
      prenom: null,
      email: null,
      search: "",
      confirmPassword: "",
      newPassword: "",
      telephone: "",
      smsCode: "0",
      image: null,
      errors: [],
      errorNomRequired: [],
      errorPrenomRequired: [],
      errorTelephoneRequired: [],
      errorCode: [],
      errorOldPwd: [],
      errorPwd: [],
      errorConfirmPwd: [],
      invalidPassword: false,
      showDialogActivation: false,
      resend: false,
      number1: null,
      number2: null,
      number3: null,
      number4: null,
      number5: null,
      number6: null,
      showButton: false,
      countDown: RESEND_WAITING / 1000,
      usersList: null,

      errorAffiliated: null,
      visibleAffiliated: null,
      errorFactures: null,
      visibleFatures: null,

      errorOldPassword: "",

      iconAbonnement: `
        <svg xmlns="http://www.w3.org/2000/svg" width="55.169" height="48" viewBox="0 0 55.169 48" class="mr-2">
          <g id="Groupe_53079" data-name="Groupe 53079" transform="translate(0 0)">
            <path id="Tracé_42431" data-name="Tracé 42431" d="M-86.252-73.489a3.833,3.833,0,0,1-2.03,2.692,4.622,4.622,0,0,1-1.333.376.6.6,0,0,0-.605.523q-1.5,5.525-3.038,11.043c-.53,1.918-1.073,3.832-1.584,5.754a.5.5,0,0,1-.584.453q-18.422-.012-36.844,0c-.37,0-.477-.149-.566-.474-1.524-5.548-3.068-11.09-4.582-16.641a.768.768,0,0,0-.77-.675,3.629,3.629,0,0,1-3.233-3.63,3.7,3.7,0,0,1,3.153-3.612,3.62,3.62,0,0,1,4.087,2.847,8.892,8.892,0,0,1,.023,1.544c.006.168.039.422.149.486,2.852,1.691,5.715,3.361,8.62,5.061l9.523-15.781a3.636,3.636,0,0,1-1.608-3.467,3.549,3.549,0,0,1,1.287-2.405,3.668,3.668,0,0,1,5.015.287c1.521,1.641,1.309,3.663-.618,5.606l9.5,15.759,1.707-1q3.368-1.968,6.739-3.932c.279-.162.41-.3.331-.668a3.637,3.637,0,0,1,2.764-4.282,3.647,3.647,0,0,1,4.294,2.446c.065.2.133.406.2.609Z" transform="translate(141.421 90.25)" fill="#5c626a"/>
            <path id="Tracé_42432" data-name="Tracé 42432" d="M-24.083,509.6q-8.674,0-17.348,0a3.149,3.149,0,0,1-3.359-2.432A3.1,3.1,0,0,1-41.7,503.4c.107-.005.215,0,.323,0q17.295,0,34.589,0a3.25,3.25,0,0,1,3.033,1.493A3.092,3.092,0,0,1-6.52,509.59c-1.256.031-2.514.006-3.771.006Z" transform="translate(51.667 -461.605)" fill="#5c626a"/>
          </g>
        </svg>
      `,
      emplacementDispo: null,
      emplacementUtilise: null,
      imgAvatar: "https://jlg.ro/wp-content/uploads/2020/09/empty-avatar.png",
      iconModif: `
          <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
            <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
            <g id="Groupe_14044" data-name="Groupe 14044" transform="translate(7.629 7.705)">
              <path id="Tracé_19671" data-name="Tracé 19671" d="M162.639,159.613c-.275.33-.533.678-.829.989q-11.931,12.529-23.869,25.051c-.421.441-.864.832-1.531.57a1.752,1.752,0,0,1-.578-.384q-5.724-5.708-11.435-11.43a1.188,1.188,0,0,1-.324-1.459,1.086,1.086,0,0,1,1.252-.616,1.949,1.949,0,0,1,.833.51q5.108,5.078,10.193,10.179c.129.129.264.251.35.333.38-.348.757-.656,1.091-1.005q11.327-11.852,22.646-23.712a1.218,1.218,0,0,1,1.846-.205,3.765,3.765,0,0,1,.355.474Z" transform="translate(-104.921 -133.831)" fill="#f8bd25"/>
              <path id="Tracé_19672" data-name="Tracé 19672" d="M38.362,76.742q-1.469,0-2.941-.112A38.363,38.363,0,1,1,69.557,60.736a1.5,1.5,0,1,1-2.434-1.75,35.373,35.373,0,1,0-8.136,8.137,1.5,1.5,0,1,1,1.749,2.434A38.365,38.365,0,0,1,38.362,76.742Z" transform="translate(0 0)" fill="#242c36"/>
              <path id="Tracé_19673" data-name="Tracé 19673" d="M411.609,413.108a1.5,1.5,0,1,1,1.06-.439A1.51,1.51,0,0,1,411.609,413.108Z" transform="translate(-347.165 -347.165)" fill="#242c36"/>
            </g>
          </svg>
      `,
      showDialogRenewAuto: false,
      showDialogModificationReussi: false,
      showDialogModificationInfo: false,
      showDialogModificationPassword: false,
      iconTabs1: `
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
          <path id="Tracé_42047" data-name="Tracé 42047" d="M19,3H5A2.006,2.006,0,0,0,3,5V19a2.006,2.006,0,0,0,2,2H19a2.006,2.006,0,0,0,2-2V5A2.006,2.006,0,0,0,19,3ZM14,17H7V15h7Zm3-4H7V11H17Zm0-4H7V7H17Z" transform="translate(-3 -3)" fill="#a7aaae"/>
        </svg>
      `,
      iconTabs2: `
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="20" viewBox="0 0 18 20">
          <path id="Tracé_42429" data-name="Tracé 42429" d="M18,17H6V15H18Zm0-4H6V11H18Zm0-4H6V7H18ZM3,22l1.5-1.5L6,22l1.5-1.5L9,22l1.5-1.5L12,22l1.5-1.5L15,22l1.5-1.5L18,22l1.5-1.5L21,22V2L19.5,3.5,18,2,16.5,3.5,15,2,13.5,3.5,12,2,10.5,3.5,9,2,7.5,3.5,6,2,4.5,3.5,3,2Z" transform="translate(-3 -2)" fill="#a7aaae"/>
        </svg>
      `,
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
      iconTabs3: `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="12" viewBox="0 0 24 12">
          <path id="Tracé_42430" data-name="Tracé 42430" d="M12,12.75a10.611,10.611,0,0,1,4.24.9A2.984,2.984,0,0,1,18,16.38V18H6V16.39a2.963,2.963,0,0,1,1.76-2.73A10.44,10.44,0,0,1,12,12.75ZM4,13a2,2,0,1,0-2-2A2.006,2.006,0,0,0,4,13Zm1.13,1.1A6.983,6.983,0,0,0,4,14a6.95,6.95,0,0,0-2.78.58A2.011,2.011,0,0,0,0,16.43V18H4.5V16.39A4.5,4.5,0,0,1,5.13,14.1ZM20,13a2,2,0,1,0-2-2A2.006,2.006,0,0,0,20,13Zm4,3.43a2.011,2.011,0,0,0-1.22-1.85,6.8,6.8,0,0,0-3.91-.48,4.5,4.5,0,0,1,.63,2.29V18H24ZM12,6A3,3,0,1,1,9,9,3,3,0,0,1,12,6Z" transform="translate(0 -6)" fill="#a7aaae"/>
        </svg>
      `,
      pageBill: 1,
      sizeBill: 5,
      pageAffiliated: 1,
      sizeAffiliated: 5,
      userPhoto: true,
    };
  },
};
</script>

<style>
@media (max-width: 479px) {
  #mon-compte .md-tabs-navigation {
    flex-wrap: nowrap !important;
  }
}
@media (max-width: 479px) {
  #mon-compte .md-tabs-navigation .md-ripple {
    justify-content: center;
    padding: 0 6px;
  }
}
@media (max-width: 479px) {
  .md-tabs-navigation .md-button {
    font-size: 10px;
  }
}
@media (max-width: 639px) {
  .md-app-content {
    padding: 8px;
  }
}
@media (max-width: 1023px) {
  #mon-compte .tabs-monCompte .md-tabs-content {
    height: auto !important;
  }
}
@media (max-width: 599px) {
  .md-dialog.predict-dialog {
    margin: auto;
    max-width: 90%;
  }
  .predict-dialog .md-dialog-fullscreen {
    height: auto;
    width: auto;
  }
}
@media (max-width: 639px) {
  #mon-compte .form-group .md-field label {
    font-size: 12px !important;
    padding-left: 0;
    padding-right: 0;
  }
}
@media (max-width: 639px) {
  #mon-compte .form-group .md-input {
    font-size: 12px !important;
    padding: 6px 0.5rem !important;
  }
}
@media (max-width: 479px) {
  #mon-compte .vti__dropdown-list {
    max-width: 215px;
  }
  #mon-compte .vti__dropdown-item {
    font-size: 12px;
    padding: 4px 5px;
  }
}
@media (max-width: 479px) {
  #mon-compte .vue-tel-input .vti__input {
    font-size: 12px !important;
  }
}

#mon-compte .monCompte-table .md-table-content table .table-container {
  height: 100%;
}
#mon-compte .monCompte-table .md-table-content table {
}
#mon-compte .monCompte-table .date_col {
  width: 5%;
}
#mon-compte .monCompte-table .codeNumber_col {
  width: 10%;
}
#mon-compte .monCompte-table .subscription_col {
  width: 15%;
}
#mon-compte .monCompte-table .amount_col {
  width: 20%;
}
#mon-compte .monCompte-table .actions_col {
  width: 10%;
}

#mon-compte .beforeUpload .icon {
  display: none;
}
#mon-compte .beforeUpload:before {
  background: url(../../assets/images/default_profil.svg) no-repeat;
  background-size: cover;
  background-position: center;
  border-radius: 50%;
  display: block;
  content: "";
  height: 100%;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
}

#mon-compte .imgsPreview .imageHolder img {
  object-position: center top;
}
</style>

<style scoped>
@media (max-width: 479px) {
  #mon-compte .search-code-field {
    padding-left: 0;
    padding-right: 0;
  }
}
#mon-compte .search-code-field .md-field {
  flex-wrap: nowrap;
  justify-content: flex-start;
}
@media (max-width: 479px) {
  #mon-compte .search-code-field .md-field .md-input {
    font-size: 12px !important;
    padding: 7px 0.5rem !important;
  }
  #mon-compte .search-code-field .md-field input::-webkit-input-placeholder {
    font-size: 12px !important;
  }
}

#mon-compte > .md-layout {
  margin-left: -10px;
  margin-right: -10px;
}
#mon-compte .titre-page {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0.15px;
  color: #5c626a;
}
#mon-compte .nom-utilisateur,
#mon-compte .pseudo-label {
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.25px;
  color: var(--black);
  white-space: nowrap;
}
#mon-compte #tab-parrainage .pseudo-label {
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;
}
#mon-compte .description {
  letter-spacing: 0.25px;
  color: var(--black);
  font-size: 14px;
  line-height: 20px;
}

#mon-compte .mail-utilisateur {
  text-decoration: none !important;
  font-family: "Poppins-Regular", Arial, Helvetica, sans-serif;
}
#mon-compte .mail-utilisateur,
#mon-compte p {
  font-size: 12px;
  line-height: 1.7;
  letter-spacing: 0.12px;
  color: var(--black);
}
#mon-compte .avatar-wrapper .avatar-innerwrapper {
  border-radius: 50%;
  height: 146px;
  margin: 0 auto;
  overflow: hidden;
  position: relative;
  width: 146px !important;
}
#mon-compte .avatar-wrapper .upload-file {
  width: 146px !important;
  height: 146px;
  padding: 9px;
  border: 1px dashed var(--placeholder);
  border-radius: 50%;
}
#mon-compte .avatar-wrapper span.b-avatar {
  border: 1px dashed var(--placeholder);
  background-color: transparent;
  padding: 9px;
}
#mon-compte .avatar-wrapper .avatar_loaded {
  border-radius: 50%;
  height: 126px;
  overflow: hidden;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: 126px;
  z-index: 2;
}
#mon-compte .avatar-wrapper .avatar_loaded:before {
  background-color: #fdca4038;
  border-radius: 50%;
  content: "";
  cursor: pointer;
  height: 100%;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  pointer-events: none;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  z-index: 3;
}
#mon-compte .avatar-wrapper .avatar_loaded:hover:before {
  opacity: 1;
}
#mon-compte .avatar-wrapper .avatar_loaded img {
  cursor: pointer;
  display: block;
  font-size: 0;
  height: 100%;
  line-height: 126px;
  object-fit: cover;
  object-position: center top;
  width: 100%;
}
#mon-compte .avatar-wrapper .avatar_loaded #alttext {
  display: none;
}
#mon-compte .avatar-wrapper .avatar_loaded .fake_btn {
  color: #000;
  cursor: pointer;
  font-size: 16px;
  font-weight: 800;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 3;
}
#mon-compte .avatar-wrapper .avatar_loaded:hover .fake_btn {
  opacity: 1;
}

#mon-compte .fake-avatar {
  border: 1px dashed var(--placeholder);
  padding: 9px;
}
#mon-compte .fake-avatar .text-wrapper {
  font-size: 34px;
  line-height: 36px;
  color: var(--placeholder);
  background-color: #f6f6f7;
}
#mon-compte .column-wrapper > div {
  /* flex: 1 0 534px;
    max-width: 534px; */
  margin-left: 0 !important;
  margin-right: 24px !important;
}

#mon-compte #tab-parrainage .column-wrapper > div {
  flex: 1 0 48%;
  max-width: 100%;
}

#mon-compte .column-wrapper > div:first-child {
  flex: 1 0 473px;
  max-width: 473px;
}
#mon-compte .column-wrapper > div:last-child {
  margin-right: 0 !important;
}

#mon-compte .bloc-content {
  padding: 20px;
  margin: 10px;
}
#mon-compte .details {
  color: var(--placeholder);
  font-size: 12px;
}
#mon-compte .details .text {
  font-size: 16px;
  color: var(--primary);
}
#mon-compte .modifier {
  top: 5px;
  right: 5px;
  min-width: auto;
}

#mon-compte .future-cost {
  font-size: 24px;
}
/* input:disabled {
  background-color: rgb(235, 235, 228);
} */
@media screen and (max-width: 1400px) {
  #mon-compte .column-wrapper > div {
    flex: 1 0 47% !important;
    max-width: 47% !important;
  }
}

@media screen and (max-width: 1080px) {
  #mon-compte .column-wrapper > div {
    flex: 1 0 100% !important;
    max-width: 100% !important;
  }
}

.titre-recherche {
  color: #5c626a;
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
  font-size: 20px;
  line-height: 24px;
}
@media (max-width: 479px) {
  .titre-recherche {
    font-size: 16px;
  }
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

#mon-compte #tab-factures > div {
  flex-wrap: nowrap;
}

@media (max-width: 1200px) {
  #mon-compte #tab-factures > div {
    flex-wrap: wrap;
  }
}

#mon-compte .historique-wrapper {
  max-width: calc(100% - 498px);
}

#mon-compte .code-wrapper {
  background-color: #f6f6f7;
}
#mon-compte .copy-wrapper {
  /* background-color: #f6f6f7; */
  cursor: pointer;
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;

  font-size: 16px;
  color: var(--primary);
  right: 15px;
}
#mon-compte .copy-wrapper:hover,
#mon-compte .copy-wrapper:focus {
  color: var(--primary-hover);
}
#mon-compte .copy-wrapper:hover svg,
#mon-compte .copy-wrapper:focus svg {
  fill: var(--primary-hover);
}
@media (max-width: 639px) {
  #mon-compte .copy-wrapper {
    /* right: 50%;
    transform: translateX(50%);
    text-align: center; */
  }
}
#mon-compte .partage-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 5px 10px;
  margin-bottom: 10px;
  width: 100%;
}
@media (max-width: 479px) {
  #mon-compte .partage-item {
    flex-direction: column;
    justify-content: center;
    padding: 10px;
  }
}
#mon-compte .partage-item:last-child {
  margin-bottom: 0;
}
#mon-compte svg {
  font-size: 1.5rem;
  margin-right: 0;
  min-width: 1.5rem;
}
#mon-compte .text_content {
  display: flex;
  align-items: center;
  font-size: 14px;
  line-height: 1.25;
  margin: 0;
}
@media (max-width: 479px) {
  #mon-compte .text_content {
    justify-content: center;
  }
}
#mon-compte .submit-dialog {
  max-width: 175px;
}
#mon-compte .btn-upgrade {
  min-width: 115px;
}
@media (max-width: 575px) {
  #mon-compte .btn-upgrade {
    min-width: 190px;
  }
}
@media (max-width: 479px) {
  #mon-compte .btn_content {
    margin-top: 10px;
  }
}

#mon-compte .total-wrapper {
  flex: 1 0 250px;
  max-width: 250px;
}
@media (max-width: 479px) {
  #mon-compte .total-wrapper {
    flex: 1 0 100%;
    max-width: 100%;
  }
}
#mon-compte .total-wrapper .pseudo-label {
  font-size: 24px;
  line-height: 1.4;
}
#mon-compte .details-total {
  display: flex;
  flex-direction: row;
  min-width: 320px;
  background-color: var(--black);
  border-radius: 12px;
  /*   font-family: "Poppins-Regular", Arial, Helvetica, sans-serif; */
  font-weight: 500;
  color: var(--primary);
  flex-grow: 1;
  font-size: 24px;
  margin-top: 0;
  margin-bottom: 0;
  margin-right: 0;
}
@media (max-width: 767px) {
  #mon-compte .details-total {
    margin: 0;
    width: 100%;
  }
}
@media (max-width: 639px) {
  #mon-compte .details-total {
    padding: 10px;
  }
}
@media (max-width: 479px) {
  #mon-compte .details-total {
    flex-direction: column;
    min-width: 100%;
  }
}
#mon-compte .details-total > .content_item {
  border-right: 1px solid var(--placeholder);
  display: flex;
  flex-direction: column;
  flex: 1 0 33%;
  max-width: 33%;
  padding: 0 5px;
  text-align: center;
}
@media (max-width: 767px) {
  #mon-compte .details-total > .content_item {
    padding: 5px;
    width: 100%;
  }
}
@media (max-width: 479px) {
  #mon-compte .details-total > .content_item {
    border-bottom: 1px solid var(--placeholder);
    border-right: none;
    flex-basis: 100%;
    max-width: 100%;
  }
}
#mon-compte .details-total > .content_item:last-child {
  border: none;
  padding-bottom: 0;
}

#mon-compte .details-total span {
  color: var(--placeholder);
  font-size: 12px;
}
@media (max-width: 639px) {
  #mon-compte .details-total span {
    vertical-align: baseline;
  }
}
#mon-compte .details-total .value {
  color: var(--primary);
  font-size: 24px;
}

body {
  font-family: Arial, sans-serif;
  line-height: 12px;
  height: 100%;
}
#app {
  height: 100%;
}
.wrapper {
  margin-left: auto;
  margin-right: auto;
  padding-top: 60px;
  padding-bottom: 60px;
}
.logo {
  width: 36px;
}

.barre_jaune {
  display: flex;
  background-color: var(--primary);
  margin: auto;
  /* margin-top: 30px; */
  height: 20px;
}

.first-box span span {
  color: #666666;
}

.first-box div {
  padding: 20px 20px 20px 10px;
  display: flex;
  background-color: var(--lightGrey);
}

.title-table {
  font-size: 18px;
}
.tabld-facture {
  margin-bottom: 50px;
}
.tabld-facture th,
.table-facture td {
  font-size: 11px;
}
.table-facture th {
  padding: 8px 11px;
}
.table-facture td {
  padding: 8px 11px;
}

.table-facture .col-desc {
  width: 30.5%;
}
.table-facture .col-ref {
  width: 18.5%;
  text-align: center;
}
.table-facture .col-qte {
  text-align: center;
  width: 15%;
}
.table-facture .col-pu {
  text-align: center;
  width: 18%;
}
.table-facture .col-pht {
  text-align: center;
  width: 18%;
}
.table-facture .no_padding {
  padding: 0;
}
.table-facture .border_bottom {
  border-bottom: 1px solid #999999;
}
.table-facture .col-total.border_bottom {
  border-bottom: 2px solid #999999;
}

.table-facture .infos-paiement {
  background-color: var(--lightGrey);
  padding: 16px 10px;
}
.table-facture .infos-paiement h6 {
  color: var(--black);
  font-size: 14px;
  font-weight: 700;
  margin: 0;
}
.table-facture .infos-paiement p {
  color: #666666;
  font-size: 11px;
  margin: 0;
}
.table-facture .col-label,
.table-facture .col-value {
  color: #666666;
  font-weight: 700;
  text-align: center;
}
.table-facture .col-label.col-total,
.table-facture .col-value.col-total {
  color: #434343;
  font-weight: 700;
}
.content-text {
  font-size: 11px;
  line-height: 125%;
  margin-top: 50px;
}
.content-text p {
  margin-bottom: 0;
}
.content-text .coordonne-bank {
  margin-top: 15px;
}

.submit-compte:hover svg path {
  fill: #fff !important;
}

.link-mis-niveau {
  text-decoration: none !important;
  color: #fff !important;
}

@media (max-width: 479px) {
  .custom-input-number {
    margin-right: 0 !important;
    width: 100%;
  }
}
.form-user .form-group input[disabled] {
  background-color: #fff;
  cursor: not-allowed;
}
</style>
