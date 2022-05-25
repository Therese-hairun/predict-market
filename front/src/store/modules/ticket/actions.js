import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadTickets: async (
    { commit },
    { token, order, page, search, size, show_all }
  ) => {
    const response = await axios.get(
      `${API_URL}/api/tickets_list?ordering=${order}&page=${page}&search=${search}&size=${size}&show_all=${show_all}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setTickets", response.data);
  },

  loadUserTickets: async ({ commit }, { token, order, page, search, size }) => {
    const response = await axios.get(
      `${API_URL}/api/tickets?ordering=${order}&page=${page}&search=${search}&size=${size}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("setTickets", response.data);
  },

  createTicket: async (context, { payload, token }) => {
    await axios.post(
      `${API_URL}/api/create_ticket`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateStatusTicket: async (context, { id, payload, token }) => {
    await axios.patch(
      `${API_URL}/api/update_ticket_status/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updateStatusTicketAdmin: async (context, { id, payload, token }) => {
    await axios.patch(
      `${API_URL}/api/update_admin_ticket_status/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  getTicketById: async ({ commit }, { id, token }) => {
    const response = await axios.get(`${API_URL}/api/ticket/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setTickets", response.data);
  },

  getTicketByIdAdmin: async ({ commit }, { id, token }) => {
    const response = await axios.get(`${API_URL}/api/admin_ticket/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setTicketAdmin", response.data);
  },

  sendMessage: async (context, { id, payload, token }) => {
    await axios.post(
      `${API_URL}/api/create_ticket_message/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  sendMessageAdmin: async (context, { id, payload, token }) => {
    await axios.post(
      `${API_URL}/api/create_admin_ticket_message/${id}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },
};
