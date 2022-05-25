import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const paireStore = {
  state: {
    paires: [],
    assets: null,
    requests: {},
    coupleId: {},
    coupleIdUser: {},
    updateCouple: null,
  },
  getters,
  mutations,
  actions,
};

export default paireStore;
