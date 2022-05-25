import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadSubscriptions: async (
    { commit },
    { order, page, search, size, token }
  ) => {
    const response = await axios.get(
      `${API_URL}/api/subscribe?ordering=${order}&page=${page}&search=${search}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setSubscriptions", response.data);
  },

  upgradeListSubscription: async ({ commit }, { id, token }) => {
    const response = await axios.get(`${API_URL}/api/upgrade_subscribe/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setUpgrade", response.data);
  },

  listSubscriptions: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/subscribe`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setListSubscriptions", response.data);
  },

  addSubscription: async (context, { payload, token }) => {
    await axios.post(
      `${API_URL}/api/add_subscribe`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateSubscriptionStatus: async (context, { id, payloadUpdate, token }) => {
    await axios.put(
      `${API_URL}/api/updateSubscribeStatus/${id}`,
      { ...payloadUpdate },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateSubscription: async (context, { id, payloadUpdate, token }) => {
    await axios.patch(
      `${API_URL}/api/updateSubscribe/${id}`,
      { ...payloadUpdate },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  setRecommandedSubscription: async (context, { token, id, payload }) => {
    await axios.put(
      `${API_URL}/api/recommanded_subscribe/${id}`,
      {
        ...payload,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  getSubscriptionById: async ({ commit }, { id, token }) => {
    const response = await axios.get(`${API_URL}/api/subscribe/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setSubscriptionId", response.data);
  },

  getUserSubscription: async ({ commit }, { clientId, token }) => {
    const response = await axios.get(`${API_URL}/api/user_list/${clientId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("getUserSubscription", response.data);
  },
};
