import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const clientStore = {
  state: {
    clients: [],
  },
  getters,
  mutations,
  actions,
};

export default clientStore;
