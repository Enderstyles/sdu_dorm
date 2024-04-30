<template>
  <div class="bookboard">
    <div class="bookboard__block">
      <h3 class="medium-txt">Reserved place</h3>
      <div class="bookboard__block_info">
        <div
            class="bookboard__block_info-place"
            v-for="place in myPlace"
            :key="place"
        >
          <div class="bookboard__block_info-place-content">
            <div class="bookboard__block_info-place-content-border">
              <p class="medium-txt">Block</p>
            </div>
            <p class="semi-bold-txt">{{ blockLetters(place.block) }}</p>
          </div>
          <div class="bookboard__block_info-place-content">
            <div class="bookboard__block_info-place-content-border">
              <p class="medium-txt">Floor</p>
            </div>
            <p class="semi-bold-txt">{{ place.floor }}</p>
          </div>
          <div class="bookboard__block_info-place-content">
            <div class="bookboard__block_info-place-content-border">
              <p class="medium-txt">Taraf</p>
            </div>
            <p class="semi-bold-txt">{{ place.taraf }}</p>
          </div>
          <div class="bookboard__block_info-place-content">
            <div class="bookboard__block_info-place-content-border">
              <p class="medium-txt">Room</p>
            </div>
            <p class="semi-bold-txt">{{ place.room }}</p>
          </div>
          <div class="bookboard__block_info-place-content">
            <div class="bookboard__block_info-place-content-border">
              <p class="medium-txt">Bed</p>
            </div>
            <p class="semi-bold-txt">{{ place.place }}</p>
          </div>
        </div>

        <div class="bookboard__block_info-status">
          <div class="bookboard__block_info-status-booking">
            <div class="bookboard__block_info-status-booking-response">
              <p class="medium-txt">Status:</p>
              <p class="status light-txt"><span></span> {{ getUser.status }}</p>
            </div>
            <p class="regular-txt">
              Congratulations! Your application has been approved, and your booking for the dormitory room has been confirmed.
            </p>
          </div>
          <button
              class="unfilled-button"
              @click="cancelReservation"
          >
            Cancel reservation
          </button>
        </div>
      </div>
    </div>
    <div class="bookboard__block">
      <h3 class="medium-txt">Settle:</h3>
      <p class="regular-txt">You can settle down from 25 August</p>
    </div>
    <div class="bookboard__block">
      <h3 class="medium-txt">Payment:</h3>
      <p class="regular-txt">You paid 470 000kzt for 1 semester. No dept</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: ['myPlace'],
  data: () => ({
  }),
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
  },
  methods: {
    blockLetters(block) {
      const blockMapping = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
      };
      return blockMapping[block] || '';
    },
    async cancelReservation() {
      await this.$axios
          .post(`cancel_reservation/`, {},
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            this.$toaster.success('Your reservation has been cancelled successfully!');
            this.$router.push("/booking");
          })
          .catch((err) => {
            console.log(err);
          });
    }
  },
  created() {
  }
}
</script>

<style lang="scss" scoped>
.bookboard {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 36px;
  &__block {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
    p {
      font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
    }
    &_info {
      display: flex;
      align-items: flex-start;
      gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 4.5842))), 100px);
      @media screen and (max-width: $laptopSm) {
        flex-direction: column;
      }
      @media screen and (max-width: $desktop) {
        flex-direction: row;
      }
      @media screen and (max-width: $mobile) {
        flex-direction: column;
      }
      &-place {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
        &-content {
          display: flex;
          align-items: center;
          gap: 20px;
          &-border {
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid $black;
            border-radius: 5px;
            width: 125px;
            height: 50px;
          }
        }
      }

      &-status {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 1.8459))), 70px);
        button {
          width: 303px;
          height: 69px;
          @media screen and (max-width: $desktop) {
            width: 200px;
            height: 40px;
            padding: 10px;
          }
        }
        &-booking {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 15px;
          &-response {
            display: flex;
            align-items: center;
            gap: 30px;
            .status {
              position: relative;
              padding-left: 32px;
              span {
                content: "";
                background: #6ED23F;
                position: absolute;
                width: 24px;
                height: 24px;
                top: 2px;
                left: 0;
                aspect-ratio: 2;
                border-radius: 50%;
              }
            }
          }
          p {
            font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
          }
        }
      }
    }
  }
}
</style>