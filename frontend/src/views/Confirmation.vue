<template>
  <div class="confirmation container">
    <div class="confirmation__main">
      <div class="confirmation__main_info">
        <h1 class="regular-txt">Confirmation of applying</h1>
        <div class="confirmation__main_info-choice">
          <p class="regular-txt">
            block {{selectedBlockLetter}} - floor {{selectedTaraf}} - room {{selectedRoom}} - bed {{selectedBed}}
          </p>
        </div>
      </div>
      <div class="confirmation__main_total">
        <div class="confirmation__main_total-reservation">
          <h4 class="regular-txt">Reservation valid</h4>
          <h1 class="confirmation__main_total-reservation-timer regular-txt">{{ formattedTimer  }}</h1>
        </div>
        <div class="confirmation__main_total-payment">
          <p class="regular-txt">Pay for the place until timer ends in order to confirm your reservation</p>
          <p class="bold-txt">Total for 1 semester: 470 000 kzt</p>
        </div>
      </div>
    </div>
    <div class="confirmation__main_btn">
      <button
          class="main-button"
          @click="payment"
      >
        <span class="regular-txt">Go to the payment</span>
      </button>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
    return {
      selectedBlock: parseInt(localStorage.getItem('selectedBlock')) || 0,
      selectedFloor: parseInt(localStorage.getItem('selectedFloor')) || 0,
      selectedTaraf: parseInt(localStorage.getItem('selectedTaraf')) || 0,
      selectedRoom:  parseInt(localStorage.getItem('selectedRoom')) || 0,
      selectedBed:  parseInt(localStorage.getItem('selectedBed')) || 0,
      timerStart: localStorage.getItem('timerStart') ? parseInt(localStorage.getItem('timerStart')) : null,
      timerDuration: 600,
      timerInterval: null,
    };
  },
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
    selectedBlockLetter() {
      const blockMapping = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
      };
      return blockMapping[this.selectedBlock] || '';
    },
    formattedTimer() {
      const minutes = Math.floor(this.timerDuration / 60);
      const seconds = this.timerDuration % 60;
      return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }
  },
  // beforeRouteLeave(to, from, next) {
  //   if (localStorage.getItem('timerStart') > 0) {
  //     this.$toaster.error('You will not be able to leave this page until you have made the payment!');
  //     next(false);
  //   } else {
  //     next();
  //   }
  // },
  created() {
    if (!localStorage.getItem('timerStart')) {
      this.startTimer();
    } else {
      this.restoreTimer();
    }
    this.createPaymentObject();
  },
  beforeDestroy() {
    clearInterval(this.timerInterval);
  },
  methods: {
    startTimer() {
      this.timerStart = Date.now();
      localStorage.setItem('timerStart', this.timerStart);
      this.timerInterval = setInterval(() => {
        this.updateTimer();
      }, 1000);
    },
    restoreTimer() {
      const elapsedTime = Math.floor((Date.now() - this.timerStart) / 1000);
      this.timerDuration = Math.max(this.timerDuration - elapsedTime, 0);
      this.timerInterval = setInterval(() => {
        this.updateTimer();
      }, 1000);
    },
    updateTimer() {
      if (this.timerDuration > 0) {
        this.timerDuration--;
        localStorage.setItem('timer', this.timerDuration);
      } else {
        clearInterval(this.timerInterval);
        this.handleTimeout();
        this.$toaster.error('Your time for confirmation and payment has expired!');
        this.$router.push("/");
      }
    },
    handleTimeout() {
      localStorage.removeItem('selectedBlock');
      localStorage.removeItem('selectedTaraf');
      localStorage.removeItem('selectedFloor');
      localStorage.removeItem('selectedRoom');
      localStorage.removeItem('selectedBed');
      localStorage.removeItem('bookingStage');
      localStorage.removeItem('timer');
      localStorage.removeItem('timerStart');
    },
    payment() {
        this.$axios
          .post(`take_place/`, {
                taken_by_id: this.getUser.id,
                block: this.selectedBlock,
                floor: this.selectedFloor,
                taraf: this.selectedTaraf,
                room: this.selectedRoom,
                place: this.selectedBed,
              },
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            clearInterval(this.timerInterval);
            localStorage.setItem('timer', this.timerDuration);

              const auth = response.data.response_data;
              const invoiceID = response.data.invoiceID;
              const amount = response.data.amount;
              halyk.showPaymentWidget(
                  this.createPaymentObject(auth, invoiceID, amount),
                  (response) => {
                    if (response.success) {
                      this.$toaster.success('You have successfully purchased a place in the dormitory!');
                      this.handleTimeout();
                      this.$router.push("/");
                    } else {
                      this.$toaster.error('An error occurred with the payment');
                      this.handleTimeout();
                      this.$router.push("/booking");
                    }
                  }
              );
          })
          .catch((err) => {
            if (err.response.data.message) {
              this.$toaster.error(err.response.data.message);
            } else if (err.response.data.detail) {
              this.$toaster.error(err.response.data.detail);
            }
          });
    },
    createPaymentObject(auth, invoiceID, amount) {
      let paymentObject = {
        invoiceId: invoiceID,
        backLink: "",
        failureBackLink: "",
        postLink: "https://example.kz",
        failurePostLink: "https://example.kz",
        language: "rus",
        description: "SDU Dormitory booking system",
        accountId: "test",
        terminal: "67e34d63-102f-4bd1-898e-370781d0074d",
        amount: amount,
        currency: "KZT",
        phone: "+7 (777) 777 77 77",
        email: "example@mail.ru",
        cardSave: true, //Параметр должен передаваться как Boolean
      };
      paymentObject.auth = auth;
      return paymentObject;
    },
  },
}
</script>

<style lang="scss" scoped>
.confirmation {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 200px 0 80px 0;
  gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 3.2303))), 100px);
  width: 100%;
  height: auto;
  @media screen and (max-width: $desktop) {
    padding: 150px 0 50px 0;
  }
  &__main {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
    @media screen and (max-width: $tablet) {
      flex-direction: column;
      align-items: center;
      gap: 30px;
    }
    &_info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 4.5842))), 100px);
      width: 50%;
      height: 100%;
      @media screen and (max-width: $tablet) {
        width: 100%;
        align-items: center;
        justify-content: center;
      }
      &-choice {
        display: flex;
        padding: 55px 75px;
        box-sizing: border-box;
        border: 2px solid #000000;
        border-radius: 25px;
        p {
          font-size: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.7859))), 32px);
        }
        @media screen and (max-width: $laptopSm) {
          padding: 25px 30px;
        }
      }
    }
    &_total {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 4.5842))), 100px);
      width: 50%;
      height: 100%;
      @media screen and (max-width: $tablet) {
        width: 100%;
        align-items: center;
        justify-content: center;
        flex-direction: row;
      }
      &-reservation {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 100%;
        gap: 5px;
        @media screen and (max-width: $tablet) {
          width: 100%;
          align-items: flex-start;
          justify-content: flex-start;
        }
        h1 {
          font-size: min(max(40px, calc(2.5rem + ((1vw - 3.93px) * 5.7629))), 128px);
        }
      }
      &-payment {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 100%;
        gap: 35px;
        @media screen and (max-width: $tablet) {
          align-items: flex-end;
          justify-content: flex-end;
        }
        p {
          font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
          max-width: 60%;
          text-align: right;
          @media screen and (max-width: $tablet) {
            max-width: 100%;
          }
        }
      }
    }
    &_btn {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      button {
        width: min(max(200px, calc(12.5rem + ((1vw - 3.93px) * 13.844))), 500px);
        height: min(max(70px, calc(4.375rem + ((1vw - 3.93px) * 5.5376))), 190px);

      }
    }
  }
}
</style>