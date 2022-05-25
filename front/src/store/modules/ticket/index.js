import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const ticketStore = {
  state: {
    tickets: [],
    ticketAdmin: {},
  },
  getters,
  mutations,
  actions,
};

export default ticketStore;
