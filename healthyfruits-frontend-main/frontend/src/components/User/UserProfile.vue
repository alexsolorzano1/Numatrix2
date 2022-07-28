<template>
  <div>
    <EditProfile :user="user" :getUser="getUser"> </EditProfile>
    <b-row>
      <b-col sm="12" md="6">
        <b-card
          img-src="https://picsum.photos/400/180/?image=866"
          img-alt="Card image"
          img-top
          img-height="230"
          class="bottom-card"
          body-class="m-2"
        >
          <div
            class="no-bg-color d-flex justify-content-center border-0 mb-4"
            style="
              position: absolute;
              top: 70px;
              left: 0;
              right: 0;
              margin: auto;
            "
          >
            <b-img
              src="user3.png"
              style="height: 100px; border: 2px solid white"
              class="rounded-circle"
            ></b-img>
          </div>

          <b-row class="mb-4 mt-3">
            <b-col class="title"><h4>Mi perfil</h4></b-col>
            <b-col class="date text-right">{{ user.birthday }}</b-col>
          </b-row>
          <b-row class="mb-4">
            <b-col>
              {{ user.name + " " + user.last_name }}
              <div><hr class="mt-2 mb-0 w-100 float-left" /></div>
            </b-col>
            <b-col class="text-right">
              {{ user.phone }}
              <div><hr class="mt-2 mb-0 w-75 float-right" /></div>
            </b-col>
          </b-row>
          <b-row class="mb-4">
            <b-col cols="12"
              >{{ user.email }}
              <div><hr class="mt-2 mb-0 w-50 float-left" /></div>
            </b-col>
          </b-row>

          <b-row class="mb-4">
            <b-col>
              Edad: {{ user.age }} Años
              <div><hr class="mt-2 mb-0 w-75 float-left" /></div>
            </b-col>
            <b-col class="text-center">
              Peso: {{ user.weight }}kg
              <div><hr class="mt-2 mb-0 w-75 float-center" /></div>
            </b-col>
            <b-col class="text-right">
              Altura: {{ user.height }}cm
              <div><hr class="mt-2 mb-0 w-75 float-right" /></div>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-button
                pill
                variant="danger"
                class="px-3 mt-2 float-right ml-2"
                @click="logout"
                ><b-icon icon="power"></b-icon> Cerrar Sesión</b-button
              >
              <b-button
                pill
                variant="info"
                class="px-4 mt-2 float-right"
                @click="editProfile($event.target)"
                ><b-icon icon="pencil-square"></b-icon> Editar</b-button
              >
            </b-col>
          </b-row>
        </b-card>
      </b-col>
      <b-col sm="12" md="6">
        <b-card style="" body-class="m-2">
          <b-card-title class="mb-4">
            <b-row>
              <b-col class="title"><h4>Alimentos consumidos</h4></b-col>
              <b-col cols="auto" class="title">
                <b-icon icon="search" class="float-right"></b-icon>
              </b-col>
            </b-row>
          </b-card-title>
          <b-table
            responsive
            class="border-bottom"
            hover
            :fields="fields"
            :items="userAliments"
            :per-page="perPage"
            :current-page="currentPage"
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
    </b-row>
  </div>
</template>
<script>
import EditProfile from "@/components/User/EditProfile";
import AuthService from "@/services/AuthService.js";
export default {
  components: {
    EditProfile,
  },
  data() {
    return {
      user: {
        id: 3,
        name: "Jhon",
        last_name: "Mamani Mamani",
        email: "jmamanimama@unsa.edu.pe",
        phone: "+51 987 704 704",
        age: 45,
        height: 167,
        weight: 68,
        year: 15,
        created: new Date("2017-01-03"),
        password: "",
      },
      fields: [
        {
          key: "name",
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
          key: "consumed",
          label: "Tiempo",
          formatter: (value) => {
            return this.prettyDate(value);
          },
          sortable: true,
          sortBy: true,
          filter: true,
        },
      ],
      userAliments: [
        {
          id: 53,
          name: "Sandia",
          consumed: new Date(2021, 9, 31, 21, 24, 0),
          calories: 80,
        },

        {
          id: 54,
          name: "Trigo",
          consumed: new Date(2021, 9, 31, 21, 24, 0),
          calories: 70,
        },

        {
          id: 55,
          name: "manzana",
          consumed: new Date(2021, 9, 12, 12, 24, 0),
          calories: 70,
        },
        {
          id: 56,
          name: "pera",
          consumed: new Date(2021, 8, 31, 9, 24, 0),
          calories: 70,
        },
        {
          id: 57,
          name: "manzana",
          consumed: new Date(2021, 7, 30, 18, 24, 0),
          calories: 70,
        },
        {
          id: 58,
          name: "Platano",
          consumed: new Date(2021, 6, 39, 17, 24, 0),
          calories: 70,
        },
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 4,
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/home");
    },
    editProfile(button) {
      this.$root.$emit("bv::show::modal", "edit-profile-modal", button);
    },
    formatterState() {
      return this.user.status ? "Activo" : "Inactivo";
    },
    /**
     * @description Obtiene los datos de un usuario en especifico
     * @return {user}
     */

    async getUser() {
       this.user = await AuthService.getUser();
      this.getAliment(this.user.id);
    },
    getAliment(idUser) {
      console.log(idUser);
      this.totalRows = this.userAliments.length;
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
  },
  async created() {
    await this.getUser();
  },
};
</script>
<style lang="css" scoped>
.f-perfil {
  max-height: 180px;
  max-width: 280px;
  scale: "scale";
}
.title {
  color: black;
  /*font-size: 24px;*/
  font-family: "Trebuchet MS", Verdana, sans-serif;
  font-style: bold;
}
.date {
  font-size: 14px;
  font-style: italic;
}
</style>
