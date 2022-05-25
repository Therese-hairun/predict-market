import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadAdmin: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/admin`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setAdmins", response.data);
  },
};
