import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
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

  checkDowngrade: async ({ commit }, { token }) => {
    const response = await axios.post(
      `${API_URL}/api/check_downgrade`,
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setDowngrade", response.data);
  },

  downgradeBackOffice: async (context, { token, payload }) => {
    await axios.post(
      `${API_URL}/api/remove_client_couple`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },
};
