import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

export const subscriptionStore = {
  state: {
    subscriptions: [],
    subscriptionId: {},
    userSubscription: null,
    listSubscriptions: [],
    upgradeSubscriptions: [],
  },
  getters,
  mutations,
  actions,
};

export default subscriptionStore;
