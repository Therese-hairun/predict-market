import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadPaires: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/assets`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setListPaires", response.data);
  },
};
