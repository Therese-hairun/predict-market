import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const adminStore = {
  state: {
    admins: [],
  },
  getters,
  mutations,
  actions,
};

export default adminStore;
