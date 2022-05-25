<template>
  <div
    :class="
      idUserSubscription === typeId
        ? 'abonnement-item abonnement-active dashboard-border position-relative my-1 h-100 p-0'
        : 'abonnement-item dashboard-border position-relative my-1 h-100 p-0'
    "
    :style="[
      recommande === true
        ? { borderColor: 'var(--primary) !important', borderWidth: ' 2px' }
        : {},
    ]"
  >
    <span
      v-html="iconRecommande"
      class="iconRecommande position-absolute"
      v-if="recommande"
    ></span>
    <md-badge
      md-position="top"
      class="badge w-auto bg-transparent position-absolute"
      v-if="is_active"
    >
      -{{ pourcentage }}%
    </md-badge>
    <md-card class="card shadow-none border-0 mx-0">
      <md-card-media>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="70.5"
          height="70.5"
          viewBox="0 0 70.5 70.5"
        >
          <g
            id="Groupe_53081"
            data-name="Groupe 53081"
            transform="translate(-85 -147.981)"
          >
            <g
              id="Oval"
              transform="translate(85 147.981)"
              fill="transparent"
              stroke="#5c626a"
              stroke-miterlimit="10"
              stroke-width="2"
            >
              <circle cx="35.25" cy="35.25" r="35.25" stroke="none" />
              <circle cx="35.25" cy="35.25" r="34.25" fill="none" />
            </g>
            <path
              id="crown"
              d="M41.8,27.993a4.242,4.242,0,1,0-8.484,0,3.984,3.984,0,0,0,.509,1.994l-4.5,3.436-4.454-5.854a4.237,4.237,0,1,0-7.3-2.927,4.161,4.161,0,0,0,1.1,2.842l-4.793,5.938L9.732,30.071a4.341,4.341,0,0,0,.551-2.078A4.242,4.242,0,1,0,5.7,32.235l1.612,8.441v4.411A1.25,1.25,0,0,0,8.587,46.36H34.971a1.25,1.25,0,0,0,1.273-1.273V40.676l1.612-8.441A4.286,4.286,0,0,0,41.8,27.993Zm-4.242-1.7a1.7,1.7,0,1,1-1.7,1.7A1.7,1.7,0,0,1,37.558,26.3ZM21.821,22.945a1.7,1.7,0,1,1-1.7,1.7A1.7,1.7,0,0,1,21.821,22.945ZM14.1,36.519h.127a1.311,1.311,0,0,0,.848-.467L20.888,28.8a6.328,6.328,0,0,0,.891.085,5.2,5.2,0,0,0,.806-.085l5.429,7.211a1.366,1.366,0,0,0,.848.509h.17a1.184,1.184,0,0,0,.764-.255l5.514-4.242-1.4,7.253H9.69L8.332,32.192l5.005,4.072A1.107,1.107,0,0,0,14.1,36.519ZM4.387,27.993a1.7,1.7,0,1,1,1.7,1.7A1.7,1.7,0,0,1,4.387,27.993ZM9.9,43.815V41.821H33.741v1.994Z"
              transform="translate(99.2 149.582)"
              fill="#5c626a"
            />
          </g>
        </svg>
      </md-card-media>
      <md-card-header>
        <div class="md-subhead">{{ $t("offer") }}</div>
        <div class="md-title">{{ nom }}</div>
      </md-card-header>
    </md-card>
    <div
      class="content-wrapper py-4"
      :style="[recommande === true ? { paddingTop: '40px !important' } : {}]"
    >
      <div
        v-if="mensuelAnnuel"
        class="discount d-flex align-items-baseline justify-content-center px-2"
      >
        <span class="mr-1"
          ><del>{{ pointToComma(discountPrix) }}€</del></span
        ><span class="color-primary"
          >{{ $t("card:save") }} {{ pointToComma(discountSaved) }} €</span
        >
      </div>
      <div class="price-wrapper d-flex justify-content-center my-3">
        <div class="unite align-self-start">€</div>
        <div class="price align-self-center">{{ pointToComma(price) }}</div>
        <div class="align-self-end">{{ $t("ttcMonth") }}</div>
      </div>

      <div
        class="children-wrapper d-flex flex-column justify-content-center my-3"
      >
        <slot></slot>
      </div>

      <div
        class="w-100 text-center"
        :style="[recommande === true ? { paddingTop: '20px' } : {}]"
      >
        <router-link
          :to="{
            name: 'Commande',
            params: { typeId: typeId, status: status },
          }"
          class="mt-3 align-self-start d-inline-block w-100"
          style="max-width: 172px"
        >
          <md-button
            class="submit-dialog text-center btn-submit text-normal p-0 m-0"
            :disabled="idUserSubscription === typeId && true"
          >
            {{ $t("subscribe:button") }}
          </md-button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AbonnementItem",
  props: {
    nom: String,
    discountPrix: Number,
    discountSaved: Number,
    pourcentage: Number,
    price: Number,
    mensuelAnnuel: Boolean,
    recommande: Boolean,
    is_active: Boolean,
    typeId: Number,
    idUserSubscription: Number,
  },
  data: () => {
    return {
      iconRecommande: `
        <svg xmlns="http://www.w3.org/2000/svg" width="113.469" height="113.468" viewBox="0 0 113.469 113.468">
          <g id="Groupe_14302" data-name="Groupe 14302" transform="translate(-3419.054 2.117)">
            <g id="Groupe_14300" data-name="Groupe 14300" transform="translate(3419.054 -2.117)">
              <g id="Groupe_14299" data-name="Groupe 14299" transform="translate(0 0)">
                <g id="Groupe_14298" data-name="Groupe 14298">
                  <g id="Groupe_14293" data-name="Groupe 14293">
                    <path id="Tracé_42181" data-name="Tracé 42181" d="M3527.388-2.063l-108.28,108.28-.054-30.719a6.744,6.744,0,0,1,1.975-4.78l70.86-70.86a6.743,6.743,0,0,1,4.78-1.975Z" transform="translate(-3419.054 2.117)" fill="#d80303"/>
                  </g>
                  <g id="Groupe_14294" data-name="Groupe 14294" transform="translate(103.2 0.054)">
                    <path id="Tracé_42182" data-name="Tracé 42182" d="M3941.609-1.847l5.135,5.134h-10.269Z" transform="translate(-3936.474 1.847)" fill="#890303"/>
                  </g>
                  <g id="Groupe_14295" data-name="Groupe 14295" transform="translate(0.054 103.199)">
                    <path id="Tracé_42183" data-name="Tracé 42183" d="M3419.323,520.437l5.135-5.135v10.269Z" transform="translate(-3419.323 -515.303)" fill="#890303"/>
                  </g>
                  <g id="Groupe_14296" data-name="Groupe 14296" transform="translate(1.812 1.812)">
                    <path id="Tracé_42184" data-name="Tracé 42184" d="M3428.948,107.947a.805.805,0,0,0,.572-.236l99.6-99.36a.809.809,0,1,0-1.143-1.146l-99.6,99.36a.809.809,0,0,0,.571,1.382Z" transform="translate(-3428.139 -6.969)" fill="#fff"/>
                  </g>
                  <g id="Groupe_14297" data-name="Groupe 14297" transform="translate(1.812 2.043)">
                    <path id="Tracé_42185" data-name="Tracé 42185" d="M3428.948,82.672a.807.807,0,0,0,.573-.238l72.7-72.927a.809.809,0,0,0-1.146-1.143l-72.7,72.927a.809.809,0,0,0,.573,1.381Z" transform="translate(-3428.138 -8.127)" fill="#fff"/>
                  </g>
                </g>
              </g>
            </g>
            <g id="Groupe_14301" data-name="Groupe 14301" transform="translate(3424.379 1.979)">
              <path id="Tracé_42186" data-name="Tracé 42186" d="M3448.19,374.433c1.676-1.676,3.463-1.534,4.611-.386a2.84,2.84,0,0,1,.386,3.656l4.671,1.178-1.381,1.381-4.448-1.2-.884.884,2.823,2.823-1.157,1.158-7.058-7.058Zm.945.944-1.28,1.28,2.366,2.366,1.28-1.28a1.612,1.612,0,0,0,.112-2.509A1.577,1.577,0,0,0,3449.135,375.377Z" transform="translate(-3445.753 -302.422)" fill="#fff"/>
              <path id="Tracé_42187" data-name="Tracé 42187" d="M3497.694,355.28a3.84,3.84,0,0,1-5.687-.1,3.79,3.79,0,0,1-.091-5.677,3.691,3.691,0,0,1,5.474.031,5.016,5.016,0,0,1,.528.609l-4.276,4.276a2.177,2.177,0,0,0,3.077-.112,1.916,1.916,0,0,0,.538-2.1l1.249-1.249A3.615,3.615,0,0,1,3497.694,355.28Zm-4.977-1.808,3.1-3.1a2.055,2.055,0,0,0-2.976.152A2.155,2.155,0,0,0,3492.718,353.472Z" transform="translate(-3481.72 -282.507)" fill="#fff"/>
              <path id="Tracé_42188" data-name="Tracé 42188" d="M3523.262,318.2a3.443,3.443,0,0,1,4.438-.721l-1.249,1.249a1.85,1.85,0,0,0-2.214.447c-.934.934-.863,2.244.355,3.463s2.539,1.3,3.473.366a1.807,1.807,0,0,0,.447-2.214l1.249-1.249a3.555,3.555,0,0,1-.721,4.438,4.092,4.092,0,0,1-5.779-5.779Z" transform="translate(-3506.854 -257.423)" fill="#fff"/>
              <path id="Tracé_42189" data-name="Tracé 42189" d="M3559.945,292.827a3.858,3.858,0,0,1-5.7-.091,4.036,4.036,0,1,1,5.708-5.707A3.964,3.964,0,0,1,3559.945,292.827Zm-1.006-1.005a2.437,2.437,0,0,0-.173-3.605,2.394,2.394,0,0,0-3.564-.193,2.357,2.357,0,0,0,.223,3.534C3556.7,292.827,3558.066,292.7,3558.939,291.822Z" transform="translate(-3531.59 -232.436)" fill="#fff"/>
              <path id="Tracé_42190" data-name="Tracé 42190" d="M3590.1,235.218a2,2,0,1,0-2.813,2.813l3.128,3.128-1.147,1.148-3.128-3.128a2,2,0,1,0-2.813,2.813l3.128,3.128-1.158,1.158-5.6-5.6,1.158-1.158.64.64a3.012,3.012,0,0,1,.924-2.387,3.052,3.052,0,0,1,3.118-.9,3.244,3.244,0,0,1,5.535-2.976l3.3,3.3-1.147,1.148Z" transform="translate(-3552.984 -190.025)" fill="#fff"/>
              <path id="Tracé_42191" data-name="Tracé 42191" d="M3643.008,182.308a2,2,0,1,0-2.813,2.813l3.127,3.128-1.147,1.148-3.128-3.128a2,2,0,1,0-2.813,2.813l3.128,3.128-1.158,1.158-5.6-5.6,1.158-1.158.64.64a3.014,3.014,0,0,1,.925-2.387,3.052,3.052,0,0,1,3.118-.9,3.244,3.244,0,0,1,5.535-2.976l3.3,3.3-1.148,1.148Z" transform="translate(-3595.34 -147.668)" fill="#fff"/>
              <path id="Tracé_42192" data-name="Tracé 42192" d="M3691.991,142.716a3.369,3.369,0,0,1,2.844-1.036l-.812-.812,1.168-1.168,5.6,5.6-1.168,1.168-.833-.833a3.408,3.408,0,0,1-1.036,2.884,3.826,3.826,0,0,1-5.535-.295A3.767,3.767,0,0,1,3691.991,142.716Zm1.249.762a2.428,2.428,0,0,0,.163,3.555,2.493,2.493,0,0,0,3.6.213,2.679,2.679,0,0,0-3.768-3.768Z" transform="translate(-3642.007 -115.511)" fill="#fff"/>
              <path id="Tracé_42193" data-name="Tracé 42193" d="M3726.468,114.727a2,2,0,1,0-2.813,2.813l3.128,3.128-1.158,1.158-5.6-5.6,1.158-1.158.64.64a3.045,3.045,0,0,1,.935-2.4,3.082,3.082,0,0,1,4.682.092l3.3,3.3-1.147,1.148Z" transform="translate(-3665.324 -93.562)" fill="#fff"/>
              <path id="Tracé_42194" data-name="Tracé 42194" d="M3759.556,67.451a3.645,3.645,0,0,1,2.8-1.056l-2.7-2.7,1.168-1.168,7.515,7.515-1.168,1.168-.843-.843a3.282,3.282,0,0,1-1.005,2.874,3.831,3.831,0,0,1-5.556-.274A3.769,3.769,0,0,1,3759.556,67.451Zm1.239.772a2.428,2.428,0,0,0,.163,3.554,2.492,2.492,0,0,0,3.6.213,2.679,2.679,0,0,0-3.768-3.768Z" transform="translate(-3696.089 -53.728)" fill="#fff"/>
              <path id="Tracé_42195" data-name="Tracé 42195" d="M3800.03,52.943a3.839,3.839,0,0,1-5.687-.1,3.789,3.789,0,0,1-.091-5.677,3.69,3.69,0,0,1,5.473.031,5.01,5.01,0,0,1,.529.609l-4.276,4.276a2.177,2.177,0,0,0,3.078-.112,1.916,1.916,0,0,0,.538-2.1l1.249-1.249A3.615,3.615,0,0,1,3800.03,52.943Zm-4.976-1.808,3.1-3.1a2.055,2.055,0,0,0-2.975.152A2.155,2.155,0,0,0,3795.054,51.135Z" transform="translate(-3723.755 -40.471)" fill="#fff"/>
              <path id="Tracé_42196" data-name="Tracé 42196" d="M3825.771,25.783l-1.158,1.158-5.6-5.6,1.158-1.158.813.812a2.577,2.577,0,0,1,.771-2.579l1.2,1.2-.294.295c-.853.853-1.026,1.737.163,2.925Z" transform="translate(-3744.569 -18.42)" fill="#fff"/>
            </g>
          </g>
        </svg>
      `,
    };
  },
  computed: {
    status() {
      return this.is_active ? "annuel" : "mensuel";
    },
  },
  methods: {
    pointToComma(val) {
      return val.toString().replace(".", ",");
    },
  },
};
</script>

<style scoped>
.abonnement-item {
  border: 1px solid var(--line);
  box-shadow: 0px 2px 4px #14141414;
  width: 100%;
  max-width: 241px;
}
.abonnement-item.abonnement-active .content-wrapper {
  position: relative;
}
.abonnement-item.abonnement-active .content-wrapper:before {
  background: rgba(255, 255, 255, 0.9);
  content: "Abonnement actif";
  display: flex;
  font-size: 16px;
  font-weight: 700;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 6;
}
.abonnement-item .iconRecommande {
  z-index: 2;
  top: -5px;
  left: -5px;
}
.abonnement-item .badge {
  color: var(--primary);
  border: 1px solid var(--primary);
  border-radius: 16px;
  font-size: 10px;
  letter-spacing: 1.5px;
  line-height: 16px;
  margin: 12px;
  right: 0;
  top: 0;
  z-index: 2;
}
.abonnement-item .md-subhead {
  color: var(--placeholder);
  letter-spacing: 0.25px;
  font-size: 14px;
  line-height: 20px;
}
.abonnement-item .md-title {
  color: var(--line);
  font-family: "Poppins-Bold", Arial, Helvetica, sans-serif;
  font-size: 24px;
  letter-spacing: 0.18px;
  line-height: 24px;
}
.abonnement-item .discount {
  letter-spacing: 0px;
  font-size: 22px;
  line-height: 33px;
}
.abonnement-item .discount span.color-primary {
  font-size: 14px;
  color: var(--primary);
}
.abonnement-item .card {
  border-radius: 12px 12px 0 0;
  padding-top: 35px;
  padding-bottom: 18.75px;
  background-color: #000;
}
.abonnement-item .content-wrapper {
  padding-left: 22px;
  padding-right: 22px;
  /* padding-left: 32px;
    padding-right: 32px; */
}
@media (max-width: 639px) {
  .abonnement-item .content-wrapper {
    padding-left: 10px;
    padding-right: 10px;
  }
}
.abonnement-item .children-wrapper > div {
  line-height: 1.4;
  text-align: left;
}
.abonnement-item .price-wrapper .price {
  font-size: 40px;
  line-height: 38px;
}
@media (max-width: 479px) {
  .abonnement-item .price-wrapper .price {
    font-size: 30px;
    line-height: 28px;
  }
}
.abonnement-item .btn-submit {
  font-size: 12px;
  line-height: 16px;
  border-radius: 16px;
  height: 32px;
  font-family: "Poppins-Regular", Arial, Helvetica, sans-serif;
}
</style>
