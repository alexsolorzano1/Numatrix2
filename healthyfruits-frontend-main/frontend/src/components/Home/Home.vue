<template>
  <div class="mx-auto center-home justify-content-center">
    <b-row align-h="center">
      <b-col
        style="color: white"
    
        xl="7"
        lg="8"
        md="9"
        sm="12"
        class="c-tra text-center text-barlow"
      >
        <h2>MEJORA TU SALUD</h2>
        <h4>
          Encuentar las mejores recomendaciones de alimentos registrandote en
          nuestra pagina
        </h4>
        <b-button
          pill
          size="lg"
          variant="primary"
          class="px-5 mt-3"
          :to="{ name: 'signin' }"
          >INICIAR
        </b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {};
  },
  components: {},
  methods: {},
  
};
</script>
<style scoped>
.c-tra {
  padding: 50px;
  border-radius: 50px;
  /*background: rgba(0, 0, 0, 0.2);*/
}
</style>>
