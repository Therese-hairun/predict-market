import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const paymentStore = {
  state: {
    payments: [],
  },
  getters,
  mutations,
  actions,
};

export default paymentStore;
