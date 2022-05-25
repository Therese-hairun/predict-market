import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadCouples: async ({ commit }, { token, order, page, search, size }) => {
    const response = await axios.get(
      `${API_URL}/api/couples?search=${search}&ordering=${order}&page=${page}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setCouples", response.data);
  },

  displayGraphData: async ({ commit }, { symbol, interval, token }) => {
    const response = await axios.get(
      `${API_URL}/api/couple_data/${symbol}?interval=${interval}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setGraphData", response.data);
  },

  displayGraphPrediction: async ({ commit }, { symbol, interval, token }) => {
    const response = await axios.get(
      `${API_URL}/api/prediction/${symbol}?interval=${interval}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setGraphPrediction", response.data);
  },

  getACouple: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/add_couple_visualisation`,
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

  addFavorite: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/create_favorite_couple`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  deleteFavorite: async (context, { token, symbol }) => {
    await axios.delete(`${API_URL}/api/delete_favorite_couple/${symbol}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },

  countViewCouple: async (context, { symbol, token }) => {
    await axios.post(
      `${API_URL}/api/visualize/${symbol}`,
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  removeCouple: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/remove_couple_visualisation`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  requestCouple: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/create_demande_couple`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  finalizeRequest: async (context, { symbol1, symbol2, token }) => {
    await axios.post(
      `${API_URL}/api/validate_demand/${symbol1}/${symbol2}`,
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },
};
