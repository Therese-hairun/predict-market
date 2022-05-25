import axios from "axios";
import { API_URL } from "../../../utils/Constant";

export const actions = {
  loadClients: async ({ commit }, { token }) => {
    const response = await axios.get(`${API_URL}/api/client`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    commit("setClients", response.data);
  },

  isPhoneUsed: async ({ commit }, { payload, token }) => {
    const response = await axios.post(
      `${API_URL}/api/phone_used`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("checkPhone", response.data);
  },

  verifyPassword: async ({ commit }, { token, payload }) => {
    const response = await axios.post(
      `${API_URL}/api/verify_password`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    commit("checkPassword", response.data);
  },

  updateClientInfo: async (context, { token, payload }) => {
    await axios.patch(
      `${API_URL}/api/update_client_infos`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  getSMS: async (context, { smsPayload }) => {
    await axios.post(`${API_URL}/api/sendSMS`, smsPayload);
  },

  updateClientPhone: async (context, { payload, token }) => {
    await axios.patch(
      `${API_URL}/api/update_phone`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  updatePassword: async (context, { token, payload }) => {
    await axios.patch(
      `${API_URL}/api/updatePassword`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },

  resendCode: async (context, { smsPayload }) => {
    await axios.post(`${API_URL}/api/sendSMS`, smsPayload);
  },

  uploadUserProfile: async (context, { image, token }) => {
    let formdata = new FormData();
    formdata.append("profil", image);
    await axios.post(`${API_URL}/api/upload_user_profil`, formdata, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },

  shareLinkedin: async (context, { payload, token, language }) => {
    await axios.post(
      `${API_URL}/api/share_linkedin?language=${language}`,
      { ...payload },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
  },
};
