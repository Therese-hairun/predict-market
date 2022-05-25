export const mutations = {
  setPaires: (state, paires) => {
    state.paires = paires;
  },
  setRequested: (state, requests) => {
    state.requests = requests;
  },
  setAssets: (state, assets) => {
    state.assets = assets;
  },
  setCoupleId: (state, coupleId) => {
    state.coupleId = coupleId;
  },
  setCoupleIdUser: (state, coupleIdUser) => {
    state.coupleIdUser = coupleIdUser;
  },
  setUpdate: (state, updateCouple) => {
    state.updateCouple = updateCouple;
  },
};
