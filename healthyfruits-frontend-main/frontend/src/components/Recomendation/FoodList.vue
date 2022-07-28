<template>
  <div>
    <div>
      <b-modal
        id="view-food-modal"
        ref="modal-food"
        :title="item_selected.recipe_name"
        scrollable
        cancel-title="Cancelar"
        content-class="p-1"
        size="lg"
      >
        <div v-if="item_selected.recipe_name">
          <div class="d-flex justify-content-center">
            <b-img
              :src="item_selected.image_url"
              alt="Image"
              class="rounded"
              style="max-height: 170px"
            >
            </b-img>
          </div>
          <b-row class="mt-3">
            <b-col>
              <p class="my-2">Ingredientes:</p>
              <hr class="my-2" />
              <ul class="pl-4">
                <li
                  v-for="(ingrediente, index) of item_selected.finingredients"
                  :key="index"
                >
                  {{ ingrediente }}
                </li>
              </ul>
            </b-col>
            <b-col>
              <p class="my-2">Informacion Nutricional:</p>
              <hr class="my-2" />
              <b-row v-for="(nutrition, index) of Object.keys(item_selected.finnutrition)" :key="index">
                <b-col>
                  {{item_selected.finnutrition[nutrition].name}}:
                </b-col>
                <b-col>
                  {{item_selected.finnutrition[nutrition].amont+" "+item_selected.finnutrition[nutrition].nit}}
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <template #modal-footer="{ cancel }">
          <b-button variant="danger" pill @click="cancel()" class="px-3">
            Cancelar
          </b-button>
        </template>
      </b-modal>
    </div>
    <div v-if="loading">
      <div class="mx-auto justify-content-center my-5" style="color: #f7912b">
        <b-row>
          <b-col cols="12"> </b-col
          ><b-col cols="12">
            <div class="d-flex justify-content-center">
              <b-spinner label="Spinning"></b-spinner>&nbsp;
              <h5 class="mt-1 ml-2 align-middle">Cargando...</h5>
            </div>
          </b-col>
        </b-row>
      </div>
    </div>
    <div v-if="!loading">
      <div class="masonry">
        <b-card
          v-show="3"
          no-body
          v-for="item in food_list"
          :key="item.id"
          class="my-2 item"
          style="border-radius: 10px; max-heigth: 100px !important; width: 100%"
        >
          <b-row no-gutters>
            <b-col md="6" style="overflow: hidden">
              <div
                class="background-image"
                :style="imagenDir(item.image_url)"
              ></div>
              <div class="content">
                <b-card-img
                  :src="item.image_url"
                  alt="Image"
                  class="rounded-0"
                  style="min-width: 100%"
                ></b-card-img>
              </div>
            </b-col>
            <b-col md="6">
              <b-card-body>
                <p class="text-center my-0">{{ item.recipe_name }}</p>
                <hr class="my-2" />
                <div v-if="showOptions">
                  <div class="div-scroll scrollbar-young-passion mt-2">
                    <p class="">Ingredientes:</p>
                    <ul class="pl-4">
                      <li
                        v-for="(ingrediente, index) of item.finingredients"
                        :key="index"
                      >
                        {{ ingrediente }}
                      </li>
                    </ul>
                  </div>
                  <div class="mt-3" v-if="is_recomendation==false">
                    <b-button
                      pill
                      variant="info"
                      size="sm"
                      block
                      @click="likeFood(item.id)"
                    >
                      <b-icon icon="check2" class="align-middle"></b-icon>
                      Seleccionar
                    </b-button>
                  </div>
                </div>
                <div v-else>
                  <div class="mt-3">
                    <b-button
                      pill
                      variant="info"
                      size="sm"
                      block
                      @click="viewFood(item)"
                    >
                      <b-icon
                        icon="plus"
                        scale="1.3"
                        class="align-middle"
                      ></b-icon>
                      Ver más
                    </b-button>
                  </div>
                  <b-button
                    class="mt-2"
                    pill
                    variant="danger"
                    size="sm"
                    block
                    @click="addHistory(item.recipe_name,item.finnutrition.calories)"
                  >
                    <b-icon icon="check2" class="align-middle"></b-icon>
                    Lo consumí
                  </b-button>
                </div>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
      </div>
      <b-pagination
      v-if="is_recomendation==false"
        class="mt-3"
        align="center"
        :total-rows="count"
        v-model="currentPage"
        :per-page="itemsPorPagina"
      ></b-pagination>
    </div>
  </div>
</template>
<script>
import axios from "axios";
const url = process.env.VUE_APP_RUTA_API;
export default {
  props: [
    "food_list",
    "count",
    "next",
    "previus",
    "page",
    "showOptions",
    "getRecomentation",
    "loading",
    "paginationFoodList",
    "is_recomendation"
  ],
  data() {
    return {
      paginaActual: 1,
      itemsPorPagina: 10,
      currentPage: 1,
      item_selected: {
        recipe_name: null,
      },
    };
  },
  watch: {
    currentPage: function () {
      this.paginationFoodList(this.currentPage);
    },
  },
  methods: {
    imagenDir(img) {
      return (
        "background: url('" +
        img +
        "') no-repeat center center; background-size: cover;"
      );
    },
    viewFood(item, button) {
      console.log(this.item_selected);
      this.$root.$emit("bv::show::modal", "view-food-modal", button);
      this.item_selected = item;
      
    },
    likeFood(value = null) {
      this.getRecomentation(value);
      console.log(value);
    },
    async addHistory(value = null,dataCalories) {
      var formData = new FormData();
      formData.append('id_foodmeal',value);
      formData.append('id_user',this.$store.getters.getId);
      formData.append('calories',(dataCalories.amont).toFixed(2));
      this.loadingFood = true;
      
      var path = url + "food/history_food/";
      await axios.post(path, formData);
      this.$bvToast.toast("Se añadio a tu historial alimenticio", {
        title: "Healthy Fruits",

        variant: "primary",
        solid: true,
      });
    },
  },
  created() {
    this.currentPage = this.page;
  },
};
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
.div-scroll {
  overflow-y: scroll;
  max-height: 25vh;
  padding-right: 10px;
  overflow-x: hidden;
}
.scrollbar-young-passion::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #f5f5f5;
  border-radius: 10px;
}
.scrollbar-young-passion::-webkit-scrollbar {
  width: 8px;
  background-color: rgba(0, 0, 0, 0);
}
.scrollbar-young-passion::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #f7912b;
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
@media only screen and (max-width: 575px) {
  .masonry {
    /* Masonry container */
    -webkit-column-count: 1;
    -moz-column-count: 1;
    column-count: 1;
    column-gap: 1.5em;
  }
}
</style>
