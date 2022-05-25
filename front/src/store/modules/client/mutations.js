export const mutations = {
  setClients: (state, clients) => {
    state.clients = clients;
  },
  checkPhone: (state, phone) => {
    state.phone = phone;
  },
  checkPassword: (state, password) => {
    state.password = password;
  },
};
