<template>
  <div>
    <!-- Loader -->
    <div class="loader-content" v-if="loader">
      <p class="msg">{{ $t("loading") }}</p>
      <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
    </div>
    <!-- /Loader -->
    <div id="dashboard">
      <PermanentFull
        :titre="$t('allCouples')"
        :icon="icon"
        :menuItems="menuItems"
      >
        <div
          id="content-dashboard-wrapper"
          class="md-layout-item d-flex flex-column w-100 tous-les-couples"
        >
          <span v-if="showInfo">{{ $t("info:search") }}</span>

          <div class="table-wrapper flex-grow-1">
            <md-table md-table-fixed-header class="predict-table couple-tables">
              <md-table-toolbar class="filter-bloc px-2 mb-3">
                <md-field class="md-toolbar-section-end m-0 p-0">
                  <md-input
                    :placeholder="$t('exampleCouple')"
                    v-model="search"
                    class="input-search border-0"
                    @keyup.enter="handleSearch()"
                    :disabled="loader"
                  />
                  <svg
                    v-if="search.length == 0"
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
                  <!-- icon X -->
                  <svg
                    v-if="search.length != 0"
                    @click="clearSearchInput"
                    height="24"
                    viewBox="0 0 24 24"
                    width="24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                </md-field>
              </md-table-toolbar>
              <div
                v-if="
                  this.couples.length == 1 &&
                    search.toUpperCase() == this.couples[0].symbol &&
                    (this.couples[0].status == 'unrequested' ||
                      this.couples[0].status == 'requested')
                "
              >
                <md-table-empty-state
                  :md-label="$t('pairUnavailable')"
                  :md-description="$t('pairUnaivalableDetail')"
                >
                  <md-button
                    class="md-primary md-raised md-demande bgColor-primary"
                    @click="requestCouple(null)"
                    v-bind:class="{ isRequested: isRequested }"
                    v-if="this.couples[0].status == 'unrequested'"
                  >
                    <span class="d-flex align-items-center">
                      <svg
                        id="downloading_black_24dp"
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                      >
                        <g id="Groupe_14230" data-name="Groupe 14230">
                          <rect
                            id="Rectangle_2479"
                            data-name="Rectangle 2479"
                            width="24"
                            height="24"
                            fill="none"
                          />
                        </g>
                        <g id="Groupe_14232" data-name="Groupe 14232">
                          <g id="Groupe_14231" data-name="Groupe 14231">
                            <path
                              id="Tracé_42166"
                              data-name="Tracé 42166"
                              d="M18.32,4.26A9.949,9.949,0,0,0,13,2.05V4.07a7.941,7.941,0,0,1,3.9,1.62ZM19.93,11h2.02a9.949,9.949,0,0,0-2.21-5.32L18.31,7.1A7.941,7.941,0,0,1,19.93,11Zm-1.62,5.9,1.43,1.43a9.981,9.981,0,0,0,2.21-5.32H19.93A7.945,7.945,0,0,1,18.31,16.9ZM13,19.93v2.02a9.949,9.949,0,0,0,5.32-2.21l-1.43-1.43A7.868,7.868,0,0,1,13,19.93ZM13,12V7H11v5H7l5,5,5-5Zm-2,7.93v2.02a10,10,0,0,1,0-19.9V4.07a7.992,7.992,0,0,0,0,15.86Z"
                              fill="#fff"
                            />
                          </g>
                        </g>
                      </svg>
                      {{ $t("request") }}
                    </span> </md-button
                  ><md-button v-if="this.couples[0].status == 'requested'">
                    <span class="isRequested d-flex align-items-center">
                      <svg
                        id="done_black_24dp"
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                      >
                        <path
                          id="Tracé_42162"
                          data-name="Tracé 42162"
                          d="M0,0H24V24H0Z"
                          fill="none"
                        />
                        <path
                          id="Tracé_42163"
                          data-name="Tracé 42163"
                          d="M9,16.2,4.8,12,3.4,13.4,9,19,21,7,19.6,5.6Z"
                          fill="#21a179"
                        />
                      </svg>
                      {{ $t("requestSend") }}
                    </span>
                  </md-button>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="148.453"
                    height="121.888"
                    viewBox="0 0 148.453 121.888"
                    style="order:1; margin-bottom: 0.75rem;"
                  >
                    <g
                      id="Groupe_53078"
                      data-name="Groupe 53078"
                      transform="translate(9259.094 3855.75)"
                    >
                      <g
                        id="Oval"
                        transform="translate(-9259.094 -3855.75)"
                        fill="#fff"
                        stroke="#5c626a"
                        stroke-miterlimit="10"
                        stroke-width="2"
                      >
                        <circle
                          cx="53.131"
                          cy="53.131"
                          r="53.131"
                          stroke="none"
                        />
                        <circle
                          cx="53.131"
                          cy="53.131"
                          r="52.131"
                          fill="none"
                        />
                      </g>
                      <path
                        id="Tracé_42175"
                        data-name="Tracé 42175"
                        d="M717.108,67.788a25.785,25.785,0,1,0,25.785,25.785,25.8,25.8,0,0,0-25.785-25.785Zm0,49.531h0a23.747,23.747,0,1,1,23.747-23.747,23.783,23.783,0,0,1-23.747,23.747ZM704.1,98.117H731.37a14.219,14.219,0,0,1-27.273,0Zm17.87-8.935h0l-1.724-1.722L725.1,82.6l4.86,4.86-1.722,1.722L725.1,85.97Zm-14.656,0h0l-1.645-1.722,4.778-4.86h.082l4.777,4.86-1.722,1.722-3.055-3.212Z"
                        transform="translate(-9922.287 -3896.973)"
                        fill="#5c626a"
                      />
                      <g id="Groupe_53077" data-name="Groupe 53077">
                        <g
                          id="Oval_Copy"
                          data-name="Oval Copy"
                          transform="translate(-9176.272 -3799.494)"
                          fill="#fff"
                          stroke="#a7aaae"
                          stroke-miterlimit="10"
                          stroke-width="1"
                        >
                          <circle
                            cx="32.816"
                            cy="32.816"
                            r="32.816"
                            stroke="none"
                          />
                          <circle
                            cx="32.816"
                            cy="32.816"
                            r="32.316"
                            fill="none"
                          />
                        </g>
                        <path
                          id="Tracé_42176"
                          data-name="Tracé 42176"
                          d="M706.949,67.788a15.626,15.626,0,1,0,15.626,15.626,15.638,15.638,0,0,0-15.626-15.626Zm0,30.017h0A14.391,14.391,0,1,1,721.34,83.414a14.413,14.413,0,0,1-14.391,14.391Zm-7.885-11.637h16.528a8.617,8.617,0,0,1-16.528,0Zm10.83-5.415h0l-1.045-1.044,2.943-2.945,2.945,2.945-1.044,1.044-1.9-1.947Zm-8.882,0h0l-1-1.044,2.9-2.945h.05l2.9,2.945-1.044,1.044-1.852-1.947Z"
                          transform="translate(-9850.406 -3850.093)"
                          fill="#5c626a"
                        />
                      </g>
                    </g>
                  </svg>
                </md-table-empty-state>
              </div>
              <div v-else class="table-container tous-les-couples">
                <md-table-row class="table-header">
                  <md-table-head scope="col" class="favori_col"></md-table-head>
                  <md-table-head scope="col" class="paire_col">
                    {{ $t("pair") }}
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        @click="orderBy('symbol')"
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
                        @click="orderBy('-' + 'symbol')"
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
                  <md-table-head scope="col" class="lastvalue_col">
                    {{ $t("lastValue") }}
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        @click="orderBy('closeNow')"
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
                        @click="orderBy('-' + 'closeNow')"
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
                  <md-table-head scope="col" class="sur_col">
                    {{ $t("on24h") }}
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        @click="orderBy('h24')"
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
                        @click="orderBy('-' + 'h24')"
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
                  <md-table-head scope="col" class="haut_col">
                    + {{ $t("high")
                    }}<b-badge class="status-badge bg-transparent"
                      >/24h</b-badge
                    >
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        @click="orderBy('highStart')"
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
                        @click="orderBy('-' + 'highStart')"
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
                  <md-table-head scope="col" class="bas_col">
                    + {{ $t("low")
                    }}<b-badge class="status-badge bg-transparent"
                      >/24h</b-badge
                    >
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        @click="orderBy('lowStart')"
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
                        @click="orderBy('-' + 'lowStart')"
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
                  <md-table-head scope="col" class="cloture_col">
                    {{ $t("closing") }}
                    <span class="table-tri d-flex flex-column">
                      <md-button
                        class="btn-tri arrow-up"
                        @click="orderBy('closeStart')"
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
                        @click="orderBy('-' + 'closeStart')"
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
                  <md-table-head scope="col" class="action_col"></md-table-head>
                </md-table-row>

                <md-table-row
                  v-for="(item, index) in couples"
                  :key="index"
                  class="tr-mobile"
                >
                  <md-table-cell
                    data-label=""
                    class="favori_col favori-col-mobile"
                  >
                    <md-card-actions
                      class="add-favoris-wrapper"
                      v-if="item.assetFullName"
                    >
                      <md-button
                        class="add-favoris w-100"
                        v-bind:class="{ active: item.favorite }"
                        @click="
                          item.favorite
                            ? deleteFavorite(item.symbol)
                            : addFavorite(item.symbol)
                        "
                        :disabled="disable"
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="13.75"
                          height="11.634"
                          viewBox="0 0 13.75 11.634"
                        >
                          <path
                            id="Path"
                            d="M6.375,10.5,6.2,10.362C5.861,10.1,5.4,9.81,4.877,9.478,2.818,8.183,0,6.41,0,3.387A3.5,3.5,0,0,1,3.6,0,3.69,3.69,0,0,1,6.375,1.224,3.69,3.69,0,0,1,9.147,0a3.5,3.5,0,0,1,3.6,3.387c0,3.023-2.818,4.8-4.877,6.091-.528.332-.984.619-1.321.883Z"
                            transform="translate(0.5 0.5)"
                            fill="none"
                            stroke="#242c36"
                            stroke-width="1"
                          />
                        </svg>
                      </md-button>
                    </md-card-actions>
                  </md-table-cell>
                  <md-table-cell
                    data-label=""
                    class="paire_col paire-col-mobile"
                    md-sort-by="paire"
                    >{{ item.symbol }}
                  </md-table-cell>
                  <md-table-cell
                    data-label=""
                    v-if="!item.assetFullName"
                    :colspan="5"
                    >{{ $t("pairUnavailableMessage") }}</md-table-cell
                  >
                  <md-table-cell
                    data-label="Dernière valeur"
                    v-if="item.assetFullName"
                    class="lastvalue_col last-value-col-mobile"
                    md-sort-by="lastValue"
                    >{{ pointToComma(item.closeNow) }} /
                    <span class="grise"
                      >$ {{ pointToComma(item.volume) }}</span
                    ></md-table-cell
                  >
                  <md-table-cell
                    data-label="sur 24h"
                    v-if="item.assetFullName"
                    class="sur_col"
                    md-sort-by="percent"
                  >
                    <span class="decrease" v-if="item.h24 < 0">
                      {{ pointToComma(item.h24) }}%
                    </span>
                    <span class="increase" v-else>
                      {{ pointToComma(item.h24) }}%
                    </span>
                  </md-table-cell>
                  <md-table-cell
                    data-label="+ Haut/24h"
                    v-if="item.assetFullName"
                    class="up_col"
                    md-sort-by="upValue"
                    >{{ pointToComma(item.highStart) }} /
                    <span class="jaune">{{
                      pointToComma(item.highNow)
                    }}</span></md-table-cell
                  >
                  <md-table-cell
                    data-label="+ Bas/24h"
                    v-if="item.assetFullName"
                    class="down_col"
                    md-sort-by="downValue"
                    >{{ pointToComma(item.lowStart) }} /
                    <span class="jaune">{{
                      pointToComma(item.lowNow)
                    }}</span></md-table-cell
                  >
                  <md-table-cell
                    data-label="Clôture"
                    v-if="item.assetFullName"
                    class="cloture_col"
                    md-sort-by="cloture"
                    >{{ pointToComma(item.closeStart) }} /
                    <span class="jaune">{{
                      pointToComma(item.closeNow)
                    }}</span></md-table-cell
                  >
                  <md-table-cell
                    data-label=""
                    class="action_col text-center"
                    v-if="activateSubscription"
                  >
                    <md-button
                      :md-ripple="false"
                      @click="getACouple(item.coupleId)"
                      v-if="item.status === 'unowned'"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="18"
                        height="18"
                        viewBox="0 0 18 18"
                      >
                        <path
                          id="Tracé_42161"
                          data-name="Tracé 42161"
                          d="M19,3H5A2,2,0,0,0,3,5V19a2,2,0,0,0,2,2H19a2.006,2.006,0,0,0,2-2V5A2.006,2.006,0,0,0,19,3ZM17,13H13v4H11V13H7V11h4V7h2v4h4Z"
                          transform="translate(-3 -3)"
                          fill="#242c36"
                        />
                      </svg>
                    </md-button>
                    <md-button
                      :md-ripple="false"
                      @click="requestCouple(item.symbol)"
                      v-if="item.status === 'unrequested'"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        viewBox="0 0 20 20"
                      >
                        <path
                          id="Tracé_42541"
                          data-name="Tracé 42541"
                          d="M13,7H11v4H7v2h4v4h2V13h4V11H13ZM12,2A10,10,0,1,0,22,12,10,10,0,0,0,12,2Zm0,18a8,8,0,1,1,8-8A8.011,8.011,0,0,1,12,20Z"
                          transform="translate(-2 -2)"
                          fill="#242c36"
                        />
                      </svg>
                    </md-button>
                    <md-button v-if="item.status === 'requested'">
                      <svg
                        id="done_black_24dp"
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                      >
                        <path
                          id="Tracé_42162"
                          data-name="Tracé 42162"
                          d="M0,0H24V24H0Z"
                          fill="none"
                        />
                        <path
                          id="Tracé_42163"
                          data-name="Tracé 42163"
                          d="M9,16.2,4.8,12,3.4,13.4,9,19,21,7,19.6,5.6Z"
                          fill="#21a179"
                        />
                      </svg>
                    </md-button>
                    <b-dropdown
                      variant="link"
                      toggle-class="text-decoration-none"
                      no-caret
                      class="table-dropdown"
                      v-if="item.status === 'owned'"
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
                      <b-dropdown-item @click="shareData(item.symbol)">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="22"
                          height="15"
                          viewBox="0 0 22 15"
                          style="text-decoration: none;"
                        >
                          <path
                            id="Tracé_988"
                            data-name="Tracé 988"
                            d="M23.637-39c-5,0-9.27,3.61-11,8,1.73,4.39,6,7,11,7s9.27-2.61,11-7C32.907-35.39,28.637-39,23.637-39Zm0,13a5,5,0,0,1-5-5,5,5,0,0,1,5-5,5,5,0,0,1,5,5A5,5,0,0,1,23.637-26Zm0-8a3,3,0,0,0-3,3,3,3,0,0,0,3,3,3,3,0,0,0,3-3A3,3,0,0,0,23.637-34Z"
                            transform="translate(-12.637 39)"
                            fill="#242c36"
                          />
                        </svg>
                        {{ $t("visualize") }}
                      </b-dropdown-item>

                      <b-dropdown-item @click="removeCouple(item.coupleId)">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="20"
                          height="20"
                          viewBox="0 0 20 20"
                        >
                          <path
                            id="Tracé_42174"
                            data-name="Tracé 42174"
                            d="M14.59,8,12,10.59,9.41,8,8,9.41,10.59,12,8,14.59,9.41,16,12,13.41,14.59,16,16,14.59,13.41,12,16,9.41ZM12,2A10,10,0,1,0,22,12,9.991,9.991,0,0,0,12,2Zm0,18a8,8,0,1,1,8-8A8.011,8.011,0,0,1,12,20Z"
                            transform="translate(-2 -2)"
                            fill="#242c36"
                          />
                        </svg>
                        {{ $t("remove") }}
                      </b-dropdown-item>
                    </b-dropdown>
                  </md-table-cell>
                </md-table-row>
                <md-table-row v-if="this.visible" class="empty-data">
                  <md-table-cell
                    data-label=""
                    :colspan="8"
                    class="align-text"
                    >{{ $t("table:NotFound") }}</md-table-cell
                  >
                </md-table-row>

                <md-table-row class="pagination-row" v-if="!visible">
                  <md-table-cell :colspan="8">
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
          <Dialog
            :showDialog="showDialog"
            :titreDialog="$t('warning')"
            :iconDialog="iconDialog"
            @close="showDialog = !showDialog"
          >
            <p class="text-center" v-html="errorCouplePopUp">
              {{ errorCouplePopUp }}
            </p>

            <div
              class="
                w-100
                row-fluid
                d-flex
                flex-column flex-sm-row
                align-items-center
                justify-content-between
                rememberMe-wrapper
              "
            >
              <form action="" class="w-100">
                <div class="w-100 text-center">
                  <md-button
                    type="submit"
                    class="
                      submit-dialog
                      text-center
                      btn-submit
                      text-center
                      w-100
                    "
                    @click="showDialog = false"
                  >
                    {{ $t("continue") }}
                  </md-button>
                </div>
              </form>
            </div>
          </Dialog>
        </div>
      </PermanentFull>
    </div>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import Dialog from "../../components/Dialog/Dialog.vue";
import MenuUser from "../../data/MenuUser.js";
import TablePagination from "../Pagination/TablePagination.vue";

export default {
  name: "TousLesCryptos",
  components: {
    PermanentFull,
    Dialog,
    TablePagination,
  },
  data: () => ({
    visible: false,
    isActive: false,
    isRequested: false,
    isAdded: false,
    isDispo: false,
    showDialog: false,
    rememberMe: false,
    loader: false,
    disable: false,
    order: "",
    page: 1,
    size: 5,
    search: "",
    couples: [],
    menuItems: MenuUser,
    showInfo: false,
    iconDialog: `
          <svg id="account_circle-24px" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 92 92">
            <path id="Tracé_2166" data-name="Tracé 2166" d="M0,0H92V92H0Z" fill="none"/>
            <g id="Groupe_53071" data-name="Groupe 53071" transform="translate(-37.371 -57.653)">
              <g id="Groupe_53075" data-name="Groupe 53075">
                <path id="Tracé_42545" data-name="Tracé 42545" d="M45,129.664q7.829-13.7,15.662-27.4,8.411-14.638,16.884-29.241A6.476,6.476,0,0,1,86.3,70.229a6.342,6.342,0,0,1,2.615,2.514q6.548,11.339,13.1,22.677a1.557,1.557,0,0,1-.374,2.3c-.79.479-1.646.167-2.241-.822-.116-.193-.224-.391-.337-.586Q92.982,85.789,86.9,75.263a12.637,12.637,0,0,0-.886-1.39,3.385,3.385,0,0,0-5.428,0,8.441,8.441,0,0,0-.613.942q-15.686,27.16-31.368,54.323c-1.158,2.007-.912,3.953.791,5.02a4.717,4.717,0,0,0,2.332.61c3.78.063,7.561.033,11.342.033q25.8,0,51.6.008a3.836,3.836,0,0,0,3.189-1.172,3.479,3.479,0,0,0,.213-4.378q-3.35-5.821-6.714-11.633-2.833-4.906-5.665-9.812a3.649,3.649,0,0,1-.332-.75,1.462,1.462,0,0,1,2.447-1.444,3.4,3.4,0,0,1,.478.669q6.248,10.818,12.484,21.644a6.46,6.46,0,0,1-2.037,8.9,6.658,6.658,0,0,1-3.716.982c-3.706-.014-7.411,0-11.117,0q-26.027,0-52.054.008a6.538,6.538,0,0,1-6.022-3.1,15.884,15.884,0,0,1-.83-1.752Z" fill="#242c36"/>
                <path id="Tracé_42546" data-name="Tracé 42546" d="M232.582,199.652c0,2.227.037,4.454-.008,6.68a4.769,4.769,0,0,1-7.27,4.148,4.473,4.473,0,0,1-2.311-3.967c-.046-4.628-.069-9.257.006-13.884a4.707,4.707,0,0,1,4.8-4.586,4.8,4.8,0,0,1,4.781,4.78c.036,1.15.011,2.3.011,3.452q0,1.689,0,3.377Zm-3-.042c0-2.2.016-4.4-.007-6.607a1.8,1.8,0,1,0-3.591.005c-.017,4.4-.028,8.809.023,13.213a2.606,2.606,0,0,0,.663,1.507,1.486,1.486,0,0,0,1.8.294,1.822,1.822,0,0,0,1.105-1.806C229.584,204.014,229.579,201.812,229.579,199.61Z" transform="translate(-144.468 -96.251)" fill="#f8bd25"/>
                <path id="Tracé_42547" data-name="Tracé 42547" d="M227.891,339.875a4.8,4.8,0,1,1,4.778-4.784A4.853,4.853,0,0,1,227.891,339.875Zm-.025-3.011a1.791,1.791,0,1,0-1.789-1.773A1.851,1.851,0,0,0,227.866,336.864Z" transform="translate(-144.558 -211.717)" fill="#f8bd25"/>
                <path id="Tracé_42548" data-name="Tracé 42548" d="M352.943,235.021a1.474,1.474,0,1,1-.026,2.948,1.474,1.474,0,0,1,.026-2.948Z" transform="translate(-248.795 -134.391)" fill="#242c36"/>
              </g>
            </g>
          </svg>
        `,
    titre: "Toutes les paires",
    icon: `
        <svg class="mr-1 icon-item" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24">
          <rect id="Rectangle_1874" data-name="Rectangle 1874" width="24" height="24" fill="none"/>
          <path id="Tracé_19677" class="to-fill" data-name="Tracé 19677" d="M2.88,7.88,4.42,9.42A8.158,8.158,0,0,0,4,12a8,8,0,1,0,8-8,8.158,8.158,0,0,0-2.58.42L7.89,2.89A10,10,0,1,1,2,12,10.11,10.11,0,0,1,2.88,7.88ZM6,12a6,6,0,1,1,6,6A6,6,0,0,1,6,12ZM7,5.5A1.5,1.5,0,1,1,5.5,4,1.5,1.5,0,0,1,7,5.5Z" fill="#5c626a"/>
        </svg>
      `,

    searched: [],
    rowsPerPage: 3,

    errorCouplePopUp: "",
    activateSubscription: false,
  }),
  created() {
    document.title = this.$route.meta.title;
  },
  methods: {
    handleChangePageValue(val) {
      this.page = val;
    },
    handleChangeSizeValue(val) {
      this.size = val;
    },
    shareData(symbol) {
      this.countViewCouple(symbol);
      this.$router.push({
        name: "VisualiserCrypto",
        params: { symbol: symbol.replace("/", "_") },
      });
    },
    getUserSubscription: async function() {
      try {
        await this.$store.dispatch("loadClients", {
          token: localStorage.getItem("token"),
        });
        this.activateSubscription = this.$store.state.client.clients.subscription.activate;
      } catch (e) {
        //
      }
    },
    clearSearchInput() {
      this.search = "";
      this.loadCouples();
    },
    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
    toggleActive() {
      this.isActive = !this.isActive;
    },
    toggleAdded() {
      this.isAdded = true;
      this.showDialog = !this.showDialog;
    },
    toggleDispo() {
      this.isDispo = true;
    },
    requestCouple: async function(item) {
      const payload = {
        symbol: item ? item : this.search.toUpperCase(),
      };
      try {
        await this.$store.dispatch("requestCouple", {
          token: localStorage.getItem("token"),
          payload,
        });
        await this.loadCouples();
        this.errorCouplePopUp = "";
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
      }
    },
    toReplace(item) {
      return item.replace("/", "_");
    },
    onPagination(pagination) {
      if (pagination) {
        this.limit = pagination.size;
        this.offset = (pagination.page - 1) * this.limit;
      }
      this.find();
    },
    countViewCouple: async function(symbol) {
      try {
        await this.$store.dispatch("countViewCouple", {
          symbol,
          token: localStorage.getItem("token"),
        });
        this.errorCouplePopUp = "";
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
      }
    },
    setOverflow: (cntOverflow) => {
      const mainEl = Array.from(
        document.getElementById("permanentfull").getElementsByTagName("main")
      )[0];
      if (mainEl) {
        if (cntOverflow) {
          mainEl.classList.add("hiddenOverflow");
        } else {
          mainEl.classList.remove("hiddenOverflow");
        }
      }
    },

    getACouple: async function(item) {
      let temp = [];
      temp.push(item);
      const payload = {
        couple: temp,
      };
      try {
        this.loader = true;
        await this.$store.dispatch("getACouple", {
          token: localStorage.getItem("token"),
          payload,
        });
        await this.loadCouples();
        this.loader = false;
        this.errorCouplePopUp = "";
      } catch (e) {
        this.loader = false;
        this.errorCouplePopUp = this.$t("numberCoupleReached");
        this.toggleAdded();
      }
    },
    loadCouples: async function() {
      try {
        this.loader = true;
        this.setOverflow(true);
        await this.$store.dispatch("loadCouples", {
          token: localStorage.getItem("token"),
          order: "symbol",
          page: this.page,
          search: this.search.toUpperCase(),
          size: this.size,
        });
        this.couples = this.getCouples;
        this.loader = false;
        this.setOverflow(false);
        this.errorCouplePopUp = "";
      } catch (e) {
        this.loader = false;
        this.setOverflow(false);
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
      }
    },
    orderBy: async function(field) {
      try {
        this.loader = true;
        await this.$store.dispatch("loadCouples", {
          token: localStorage.getItem("token"),
          order: field,
          page: this.page,
          search: this.search.toUpperCase(),
          size: this.size,
        });
        this.loader = false;
        this.errorCouplePopUp = "";
      } catch (e) {
        this.loader = false;
        this.errorCouplePopUp = e;
        this.toggleAdded();
      }
    },
    deleteFavorite: async function(symbol) {
      this.disable = true;
      try {
        await this.$store.dispatch("deleteFavorite", {
          token: localStorage.getItem("token"),
          symbol,
        });
        await this.loadCouples();
        this.disable = false;
        this.errorCouplePopUp = "";
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
        this.disable = false;
      }
    },
    addFavorite: async function(item) {
      this.disable = true;
      const payload = {
        couple: item,
      };
      try {
        await this.$store.dispatch("addFavorite", {
          token: localStorage.getItem("token"),
          payload,
        });
        await this.loadCouples();
        this.disable = false;
        this.errorCouplePopUp = "";
      } catch (e) {
        this.errorCouplePopUp = `${this.$t("errorOccured")} ${e}`;
        this.toggleAdded();
        this.disable = false;
      }
    },
    removeCouple: async function(item) {
      const payload = {
        couple: item,
      };
      try {
        await this.$store.dispatch("removeCouple", {
          token: localStorage.getItem("token"),
          payload,
        });
        await this.loadCouples();
        this.errorCouplePopUp = "";
      } catch (error) {
        if (error.response.status === 400) {
          this.errorCouplePopUp = this.$t("removeCoupleMessage");
          this.toggleAdded();
        }
      }
    },
    async handleSearch() {
      await this.loadCouples();
      if (!this.couples.length) {
        this.visible = true;
      } else {
        this.visible = false;
      }
    },
  },
  async mounted() {
    await this.loadCouples();
    await this.getUserSubscription();
  },
  computed: {
    getCouples() {
      return this.$store.state.couple.couples.results;
    },
    dataSize() {
      return this.$store.state.couple.couples.count;
    },
    next() {
      return this.$store.state.couple.couples.next;
    },
    client() {
      return this.$store.state.client.clients;
    },
  },
  watch: {
    async page() {
      await this.loadCouples();
    },
    async size() {
      await this.loadCouples();
    },
    search(val) {
      this.showInfo = val.length == 0 ? false : true;
    },
  },
};
</script>

<style>
#permanentfull .hiddenOverflow {
  overflow: hidden;
}
#content-dashboard-wrapper .md-table-content {
  overflow-y: hidden;
}
#content-dashboard-wrapper .md-table-head-container {
  height: 52px;
  padding: 12px 0;
}
#content-dashboard-wrapper .md-table-head {
  color: var(--placeholder);
  font-size: 14px;
  font-weight: 400;
  height: 52px;
  vertical-align: middle;
}
@media (max-width: 479px) {
  #content-dashboard-wrapper .md-table-head {
    font-size: 12px;
  }
}
.align-text {
  text-align: center;
}
#content-dashboard-wrapper .md-table-head-label {
  padding-left: 20px;
  padding-right: 20px;
}
@media (max-width: 1023px) {
  #content-dashboard-wrapper .md-table-head-label {
    padding-left: 10px;
    padding-right: 10px;
  }
}
#content-dashboard-wrapper .md-table-row .md-table-cell {
  height: 52px;
  vertical-align: middle;
  padding-left: 20px;
  padding-right: 20px;
}
@media (max-width: 1023px) {
  #content-dashboard-wrapper .md-table-row .md-table-cell {
    padding-left: 10px;
    padding-right: 10px;
  }
}
#content-dashboard-wrapper
  .md-table-row
  .md-table-cell
  .add-favoris
  .md-ripple {
  /* padding-left: 0;
  padding-right: 0; */
}
#content-dashboard-wrapper .md-table-cell-container {
  font-size: 14px;
  font-weight: 400;
  padding: 0;
  white-space: nowrap;
}
@media (max-width: 479px) {
  #content-dashboard-wrapper .md-table-cell-container {
    font-size: 12px;
  }
}
@media (max-width: 479px) {
  #content-dashboard-wrapper .md-button {
    font-size: 12px;
  }
}

#content-dashboard-wrapper .md-table-pagination {
  height: 52px;
}
@media (max-width: 1023px) {
  #content-dashboard-wrapper .md-table-pagination {
    justify-content: flex-start;
    padding: 0 5px;
  }
}
@media (max-width: 479px) {
  #content-dashboard-wrapper .md-table-pagination .md-table-pagination-label,
  #content-dashboard-wrapper .md-table-pagination span {
    white-space: nowrap;
  }
}
@media (max-width: 479px) {
  #content-dashboard-wrapper .md-table-pagination .md-field {
    margin: 0;
  }
}
@media (max-width: 479px) {
  #content-dashboard-wrapper .md-table-pagination .md-select-value {
    padding: 0px 0.5rem !important;
  }
}
@media (max-width: 479px) {
  #content-dashboard-wrapper
    .md-table-pagination
    .md-field
    .md-select-value
    + .md-icon {
    right: 0;
  }
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
.predict-table table {
  width: 100%;
}
.predict-table .table-header {
  background-color: var(--black) !important;
}

.predict-table .table-header th {
  vertical-align: middle;
}
.predict-table .md-table-head-container {
  padding: 0;
  height: 52px;
}
.predict-table .favori_col {
  width: 5%;
}
.predict-table .paire_col {
  width: 10%;
}
.predict-table .lastvalue_col {
  width: 15%;
}
.predict-table .sur_col {
  width: 5%;
}
.predict-table .up_col {
  width: 20%;
}
.predict-table .down_col {
  width: 20%;
}
.predict-table .cloture_col {
  width: 20%;
}
@media (max-width: 600px) {
  .predict-table .action_col .btn-link {
    padding-left: 0;
    padding-right: 0;
  }
}

.predict-table .action_col {
  width: 5%;
  text-align: center;
}
.predict-table .action_col .md-button-content svg {
  width: 0.75rem;
}
#content-dashboard-wrapper .couple-tables {
  flex-direction: column;
  flex-wrap: nowrap;
}
#content-dashboard-wrapper .couple-tables > .md-toolbar {
  flex: 1 0 50px;
  height: 50px;
  max-height: 50px;
}
#content-dashboard-wrapper .couple-tables > .md-table-content {
  flex: 1 1 100%;
  /* height: calc(100% - 50px); */
  height: calc(100vh - 210px);
}
</style>

<style scoped>
.tous-les-couples .table-container {
  height: 100%;
  /* max-height: calc(100vh - 200px); */
}
.tous-les-couples .table-container table {
  height: 100%;
}
.tous-les-couples .table-container tbody {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.input-search {
  background-color: #f6f6f7;
  border-radius: 4px;
  color: var(--placeholder);
}
.md-demande {
  font-family: "Roboto", Arial, Helvetica, sans-serif;
  font-weight: bold;
  font-size: 16px;
  border-radius: 4px;
  box-shadow: none !important;
  padding: 15px 31px;
  height: auto;
}
.md-demande:hover {
  background-color: var(--primary-hover) !important;
}
.md-demande.isRequested {
  background-color: #f6f6f7 !important;
  color: #21a179 !important;
}
.md-demande svg {
  margin-right: 10px;
}
.add-favoris-wrapper {
  width: fit-content !important;
  right: 0;
  top: 0;
  padding: 0;
}
.add-favoris {
  min-width: 36px;
}
.add-favoris::before {
  display: none;
}
.add-favoris:hover path {
  fill: #d3d4d6;
}
.add-favoris.active path {
  fill: #242c36;
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
@media (max-width: 639px) {
  .filter-bloc .md-field .md-input::-webkit-input-placeholder,
  .filter-bloc .md-field .md-textarea::-webkit-input-placeholder {
    font-size: 14px !important;
  }
}
@media (max-width: 600px) {
  .tr-mobile {
    display: flex;
    flex-flow: row wrap;
  }
  .md-table-row td,
  table td {
    order: 5;
  }
  .paire-col-mobile {
    max-width: calc(100% - 50px) !important;
    order: 1 !important;
    text-align: left;
  }
  .favori-col-mobile {
    padding-left: 16px;
    width: auto !important;
    /* max-width: 57px !important; */
    order: 3 !important;
    /* margin-left: auto; */
  }
  .last-value-col-mobile {
    display: none;
  }
  .valeur-mobile {
    font-weight: 400;
    font-size: 0.7rem;
  }
}
.back i {
  margin-right: 12px;
  vertical-align: middle;
}
</style>
