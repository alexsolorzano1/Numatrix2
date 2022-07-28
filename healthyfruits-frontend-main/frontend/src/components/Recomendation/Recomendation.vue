<template>
  <div>
    <b-card body-class="m-3">
      <b-row>
        <b-col>
          <h4>Recomendacion de alimentos</h4>

          <p>Seleccione un alimento para proporcionarle una recomendación</p>
        </b-col>
        <b-col cols="auto" v-if="is_recomendation == true">
          <b-button pill variant="info" @click="back()">
            <b-icon icon="arrow-left"  class="align-middle"></b-icon>
            Regresar
          </b-button>
        </b-col>
      </b-row>
      <div>
        <b-input-group class="mb-4">
          <b-form-input
            id="filter-input"
            v-model="filter"
            type="search"
            placeholder="Escribe lo que necesites"
            class="item-left"
          ></b-form-input>

          <b-input-group-append>
            <b-button
              variant="info"
              v-on:click="filterRecomendation"
              class="item-right"
              ><b-icon icon="search" pill></b-icon> Buscar</b-button
            >
          </b-input-group-append>
        </b-input-group>
        <FoodList
          :food_list="recomendation_list"
          :count="count"
          :page="page"
          :next="next"
          :previus="previus"
          :showOptions="true"
          :getRecomentation="getRecomentation"
          :loading="loadingFood"
          :paginationFoodList="paginationFoodList"
          :is_recomendation="is_recomendation"
        >
        </FoodList>
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
const url = process.env.VUE_APP_RUTA_API;
import FoodList from "@/components/Recomendation/FoodList";
export default {
  components: {
    FoodList,
  },

  data() {
    return {
      is_recomendation: false,
      loadingFood: false,
      recomendation_list: [],
      count: "",
      next: "",
      page: "1",
      previus: "",
      filter: "",
    };
  },
  methods: {
    async getData() {
      this.loadingFood = true;
      const path = url + `recomendation/npl/listData`;
      await axios
        .get(path)
        .then((response) => {
          this.count = response.data.count;
          this.next = response.data.next;
          this.previus = response.data.previous;
          this.recomendation_list = response.data.results;
          this.getIngredient();
          this.loadingFood = false;
        })
        .catch((error) => {
          console.log(error);
          this.loadingFood = false;
        });
    },
    paginationFoodList(number) {
      this.loadingFood = true;
      var path = url + "recomendation/npl/listData?page=" + number;
      axios
        .get(path)
        .then((response) => {
          this.count = response.data.count;
          this.next = response.data.next;
          this.previus = response.data.previous;
          this.recomendation_list = response.data.results;
          this.getIngredient();
          this.getDataNutritional();
          this.loadingFood = false;
        })
        .catch((error) => {
          console.log(error);
          this.loadingFood = false;
        });
    },
    getIngredient() {
      this.recomendation_list.forEach((Element) => {
        var myArray = Element.ingredients.split("^");
        Element.finingredients = myArray;
      });
      //var myArray = data.split("^");
    },
    getIngredient2() {
      this.recomendation_list.forEach((Element) => {
        var myArray = Element.ingredientes.split("^");
        Element.finingredients = myArray;
      });
      //var myArray = data.split("^");
    },
    getDataNutritional() {
      this.recomendation_list.forEach((Element) => {
        Element.finnutrition = JSON.parse(Element.nutrition.toLowerCase());
      });
    },
    getRecomentation(value) {
      if (value == null) return;
      
      var formData = new FormData();
      formData.append("id_recipe", value);
      formData.append("id_user", this.$store.getters.getId);
      this.loadingFood = true;
      console.log(value);

      var path = url + "recomendation/npl/";
      axios
        .post(path, formData)
        .then((response) => {
          this.recomendation_list = response.data.recomendation_food;
          this.updateData();
          this.getIngredient2();
          this.getDataNutritional();
          setTimeout(() => {
            this.loadingFood = false;
            this.is_recomendation = true;
          }, 10000);
        })
        .catch(() => {
          console.log("error");
          setTimeout(() => {
            this.loadingFood = false;
            this.is_recomendation = true;
          }, 10000);
        });

      this.$bvToast.toast(
        "Espere un momento, se estan buscando recomendaciones relacionadas con el alimento que selecciono",
        {
          title: "Healthy Fruits",

          variant: "primary",
          solid: true,
        }
      );
    },
    updateData() {
      this.recomendation_list.forEach((element) => {
        console.log(element.name_food);
        element.recipe_name = element.name_food;
      });
    },
    filterRecomendation() {
      if (this.filter != "") {
        console.log("consulta a back");
      } else {
        this.$bvToast.toast("Por favor ingrese un alimento", {
          title: "Healthy Fruits",

          variant: "warning",
          solid: true,
        });
      }
    },
    back() {
      this.is_recomendation = false;
      this.getData();
    },
  },
  async created() {
    await this.getData();
  },
};
</script>
<style scoped>
.item-right {
  border-top-right-radius: 1.1rem;
  border-bottom-right-radius: 1.1rem;
}
.item-left {
  border-top-right-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}
</style>
