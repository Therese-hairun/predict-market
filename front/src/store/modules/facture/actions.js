import axios from "axios";
import { API_URL } from "../../../utils/Constant";
export const actions = {
  loadFactures: async ({ commit }, { token, order, search, page, size }) => {
    const response = await axios.get(
      `${API_URL}/api/invoice?search=${search}&ordering=${order}&page=${page}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setFactures", response.data);
  },
};
