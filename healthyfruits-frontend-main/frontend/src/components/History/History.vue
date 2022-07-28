<template>
  <div v-if="!loading">
    <b-row>
      <b-col sm="12" md="6">
        <b-card body-class="m-2" class="bottom-card">
          <b-card-title class="mb-4">
            <b-row>
              <b-col class="title"><h4>Alimentos consumidos</h4></b-col>
              <b-col cols="auto" class="title">
                <b-icon icon="search" class="float-right"></b-icon>
              </b-col>
            </b-row>
          </b-card-title>
          <b-table
            striped
            hover
            responsive
            :fields="fields"
            :items="userAliments"
            :per-page="perPage"
            :current-page="currentPage"
            class="border-bottom"
          ></b-table>

          <b-row class="my-0" align-h="center">
            <b-col sm="7" class="my-0">
              <b-pagination
                v-model="currentPage"
                :total-rows="totalRows"
                :per-page="perPage"
                align="fill"
                size="sm"
                class="my-0"
              ></b-pagination>
            </b-col>
          </b-row>
        </b-card>
      </b-col>
      <!-- -->
      <b-col sm="12" md="6">
        <b-card body-class="m-2">
          <b-card-title class="mb-4">
            <b-row>
              <b-col class="title"
                ><h4>Alimentos Consumidos la Ultima Semana</h4></b-col
              >
            </b-row>
            <hr />
          </b-card-title>
          <template>
            <JSCharting1
              :options="optionsGraph"
              class="columnChart"
            ></JSCharting1>
          </template>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>
<script>
import axios from "axios";
const url = process.env.VUE_APP_RUTA_API;
import JSCharting1 from "jscharting-vue";
export default {
  props: ["show_loading_side_bar"],
  components: {
    JSCharting1,
  },
  data() {
    return {
      loading: false,
      fields: [
        {
          key: "id_foodmeal",
          label: "Nombre",
          sortable: true,
          sortByFormatted: true,
          filterByFormatted: true,
          sortDirection: "desc",
        },
        {
          key: "calories",
          label: "Calorias",
          sortable: true,
          sortByFormatted: true,
          filterByFormatted: true,
          sortDirection: "desc",
        },
        {
          key: "created",
          label: "Tiempo",
          formatter: (value) => {
            return this.prettyDate(value);
          },
          sortable: true,
          sortBy: true,
          filter: true,
        },
      ],
      userAliments: [],
      nameAliment:"",
      totalRows: 1,
      currentPage: 1,
      perPage: 10,
      datesCharts: [],
      dataCharts: [0, 0, 0, 0, 0, 0, 0],

      optionsGraph: {
        legend: {
          position: "top left",
        },
      },
      name: "columnChart",
    };
  },
  methods: {
    getAliment() {
      var path = url + "food/history_food/?id_user="+this.$store.getters.getId;
      axios.get(path).then((response) => {
          this.userAliments= response.data.results;
          this.createDataCharts();  
        })
        .catch((error) => {
          console.log(error);
        });
    },

    prettyDate(time) {
      var date = new Date(time),
        diff = (new Date().getTime() - date.getTime()) / 1000,
        day_diff = Math.floor(diff / 86400);
      if (isNaN(day_diff) || day_diff < 0) return;

      return (
        (day_diff == 0 &&
          ((diff < 60 && "just now") ||
            (diff < 120 && "1 minute ago") ||
            (diff < 3600 && Math.floor(diff / 60) + " minutes ago") ||
            (diff < 7200 && "1 hour ago") ||
            (diff < 86400 && Math.floor(diff / 3600) + " hours ago"))) ||
        (day_diff == 1 && "Yesterday") ||
        (day_diff < 7 && day_diff + " days ago") ||
        (day_diff < 31 && Math.ceil(day_diff / 7) + " weeks ago") ||
        (day_diff > 31 &&
          time.getDate() +
            "/" +
            time.getMonth() +
            "/" +
            time.getFullYear() +
            "")
      );
    },
    CompareDate(DateA, DateB) {
      var newDataA = new Date(DateA),
        newDataB = new Date(DateB);
      if (
        newDataA.getDate() == newDataB.getDate() &&
        newDataA.getMonth() == newDataB.getMonth() &&
        newDataA.getFullYear() == newDataB.getFullYear()
      )
        return true;
      return false;
    },
    createDates() {
      var dt = new Date(); //current date of week
      var lessDays = 6;
      var wkStart = new Date(new Date(dt).setDate(dt.getDate() - lessDays));
      for (let index = 0; index < 7; index++) {
        var day = new Date(
          new Date(wkStart).setDate(wkStart.getDate() + index)
        );
        this.datesCharts.push(day);
      }
    },
    createDataCharts() {
      console.log("jola")
      console.log(this.userAliments)
      this.userAliments.forEach((element) => {
        if (this.CompareDate(element.created, this.datesCharts[0]))
          this.dataCharts[0] = this.dataCharts[0] + parseFloat(element.calories);
        if (this.CompareDate(element.created, this.datesCharts[1]))
          this.dataCharts[1] = this.dataCharts[1] + parseFloat(element.calories);
        if (this.CompareDate(element.created, this.datesCharts[2]))
          this.dataCharts[2] = this.dataCharts[2] + parseFloat(element.calories);
        if (this.CompareDate(element.created, this.datesCharts[3]))
          this.dataCharts[3] = this.dataCharts[3] + parseFloat(element.calories);
        if (this.CompareDate(element.created, this.datesCharts[4]))
          this.dataCharts[4] = this.dataCharts[4] + parseFloat(element.calories);
        if (this.CompareDate(element.created, this.datesCharts[5]))
          this.dataCharts[5] = this.dataCharts[5] + parseFloat(element.calories);
        if (this.CompareDate(element.created, this.datesCharts[6]))
          this.dataCharts[6] = this.dataCharts[6] + parseFloat(element.calories);
      });
      this.llenarGrafica();
    },
    llenarGrafica() {
      this.optionsGraph = {
        type: "column",
        series: [
          {
            name: "Calorias Semanales",
            legend: {
              position: "top",
              template: "%icon %name",
            },
            points: [
              { x: "Hace 6 dias", y: this.dataCharts[0] },
              { x: "Hace 5 dias", y: this.dataCharts[1] },
              { x: "Hace 4 dias", y: this.dataCharts[2] },
              { x: "Hace 3 dias", y: this.dataCharts[3] },
              { x: "Hace 2 dias", y: this.dataCharts[4] },
              { x: "Hace 1 dia", y: this.dataCharts[5] },
              { x: "Hoy", y: this.dataCharts[6] },
            ],
          },
        ],
      };
    },
  },
  async created() {
    this.show_loading_side_bar(true);
    await this.getAliment();
    await this.createDates();
    await this.createDataCharts();
    this.llenarGrafica();
    this.show_loading_side_bar(false);
    this.loading = false;
  },
};
</script>
<style lang="css" scoped>
.title {
  color: black;
  font-size: 24px;
  font-family: "Trebuchet MS", Verdana, sans-serif;
  font-style: bold;
}
.date {
  font-size: 14px;
  font-style: italic;
}
</style>
