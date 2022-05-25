import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const coupleDashboardStore = {
  state: {
    couplesDashboard: [],
    userCouple: [],
  },
  getters,
  mutations,
  actions,
};

export default coupleDashboardStore;
