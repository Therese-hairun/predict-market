import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const listPaireStore = {
  state: {
    listPaires: [],
  },
  getters,
  mutations,
  actions,
};

export default listPaireStore;
