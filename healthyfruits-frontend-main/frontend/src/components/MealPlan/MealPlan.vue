<template>
  <div>
    
    <b-card body-class="m-3">
      <h4>Plan Nutricional</h4>

    <p class="mb-4">Para poder seguir la dieta recomendada deberias seguir la siguiente dieta</p>
      <b-table
      responsive
        hover
        :fields="fields"
        :items="meal_plan_list"
 

        class="table-meal"
      ></b-table>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      fields: [
        {
          key: "dia",
          label: "Dia",
          tdClass:"column-table"
        },
        {
          key: "desayuno",
          label: "Desayuno",
        },
        {
          key: "almuerzo",
          label: "Almuerzo",
        },
        {
          key: "cena",
          label: "Cena",
        },
      
      ],
      meal_plan_list:[
        {
          dia:"Lunes",
          desayuno: "manzana",
          almuerzo: "leche",
          cena:"arroz"
        },
        {
          dia:"Martes",
          desayuno: "manzana",
          almuerzo: "leche",
          cena:"arroz"
        },
        {
          dia:"Miercoles",
          desayuno: "manzana",
          almuerzo: "leche",
          cena:"arroz"
        },{
          dia:"Jueves",
          desayuno: "manzana",
          almuerzo: "leche",
          cena:"arroz"
        },{
          dia:"Viernes",
          desayuno: "manzana",
          almuerzo: "leche",
          cena:"arroz"
        },{
          dia:"Sabado",
          desayuno: "manzana",
          almuerzo: "leche",
          cena:"arroz"
        },{
          dia:"Domingo",
          desayuno: ["arroz", "pollo"],
          almuerzo: "leche",
          cena:"arroz"
        }
      ]
    };
  },
  components: {},
  methods: {},
};
</script>
<style>
.column-table{
  background-color: #2b91f7d5;
  color: white;
  border-color: black;
}
.table-meal thead th{
  background-color: #2b91f7d5;
  color: white;
  font-weight: normal;
  border:0px
}
.table-meal{
  box-shadow: 0 0 0 1px rgb(224, 224, 224);
  border-radius: 8px;
  overflow: hidden;

}
</style>>
