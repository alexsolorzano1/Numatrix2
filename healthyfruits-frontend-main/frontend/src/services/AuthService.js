import store from "../store";
import axios from 'axios';

const url = process.env.VUE_APP_RUTA_API;

export default {
    //metodo para obtener token de un usuario enviando sus credenciales (correo,contraseña)
    async obtain_token (credentials) {
        const response = await axios
            .post(url + 'user/active/', credentials);
        store.commit("SET_ID", response.data.id);
        
        return response.data;
    },
    //metodo para extender el tiempo de vida de un token
    async refresh_token (token) {
        const response = await axios
            .post(url + 'user/refresh_token/', token);
        return response.data;
    },
    //metodo para registrar un usuario enviando sus credenciales(correo,contraseña)
    async register (credentials) {
        console.log(credentials);
        console.log(url);
        const response = 
        await axios
            .post(url + 'user/register/', credentials).then((response) => {
                console.log(response);
              }, (error) => {
                console.log(error);
              });
        //return response.data;
        return response;
    }
    ,
    //metodo para obtener todos los datos de un usuario logueado
    async getUser() {
        const response = await axios.get(url + 'user/profile/'+store.getters.getId+"/");
        return response.data;
    },

};