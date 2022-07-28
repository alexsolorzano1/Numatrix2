<template  >
  <div>
    <div class="fixed-top nav-modified">
      <b-navbar toggleable="md" class="nav-top-modified">
        <b-container>
          <b-navbar-brand href="#" class="text-dancing">
            <span style="font-size: 2.2rem !important; color: white">
              <strong>Numatrix</strong>
            </span>
          </b-navbar-brand>

          <b-navbar-toggle target="nav-collapse" style="" class="btn-toggle">
            <h3 class="py-0 my-0"><b-icon icon="list"></b-icon></h3>
          </b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto text-barlow nav-bar-content">
              <b-nav-item
                v-for="item in nav_items"
                v-on:click="changeActive(item.value)"
                :key="item.value"
                right
                :to="{ name: item.to }"
                :class="'item-navbar ' + item.active"
                >{{ item.name }}
              </b-nav-item>
              <b-nav-item>
                <b-button
                  pill
                  variant="primary"
                  class="px-4 my-0 ml-2"
                  :to="{ name: 'login' }"
                  >INGRESAR
                </b-button></b-nav-item
              >
            </b-navbar-nav>
          </b-collapse>
        </b-container>
      </b-navbar>
    </div>
    <div id="main-home" class="portada-home">
      <div class="color-bg">
        <b-container>
          <transition name="slide-fade" mode="out-in">
            <router-view />
          </transition>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["show_loading_app"],
  name: "Home",
  data() {
    return {
      nav_items: [
        {
          value: 1,
          name: "INICIO",
          to: "Home",
          active: "active-item-home",
        },
        {
          value: 2,
          name: "NOSOTROS",
          to: "About",
          active: "",
        },
        {
          value: 3,
          name: "CONTACTANOS",
          to: "Contact",
          active: "",
        },
      ],
    };
  },
  components: {},
  methods: {
    changeActive(value) {
      for (let i = 0; i < this.nav_items.length; i++) {
        this.nav_items[i].active = "";
        if (value == this.nav_items[i].value) {
          this.nav_items[i].active = "active-item-home";
        }
      }
    },
  },
  created() {
    this.nav_items.forEach((element) => {
      if (element.to == this.$route.name) {
        this.changeActive(element.value);
      }
    });
    this.show_loading_app(false);
  },
};
</script>
<style scoped>
.nav-top-modified {
  /*background: rgba(0, 0, 0, 0.1);*/
}
.nav-modified .navbar-light .navbar-nav .nav-link {
  padding-top: 0px;
  padding-bottom: 0px;
  color: white !important;
}
.portada-home {
  background: url("../../../public/carr1.jpg") no-repeat center center fixed;
  min-height: 100vw;
}
.color-bg {
  background-color: rgba(97, 53, 33, 0.15);
}
.active-item-home {
  border-bottom: 3px solid;
  color: white;
}
.item-navbar {
  padding-bottom: 0.4rem;
  padding-top: 0.4rem;
  margin-left: 0.5rem;
  transition: all ease-in-out 0.08s;
  color: white;
}
.item-navbar:hover {
  border-bottom: 3px solid;
  color: white;
}

#main-home {
  overflow-x: hidden;
}
.btn-toggle {
  color: white !important;
  border-color: white !important;
}
@media only screen and (max-width: 767px) {
  .nav-modified {
    background-color: rgba(0, 0, 0, 0.4);
  }
  .item-navbar {
    margin-bottom: 0.5rem !important;
  }
  .nav-bar-content {
    padding-bottom: 0.8rem !important;
  }
}
</style>
