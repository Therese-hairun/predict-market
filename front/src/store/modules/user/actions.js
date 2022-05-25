import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadUsers: async ({ commit }, { order, page, search, size, token }) => {
    const response = await axios.get(
      `${API_URL}/api/user_list?ordering=${order}&page=${page}&search=${search}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setUsers", response.data);
  },

  getUserCouples: async ({ commit }, { id, token }) => {
    const response = await axios.get(`${API_URL}/api/couple_client/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setUserCouples", response.data);
  },

  loadUserById: async ({ commit }, { id, token }) => {
    const response = await axios.get(`${API_URL}/api/user_list/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setUserList", response.data);
  },

  updateUserStatus: async (context, { id, payload, token }) => {
    await axios.put(
      `${API_URL}/api/account_status/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateSubscriptionUser: async (context, { id, payload, token }) => {
    await axios.patch(
      `${API_URL}/api/update_client_subscribe/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateRenewStatus: async (context, { token, payload }) => {
    await axios.patch(
      `${API_URL}/api/update_renew_status`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateCredit: async (context, { id, payload, token }) => {
    await axios.patch(`${API_URL}/api/updateClient_credit/${id}`, payload, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },

  updateFreeDay: async (context, { id, payload, token }) => {
    await axios.patch(
      `${API_URL}/api/updateClient_free_day/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  addDays: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/add_days`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  addCredits: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/add_credits`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },
};
