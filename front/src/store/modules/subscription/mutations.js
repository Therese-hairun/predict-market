export const mutations = {
  setSubscriptions: (state, subscriptions) => {
    state.subscriptions = subscriptions;
  },
  setUpgrade: (state, upgradeSubscriptions) => {
    state.upgradeSubscriptions = upgradeSubscriptions;
  },
  setListSubscriptions: (state, listSubscriptions) => {
    state.listSubscriptions = listSubscriptions;
  },
  setSubscriptionId: (state, subscriptionId) => {
    state.subscriptionId = subscriptionId;
  },
  getUserSubscription: (state, userSubscription) => {
    state.userSubscription = userSubscription;
  },
};
