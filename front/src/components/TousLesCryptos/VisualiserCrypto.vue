<template id="magique">
  <div class="dashboard">
    <PermanentFull
      :menuItems="menuItems"
      appContentClass="p-0"
      v-on:refresh="stopWebsocket"
    >
      <!-- Loader -->
      <div class="loader-content" v-if="loader">
        <p class="msg">{{ $t("loading") }}</p>
        <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
      </div>
      <!-- /Loader -->
      <div
        id="content-dashboard-wrapper"
        class="md-layout-item d-flex flex-column px-0"
      >
        <div id="visualiser-crypto" class="mx-0 d-flex flex-column flex-grow-1">
          <div class="d-flex flex-column justify-content-center px-2 px-sm-3">
            <router-link
              to="/tous-les-couples"
              class="back mb-3 align-self-start"
              ><i class="fa fa-chevron-left" aria-hidden="true"></i>
              {{ $t("back") }}</router-link
            >
            <div
              class="d-flex flex-wrap justify-content-between align-items-center mb-3"
            >
              <div class="left">
                <h3 class="titre-recherche">{{ $t("visualisation") }}</h3>
                <p class="description">
                  {{ $t("visualisation:description") }}
                  <strong>"{{ $t("addAnotherPair") }}"</strong>.
                </p>
              </div>

              <div class="right">
                <md-button
                  class="submit-dialog text-center btn-submit text-normal w-100 py-0 m-0"
                  @click="toggleListeCouples()"
                >
                  <md-icon class="text-white">add</md-icon
                  >{{ $t("addAnotherCouple") }}</md-button
                >
              </div>
            </div>
          </div>
          <div class="px-2 px-sm-3">
            <div class="border-dashed dashboard-border slider-container p-2">
              <vueper-slides
                class="no-shadow"
                :slide-ratio="0.2"
                :infinite="false"
                slide-multiple
                :dragging-distance="200"
                :gap="2"
                :arrows="true"
                :bullets="false"
                :breakpoints="breakpoints"
              >
                <vueper-slide v-for="(item, i) in cardList" :key="i">
                  <template #content>
                    <div @click="handleSlideClick(item.name)" class="slideItem">
                      <md-card
                        class="crypto-card  position-relative d-flex flex-column m-0"
                      >
                        <div class="d-flex align-items-center">
                          <div
                            class="md-card-media cryto-item-md-card-media mr-2"
                          >
                            <span
                              class="b-avatar cryto-item-b-avatar bg-white cryto-item-big-avatar badge-secondary rounded-circle"
                              style="width: 86px; height: 86px;"
                            >
                              <span class="b-avatar-custom">
                                <span class="b-avatar-img">
                                  <img :src="item.symbol_1_logo" alt="logo_1" />
                                </span>
                              </span>
                            </span>
                            <span
                              class="b-avatar cryto-item-b-avatar bg-white cryto-item-avatar badge-secondary rounded-circle"
                              style="width: 53px; height: 53px;"
                            >
                              <span class="b-avatar-custom">
                                <span class="b-avatar-img">
                                  <img :src="item.symbol_2_logo" alt="logo_2" />
                                </span>
                              </span>
                            </span>
                          </div>

                          <md-card-header class="p-0 m-0">
                            <div
                              class="crypto-item-title d-flex flex-column align-items-center justify-content-center"
                            >
                              {{ item.assetFullName }}
                              <span class="crypto-sigle text-uppercase">{{
                                item.name
                              }}</span>
                            </div>
                          </md-card-header>
                        </div>

                        <md-card-content class="crypto-content w-100 mt-2 p-0">
                          <div class="crypto-status">
                            <span class="increase" v-if="item.h24 >= 0">
                              <svg
                                class="Trac_19695"
                                width="20"
                                height="12"
                                viewBox="2 6 20 12"
                              >
                                <path
                                  id="Trac_19695"
                                  d="M 16 6 L 18.29000091552734 8.289999961853027 L 13.41000080108643 13.17000007629395 L 9.410000801086426 9.170000076293945 L 2 16.59000015258789 L 3.410000085830688 18 L 9.409999847412109 12 L 13.40999984741211 16 L 19.70999908447266 9.710000038146973 L 22 12 L 22 6 L 16 6 Z"
                                ></path>
                              </svg>
                              {{ pointToComma(item.h24) }}%
                              <b-badge
                                class="status-badge bg-transparent position-absolute"
                                >{{ $t("now") }}</b-badge
                              >
                            </span>
                            <span class="decrease" v-if="item.h24 < 0">
                              <svg
                                class="Trac_19693"
                                width="20"
                                height="12"
                                viewBox="2 6 20 12"
                              >
                                <path
                                  id="Trac_19693"
                                  d="M 16 18 L 18.29000091552734 15.71000003814697 L 13.41000080108643 10.82999992370605 L 9.410000801086426 14.82999992370605 L 2 7.409999847412109 L 3.410000085830688 6 L 9.409999847412109 12 L 13.40999984741211 8 L 19.70999908447266 14.28999996185303 L 22 12 L 22 18 L 16 18 Z"
                                ></path>
                              </svg>
                              {{ pointToComma(item.h24) }}%
                              <b-badge
                                class="status-badge bg-transparent position-absolute"
                                >{{ $t("now") }}</b-badge
                              >
                            </span>
                          </div>
                        </md-card-content>
                      </md-card>
                      <md-card-actions
                        class="add-favoris-wrapper position-absolute"
                      >
                        <md-button
                          class="add-favoris w-100"
                          v-bind:class="{ active: item.favorite }"
                          @click="
                            item.favorite
                              ? deleteFavorite(item.name)
                              : addFavorite(item.name)
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
                    </div>
                  </template>
                </vueper-slide>
              </vueper-slides>
            </div>
          </div>
          <div class="graphe-wrapper">
            <div
              class="interval-checkbox custom-checkbox mt-3 selectors-container"
            >
              <div class="d-flex flex-wrap px-2 px-sm-3 listInterval-time">
                <div v-for="(item, index) in listInterval" :key="index">
                  <md-checkbox
                    class="mt-0"
                    v-model="interval_checkbox"
                    v-if="interval_checkbox"
                    :value="item"
                    :disabled="item == interval_checkbox ? true : false"
                    >{{ item }}</md-checkbox
                  >
                </div>
              </div>
            </div>

            <div class="main-wrapper">
              <div class="d-flex flex-wrap px-2 px-sm-3">
                <div id="container" class=""></div>
                <div class="selectors-container">
                  <div class="for-chart mt-auto">
                    <input
                      v-model="array"
                      id="sma"
                      class="checkbox"
                      type="checkbox"
                      value="sma"
                      @change="onOverlaysChange($event)"
                    />
                    <label for="sma">MA</label>

                    <input
                      v-model="array"
                      id="ema"
                      class="checkbox"
                      type="checkbox"
                      value="ema"
                      @change="onOverlaysChange($event)"
                    />
                    <label for="ema">EMA</label>

                    <input
                      v-model="array"
                      id="vwap"
                      class="checkbox"
                      type="checkbox"
                      value="vwap"
                      @change="onOverlaysChange($event)"
                    />
                    <label for="vwap">WMA</label>

                    <input
                      v-model="array"
                      id="bb"
                      class="checkbox"
                      type="checkbox"
                      value="bb"
                      @change="onOverlaysChange($event)"
                    />
                    <label for="bb">BOLL</label>

                    <input
                      v-model="array"
                      id="wma"
                      class="checkbox"
                      type="checkbox"
                      value="wma"
                      @change="onOverlaysChange($event)"
                    />
                    <label for="wma">VWAP</label>

                    <input
                      v-model="array"
                      id="psar"
                      class="checkbox"
                      type="checkbox"
                      value="psar"
                      @change="onOverlaysChange($event)"
                    />
                    <label for="psar">SAR</label>

                    <input
                      v-model="array"
                      id="trix"
                      class="checkbox"
                      type="checkbox"
                      value="trix"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="trix">TRIX</label>

                    <input
                      v-model="array"
                      id="macd"
                      class="checkbox"
                      type="checkbox"
                      value="macd"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="macd">MACD</label>

                    <input
                      v-model="array"
                      id="rsi"
                      class="checkbox"
                      type="checkbox"
                      value="rsi"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="rsi">RSI</label>

                    <input
                      v-model="array"
                      id="obv"
                      class="checkbox"
                      type="checkbox"
                      value="obv"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="obv">OBV</label>

                    <input
                      v-model="array"
                      id="cci"
                      class="checkbox"
                      type="checkbox"
                      value="cci"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="cci">CCI</label>

                    <input
                      v-model="array"
                      id="stochastic"
                      class="checkbox"
                      type="checkbox"
                      value="stochastic"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="stochastic">Stochastic</label>

                    <input
                      v-model="array"
                      id="williamsr"
                      class="checkbox"
                      type="checkbox"
                      value="williamsr"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="williamsr">WR</label>

                    <input
                      v-model="array"
                      id="dmi"
                      class="checkbox"
                      type="checkbox"
                      value="dmi"
                      @change="onOscillatorChange($event)"
                    />
                    <label for="dmi">DMI</label>

                    <!-- predictionGraph -->
                    <input
                      v-model="array"
                      id="prediction"
                      class="checkbox"
                      type="checkbox"
                      value="prediction"
                      @change="predictionGraph($event)"
                    />
                    <label for="prediction">{{ $t("prediction") }}</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </PermanentFull>
    <Dialog
      :showDialog="showDialogListeCouples"
      :dialogName="$t('dialog:listeCouples')"
      :iconDialog="iconModifJours"
      @close="showDialogListeCouples = false"
    >
      <div class="listeCouples pt-2">
        <div
          class="itemCouples text-center pt-2 pt-sm-3"
          v-for="(item, index) in listUserCouple"
          :key="index"
        >
          <div class="d-flex align-items-center justify-content-between">
            <div
              class="crypto-item-title d-flex flex-column align-items-start justify-content-center"
            >
              {{ item.fullName }}
              <span class="crypto-sigle text-uppercase text-left">{{
                item.symbol
              }}</span>
            </div>
            <md-checkbox
              class="mr-0 ml-1"
              v-model="arraySymbol"
              :value="item.symbol"
            ></md-checkbox>
          </div>
        </div>
      </div>
      <div class="form-group text-center mb-0">
        <md-button
          class="submit-dialog text-center btn-submit text-center w-100 px-0 mt-2 mt-sm-3"
          @click="addAnotherCouple()"
          :disabled="disableButton"
        >
          <md-icon class="text-white">add</md-icon>
          {{ $t("addMySelection") }}
        </md-button>
      </div>
    </Dialog>
    <div class="notifError" v-if="showDialogError">
      <md-button class="close-btn" @click="showDialogError = !showDialogError">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="14"
          height="14"
          viewBox="0 0 14 14"
        >
          <path
            id="Tracé_2542"
            data-name="Tracé 2542"
            d="M19,6.41,17.59,5,12,10.59,6.41,5,5,6.41,10.59,12,5,17.59,6.41,19,12,13.41,17.59,19,19,17.59,13.41,12Z"
            transform="translate(-5 -5)"
            fill="#fff"
          />
        </svg>
      </md-button>
      <div class="container">
        <p class="textError">{{ errorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import PermanentFull from "../PermanentFull/PermanentFull.vue";
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import MenuUser from "../../data/MenuUser";
import Dialog from "../Dialog/Dialog.vue";
import { PARAPHRASE } from "../../utils/Constant";

export default {
  name: "VisualiserCrypto",
  components: {
    PermanentFull,
    Dialog,
    VueperSlides,
    VueperSlide,
  },
  methods: {
    stopWebsocket() {
      if (this.conn) this.conn.close();
    },
    appendSlide() {
      this.slides.push({
        title: `${this.slides.length + 1}`,
        content: ` ${this.slides.length + 1} content.`,
      });
    },
    removeSlide() {
      this.slides.pop();
    },
    toggleSlideshow() {
      this.slideshowDisabled = !this.slideshowDisabled;
    },
    toggleDialogError() {
      this.showDialogError = !this.showDialogError;
    },
    onOverlaysChange(e) {
      const { value, checked } = e.target;
      if (checked) {
        this.chart.addSeries({
          type: value,
          linkedTo: "predictMarket",
          id: value,
          dataGrouping: {
            enabled: false,
          },
          groupPadding: 0,
          pointPadding: 0.04,
        });
      } else {
        const series = this.chart.get(value);
        if (series) series.remove(false);
      }
    },
    onOscillatorChange(e) {
      const { value, checked } = e.target;
      if (checked) {
        this.chart.addSeries({
          states: { hover: { enabled: false } },
          type: value,
          linkedTo: "predictMarket",
          id: value,
          yAxis: 2,
          dataGrouping: {
            enabled: false,
          },
          groupPadding: 0,
          pointPadding: 0.04,
        });
      } else {
        const series = this.chart.get(value);
        if (series) series.remove(false);
      }
    },
    predictionGraph(e) {
      const getPrediction = this.getDataPrediction.reverse();
      if (this.getDataPrediction.length !== 0) {
        let dataHigh = [];
        let dataLow = [];
        let dataClose = [];
        for (var i = 0; i < getPrediction.length; i += 1) {
          if (getPrediction[i].tag == "high") {
            dataHigh.push({
              x: new Date(getPrediction[i].predictime + 1).getTime(),
              y: getPrediction[i].prediction,
            });
          }
          if (getPrediction[i].tag == "low") {
            dataLow.push({
              x: new Date(getPrediction[i].predictime + 1).getTime(),
              y: getPrediction[i].prediction,
            });
          }
          if (getPrediction[i].tag == "close") {
            dataClose.push({
              x: new Date(getPrediction[i].predictime + 1).getTime(),
              y: getPrediction[i].prediction,
            });
          }
        }
        const { value, checked } = e.target;
        console.log(value);
        if (checked) {
          this.chart.addSeries({
            type: "line",
            name: "High-Prediction",
            data: dataHigh,
            id: "high",

            color: "yellow",
            dataGrouping: {
              enabled: false,
            },
            groupPadding: 0,
            pointPadding: 0.04,
          });
          this.chart.addSeries({
            type: "line",
            name: "Low-Prediction",
            data: dataLow,
            color: "#00FFFF",
            id: "low",
            dataGrouping: {
              enabled: false,
            },
            groupPadding: 0,
            pointPadding: 0.04,
          });
          this.chart.addSeries({
            type: "line",
            name: "Close-Prediction",
            data: dataClose,
            color: "#DB7093",
            id: "close",
            dataGrouping: {
              enabled: false,
            },
            groupPadding: 0,
            pointPadding: 0.04,
          });
        } else {
          ["low", "high", "close"].forEach((id) => {
            const series = this.chart.get(id);
            if (series) series.remove(false);
          });
        }
      }
    },

    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
    async handleSlideClick(item) {
      this.clicked = item;
      this.loader = true;
      await this.$store.dispatch("getCoupleBySymbolUser", {
        symbol: item,
        token: localStorage.getItem("token"),
      });
      this.paire = this.getPaire;
      this.listInterval = this.getPaire.intervals;
      var a = document.querySelectorAll(".slideItem");
      for (var i = 0, length = a.length; i < length; i++) {
        a[i].onclick = function() {
          var b = document.querySelector(".slideItem.active");
          if (b) b.classList.remove("active");
          this.classList.add("active");
        };
      }
      this.coupleWeb = item.replace("/", "").toLowerCase();
      this.interval_checkbox = this.listInterval[0];
      this.loader = false;
    },
    setAllFalse() {
      this.showDialog = false;
      this.showModal = false;
      this.showDialogListeCouples = false;
    },
    toggleActive() {
      this.isActive = !this.isActive;
    },
    toggleAdded() {
      this.isAdded = true;
      this.showDialog = !this.showDialog;
    },
    toggleListeCouples() {
      this.setAllFalse();
      this.showDialogListeCouples = !this.showDialogListeCouples;
    },
    deleteFavorite: async function(symbol) {
      this.disable = true;
      try {
        await this.$store.dispatch("deleteFavorite", {
          token: localStorage.getItem("token"),
          symbol,
        });
        await this.addAnotherCouple();
        this.disable = false;
      } catch (e) {
        this.errorMessage = this.$t("errorOccured");
        this.toggleDialogError();
        this.disable = false;
      }
    },
    addFavorite: async function(symbol) {
      this.disable = true;
      const payload = {
        couple: symbol,
      };
      try {
        await this.$store.dispatch("addFavorite", {
          token: localStorage.getItem("token"),
          payload,
        });
        await this.addAnotherCouple();
        this.disable = false;
      } catch (e) {
        this.errorMessage = this.$t("errorOccured");
        this.toggleDialogError();
        this.disable = false;
      }
    },
    displayGraph: async function(item, interval) {
      this.loader = true;
      const symbol = this.$route.params.symbol.replace("_", "");
      await this.$store.dispatch("displayGraphData", {
        symbol: item ? item.replace("/", "") : symbol,
        interval: interval,
        token: localStorage.getItem("token"),
      });
      await this.$store.dispatch("displayGraphPrediction", {
        symbol: item ? item.replace("/", "") : symbol,
        interval: interval,
        token: localStorage.getItem("token"),
      });
      this.prediction = this.getDataPrediction;
      this.couple = this.getCouple;
      this.displayChart(interval);
      this.loader = false;
    },
    getCoupleBySymbol: async function(item) {
      this.array = [];
      this.loader = true;
      try {
        await this.$store.dispatch("getCoupleBySymbolUser", {
          symbol: item,
          token: localStorage.getItem("token"),
        });
        this.cardList.push(this.getPaire);
        this.listInterval = this.getPaire.intervals;
        this.interval_checkbox = this.listInterval[0];
        this.loader = false;
      } catch (e) {
        //erreur de connexion
        this.errorMessage = this.$t("message:errorConnection");
        this.toggleDialogError();
        this.loader = false;
      }
    },
    async getDataForCardList(symbol, item) {
      await this.$store.dispatch("getCoupleBySymbolUser", {
        symbol: symbol,
        token: localStorage.getItem("token"),
      });
      if (item == 0) {
        this.listInterval = this.getPaire.intervals;
        this.interval_checkbox = this.listInterval[0];
      }
      this.cardList.push(this.getPaire);
    },
    getUserCouple: async function() {
      await this.$store.dispatch("getUserCouple", {
        token: localStorage.getItem("token"),
      });
    },
    async addAnotherCouple() {
      this.cardList = [];
      this.showDialogListeCouples = false;
      this.loader = true;
      for (let i = 0; i < this.arraySymbol.length; i++) {
        await this.getDataForCardList(this.arraySymbol[i], i);
      }
      this.loader = false;
    },
    getTimeWebsocket(item) {
      if (item.includes("m")) {
        return +item.slice(0, -1) * 60000;
      }
      if (item.includes("h")) {
        return +item.slice(0, -1) * 60 * 60000;
      }
      if (item.includes("d")) {
        return 24 * 60 * 60000;
      }
      return 60000;
    },
    setValueNavigator(interval) {
      //set the width of the navigator according to the interval
      if (interval.includes("h")) return +interval.slice(0, -1) * 172800000;
      else if (interval.includes("m")) return +interval.slice(0, -1) * 1200000;
      else return +interval.slice(0, -1) * 24 * 48 * 60 * 60 * 1000;
    },
    volumeBarColor(point) {
      if (point[1] < point[4]) return "rgba(14,203,129,255)";
      if (point[1] > point[4]) return "rgba(246,70,93,255)";
      return "rgba(246,70,93,255)";
    },
    translateHighcharts() {
      // eslint-disable-next-line no-undef
      Highcharts.setOptions({
        lang: {
          months: [
            this.$t("january"),
            this.$t("february"),
            this.$t("march"),
            this.$t("april"),
            this.$t("may"),
            this.$t("june"),
            this.$t("july"),
            this.$t("august"),
            this.$t("september"),
            this.$t("october"),
            this.$t("november"),
            this.$t("december"),
          ],
          weekdays: [
            this.$t("sunday"),
            this.$t("monday"),
            this.$t("tuesday"),
            this.$t("wednesday"),
            this.$t("thursday"),
            this.$t("friday"),
            this.$t("saturday"),
          ],
        },
      });
    },
    displayChart(item) {
      // eslint-disable-next-line no-undef
      Highcharts.setOptions({
        global: {
          useUTC: false,
        },
      });
      const overscrollValue = 5 * this.getTimeWebsocket(item);
      const data = this.getCouple;
      const valueNavigator = this.setValueNavigator(item);
      let ohlc = [];
      let volume = [];
      let dataLength = data.length;

      for (var i = 0; i < dataLength; i += 1) {
        ohlc.push([
          data[i][0], // the date
          data[i][1], // open
          data[i][2], // high
          data[i][3], // low
          data[i][4], // close
        ]);
        volume.push({
          x: data[i][0], // the date
          y: +data[i][5], // the volume
          color: this.volumeBarColor(data[i]),
        });
      }
      // eslint-disable-next-line no-undef
      this.chart = Highcharts.stockChart("container", {
        chart: {
          height: 600,
          marginRight: 65,
          spacingRight: 30,
          animation: false,
          plotBorderWidth: 1,
          plotBorderColor: "#383838",
          backgroundColor: "black",
          plotBackgroundColor: "rgba(10,0,0,0)",
          events: {
            //label yAxis
            render: function() {
              const lastPoint = this.series[0].points[
                this.series[0].points.length - 1
              ];
              if (lastPoint) {
                const lastPointClose = lastPoint.close,
                  xPos = this.plotLeft + this.xAxis[0].width,
                  yPos = lastPoint.plotClose + this.plotTop;
                if (this.customLabel) {
                  this.customLabel.destroy();
                  this.customLabel = undefined;
                }

                this.customLabel = this.renderer
                  .g()
                  .add()
                  .toFront();
                this.renderer
                  .rect(xPos, yPos - 10, 50, 20)
                  .attr({
                    fill: lastPoint.color,
                  })
                  .add(this.customLabel);
                this.renderer
                  .text(lastPointClose, xPos, yPos)
                  .css({
                    color: "white",
                    // backgroundColor: "red",
                    alignmentBaseline: "middle",
                  })
                  .add(this.customLabel);
              }
            },
            load() {
              //CROSSHAIR
              if (this.plotBackground) {
                this.plotBackground.toFront().css({
                  cursor: "crosshair",
                });
              }

              //NAVIGATOR
              const max = this.xAxis[0].max,
                min = max - valueNavigator;
              this.xAxis[0].setExtremes(min, max);

              //ZOOM
              const chart = this;
              // eslint-disable-next-line no-undef
              Highcharts.addEvent(
                chart.container,
                document.onmousewheel === undefined
                  ? "DOMMouseScroll"
                  : "mousewheel",
                function(e) {
                  const axis = chart.xAxis[0],
                    extremes = axis.getExtremes(),
                    min = extremes.min,
                    max = extremes.max,
                    range = max - min,
                    delta = -(e.deltaY || e.detail || 0),
                    precision = range / 20;

                  if (
                    chart.isInsidePlot(
                      e.x - chart.plotLeft,
                      e.y - chart.plotTop
                    )
                  ) {
                    // Calculate where the user mouse is on chart.
                    const proportion = (e.x - chart.plotLeft) / chart.plotWidth;
                    const newMin = min + proportion * delta * precision;
                    const newMax = max - (1 - proportion) * delta * precision;

                    if (newMin < newMax) {
                      axis.setExtremes(
                        newMin < extremes.dataMin ? extremes.dataMin : newMin,
                        newMax > extremes.dataMax ? extremes.dataMax : newMax
                      );

                      e.preventDefault();
                      e.stopPropagation();
                    }
                  }
                }
              );
            },
          },
        },

        legend: {
          enabled: false,
        },
        exporting: { enabled: false },
        rangeSelector: {
          inputEnabled: false,
          selected: 0,
          enabled: false,
        },
        mapNavigation: {
          enabled: false,
          enableMouseWheelZoom: true,
        },
        navigator: {
          enabled: false,
        },
        scrollbar: {
          enabled: false,
        },
        xAxis: {
          overscroll: overscrollValue,
          minRange: 2 * overscrollValue,
          gridLineWidth: 1,
          gridLineColor: "#383838",
          lineColor: "#383838",
          tickColor: "#383838",
          crosshair: {
            width: 2,
            color: "gray",
            dashStyle: "Dash",
            label: {
              enabled: true,
              backgroundColor: "#666666",
              format: "{value:%Y/%m/%d %k:%M}",
            },
          },
        },
        tooltip: {
          xDateFormat: "%Y/%m/%d",
          shape: "square",
          headerShape: "callout",
          borderWidth: 0,
          shadow: false,
          useHTML: true,
          positioner: function() {
            return {
              x: 10,
              y: 0,
            };
          },
          split: true,
          distance: 30,
          padding: 5,
          valueDecimals: 2,
          formatter() {
            let s = "";
            this.points.forEach(function(point) {
              if (point.series.name === "Predict Market") {
                // eslint-disable-next-line no-undef
                s += `${Highcharts.dateFormat("%Y/%m/%d", point.x)}`;
                s += ` Open : <b> <span style="color: ${point.point.color}">${point.point.open} </span></b>`;
                s += ` High : <b> <span style="color: ${point.point.color}"> ${point.point.high} </span></b>`;
                s += ` Low : <b> <span style="color: ${point.point.color}">${point.point.low} </span></b>`;
                s += ` Close : <b> <span style="color: ${point.point.color}">${point.point.close} </span></b>`;
                s += "<br>";
              }
              if (point.series.name === "High-Prediction") {
                s += "<b>Prediction</b> ";
                s += "High";
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                // s += "<br>";
              }
              if (point.series.name === "Low-Prediction") {
                s += " Low";
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                // s += "<br>";
              }
              if (point.series.name === "Close-Prediction") {
                s += " Close";
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "Volume") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "SMA (14)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "EMA (9)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "WMA (9)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "BB (20, 2)") {
                s += `${point.series.name}`;
                s += ` Top: <b><span style="color: ${
                  point.point.color
                }">${point.point.top.toFixed(2)}</span></b>`;
                s += ` Middle: <b><span style="color: ${
                  point.point.color
                }">${point.point.middle.toFixed(2)}</span></b>`;
                s += ` Bottom: <b><span style="color: ${
                  point.point.color
                }">${point.point.bottom.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "VWAP (30)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "PSAR") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "TRIX (9)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "MACD (26, 12, 9)") {
                s += ` <b>${point.series.name}</b>`;
                s += ` Value : <b><span style="color: ${
                  point.point.color
                }">${point.point.MACD.toFixed(2)}</span></b>`;
                s += ` Signal : <b><span style="color: ${
                  point.point.color
                }">${point.point.signal.toFixed(2)}</span></b>`;
                s += ` Histogram : <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "RSI (14)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "OBV") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "CCI (14)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "Stochastic (14,3)") {
                s += `${point.series.name}`;
                s += ` %K : <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += ` %D : <b><span style="color: ${
                  point.point.color
                }">${point.point.smoothed.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "Williams %R (14)") {
                s += `${point.series.name}`;
                s += `: <b><span style="color: ${
                  point.point.color
                }">${point.point.y.toFixed(2)}</span></b>`;
                s += "<br>";
              }
              if (point.series.name === "DMI (14)") {
                s += `${point.series.name}`;
                s += ` DX: <span style="color: ${
                  point.point.color
                }"></span> ${point.point.y.toFixed(
                  2
                )} +DI: <span style="color: ${
                  point.point.series.options.plusDILine.styles.lineColor
                }">${point.point.plusDI.toFixed(
                  2
                )}</span> -DI: <span style="color: ${
                  point.point.series.options.minusDILine.styles.lineColor
                }">${point.point.minusDI.toFixed(2)}</span>`;
                s += "<br>";
              }
            });
            return s;
          },
          shared: true,
        },
        yAxis: [
          {
            height: "60%",
            gridLineColor: "#383838",
            crosshair: {
              snap: false,
              width: 2,
              color: "gray",
              dashStyle: "Dash",
              //label yaxis
              label: {
                enabled: true,
                format: "{value:.2f}",
              },
            },
            //set space between yaxis
            labels: {
              align: "left",
              format: "{value:.2f}",
              y: 6,
              x: 2,
            },
          },
          {
            offset: 0,
            crosshair: {
              snap: false,
              width: 2,
              color: "gray",
              dashStyle: "Dash",
              label: {
                enabled: true,
                format: "{value:.2f}",
              },
            },
            top: "60%",
            height: "20%",
            gridLineColor: "#383838",
            labels: {
              align: "left",
              format: "{value:.2f}",
              y: 6,
              x: 2,
            },
          },
          {
            offset: 0,
            crosshair: {
              snap: false,
              width: 2,
              color: "gray",
              dashStyle: "Dash",
              label: {
                enabled: true,
                format: "{value:.2f}",
              },
            },
            top: "80%",
            height: "20%",
            gridLineColor: "#383838",
            labels: {
              align: "left",
              format: "{value:.2f}",
              y: 6,
              x: 2,
            },
          },
        ],
        plotOptions: {
          series: {
            lineWidth: 2,
            showInLegend: true,
            marker: {
              radius: 0,
            },
            states: {
              inactive: {
                opacity: 1,
              },
            },
          },
          sma: {
            color: "rgba(0,191,255)", //DeepSkyBlue
          },
          ema: {
            color: "rgba(173,255,47)", //GreenYellow
          },
          vwap: {
            color: "rgba(255,215,0)", //golden
          },
          wma: {
            color: "rgba(255,218,185)", //peachpuff
          },
          macd: {
            color: "rgba(14,203,129,255)",
            negativeColor: "rgba(246,70,93,255)",
            signalLine: {
              styles: {
                lineWidth: 3,
                lineColor: "teal",
              },
            },
            macdLine: {
              styles: {
                lineWidth: 3,
                lineColor: "purple",
              },
            },
          },
          psar: {
            color: "rgba(255,0,0)", //red
          },
          bb: {
            color: "purple",
            topLine: {
              styles: {
                lineColor: "teal",
              },
              lineWidth: 2,
            },
            bottomLine: {
              styles: {
                lineColor: "teal",
              },
              lineWidth: 2,
            },
          },
          dmi: {
            color: "teal",

            plusDILine: {
              styles: {
                lineColor: "purple",
              },
            },
            minusDILine: {
              styles: {
                lineColor: "orange",
              },
            },
          },
          williamsr: {
            color: "orange",
          },
        },
        series: [
          {
            type: "candlestick",
            upColor: "rgba(14,203,129,255)", //green
            upLineColor: "rgba(14,203,129,255)",
            color: "rgba(246,70,93,255)",
            lineColor: "rgba(246,70,93,255)", //red
            id: "predictMarket",
            name: "Predict Market",
            data: data,
            dataGrouping: {
              enabled: false,
            },
            groupPadding: 0,
            pointPadding: 0.04,
          },
          {
            type: "column",
            id: "volume",
            name: "Volume",
            data: volume,
            yAxis: 1,
            groupPadding: 0,
            pointPadding: 0.04,
            dataGrouping: {
              enabled: false,
            },
          },
        ],
      });
    },
    subscribe(couple, interval) {
      if (this.conn) {
        //this.unSubscribe(couple, interval);
        this.conn.send(
          JSON.stringify({
            method: "SUBSCRIBE",
            params: [`${couple}@kline_${interval}`], //["btcusdt@kline_1h"],
            id: 1,
          })
        );
      }
    },
    unSubscribe(couple, interval) {
      if (this.conn) {
        this.conn.send(
          JSON.stringify({
            method: "UNSUBSCRIBE",
            params: [`${couple}@kline_${interval}`], //["btcusdt@kline_1h"],
            id: 1,
          })
        );
      }
    },
    decryptValue(val) {
      return this.CryptoJS.AES.decrypt(val, PARAPHRASE).toString(
        this.CryptoJS.enc.Utf8
      );
    },
  },
  data: () => {
    return {
      fixedHeight: true,
      disableArrowsOnEdges: true,
      breakpoints: {
        3000: {
          visibleSlides: 5,
          gap: 1,
        },
        1441: {
          visibleSlides: 4,
          gap: 1,
        },
        1199: {
          visibleSlides: 3,
          gap: 2,
        },
        991: {
          visibleSlides: 2,
          gap: 2,
        },
        640: {
          visibleSlides: 1,
          gap: 0,
        },
      },
      array: [],
      showDialogListeCouples: false,
      showModal: false,
      isActive: false,
      disableButton: false,
      chart: null,
      disable: false,
      listInterval: [],
      displayListCouple: [],
      coupleWeb: null,
      loader: true,
      conn: null,
      cardList: [],
      web: null,
      isChanged: false,
      paire: {},
      xmr_ada: "",
      couple: [],
      interval_checkbox: null,
      clicked: null,
      prediction: [],
      arraySymbol: [],
      graphe: require("../../assets/images/graph.jpg"),
      showDialogError: false,
      errorMessage: "",
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
      settings: {
        arrows: false,
        dots: false,
        slidesToScroll: 1,
        slidesToShow: 5,
        swipeToSlide: true,
        responsive: [
          {
            breakpoint: 1400,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 1,
            },
          },
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
            },
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
            },
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
            },
          },
        ],
      },
      menuItems: MenuUser,
    };
  },
  async mounted() {
    this.loader = true;
    await this.getUserCouple();
    await this.getCoupleBySymbol(this.$route.params.symbol.replace("_", "/"));

    this.coupleWeb = this.$route.params.symbol.replace("_", "").toLowerCase();
    this.arraySymbol.push(this.$route.params.symbol.replace("_", "/"));

    this.conn = new WebSocket("wss://stream.binance.com:9443/ws");
    this.conn.onopen = () => {
      this.subscribe(this.coupleWeb, this.interval_checkbox);
      this.conn.onmessage = (evt) => {
        const web = JSON.parse(evt.data);
        this.isChanged = true;
        if (this.chart) {
          if (web.k) {
            let series = this.chart.series[0];
            if (series) {
              let seriesVolume = this.chart.series[1];
              if (series.data[series.data.length - 1].category < +web.k.t) {
                series.addPoint(
                  [
                    +web.k.t,
                    +web.k.o,
                    +web.k.h,
                    +web.k.l,
                    +web.k.c,
                    //+web.k.v,
                  ],
                  true,
                  true
                );
                seriesVolume.addPoint(
                  {
                    x: +web.k.t, // the date
                    y: +web.k.v, // the volume
                    color:
                      +web.k.o < +web.k.c
                        ? "rgba(14,203,129,255)"
                        : "rgba(246,70,93,255)",
                  },
                  true,
                  true
                );
                const axis = this.chart.xAxis[0], //chart.xAxis[0],
                  extremes = axis.getExtremes(),
                  min = extremes.min,
                  dataMax = extremes.dataMax;
                axis.setExtremes(min, dataMax);
              }
              var oldValueArr = series.data[series.data.length - 1].category;
              let ts = oldValueArr[0];
              let open = +web.k.o;
              let high = +web.k.h;
              let low = +web.k.l;
              let close = +web.k.c;
              high = Math.max(high, close);
              low = Math.min(low, close);
              let newValueArr = [ts, open, high, low, close];
              series.data[series.data.length - 1].update(newValueArr);

              //volume
              let newValueArr2 = {
                x: +web.k.t, // the date
                y: +web.k.v, // the volume
                color:
                  +web.k.o < +web.k.c
                    ? "rgba(14,203,129,255)"
                    : "rgba(246,70,93,255)",
              };
              seriesVolume.data[seriesVolume.data.length - 1].update(
                newValueArr2
              );
            }
          }
        }
      };
    };
    this.conn.onerror = function() {
      //console.error("an error occurred");
      location.reload();
    };
  },
  reInit() {
    this.$refs.slickone.reSlick();
  },
  computed: {
    getCouple() {
      return this.$store.state.couple.graphData.data;
    },
    getPaire() {
      return this.$store.state.paire.coupleIdUser.data;
    },
    getDataPrediction() {
      return this.$store.state.couple.graphPrediction.prediction;
    },
    listUserCouple() {
      return this.$store.state.dashboard.userCouple.data;
    },
    slickOptions() {
      return {
        slidesToShow: this.slidesToShow,
      };
    },
  },
  created() {},
  watch: {
    "$i18n.locale"() {
      this.translateHighcharts();
    },
    arraySymbol(val) {
      this.disableButton = val.length ? false : true;
      if (
        val.length === 1 &&
        val[0] === this.$route.params.symbol.replace("_", "/")
      ) {
        this.disableButton = true;
      }
    },
    interval_checkbox(val, old) {
      this.array = [];
      if (old) {
        this.unSubscribe(this.coupleWeb, old);
        this.subscribe(this.coupleWeb, val);
      }
      this.displayGraph(this.clicked, val);
    },
  },
};
</script>

<style>
#visualiser-crypto .slider-container {
}
#visualiser-crypto .slick-list .slick-track {
  background-color: #fff;
  display: flex;
  flex-wrap: nowrap;
  width: auto !important;
  max-width: 100%;
}
#visualiser-crypto .slick-list .slick-slide {
  float: none;
  min-width: 302px;
}
@media (max-width: 600px) {
  #visualiser-crypto .slick-list .slick-slide {
    min-width: unset;
  }
}

.predict-dialog .itemCouples {
  width: 312px;
}
@media (max-width: 600px) {
  .predict-dialog .itemCouples {
    width: 99%;
  }
}
#visualiser-crypto .vueperslides__parallax-wrapper {
  height: 110px;
  padding-bottom: 0 !important;
}
#visualiser-crypto .vueperslides__inner {
}
#visualiser-crypto .vueperslides {
  background-color: #fff;
}
#visualiser-crypto .vueperslides__arrows {
  color: currentColor;
  text-align: right;
}
@media (max-width: 600px) {
  #visualiser-crypto .vueperslides__arrows {
    text-align: center;
  }
}
#visualiser-crypto .vueperslides__arrow {
  border-radius: 50%;
  background-color: var(--primary);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 30px;
  margin: 0.5rem 0.25rem 0;
  padding: 0;
  position: relative;
  transform: none;
  width: 30px;
}
#visualiser-crypto .vueperslides__arrow--next {
  right: auto;
}
#visualiser-crypto .vueperslides__arrow--prev {
  left: auto;
}
#visualiser-crypto .vueperslides__arrow svg {
  padding: 0;
  width: 0.525rem;
}
#visualiser-crypto .main-wrapper #container {
  width: 100%;
}
#visualiser-crypto .highcharts-container {
  width: 100%;
}
#visualiser-crypto .highcharts-container svg {
  width: 100%;
}
#visualiser-crypto .highcharts-container .highcharts-root .highcharts-credits {
  display: none;
}
</style>
<style scoped>
.crypto-card {
  padding: 12px;
  border-radius: 12px;
  width: 100%;
  /* max-width: 300px; */
}
.crypto-card.active {
  border: 1px solid var(--primary);
  box-shadow: 0px 2px 4px #14141414;
}
#visualiser-crypto .cryto-item-md-card-media {
  height: 51px;
  min-width: 63px;
  width: 63px;
}
.cryto-item-b-avatar {
  position: absolute;
}

#visualiser-crypto .cryto-item-b-avatar:first-child {
  height: 45px !important;
  min-width: 45px;
  width: 45px !important;
}
#visualiser-crypto .cryto-item-b-avatar:first-child .b-avatar-img {
  height: 41px;
}
#visualiser-crypto .cryto-item-b-avatar:last-child {
  height: 28px !important;
  min-width: 28px;
  width: 28px !important;
}
.cryto-item-big-avatar {
  top: 0;
  left: 0;
  z-index: 2;
  border: 2px solid #5c626a;
}
.cryto-item-big-avatar .b-avatar-img {
  width: 60px;
  height: 60px;
}
.cryto-item-big-avatar img,
.cryto-item-avatar img {
  width: auto;
  height: auto;
  object-fit: inherit;
  max-width: 66%;
  max-height: 66%;
  border-radius: 0;
}
.cryto-item-avatar {
  bottom: 0;
  right: 0;
  border: 1px solid var(--placeholder);
}
.cryto-item-avatar .b-avatar-img img {
  width: 28px;
  height: 28px;
}
.crypto-status {
  font-size: 16px;
}
.crypto-status .increase,
.crypto-status .increase path {
  color: #21a179;
  fill: #21a179;
}
.crypto-status .decrease,
.crypto-status .decrease path {
  color: var(--rouge);
  fill: var(--rouge);
}
.crypto-status .status-badge {
  color: var(--placeholder);
  font-size: 8px;
}
.crypto-item-title {
  font-size: 14px;
  color: var(--black);
  font-family: "Poppins-Medium", Arial, Helvetica, sans-serif;
}
.crypto-sigle {
  color: #5c626a;
  font-size: 12px;
  letter-spacing: 0.1px;
  line-height: 18px;
  width: 100%;
}
.crypto-btn-ajouter {
  border: 1px solid #5c626a;
  border-radius: 16px;
  color: #5c626a !important;
  font-size: 12px;
  line-height: 16px;
  text-transform: inherit;
  height: 32px;
  min-width: auto;
}
.crypto-btn-ajouter.added {
  border: 1px solid var(--primary);
  background-color: var(--primary);
  color: #fff !important;
}
.crypto-btn-ajouter:hover {
  background-color: #f6f6f7;
}
.crypto-btn-ajouter.added:hover {
  background-color: #f8bd25;
}
.slideItem {
  z-index: 98;
}
.slideItem .crypto-card {
  border: 1px solid rgb(0 0 0 / 5%);
}
.slideItem:hover .crypto-card,
.slideItem.active .crypto-card {
  border: 1px solid var(--primary);
  cursor: pointer;
  box-shadow: 0px 2px 4px #14141414;
}

.add-favoris-wrapper {
  border-radius: 12px;
  width: -webkit-fit-content !important;
  width: -moz-fit-content !important;
  width: fit-content !important;
  right: 10px;
  top: 5px;
  padding: 0;
  z-index: 99;
}
@media (max-width: 600px) {
  .add-favoris-wrapper {
    right: 0px;
    top: 0px;
  }
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

@media (max-width: 600px) {
  .crypto-item-title,
  .crypto-status {
    font-size: 12px;
  }
  .crypto-sigle {
    font-size: 10px;
  }
}
.graph-wrapper {
  margin-left: -12px;
  margin-right: -12px;
  padding-left: 12px;
  padding-right: 12px;
  background: black;
  position: relative;
}
.interval-checkbox .md-checkbox {
  background-color: #5c626a;
  font-size: 12px;
  color: #fff;
  border-radius: 13px;
  font-weight: 400;
}
@media (max-width: 479px) {
  .interval-checkbox .listInterval-time {
    justify-content: center;
  }
}
.interval-checkbox .md-checked.md-checkbox {
  background-color: var(--primary) !important;
  color: var(--black);
}
/* .highcharts-container,
.highcharts-container svg {
  width: 50px !important;
} */
.graphe-wrapper {
  background: #000;
  margin-top: 20px;
}
.selectors-container {
  margin-bottom: 1rem;
  font-size: 0;
}

.selectors-container .col {
  font-size: 1.2rem;
  width: calc(50% - 1em);
  padding: 0.5em;
  display: inline-block;
}

.selectors-container select {
  width: 100%;
  font-size: 16px; /* prevent page zoom in iOS */
}

@media (max-width: 768px) {
  .selectors-container .col {
    display: block;
    width: calc(100% - 1em);
  }
}
@media (max-width: 600px) {
  .slideItemWrapper {
    max-width: 300px;
  }
}
.back i {
  margin-right: 12px;
  vertical-align: middle;
}
@media (max-width: 767px) {
  #visualiser-crypto .right {
    margin: 0 auto;
  }
}
.notifError {
  background-color: #f5222d;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;

  z-index: 10;
}
.notifError .container {
  padding: 15px 15px;
}
@media (max-width: 767px) {
  .notifError .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 15px 30px;
    width: 100%;
  }
}
.notifError .textError {
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  line-height: 125%;
  margin: 0;
  text-align: center;
}
@media (max-width: 767px) {
  .notifError .textError {
    font-size: 12px;
  }
}
.notifError .close-btn {
  margin: 0;
  min-width: unset;
  padding: 0;
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}
@media (max-width: 767px) {
  .notifError .close-btn {
    right: 5px;
  }
}
</style>
