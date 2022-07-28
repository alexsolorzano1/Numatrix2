<template >
  <div class="portada" v-if="!loading">
    <transition name="slide-fade" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<script>
export default {
  props: ["show_loading_app"],
  data() {
    return {
      loading: true,
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
    },
  },
  created() {
    this.show_loading_app(true);
    //this.$router.push("/login");

    if (this.$store.getters.isLoggedIn) {
      this.$router.push("/username");
    } else {
      this.show_loading_app(false);
      this.loading = false;
      this.logout();
    }
  },
};
</script>
<style>
.portada {
  overflow-x: hidden;
  background: url("../../../public/fondo2.jpg") no-repeat center center fixed;
  min-height: 100%;

  /* Propiedad a utilizar para la imagen */
  background-size: cover;
}
</style>