<template>
  <div class="mx-auto center justify-content-center">
    <b-container class="py-5">
      <b-row align-h="center">
        <b-col xl="6" lg="7" md="9" sm="11">
          <b-card class="login-card" body-class="mx-3 my-2">
            <div>
              <b-link :to="{ name: 'Home' }" class="title-page-link">
                <h1
                  class="d-flex justify-content-center text-dancing"
                  style="margin-bottom: 1.8rem"
                >
                  <span style="color: #f7912b; font-size: 2.8rem;!important">
                    <strong>Healthy</strong>
                  </span>
                  &nbsp;
                  <span style="color: #f7912b; font-size: 2.8rem;!important">
                    <strong>Fruits</strong>
                  </span>
                </h1>
              </b-link>
            </div>
            <b-form ref="form" @submit="onSubmit">
              <div class="div-scroll scrollbar-young-passion">
                <b-form-group
                  class="mt-3 mb-2"
                  label="Correo Electronico"
                  label-size="sm"
                >
                  <b-row>
                    <b-col>
                      <b-form-input
                        id="input-email"
                        type="email"
                        required
                        v-model="form.email"
                        placeholder="usuario@gmail.com"
                        autocomplete="new-text"
                        :state="inputTextSizeState(form.email, 2, 40)"
                      ></b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputTextSizeValidation(form.email, 2, 40)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta de 2 a 40 caracteres
                        <br />
                      </small>
                    </b-col>
                  </b-row>
                </b-form-group>
                <b-form-group label="Contraseña" label-size="sm" class="mb-2">
                  <b-row align-h="center">
                    <b-col>
                      <b-form-input
                        id="input-password"
                        type="password"
                        required
                        v-model="form.password"
                        autocomplete="new-password"
                        :state="inputTextSizeState(form.password, 8, 40)"
                      ></b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputTextSizeValidation(form.password, 8, 40)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta de 8 a 40 caracteres
                        <br />
                      </small>
                    </b-col>
                  </b-row>
                </b-form-group>
                <b-form-group
                  label="Vuelva a ingresar su contraseña"
                  label-size="sm"
                  class="mb-2"
                >
                  <b-row align-h="center">
                    <b-col>
                      <b-form-input
                        id="input-password-validate"
                        type="password"
                        required
                        v-model="form.password2"
                        autocomplete="new-password"
                        :state="PasswordState()"
                      ></b-form-input>
                    </b-col>
                  </b-row>

                  <small class="msg text-danger" v-if="!PasswordValidate()">
                    <b-icon icon="exclamation-circle" variant="danger"></b-icon
                    >&nbsp; Las contraseñas no son iguales
                    <br />
                  </small>
                </b-form-group>

                <b-row align-h="center" class="mt-3">
                  <b-col>
                    <b-form-group
                      label="Nombre(s)"
                      label-size="sm"
                      class="mb-2"
                    >
                      <b-form-input
                        id="input-name"
                        v-model="form.name"
                        required
                        placeholder="Juan"
                        :state="inputTextState(form.name, 2, 50)"
                      ></b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputTextSizeValidation(form.name, 2, 50)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta de 2 a 50 caracteres
                        <br />
                      </small>
                      <small
                        class="msg text-danger"
                        v-if="!inputOnlyTextValidation(form.name)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta texto
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group
                      label="Apellidos"
                      label-size="sm"
                      class="mb-2"
                    >
                      <b-form-input
                        id="input-lastname"
                        required
                        v-model="form.last_name"
                        placeholder="Perez"
                        :state="inputTextState(form.last_name, 2, 50)"
                      ></b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputTextSizeValidation(form.last_name, 2, 50)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta de 2 a 50 caracteres
                        <br />
                      </small>
                      <small
                        class="msg text-danger"
                        v-if="!inputOnlyTextValidation(form.last_name)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta texto
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                </b-row>

                <b-row align-h="center">
                  <b-col>
                    <b-form-group label="DNI" label-size="sm" class="mb-2">
                      <b-form-input
                        id="input-dni"
                        required
                        v-model="form.dni"
                        type="number"
                        :state="inputTextSizeState(form.dni, 8, 8)"
                      ></b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputTextSizeValidation(form.dni, 8, 8)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta 8 caracteres
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group label="Telefono" label-size="sm" class="mb-2">
                      <b-form-input
                        id="input-phone"
                        required
                        v-model="form.phone"
                        type="number"
                        :state="inputTextSizeState(form.phone, 9, 9)"
                      ></b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputTextSizeValidation(form.phone, 9, 9)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta 9 caracteres
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                </b-row>

                <b-row align-h="center">
                  <b-col>
                    <b-form-group
                      label="Fecha de nacimiento"
                      required
                      label-size="sm"
                      class="mb-2"
                    >
                      <b-form-datepicker
                        v-model="form.birthday"
                        required
                        locale="en"
                        placeholder="Ingrese una fecha"
                        :state="inputSelectState(form.birthday)"
                      >
                      </b-form-datepicker>
                     
                    </b-form-group>
                  </b-col>
                  <b-col cols="4">
                    <b-form-group label="Edad" label-size="sm" class="mb-2">
                      <b-form-input
                        id="input-age"
                        v-model="form.age"
                        type="number"
                        required
                        :state="inputNumberState(form.age, 16, 70)"
                      >
                      </b-form-input>
                      <small
                        class="msg text-danger"
                        v-if="!inputNumberValidation(form.age, 16, 70)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta numeros desde 16 a 70
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                </b-row>

                <b-row align-h="center">
                  <b-col>
                    <b-form-group label="Peso" label-size="sm">
                      <b-input-group>
                        <b-form-input
                          id="input-weight"
                          required
                          v-model="form.weight"
                          placeholder="60"
                          class="item-left"
                          type="number"
                          :state="inputNumberState(form.weight, 10, 700)"
                        ></b-form-input>
                        <template #append>
                          <b-input-group-text class="item-right">
                            kg
                          </b-input-group-text>
                        </template>
                      </b-input-group>
                      <small
                        class="msg text-danger"
                        v-if="!inputNumberValidation(form.weight, 10, 700)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta numeros desde 10 a 700
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group label="Altura" label-size="sm">
                      <b-input-group>
                        <b-form-input
                          id="input-height"
                          required
                          v-model="form.height"
                          placeholder="170"
                          class="item-left"
                          type="number"
                          :state="inputNumberState(form.height, 40, 350)"
                        ></b-form-input>
                        <template #append>
                          <b-input-group-text class="item-right">
                            cm
                          </b-input-group-text>
                        </template>
                      </b-input-group>
                      <small
                        class="msg text-danger"
                        v-if="!inputNumberValidation(form.height, 40, 350)"
                      >
                        <b-icon
                          icon="exclamation-circle"
                          variant="danger"
                        ></b-icon>
                        &nbsp; Solo se acepta numeros desde 40 a 350
                        <br />
                      </small>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group label="Sexo" label-size="sm">
                      <b-form-select
                        v-model="form.type_sex"
                        required
                        :options="sex_options"
                        :state="inputSelectState(form.type_sex)"
                        
                      ></b-form-select>
                     
                    
                    </b-form-group>
                  </b-col>
                </b-row>
              </div>
              <b-row>
                <b-col>
                  <b-button
                    :disabled="butom_loading"
                    type="submit"
                    pill
                    variant="primary"
                    class="float-right px-5 mt-2"
                  >
                    <b-spinner
                      small
                      v-if="butom_loading"
                      class="mr-2"
                    ></b-spinner>
                    Registrarse</b-button
                  >
                </b-col>
              </b-row>
            </b-form>

            <hr class="bg-white mt-3 mb-2" />

            <div class="d-flex justify-content-center">
              <small
                >¿Ya tienes una cuenta?
                <b-link class="a-mod" :to="{ name: 'login' }"
                  >Ingresa aqui.</b-link
                ></small
              >
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import AuthService from "@/services/AuthService.js";
import swal from "sweetalert";

export default {
  data() {
    return {
      butom_loading: false,
      form: {
        name: "",
        email: "",
        last_name: "",
        username: "",
        password: "",
        password2: "",
        status: true,
        dni: "",
        birthday: null,
        age: "",
        weight: "",
        height: "",
        type_sex: "1",
        phone: "",
      },
      message: {
        show: true,
        variant: "danger",
        error: "Ocurrio un error desconocido.",
      },
      sex_options: [
        { value: "1", text: "Masculino" },
        { value: "2", text: "Femenino" },
        { value: " ", text: "Otro" },
      ],
      validation: {
        onlyNumber: /^[0-9]*$/,
        onlyText: /^[a-zá-úÁ-ÚA-Z ]*$/,
        onlyTextAndNumber: /^[a-zá-úÁ-ÚA-Z0-9,._/\- ]*$/,
        email: /^([a-zA-Z0-9]+)@unsa\.edu.pe$/,
      },

      errorsList: [],
      user: [],
    };
  },
  methods: {
    /**
     * @description Verifica si se cumplio las validaciones para luego crear el usuario
     */
    onSubmit(evt) {
      evt.preventDefault();
      if (this.registerValidation()) {
        this.register();
      }else{
        swal("Ingrese los datos correctamente", "", "error", {
          button: "Aceptar",
        });
      }
    },

    /**
     * @description Metodo llamado por evento del boton Reinicar
     */
    onReset(evt) {
      evt.preventDefault();
      this.clear();
    },

    /**
     * @description Realiza el registro de un nuevo usuario al sistema con sus datos correspondientes
     * incluyendo su foto de perfil
     */
    async register() {
      this.form.username = this.form.name+this.form.last_name; 
      this.butom_loading = true;
      try {
        await AuthService.register(this.form);
        swal("Usuario Creado Exitosamente!", "", "success", {
          button: "Aceptar",
        }).then(() => {
          this.clear();
          this.$router.push("/login");
        });
      } catch (error) {
        this.errorsList = [];
        this.errorsList.push(error.response.data.email.toString());
        this.errorsList = this.errorsList.map((x) =>
          x.replace(
            "Ya existe usurario con este correo electrónico.",
            "Ya existe una usuario con ese correo electrónico."
          )
        );

        swal("No se registro el usuario", this.errorsList.join("\n"), "error", {
          button: "Aceptar",
        });
      } finally {
        this.butom_loading = false;
      }
    },

    /**
     * @param {String} text Texto ingresado
     * @description Verifica si el texto esta vacio
     * @return {boolean}
     */
    textEmpty(text) {
      return text == "";
    },

    /**
     * @param {String} text Texto ingresado
     * @param {number} a Tamaño minimo
     * @param {number} b Tamaño maximo
     * @description Verifica si el texto esa dentro de los limites establecidos
     * @return {boolean}
     */
    textSize(text, a, b) {
      return text.length >= a && text.length <= b;
    },

    /**
     * @param {String} text Texto ingresado
     * @description Verifica si el texto cumple con la expresion regular de la variable onlyText
     * @return {boolean}
     */
    onlyText(text) {
      return this.validation.onlyText.test(text);
    },

    /**
     * @param {String} text Texto ingresado
     * @description Verifica si el texto cumple con la expresion regular de la variable onlyTextAndNumber
     * @return {boolean}
     */
    onlyTextAndNumber(text) {
      return this.validation.onlyTextAndNumber.test(text);
    },

    /**
     * @param {String} text Texto ingresado
     * @description Verifica si el texto cumple con la expresion regular de la variable email
     * @return {boolean}
     */
    onlyEmail(text) {
      return this.validation.email.test(text);
    },

    onlyNumber(text) {
      return this.validation.onlyNumber.test(text);
    },
    numberSize(number, a, b) {
      return number >= a && number <= b;
    },
    inputNumberState(value, min, max) {
      if (value === null || value === "") {
        return null;
      }
      return this.numberSize(value, min, max) && this.onlyNumber(value);
    },
    inputNumberValidation(value, min, max) {
      if (value === null || value === "") {
        return true;
      }
      return this.numberSize(value, min, max) && this.onlyNumber(value);
    },

    inputSelectState(value) {
      if (value === null || value === "") {
        return null;
      }
      return true;
    },
    inputSelectValidation(value) {
      if (value === null || value === "") {
        return false;
      }
      return true;
    },
    inputTextState(value, min, max) {
      if (value === null || value === "") {
        return null;
      }
      return this.inputTextValidation(value, min, max);
    },
    inputTextValidation(value, min, max) {
      if (value === null || value === "") {
        return true;
      }
      return this.textSize(value, min, max) && this.onlyText(value);
    },



    inputTextSizeState(value, min, max) {
      if (value === null || value === "") {
        return null;
      }
      return this.inputTextSizeValidation(value, min, max);
    },
    inputTextSizeValidation(value, min, max) {
      if (value === null || value === "") {
        return true;
      }
      return this.textSize(value, min, max);
    },
    inputOnlyTextValidation(value) {
      if (value === null || value === "") {
        return true;
      }
      return this.onlyText(value);
    },

    /**
     * @description Reinicia los variables de los inputs del formulario
     */
    clear() {
      this.form.name = "";
      this.form.email = "";
      this.form.last_name = "";
      this.form.password = "";
      this.form.dni = "";
      this.form.birthday = "";
      this.form.age = "";
      this.form.weight = "";
      this.form.height = "";
      this.form.type_sex = "1";
      this.form.phone = "";
    },

    /**
     * @param {String} value Texto ingresado
     * @description Convierte el texto en minisculas
     * @return {String}
     */
    forceLowerCase(value) {
      return value.toLowerCase();
    },

    /**
     * @description Verifica que se cumplan las validaciones del nombre, apellido y correo
     */
    registerValidation() {
      /*return (
        this.firstNameValidation &&
        this.lastNameValidation &&
        this.emailValidation
      );*/
      return (
        this.inputTextSizeState(this.form.email, 2, 40) &&
        this.inputTextSizeState(this.form.password, 8, 40) &&
        this.PasswordState() &&
        this.inputTextState(this.form.name, 2, 50) &&
        this.inputTextState(this.form.last_name, 2, 50) &&
        this.inputTextSizeState(this.form.dni, 8, 8) &&
        this.inputTextSizeState(this.form.phone, 9, 9) &&
        this.inputSelectState(this.form.birthday) &&
        this.inputNumberState(this.form.age, 16, 70) &&
        this.inputNumberState(this.form.weight, 10, 700) &&
        this.inputNumberState(this.form.height, 40, 350) &&
        this.inputSelectState(this.form.type_sex)
      );
    },

    /**
     * @description Metodo que verifica si las contraseñas son iguales
     * @return {boolean}
     */
    PasswordValidate() {
      if (this.form.password == this.form.password2) {
        return true;
      }
      return false;
    },
    PasswordState() {
      if (this.form.password2 === null || this.form.password2 === "") {
        return null;
      }
      return this.PasswordValidate();
    },

  },

  computed: {
    /**
     * @description Metodo que verifica el tamaño del texto y los caracteres ingresados
     * del input del nombre
     * @return {boolean}
     */
    firstNameValidation() {
      if (this.textEmpty(this.form.name)) {
        return new Boolean(null);
      }
      return (
        this.textSize(this.form.name, 2, 32) && this.onlyText(this.form.name)
      );
    },

    /**
     * @description Metodo que verifica el tamaño del texto y los caracteres ingresados
     * del input del apellido
     * @return {boolean}
     */
    lastNameValidation() {
      if (this.textEmpty(this.form.last_name)) {
        return new Boolean(null);
      }
      return (
        this.textSize(this.form.last_name, 2, 32) &&
        this.onlyText(this.form.last_name)
      );
    },
    /**
     * @description Metodo que verifica el tamaño del texto y los caracteres ingresados
     * del input del correo
     * @return {boolean}
     */
    emailValidation() {
      if (this.textEmpty(this.form.email)) {
        return new Boolean(null);
      }
      return true;
      //return this.onlyEmail(this.form.email);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
.item-right {
  border-top-right-radius: 1.1rem;
  border-bottom-right-radius: 1.1rem;
}
.item-left {
  border-top-right-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}
.div-scroll {
  overflow-y: scroll;
  height: 55vh;
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
</style>
