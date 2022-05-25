import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const parrainageStore = {
  state: {
    parrainages: [],
  },
  getters,
  mutations,
  actions,
};

export default parrainageStore;
