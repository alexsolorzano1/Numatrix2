<template>
  <b-container>
    <b-modal
      id="edit-profile-modal"
      ref="modal"
      title="Editar Perfil"
      size="lg"
      scrollable
      @ok="handleOk"
      ok-title="Aceptar"
      cancel-title="Cancelar"
      content-class="p-1"
    >
      <b-form ref="form" @submit="handleSubmit">
        <b-row>
          <b-col>
            <b-form-group
              class="mb-2"
              label="Correo Electronico"
              label-size="sm"
            >
              <b-row>
                <b-col>
                  <b-form-input
                    id="input-email"
                    type="email"
                    required
                    v-model="user.email"
                    placeholder="Correo Electronico"
                  ></b-form-input>
                </b-col>
              </b-row>
            </b-form-group>

            <b-row align-h="center">
              <b-col>
                <b-form-group label="Nombre(s)" label-size="sm" class="mb-2">
                  <b-form-input
                    id="input-name"
                    required
                    v-model="user.name"
                    placeholder="Nombre"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col>
                <b-form-group label="Apellidos" label-size="sm" class="mb-2">
                  <b-form-input
                    id="input-lastname"
                    required
                    v-model="user.last_name"
                    placeholder="Apellidos"
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row align-h="center">
              <b-col>
                <b-form-group label="DNI" label-size="sm" class="mb-2">
                  <b-form-input
                    id="input-dni"
                    required
                    v-model="user.dni"
                    placeholder="DNI"
                    type="number"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col>
                <b-form-group label="Telefono" label-size="sm" class="mb-2">
                  <b-form-input
                    id="input-phone"
                    required
                    v-model="user.phone"
                    placeholder="Telefono"
                    type="number"
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row align-h="center">
              <b-col>
                <b-form-group label="Edad" label-size="sm" class="mb-2">
                  <b-form-input
                    id="input-age"
                    type="number"
                    required
                    v-model="user.age"
                    placeholder="Edad"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col>
                <b-form-group label="Peso" label-size="sm">
                  <b-form-input
                    id="input-weight"
                    type="number"
                    required
                    v-model="user.weight"
                    placeholder="Peso"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col>
                <b-form-group label="Altura" label-size="sm">
                  <b-form-input
                    id="input-height"
                    type="number"
                          required
                    v-model="user.height"
                    placeholder="Altura"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col>
                <b-form-group label="Sexo" label-size="sm">
                  <b-form-select
                 
                  required
                    v-model="user.type_sex"
                    :options="sex_options"
                  ></b-form-select>
                </b-form-group>
              </b-col>
            </b-row>
          </b-col>
        </b-row>
      </b-form>
      <template #modal-footer="{ ok, cancel }">
        <b-button variant="danger" pill @click="cancel()" class="px-3">
          Cancelar
        </b-button>
        <b-button variant="info" pill @click="ok()" class="px-3">
          Aceptar
        </b-button>
      </template>
    </b-modal>
  </b-container>
</template>
<script>
import swal from "sweetalert";
import axios from "axios";
const url = process.env.VUE_APP_RUTA_API;
export default {
  props: ["user"],
  data() {
    return {
      copy_password: "",
      sex_options: [
        { value: "1", text: "Masculino" },
        { value: "2", text: "Femenino" },
        { value: " ", text: "Otro" },
      ],
    };
  },

  methods: {
    handleOk(evt) {
      evt.preventDefault();
      this.handleSubmit();
    },
    /**
     * @description Verifica que se cumplan las validaciones para luego llamar al metodo de crear una incidencia y minimizar el modal
     */
    handleSubmit() {
      const path = url + `user/user/` + this.user.id + `/`;
      axios
        .put(path, this.user)
        .then(() => {
          swal("Usuario Editado!", "", "success", {
            button: "Aceptar",
          }).then(() => {
            this.$bvModal.hide("edit-profile-modal");
            this.getUser();
          });
        })
        .catch((error) => {
          console.log(error);
        });
      this.getAliment(this.user.id);
    },
    clear() {
      this.user = [];
    },
    /**
     * @description Metodo que verifica si las contraseñas son iguales
     * @return {boolean}
     */
    PasswordValidate() {
      if (this.user.password == this.copy_password) {
        return true;
      }
      return false;
    },
  },

  async created() {
    
  },
};
</script>
<style lang="css" scoped></style>