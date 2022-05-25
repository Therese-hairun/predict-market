import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  displayPaires: async ({ commit }, { token, order, page, search, size }) => {
    const response = await axios.get(
      `${API_URL}/api/couple?search=${search}&ordering=${order}&page=${page}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setPaires", response.data);
  },

  addPaire: async (
    { commit },
    { symbol_1, symbol_2, image1, image2, interval, token }
  ) => {
    let formdata = new FormData();
    formdata.append("symbol_1", symbol_1);
    formdata.append("symbol_2", symbol_2);
    formdata.append("intervals", interval);
    formdata.append("symbol_1_logo", image1);
    formdata.append("symbol_2_logo", image2);
    const response = await axios.post(
      `${API_URL}/api/create_couple`,
      formdata,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setAssets", response.data);
  },

  updatePaire: async (
    { commit },
    { symbol_1, symbol_2, image1, image2, interval, id, token }
  ) => {
    let formdata = new FormData();
    formdata.append("symbol_1", symbol_1);
    formdata.append("symbol_2", symbol_2);
    formdata.append("intervals", interval);
    formdata.append("symbol_1_logo", image1);
    formdata.append("symbol_2_logo", image2);
    const response = await axios.patch(
      `${API_URL}/api/updateCoupleInfo/${id}`,
      formdata,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setUpdate", response.data);
  },

  getCoupleBySymbol: async ({ commit }, { symbol, token }) => {
    const response = await axios.get(`${API_URL}/api/couple/${symbol}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setCoupleId", response.data);
  },

  getCoupleBySymbolUser: async ({ commit }, { symbol, token }) => {
    const response = await axios.get(`${API_URL}/api/couple_user/${symbol}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setCoupleIdUser", response.data);
  },

  updateStatusCouple: async (context, { id, payload, token }) => {
    await axios.put(
      `${API_URL}/api/updateCoupleStatus/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  requestedCouple: async ({ commit }, { token, order, page, search, size }) => {
    const response = await axios.get(
      `${API_URL}/api/get_all_couple_demand?search=${search}&ordering=${order}&page=${page}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setRequested", response.data);
  },
};
