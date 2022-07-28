<template>
  <div id="app" class="bg-app">
    <div
      v-if="loading"
      class="mx-auto center justify-content-center"
      style="color: #f7912b"
    >
      <b-row>
        <b-col cols="12">
          <div>
            <h1
              class="d-flex justify-content-center text-dancing"
              style="margin-bottom: 1.8rem"
            >
              <span style="color: #f7912b; font-size: 2.8rem;!important"
                ><strong>Healthy</strong></span
              >&nbsp;
              <span style="color: #f7912b; font-size: 2.8rem;!important"
                ><strong>Fruits</strong></span
              >
            </h1>
          </div> </b-col
        ><b-col cols="12">
          <div class="d-flex justify-content-center">
            <b-spinner label="Spinning"></b-spinner>&nbsp;
            <h5 class="mt-1 ml-2 align-middle">Cargando...</h5>
          </div>
        </b-col>
      </b-row>
    </div>

    <transition name="transition-t" mode="out-in">
      <router-view :show_loading_app="show_loading_app" />
    </transition>
  </div>
</template>
<script>
export default {
  data() {
    return {
      loading: true,
    };
  },
  methods: {
    show_loading_app(value) {
      this.loading = value;
    },
  },
  created() {},
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap");

@import url("https://fonts.googleapis.com/css2?family=Barlow&display=swap");

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

#main-home {
  min-height: 100vh;
}
.no-bg-color {
  background: transparent !important;
}
.center {
  height: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  margin: 0;
  overflow-x: hidden;
  overflow-y: hidden;

  min-height: 100%;
}
.center-home {
  height: 100%;
  min-height: 100vh;
  height: 100vh;
  display: flex;
  align-items: center;
  margin: 0;
  overflow-x: hidden;
  overflow-y: hidden;

  min-height: 100%;
}
.center-side-bar {
  height: 100%;
  min-height: calc(100vh - 4rem);
  height: calc(100vh - 4rem);
  display: flex;
  align-items: center;
  margin: 0;
  overflow-x: hidden;
  overflow-y: hidden;

  min-height: 100%;
}
.btn-none:focus {
  box-shadow: 0 0 0 0.2rem rgb(0 123 255 / 0%) !important;
}

.fade-enter-active {
  transition: opacity 0.4s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.text-dancing {
  font-family: "Dancing Script", cursive !important;
}
.text-barlow {
  font-family: "Barlow", sans-serif !important;
}
.a-mod {
  color: #f7912b !important;
}
.a-mod:hover {
  color: rgb(211, 129, 47) !important;
}

#app .btn-primary,
.modal-footer .btn-primary {
  color: #fff;
  background-color: #f7912b;
  border-color: #f7912b;
}
#app .btn-primary:hover,
.btn-primary:active,
.modal-footer .btn-primary:hover,
.modal-footer .btn-primary:active {
  color: #fff;
  background-color: #c2701f !important;
  border-color: #c2701f !important;
}
#app .btn-primary:focus,
.modal-footer .btn-primary:focus {
  background-color: #c2701f !important;
  border-color: #c2701f !important;
  box-shadow: 0 0 0 0.2rem #c2711f42;
}

#app .btn-info,
.modal-footer .btn-info {
  color: #fff;
  background-color: #2b91f7;
  border-color: #2b91f7;
}
#app .btn-info:hover,
.btn-info:active,
.modal-footer .btn-info:hover,
.modal-footer .btn-info:active {
  color: #fff;
  background-color: #2373c2 !important;
  border-color: #2373c2 !important;
}
#app .btn-info:focus,
.modal-footer .btn-info:focus {
  background-color: #2373c2 !important;
  border-color: #2373c2 !important;
  box-shadow: 0 0 0 0.2rem #2372c22a;
}

.bg-app {
  /*background-color: rgba(255, 81, 0, 0.2);*/
  background: url("../public/bg_3.jpg") no-repeat center center fixed;
  background-size: cover;
}
#app .form-control,
.modal .form-control {
  border-radius: 1.1rem;
  background-clip: border-box;
}
#app .custom-select,
.modal .custom-select {
  border-radius: 1.1rem !important;
}
#app .card {
  border-radius: 10px;
  box-shadow: 0px 0px 15px 6px rgba(0, 0, 0, 0.082);
  border: none;
  overflow: hidden;
}
.modal .modal-content,
.swal-modal {
  border-radius: 15px !important;
}
#app .login-card {
  border-radius: 25px;
  background: rgba(0, 0, 0, 0.6);
  color: #fffffff5 !important;
}
#app .title-page-link {
  text-decoration: none;
}
#app .title-page {
  -webkit-transition: all 0.9s ease; /* Safari y Chrome */
  -moz-transition: all 0.9s ease; /* Firefox */
  -o-transition: all 0.9s ease; /* IE 9 */
  -ms-transition: all 0.9s ease; /* Opera */
  transition: all 0.9s ease;
}
#app .title-page:hover {
  -webkit-transform: scale(1.05);
  -moz-transform: scale(1.05);
  -ms-transform: scale(1.05);
  -o-transform: scale(1.05);
  transform: scale(1.05) !important;
}
.swal-button--confirm {
  color: #fff;
  background-color: #2b91f7;
  border-color: #2b91f7;
  border-radius: 50rem;
}
.swal-button--confirm:hover,
.swal-button--confirm:active {
  background-color: #2373c2 !important;
  border-color: #2373c2 !important;
  box-shadow: 0 0 0 0.2rem #2372c22a;
}
/*--------------------------------------------------Transitions------------------------------------*/
/* Transition in navbarhome y autentication */
.slide-fade-enter-active {
  transition: all 0.5s ease;
}
.slide-fade-leave-active {
  transition: all 0.5s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(50vh);
  opacity: 0;
}

/* Transition in app */
.transition-t-enter-active {
  transition: all 0.5s ease;
}
.transition-t-leave-active {
  transition: all 0.5s cubic-bezier(1, 0.5, 0.8, 1);
}
.transition-t-enter, .transition-t-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateX(50vh);
}

/* Transition in navbarhome */
.transition-a-enter-active {
  transition: all 0.5s ease;
}
.transition-a-leave-active {
  transition: all 0.5s cubic-bezier(1, 0.5, 0.8, 1);
}
.transition-a-enter, .transition-a-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateY(50vh);
  opacity: 0;
}
</style>
