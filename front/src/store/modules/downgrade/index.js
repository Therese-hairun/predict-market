import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const downgradeStore = {
  state: {
    checkDowngrade: null,
  },
  getters,
  mutations,
  actions,
};

export default downgradeStore;
