import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const reductionStore = {
  state: {
    reductions: [],
    code: null,
  },
  getters,
  mutations,
  actions,
};

export default reductionStore;
