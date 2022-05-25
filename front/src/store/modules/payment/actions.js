import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  paymentCommand: async (context, { token, payload }) => {
    await axios.post(`${API_URL}/api/payement`, payload, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },

  prorata: async ({ commit }, { token, payload }) => {
    const response = await axios.post(`${API_URL}/api/prorata`, payload, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setProrata", response.data);
  },
};
