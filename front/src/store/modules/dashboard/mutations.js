export const mutations = {
  setFavoriteCouples: (state, couplesDashboard) => {
    state.couplesDashboard = couplesDashboard;
  },
  setMyCouples: (state, userCouple) => {
    state.userCouple = userCouple;
  },
  setTrendingCouples: (state, trendingCouple) => {
    state.trendingCouple = trendingCouple;
  },
  setExplosiveCouples: (state, explosiveCouple) => {
    state.explosiveCouple = explosiveCouple;
  },
};
