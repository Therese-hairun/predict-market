import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const factureStore = {
  state: {
    factures: [],
  },
  getters,
  mutations,
  actions,
};

export default factureStore;
