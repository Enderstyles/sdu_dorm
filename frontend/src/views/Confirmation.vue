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
          <h1 class="confirmation__main_total-reservation-timer regular-txt">{{ timer }}</h1>
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
          style="width: 510px; height: 190px"
      >
        <span class="regular-txt">Go to the payment</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedBlock: parseInt(localStorage.getItem('selectedBlock')) || 0,
      selectedFloor: parseInt(localStorage.getItem('selectedFloor')) || 0,
      selectedTaraf: parseInt(localStorage.getItem('selectedTaraf')) || 0,
      selectedRoom:  parseInt(localStorage.getItem('selectedRoom')) || 0,
      selectedBed:  parseInt(localStorage.getItem('selectedBed')) || 0,
      timer: null,
      timerStart: localStorage.getItem('timerStart') ? parseInt(localStorage.getItem('timerStart')) : null
    };
  },
  computed: {
    selectedBlockLetter() {
      const blockMapping = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
      };
      return blockMapping[this.selectedBlock] || '';
    }
  },
  // beforeRouteLeave(to, from, next) {
  //   // if (to.name !== 'сonfirmation') {
  //   //   next(false);
  //   // } else {
  //   //   next();
  //   // }
  // },
  mounted() {
    this.startTimer();
  },
  beforeDestroy() {
    clearInterval(this.timerInterval);
    this.stopTimer();
  },
  methods: {
    startTimer() {
      let startTime;
      if (this.timerStart) {
        const now = Math.floor(new Date().getTime() / 1000);
        const elapsedSeconds = now - this.timerStart;
        startTime = 60 - elapsedSeconds;
      } else {
        startTime = 60;
        localStorage.setItem('timerStart', Math.floor(new Date().getTime() / 1000));
      }

      const countdown = setInterval(() => {
        startTime--;
        const minutes = Math.floor(startTime / 60);
        const remainingSeconds = startTime % 60;
        this.timer = `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
        if (startTime === 0) {
          clearInterval(countdown);
          this.$router.push('/booking');
          this.handleTimeout();
          this.$toaster.error('Your time for confirmation and payment has expired!');
        }
      }, 1000);
    },
    stopTimer() {
      clearInterval(this.timer);
      this.timer = null;
    },
    handleTimeout() {
      localStorage.removeItem('selectedBlock');
      localStorage.removeItem('selectedTaraf');
      localStorage.removeItem('selectedFloor');
      localStorage.removeItem('selectedRoom');
      localStorage.removeItem('selectedBed');
      localStorage.removeItem('timerStart');
    }
  },

}
</script>

<style lang="scss" scoped>
.confirmation {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 260px 0 80px 0;
  gap: 100px;
  width: 100%;
  height: auto;
  &__main {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
    &_info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 100px;
      width: 50%;
      height: 100%;
      &-choice {
        display: flex;
        padding: 55px 75px;
        box-sizing: border-box;
        border: 2px solid #000000;
        border-radius: 25px;
        p {
          font-size: 32px;
        }
      }
    }
    &_total {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 100px;
      width: 50%;
      height: 100%;
      &-reservation {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 100%;
        gap: 5px;
        h1 {
          font-size: 128px;
        }
      }
      &-payment {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 100%;
        gap: 35px;
        p {
          font-size: 24px;
          max-width: 60%;
          text-align: right;
        }
      }
    }
  }
}
</style>