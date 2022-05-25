import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const userStore = {
  state: {
    users: [],
  },
  getters,
  mutations,
  actions,
};

export default userStore;
