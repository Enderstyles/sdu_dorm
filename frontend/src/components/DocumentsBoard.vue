<template>
  <div class="documents">
    <h3 class="semi-bold-txt">Upload the required Documents</h3>
    <div class="documents__form">
      <div class="documents__form-app">
        <p class="medium-txt">
          Student ID
        </p>
        <input
            type="text"
            required
            v-model="v$.student_id.$model"
            maxlength="9"
            class="documents__form-app-txtinput"
        />
        <template v-for="(error, index) of v$.student_id.$errors" :key="index">
          <p class="errorValid">{{ error.$message }}</p>
        </template>
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          3x4 Photo
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".jpg, .jpeg, .png"
            lang="en"
            @change="handleFileChange($event, 'photo')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          Identity Card
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'identity_card')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          075 Form
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'form_075')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          Payment Check
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'payment_check')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          Power of attorney
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'power_of_attorney')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          Address certificate
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'address_certificate')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          University admissions form
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'university_admission_form')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <p class="medium-txt">
          Application
        </p>
        <input
            type="file"
            name="docs"
            required
            accept=".pdf, .docs"
            lang="en"
            @change="handleFileChange($event, 'application')"
            class="documents__form-app-fileinput"
        />
      </div>
      <div class="documents__form-app">
        <button
            class="documents__form-app-btn"
            @click="saveDocs"
        >
          Save
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import {helpers, minLength, required} from "@vuelidate/validators";
import useVuelidate from "@vuelidate/core";
import {mapGetters} from "vuex";

export default {
  computed: {
    ...mapGetters(["getUser"])
  },
  props: ["docsData"],
  data: () => ({
    v$: useVuelidate(),
    student_id: "",
    files: {
      photo: null,
      identity_card: null,
      form_075: null,
      payment_check: null,
      power_of_attorney: null,
      address_certificate: null,
      university_admission_form: null,
      application: null,
    },
  }),
  validations() {
    return {
      student_id: {
        required: helpers.withMessage("Required field", required),
        minLength: helpers.withMessage('Minimum of numbers in the id: 9', minLength(9)),
      },
    };
  },
  created() {
    if (this.getUser) {
      this.student_id = this.getUser.id;
    }
  },
  methods: {
    saveDocs() {
      this.v$.student_id.$validate();
      if (!this.v$.student_id.$invalid) {
        const formData = new FormData();
        for (const key in this.files) {
          if (this.files.hasOwnProperty(key) && this.files[key]) {
            formData.append(key, this.files[key]);
          }
        }
        formData.append("student_id", this.student_id);

        this.$axios
            .post("upload_documents/", formData)
            .then((res) => {
              this.$toaster.success("Your documents have been uploaded successfully!");
              this.resetForm();

              const chooseBed = localStorage.getItem('selectedBed');
              setTimeout(() => {
                if(chooseBed) {
                  this.$router.push("/confirmation");
                } else {
                  this.$router.push("/");
                }
              }, 200);
            })
            .catch((err) => {
              if (err.data) {
                this.$toaster.error(err.data.detail);
              } else {
                this.$toaster.error("An error has occurred, try uploading again!");
              }
            });
      } else {
        this.$toaster.error("You must fill in all the fields");
      }
    },
    resetForm() {
      this.student_id = "";
    },
    handleFileChange(event, key) {
      this.files[key] = event.target.files[0];
    },
  },
}
</script>

<style lang="scss" scoped>
.documents {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.5538))), 32px);
  &__form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.5538))), 24px);
    &-app {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      width: 100%;
      gap: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.3692))), 20px);
      p {
        font-size: min(max(14px, calc(0.875rem + ((1vw - 3.93px) * 0.2769))), 20px);
      }
      &-txtinput {
        width: 100%;
        height: min(max(24px, calc(1.5rem + ((1vw - 3.93px) * 0.5538))), 36px);
        border: 1px solid $black;
        background: #F0F0F0;
        padding: 10px 15px;
        border-radius: 25px;
        color: $black;
        outline: none;
      }
      &-fileinput {
        &::-webkit-file-upload-button {
          padding: 10px 35px;
          margin-right: 20px;
          background: transparent;
          border-radius: 10px;
          border: 1px solid $black;
          color: $black;
          cursor: pointer;
          &:hover {
            background: $secondary;
            color: $white;
            border: none;
          }
        }
      }
      &-btn {
        width: 200px;
        height: 40px;
        margin-top: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: $secondary;
        font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
        border-radius: 25px;
        color: $white;
        &:hover {
          background-color: transparent;
          border: 1px solid $secondary;
          color: $secondary;
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