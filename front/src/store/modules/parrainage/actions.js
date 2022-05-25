import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadAffiliated: async ({ commit }, { code, order, token, page, size }) => {
    const response = await axios.get(
      `${API_URL}/api/client_filleul/${code}?ordering=${order}&page=${page}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setParrainages", response.data);
  },
};
