import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


Vue.config.productionTip = false

//Condcion para saber si existe un usuario logueado mediante su token
var token = store.state.token;
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
} else {
  axios.defaults.headers.common['Authorization'] = null;
}


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
