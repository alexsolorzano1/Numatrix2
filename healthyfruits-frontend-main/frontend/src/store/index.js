import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

//Variables que se usaran para hacer persistentes en el sistema usando el vuex-store
const getDefaultState = () => {
  return {
    idUser: "",
    token: "",
    id: '',
  };
};

//Aca se manejan el state (que son las variables que declare arriba para que se hagan persistente)
//luego usamos getters que son metodos para obtener las variables declaradas
//el mutations donde se llenan datos en las variables
//actiones donde se llama al mutatios a ejecutar desde codigo mismo
export default new Vuex.Store({
  state: getDefaultState(),
  getters: {
    isLoggedIn: (state) => {
      return state.token;
    },
    getId: state => {
      return state.id;
    },
    getIdUser: (state) => {
      return state.idUser;
    },
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token;
    },
    SET_ID: (state, id) => {
      state.id = id;
    },
    SET_IDUSER: (state, idUser) => {
      state.idUser = idUser;
    },
    RESET: (state) => {
      Object.assign(state, getDefaultState());
    },
  },
  actions: {
    userId: ({ commit }, { id }) => {
      commit('SET_ID', id);
    },
    IdUser: ({ commit }, { idUser }) => {
      commit("SET_IDUSER", idUser);
    },
    login: ({ commit }, { token }) => {
      commit("SET_TOKEN", token);
    },
    logout: ({ commit }) => {
      commit("RESET", "");
    },
  },
  plugins: [createPersistedState()],
});
