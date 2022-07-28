<template>
  <div v-if="!loading">
    <div id="nav">
      <div id="mySidenav" class="sidenav">
        <b-row>
          <b-col>
            <div class="float-right">
              <b-button
                v-if="butonNav"
                @click="closeNav"
                variant="link "
                size="lg"
                class="text-white pr-2 btn-none"
              >
                <b-icon icon="box-arrow-in-left"></b-icon>
              </b-button>
              <b-button
                v-if="!butonNav"
                @click="openNav"
                variant="link "
                class="text-white pr-2 btn-none"
                size="lg"
              >
                <b-icon icon="box-arrow-in-right"></b-icon>
              </b-button>
            </div>
          </b-col>
        </b-row>
        <b-list-group flush class="mt-2 no-bg-color text-white">
          <b-list-group-item
            class="no-bg-color d-flex justify-content-center border-0 mb-3"
          >
            <b-img
              id="perfilImage"
              src="user3.png"
              style="height: 90px; border: 2px solid white"
              class="rounded-circle"
            ></b-img>
          </b-list-group-item>
          <b-list-group-item
            :class="'no-bg-color border-0 ' + nav_items[0].active"
            v-on:click="changeActive(nav_items[0].value)" to="/username"
          >
            <b-icon icon="person-fill" class="im" scale="1.2"></b-icon>
            <transition name="fade"
              ><span v-if="menuItem" class="menuItem"
                >&nbsp;{{ user.name + " " + user.last_name }}
              </span></transition
            >
          </b-list-group-item>
          <b-link class="text-decoration-none">
            <b-list-group-item class="no-bg-color border-0" @click="logout">
              <b-icon icon="power" class="im" scale="1.3"></b-icon>
              <transition name="fade"
                ><span v-if="menuItem" class="menuItem"
                  >&nbsp; Cerrar Sesión</span
                ></transition
              >
            </b-list-group-item>
          </b-link>
        </b-list-group>
        <b-list-group flush class="mt-5 text-white">
          <b-list-group-item
            :class="'no-bg-color border-0 ' + nav_items[1].active"
            v-on:click="changeActive(nav_items[1].value)" :to="{ name: 'SearchHealthyFood' }"
          >
            <b-icon icon="search" class="im"></b-icon>
            <transition name="fade"
              ><span v-if="menuItem" class="menuItem"
                >&nbsp; Busqueda de alimentos saludables</span
              ></transition
            >
          </b-list-group-item>
          <!-----------
          <b-list-group-item
            :class="'no-bg-color border-0 ' + nav_items[2].active"
            v-on:click="changeActive(nav_items[2].value)" :to="{ name: 'MealPlan' }"
          >
            <b-icon icon="table" class="im"></b-icon>
            <transition name="fade"
              ><span v-if="menuItem" class="menuItem"
                >&nbsp; Plan nutricional</span
              ></transition
            >
          </b-list-group-item>------------>
          <b-list-group-item
            :class="'no-bg-color border-0 ' + nav_items[3].active"
            v-on:click="changeActive(nav_items[3].value)" :to="{ name: 'Recomendation' }"
          >
            <b-icon icon="receipt" class="im" scale="1.1"></b-icon>
            <transition name="fade"
              ><span v-if="menuItem" class="menuItem"
                >&nbsp; Recomendacion de alimentos</span
              ></transition
            >
          </b-list-group-item>
          <b-list-group-item
            v-on:click="changeActive(nav_items[4].value)" :class="'no-bg-color border-0 ' + nav_items[4].active"
            to="/history"
          >
            <b-icon icon="clock-history" class="im" scale="1.1"></b-icon>
            <transition name="fade"
              ><span v-if="menuItem" class="menuItem"
                >&nbsp; Historial alimenticio</span
              ></transition
            >
          </b-list-group-item>
        </b-list-group>
      </div>
    </div>

    <div id="main" style="overflow-y: hidden">
      <div
        v-if="loading_side_bar"
        class="mx-auto center-side-bar justify-content-center"
        style="color: #f7912b"
      >
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
      <transition name="transition-a" mode="out-in">
        <router-view :show_loading_side_bar="show_loading_side_bar" />
      </transition>
    </div>
  </div>
</template>

<script>
import AuthService from "@/services/AuthService.js";
export default {
  props: ["show_loading_app"],
  name: "Home",
  data() {
    return {
      widht_side: "250px",
      loading: true,
      loading_side_bar: false,
      user: {
        name: "",
        last_name: "",
      },
      menuItem: true,
      butonNav: true,
      windowWidth: window.innerWidth,
      nav_items: [
        {
          value: 1,
          to: "userProfile",
          active: "active-item",
        },
        {
          value: 2,
          to: "SearchHealthyFood",
          active: "",
        },
        {
          value: 3,
          to: "MealPlan",
          active: "",
        },
        {
          value: 4,
          to: "Recomendation",
          active: "",
        },
        {
          value: 5,
          to: "NutritionalHistory",
          active: "",
        },
      ],
    };
  },
  components: {},
  mounted() {
    window.onresize = () => {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth >= 1200) {
        this.widht_side = "250px";
        this.openNav();
      } else {
        this.closeNav();
        this.widht_side = "55px";
      }
    };
    this.windowWidth = window.innerWidth;
    if (this.windowWidth >= 1200) {
      this.widht_side = "250px";
    } else {
      this.widht_side = "55px";
      this.butonNav = false;
      this.menuItem = false;
    }
  },
  methods: {
    show_loading_side_bar(value) {
      this.loading_side_bar = value;
    },
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/home");
    },
    openNav() {
      document.getElementById("mySidenav").style.width = "250px";
      document.getElementById("main").style.marginLeft = this.widht_side;

      this.butonNav = true;
      setTimeout(() => {
        this.menuItem = true;
        document.getElementById("perfilImage").style.visibility = "visible";
      }, 300);
    },
    closeNav() {
      document.getElementById("mySidenav").style.width = "55px";
      document.getElementById("main").style.marginLeft = "55px";
      document.getElementById("perfilImage").style.visibility = "hidden";
      //document.getElementsByClassName("menuItem").style.display = "none";
      this.butonNav = false;
      this.menuItem = false;
    },
    changeActive(value) {
      for (let i = 0; i < this.nav_items.length; i++) {
        this.nav_items[i].active = "";
        if (value == this.nav_items[i].value) {
          this.nav_items[i].active = "active-item";
        }
      }
    },
  },
  updated() {
    if ("SideBarHome" == this.$route.name) {
      this.$router.push("/username");
    }
  },
  async created() {
    this.show_loading_app(true);
    try {
      if (this.$store.getters.isLoggedIn) {
        this.user = await AuthService.getUser();
        this.show_loading_app(false);
        this.loading = false;
        if ("SideBarHome" == this.$route.name) {
          this.$router.push("/username");
        }
        
      } else {
        this.show_loading_app(false);
        this.$store.dispatch("logout");
        this.$router.push("/home");
      }
    } catch (error) {
      this.show_loading_app(false);
      this.$store.dispatch("logout");
      this.$router.push("/home");
    }
    this.nav_items.forEach((element) => {
          if (element.to == this.$route.name) {
            this.changeActive(element.value);
          }
        });
  },
};
</script>
<style>
.sidenav {
  border-top-right-radius: 0.8rem;
  border-bottom-right-radius: 0.8rem;
  overflow: hidden;
  height: 100%; /* 100% Full-height */
  width: 250px; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  z-index: 100; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;

  background: linear-gradient(
    90deg,
    rgba(235, 66, 54, 1) 3%,
    rgba(237, 97, 61, 1) 34%,
    rgba(239, 123, 68, 1) 59%,
    rgba(242, 156, 76, 1) 100%
  );
  background: linear-gradient(
    90deg,
    rgba(212, 74, 64, 1) 3%,
    rgba(217, 142, 73, 1) 100%
  );
  background: linear-gradient(
    90deg,
    rgba(224, 78, 68, 1) 3%,
    rgba(237, 154, 77, 1) 100%
  );
  background: linear-gradient(
    90deg,
    rgba(230, 77, 67, 1) 3%,
    rgba(255, 166, 83, 1) 100%
  );
  /*overflow-x: hidden;*/ /* Disable horizontal scroll */

  transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
  box-shadow: 0 8px 17px 2px rgba(0, 0, 0, 0.14),
    0 3px 14px 2px rgba(0, 0, 0, 0.12), 0 5px 5px -3px rgba(0, 0, 0, 0.2);
}
.sidenav a {
  color: #f1f1f1;
}
.sidenav a:hover,
.sidenav a:focus {
  background-color: white !important;
  color: #f37d4b !important;
  transition: all 0.6s ease;
}
.active-item {
  background-color: white !important;
  color: #f37d4b !important;
  
}
/*
.sidenav a:hover::before, .sidenav a:focus::before {
  content: "";
  position: absolute;
  
  background-color: transparent;
  bottom: -50px;
  right: 0px;
  height: 50px;
  width: 25px;
  border-top-right-radius: 25px;
  box-shadow: 0 -25px 0 0 white;
}
.sidenav a:hover::after, .sidenav a:focus::after {
  content: "";
  position: absolute;
  
  background-color: transparent;
  bottom: 48px;
  right: 0px;
  height: 50px;
  width: 25px;
  border-bottom-right-radius: 25px;
  box-shadow: 0 25px 0 0  white;
}*/
.icon_menu {
  position: fixed; /* Stay in place */
  color: #f7912b !important;
}
#main {
  transition: margin-left 0.5s;
  margin-left: 250px;
  padding: 2rem;
  min-height: 100vh;
  background-size: cover;
}
.height-padding {
  min-height: calc(100vh - 4rem);
}
.bottom-card{
  margin-bottom: 0;
}
@media only screen and (max-width: 1199px) {
  #main {
    margin-left: 55px;
  }
  #mySidenav {
    width: 55px;
  }
  #perfilImage {
    visibility: hidden;
  }
}
@media only screen and (max-width: 767px) {
  .bottom-card{
  margin-bottom: 2rem;
}
}
</style>