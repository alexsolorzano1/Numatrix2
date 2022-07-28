<template>
  <div>
    <div class="masonry">
      <b-card
        no-body
        v-for="item in food_list"
        :key="item.id"
        class="my-2 item"
        style="border-radius: 10px; max-heigth: 100px !important; width: 100%"
      >
        <b-row no-gutters>
          <b-col md="6" style=" overflow:hidden">
            <div class="background-image" :style="imagenDir(item.image)"></div>
            <div class="content">
              <b-card-img
                :src="item.image"
                alt="Image"
                class="rounded-0"
                style="min-width: 100%"
              ></b-card-img>
            </div>
          </b-col>
          <b-col md="6">
            <b-card-body>
              <b-card-text>
                <p class="text-center my-0">{{ item.name }}</p>
                <hr class="my-2" />
                <p class="">Calorias: 20cal</p>
              </b-card-text>
              <div v-if="showOptions">
              <b-button pill variant="info" size="sm" block @click="likeFood('primary')">
                <b-icon icon="check2" class="align-middle"></b-icon> Me gusta
              </b-button>
              <b-button pill variant="danger" size="sm" block @click="dislikeFood('danger')">
                <b-icon icon="x" scale="1.2" class="align-middle"></b-icon>
                No me gusta
              </b-button>
              </div>
              
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>
  </div>
</template>
<script>
export default {
  props: ["food_list", "showOptions"],
  data() {
    return {
    }
  },
  methods: {
    imagenDir(img) {
      return "background: url('" + img + "') no-repeat center center; background-size: cover;";
    },
    likeFood(variant = null){
      this.$bvToast.toast('Gracias por tu opinión, trataremos de recomendarte mas este alimento en los proximos dias', {
          title: "Healthy Fruits",
          
          variant: variant,
          solid: true
        })
    },
    dislikeFood(variant = null){
      this.$bvToast.toast('Gracias por tu opinión, trataremos de recomendarte menos este alimento en los procimos dias', {
          title: "Healthy Fruits",
         
          variant: variant,
          solid: true
        })
    }

  },
}
</script>
<style scoped>
.masonry {
  /* Masonry container */
  -webkit-column-count: 2;
  -moz-column-count: 2;
  column-count: 2;
  column-gap: 1.5em;
}
.item {
  display: inline-block;
  border: 1px solid rgb(228, 228, 228) !important;
  box-shadow: 0px 0px 0px 0px !important;
}
.background-image {
  position: relative;

  z-index: 1;
  display: block;

  height: 100%;

  filter: blur(5px);
  overflow: hidden;
}
.content {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  z-index: 5;
  width: 100%;
  display: flex;
  align-items: center;
}

@media only screen and (max-width: 767px) {
  .content {
  position: relative;
  z-index: 2;
  width: 100%;
  display: flex;
  align-items: center;
}
.background-image {
  display: none;
  z-index: 1;
  height: 0;
}
}
@media only screen and (max-width: 575px){
    .masonry {
  /* Masonry container */
  -webkit-column-count: 1;
  -moz-column-count: 1;
  column-count: 1;
  column-gap: 1.5em;
}
}
</style>
