export const getters = {
  paires: (state) => {
    return state.paires;
  },
  assets: (state) => {
    return state.assets || null;
  },
  coupleId: (state) => {
    return state.coupleId || null;
  },
  coupleIdUser: (state) => {
    return state.coupleIdUser;
  },
  updateCouple: (state) => {
    return state.updateCouple;
  },
};
