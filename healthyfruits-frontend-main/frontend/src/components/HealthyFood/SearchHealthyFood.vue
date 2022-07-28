<template>
  <div>
    <b-card body-class="m-3">
      <h4>Busqueda de alimentos saludables</h4>

      <p class="mb-3">
        Busca entre diferentes alimentos y obten sus datos nutricionales.
      </p>
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
      <div v-if="!recomendation_list.length <= 0">
        <FoodList
          :food_list="recomendation_list"
          :showOptions="false"
          :loading="loadingFood"
          :count="count"
          :page="page"
          :next="next"
          :previus="previus"
          :paginationFoodList="paginationFoodList"
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
      const path = url + `recomendation/npl/listData`;
      await axios
        .get(path)
        .then((response) => {
          this.count = response.data.count;
          this.next = response.data.next;
          this.previus = response.data.previous;
          this.recomendation_list = response.data.results;
          this.getIngredient();
          this.getDataNutritional();
        })
        .catch((error) => {
          console.log(error);
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
    getDataNutritional(){
      console.log("entre");
      this.recomendation_list.forEach((Element) => {
        Element.finnutrition = JSON.parse(Element.nutrition.toLowerCase());
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