import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  getFavoriteCouple: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/favorite_couple`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setFavoriteCouples", response.data);
  },

  getUserCouple: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/client_couple`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setMyCouples", response.data);
  },

  getTrendingCouple: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/moment_couple`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setTrendingCouples", response.data);
  },

  loadDataCouples: async (context, { token }) => {
    await axios.get(`${API_URL}/api/load_couple`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },

  getExplosiveCouple: async ({ commit }, { token }) => {
    const response = await axios.get(
      `${API_URL}/api/explosive_couple`,

      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setExplosiveCouples", response.data);
  },

  downgrade: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/remove_couple_downgrade`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },
};
