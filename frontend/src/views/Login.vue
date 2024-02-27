<template>
  <div class="login">
    <div class="login__content container">
      <div class="login__content-form">
        <div class="login__content-form-logo">
          <img src="@/assets/images/png/sdu-login-logo.png" alt="sdu-login-logo">
        </div>
        <div class="login__content-form-title">
          <h1 class="semi-bold-txt">LOG IN TO STUDENT HOUSE PORTAL</h1>
        </div>
        <div class="login__content-form-enter">
          <div class="login__content-form-enter-input">
            <p class="regular-txt">Student ID</p>
            <input
                type="text"
                v-model="v$.id.$model"
                placeholder="Enter Student ID"
                @keyup.enter="loginForm"
            />
            <template v-for="(error, index) of v$.id.$errors" :key="index">
              <p class="errorValid">{{ error.$message }}</p>
            </template>
          </div>
          <div class="login__content-form-enter-input">
            <p class="regular-txt">Password</p>
            <input
                type="password"
                v-model="v$.password.$model"
                placeholder="Enter Password"
                @keyup="onlyLatin()"
                @keyup.enter="loginForm"
            />
            <template v-if="v$.password.$error">
              <p class="errorValid" v-if="v$.password.required.$invalid">Required field</p>
              <p class="errorValid" v-if="v$.password.minLength.$invalid">Minimum character length: 8</p>
              <p class="errorValid" v-if="v$.password.containsUpperCase.$invalid">Password must contain at least one uppercase letter</p>
              <p class="errorValid" v-if="v$.password.containsNumber.$invalid">Password must contain at least one number</p>
              <p class="errorValid" v-if="v$.password.noSpaces.$invalid">Password cannot contain spaces</p>
            </template>
          </div>
        </div>
        <div class="login__content-form-forgot">
          <p class="regular-txt">Forgot a password?</p>
        </div>
        <div class="login__content-form-login">
          <button class="login__content-form-login-btn" @click="loginForm">Log in</button>
        </div>
        <div class="login__content-form-return" @click="$router.push('/')">
          <img src="@/assets/images/svg/arrow-return.svg" alt="arrow-return">
          <p class="regular-txt">Return to main page</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import {
  required,
  minLength,
  helpers
} from "@vuelidate/validators";
import {mapActions} from "vuex";

export default {
  components: {
  },
  data: () => ({
    v$: useVuelidate(),
    id: "",
    password: "",
  }),
  validations() {
    return {
      id: {
        required: helpers.withMessage("Required field", required),
        minLength: helpers.withMessage('Minimum of numbers in the id: 9', minLength(9)),
      },
      password: {
        required: helpers.withMessage("Required field", required),
        minLength: helpers.withMessage('Minimum character length: 8', minLength(8)),
        containsUpperCase(value) {
          return /[A-Z]/.test(value);
        },
        containsNumber(value) {
          return /\d/.test(value);
        },
        noSpaces(value) {
          return !/\s/.test(value);
        },
      },
    };
  },
  methods: {
    ...mapActions(["requestUser"]),
    loginForm() {
      this.v$.$validate();
      if (
          !this.v$.$invalid
      ) {
        const data = {
          student_id: this.id,
          password: this.password,
        };
        this.$axios.post("login/", data)
            .then(res => {
              localStorage.setItem("access_token", res.data.access);
              this.$toaster.success("Log in Successfully");
              this.resetForm()
              setTimeout(() => {
                this.requestUser();
                this.$router.push('/personal-account');
              }, 200);
            })
            .catch(err => {
              this.$toaster.error(err.response.data.detail);
            })
      }
      else {
        this.$toaster.error("Full input");
      }
    },
    resetForm() {
      this.id = "",
      this.password = "",
      this.v$.$reset()
    },
    onlyLatin() {
      this.password = this.password.replace(/[^a-zA-Z0-9\s.!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, '');
    },
    onlyText() {
      this.password = this.password.replace(/[^а-яА-ЯёЁәӘіІңҢғҒүҮұҰқҚөӨһҺa-zA-Z\-\s.]/gi, "");
      this.password = this.password.replace(/\.{2,}|\s{2,}|\-{2,}/g, function (match) {
        return match.substr(0, 1);
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 110lvh;
  &__content {
    display: flex;
    flex-direction: column;
    width: 100%;
    &-form {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      color: $black;
      &-logo {
        display: flex;
        align-items: center;
        height: 100%;
        img {
          width: 206px;
          height: 100%;
          cursor: pointer;
        }
      }
      &-title {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 60px 0 45px 0;
        h1 {
          font-size: 64px;
        }
      }
      &-enter {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 32px;
        &-input {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          width: 365px;
          gap: 17px;
          p {
            font-size: 24px;
          }
          input {
            width: 100%;
            height: 50px;
            border: 1px solid $black;
            background: #F0F0F0;
            padding: 10px 15px;
            border-radius: 25px;
            color: $black;
            outline: none;
          }
        }
      }
      &-forgot {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 365px;
        padding-top: 15px;
        p {
          font-size: 16px;
          color: $grey;
          text-decoration: underline;
          cursor: pointer;
        }
      }
      &-login {
        display: flex;
        flex-direction: column;
        width: 365px;
        padding-top: 43px;
        &-btn {
          padding: 20px 100px;
          background: $secondary;
          border-radius: 25px;
          width: 100%;
          font-size: 24px;
        }
      }
      &-return {
        display: flex;
        align-items: center;
        padding-top: 140px;
        gap: 10px;
        cursor: pointer;
        p {
          font-size: 16px;
          color: $grey;
        }
      }
    }
  }
}
.errorValid {
  color: #f72a2a;
  font-size: 16px !important;
  padding: 8px 0;
}
</style>