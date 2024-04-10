<template>
  <div class="login">
    <div class="login__content container">
      <div class="login__content-form">
        <div class="login__content-form-logo">
          <img src="@/assets/images/png/sdu-login-logo.png" alt="sdu-login-logo" @click="$router.push('/')">
        </div>
        <div class="login__content-form-title">
          <h3 class="semi-bold-txt">Log In to student house portal</h3>
        </div>
        <div class="login__content-form-enter">
          <div class="login__content-form-enter-input">
            <p class="regular-txt">Student ID</p>
            <input
                type="text"
                v-model="v$.id.$model"
                placeholder="Enter Student ID"
                @keyup.enter="loginForm"
                maxlength="9"
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
          <p class="regular-txt" @click="isOpen = true">Forgot a password?</p>
        </div>
        <div class="login__content-form-login">
          <button class="login__content-form-login-btn main-button" @click="loginForm">Log in</button>
        </div>
        <div class="login__content-form-return" @click="$router.push('/')">
          <img src="@/assets/images/svg/arrow-return.svg" alt="arrow-return">
          <p class="regular-txt">Return to main page</p>
        </div>
      </div>
    </div>
  </div>

  <ModalWindow :is-open="isOpen" @close="isOpen = false">
    <div class="forgot" v-if="!codeTab">
      <h3 class="semi-bold-txt forgot-title">Update Your Password</h3>
      <div class="forgot-content">
        <template v-if="step === 1">
          <div class="forgot-id">
            <div class="forgot-id-input">
              <p class="regular-txt">SDU Student ID</p>
              <input
                  type="text"
                  v-model="v$.for_student_id.$model"
                  placeholder="Enter Student ID"
                  :class="{'errorValidPlace': v$.for_student_id.$error}"
                  maxlength="9"
              >
              <template v-for="(error, index) of v$.for_student_id.$errors" :key="index">
                <p class="errorValid">{{ error.$message }}</p>
              </template>
            </div>
          </div>
          <div class="forgot-pass">
            <div class="forgot-pass-input">
              <p class="regular-txt">New Password</p>
              <input
                  type="password"
                  v-model="v$.for_pass.$model"
                  placeholder="Enter new password"
                  @keyup="onlyLatin()"
                  :class="{'errorValidPlace': v$.for_pass.$error}"
              >
              <template v-if="v$.for_pass.$error">
                <p class="errorValid" v-if="v$.for_pass.required.$invalid">Required field</p>
                <p class="errorValid" v-if="v$.for_pass.minLength.$invalid">Minimum character length: 8</p>
                <p class="errorValid" v-if="v$.for_pass.containsUpperCase.$invalid">Password must contain at least one uppercase letter</p>
                <p class="errorValid" v-if="v$.for_pass.containsNumber.$invalid">Password must contain at least one number</p>
                <p class="errorValid" v-if="v$.for_pass.noSpaces.$invalid">Password cannot contain spaces</p>
              </template>
            </div>
            <div class="forgot-pass-input">
              <p class="regular-txt">Repeat Password</p>
              <input
                  type="password"
                  v-model="v$.for_pass_repeat.$model"
                  placeholder="Repeat password"
                  :class="{'errorValidPlace': v$.for_pass_repeat.$error}"
              >
              <template
                  v-for="(error, index) of v$.for_pass_repeat.$errors"
                  :key="index"
              >
                <p class="errorValid">{{ error.$message }}</p>
              </template>
            </div>
            <button class="forgot-pass-btn main-button" @click="changePassword">Confirm</button>
          </div>
        </template>
        <template v-if="step === 2">
          <div class="forgot-success">
            <h3 class="bold-txt">You have successfully changed your password!</h3>
          </div>
        </template>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import ModalWindow from "@/components/ModalWindow.vue";
import {
  required,
  minLength,
  helpers,
  sameAs
} from "@vuelidate/validators";
import {mapActions} from "vuex";

export default {
  components: {
    ModalWindow
  },
  data: () => ({
    v$: useVuelidate(),
    id: "",
    password: "",
    for_student_id: "",
    for_code: "",
    for_pass: "",
    for_pass_repeat: "",
    step: 1,
    isOpen: false,
    codeTab: false,
  }),
  validations() {
    return {
      id: {
        required: helpers.withMessage("Required field", required),
        minLength: helpers.withMessage('Minimum of numbers in the id: 9', minLength(9)),
      },
      for_student_id: {
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
      for_pass: {
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
      for_pass_repeat: {
        required: helpers.withMessage("Required field", required),
        sameAs: helpers.withMessage(
            "It’s not the same",
            sameAs(this.for_pass)
        ),
      },
    };
  },
  methods: {
    ...mapActions(["requestUser"]),
    loginForm() {
      this.v$.id.$validate();
      this.v$.password.$validate();
      if (
          !this.v$.id.$invalid && !this.v$.password.$invalid
      ) {
        const data = {
          student_id: this.id,
          password: this.password,
        };
        this.$axios.post("login/", data)
            .then(res => {
              localStorage.setItem("access_token", res.data.access);
              localStorage.setItem("refresh_token", res.data.refresh);
              this.$toaster.success("You have successfully logged in!");
              this.resetForm()
              setTimeout(() => {
                this.requestUser();
                this.$router.push('/personal-account');
              }, 200);
            })
            .catch(err => {
              if (err.response.data.detail) {
                this.$toaster.error(err.response.data.detail);
              } else {
                this.$toaster.error("An error has occurred, try logging in again!");
              }
            })
      }
      else {
        this.$toaster.error("You must fill in all the fields");
      }
    },
    changePassword() {
      this.v$.for_pass.$validate();
      this.v$.for_pass_repeat.$validate();
      this.v$.for_student_id.$validate();
      if (!this.v$.for_pass.$invalid && !this.v$.for_pass_repeat.$invalid && !this.v$.for_student_id.$invalid) {
        this.$axios
            .post(
                `forgot_password/`,
                {
                  student_id: this.for_student_id,
                  password: this.for_pass
                },
            )
            .then((response) => {
              if (response.status === 200) {
                this.$toaster.success("You have successfully changed your password");
                this.resetForm();
                this.step = 2;
              }
            })
            .catch((error) => {
              this.$toaster.error("An error has occurred");
              this.isOpen = false
            });
      } else {
        this.$toaster.error("You must fill in all the fields");
      }
    },
    resetForm() {
      this.id = "",
      this.password = "",
      this.for_student_id = "",
      this.for_pass_repeat = "",
      this.for_pass = "",
      this.v$.$reset()
    },
    onlyLatin() {
      this.password = this.password.replace(/[^a-zA-Z0-9\s.!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, '');
      this.for_pass = this.for_pass.replace(/[^a-zA-Z0-9\s.!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, '');
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
  height: 100%;
  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    margin: 40px 0;
    &-form {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: 100%;
      color: $black;
      &-logo {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        img {
          width: auto;
          height: min(max(74px, calc(4.625rem + ((1vw - 3.93px) * 8.5134))), 204px);
          cursor: pointer;
        }
      }
      &-title {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 48px 0 32px 0;
      }
      &-enter {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 16px;
        &-input {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          width: 365px;
          gap: 16px;
          p {
            font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
          }
          input {
            width: 100%;
            height: min(max(25px, calc(1.5625rem + ((1vw - 3.93px) * 1.6372))), 50px);
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
        align-items: center;
        justify-content: center;
        max-width: 365px;
        padding-top: 40px;
        &-btn {
          color: $primary;
        }
      }
      &-return {
        display: flex;
        align-items: center;
        padding-top: 64px;
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

.forgot {
  width: 850px;
  max-height: 90lvh;
  padding: 90px 150px 130px 150px;
  gap: 70px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: stretch;
  color: $black;
  &-title {
    text-align: left;
  }
  &-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 35px;
  }
  &-id {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    width: 100%;
    gap: 10px;
    &-input {
      display: flex;
      flex-direction: column;
      align-items: stretch;
      width: 100%;
      gap: 15px;
      p {
        font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
      }
      input {
        width: 100%;
        height: 64px;
        background: $white;
        border-radius: 25px;
        border: 1px solid $black;
        padding: 20px 40px;
        outline: none;
      }
    }
    button {
      font-size: 20px;
      width: 200px;
      height: 64px;
      color: $white;
      &:hover {
        background: $white;
        color: $secondary;
        border: 1px solid $secondary;
      }
    }
  }
  //&-code {
  //  display: flex;
  //  flex-direction: column;
  //  align-items: flex-start;
  //  width: 100%;
  //  gap: 30px;
  //  &-input {
  //    display: flex;
  //    flex-direction: column;
  //    align-items: stretch;
  //    width: 100%;
  //    gap: 15px;
  //    p {
  //      color: $grey;
  //      font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
  //    }
  //    input {
  //      width: 100%;
  //      height: 64px;
  //      background: $white;
  //      border-radius: 25px;
  //      border: 1px solid $grey;
  //      padding: 20px 40px;
  //      outline: none;
  //    }
  //  }
  //  button {
  //    font-size: 20px;
  //    width: 155px;
  //    height: 64px;
  //    color: $white;
  //    &:hover {
  //      background: $secondary;
  //    }
  //  }
  //}
  &-success {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    h3 {
      text-align: center;
      color: $secondary;
    }
  }
  &-pass {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    gap: 30px;
    &-input {
      display: flex;
      flex-direction: column;
      align-items: stretch;
      width: 100%;
      gap: 15px;
      p {
        font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
      }
      input {
        width: 100%;
        height: 64px;
        background: $white;
        border-radius: 25px;
        border: 1px solid $black;
        padding: 20px 40px;
        outline: none;
      }
    }
    button {
      font-size: 20px;
      width: 100%;
      height: 64px;
      color: $white;
      &:hover {
        background: $white;
        color: $secondary;
        border: 1px solid $secondary;
      }
    }
  }
  @media screen and (max-width: $tablet) {
    width: 100%;
  }
}

.errorValid {
  color: #f72a2a;
  font-size: 16px !important;
  padding: 8px 0;
}
.errorValidPlace {
  border: 1px solid #f72a2a !important;
}
</style>