<template>
  <div class="mx-auto center-home justify-content-center">
    <b-row align-h="center">
      <b-col
        style="color: white"
        xl="8"
        lg="9"
        md="10"
        sm="12"
        class="c-tra text-center text-barlow"
      >
        <h2>Contactanos</h2>
        <hr class="bg-white mt-1 mb-2 w-75" />
        <h4>Puedes encontrarnos en los siguientes enlaces</h4>
        <h2 class="mt-4">
          <b-button
            size="lg"
            variant="primary"
            class="btn-circle mx-3"
            href="https://www.facebook.com/JoelBerseker"
            ><b-icon icon="facebook"></b-icon>
          </b-button>
          <b-button
            size="lg"
            variant="primary"
            class="btn-circle mx-3"
            :to="{ name: 'signin' }"
            ><b-icon class="" icon="envelope-fill"></b-icon>
          </b-button>
          <b-button
            size="lg"
            variant="primary"
            class="btn-circle mx-3"
            :to="{ name: 'signin' }"
            ><b-icon class="" icon="phone"></b-icon>
          </b-button>
        </h2>
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
.btn-circle {
  border-radius: 50% !important;
  width: 48px;
  padding-left: 8px;
  padding-right: 8px;
  text-align: center;
}
</style>>
