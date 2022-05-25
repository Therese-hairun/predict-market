import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const coupleStore = {
  state: {
    couples: [],
    graphData: [],
    graphPrediction: [],
  },
  getters,
  mutations,
  actions,
};

export default coupleStore;
