import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadReductions: async ({ commit }, { order, page, search, size, token }) => {
    const response = await axios.get(
      `${API_URL}/api/reduction_code?ordering=${order}&page=${page}&search=${search}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setReductions", response.data);
  },

  deleteReduction: async (context, { id, token }) => {
    await axios.delete(`${API_URL}/api/delete_code/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },

  addReduction: async (context, { payload, token }) => {
    await axios.post(
      `${API_URL}/api/create_reduction_code`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateReduction: async (context, { id, payload, token }) => {
    await axios.patch(
      `${API_URL}/api/update_code/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  useReduction: async ({ commit }, { token, payload }) => {
    const response = await axios.post(
      `${API_URL}/api/use_reduction`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("getReductions", response.data);
  },
};
