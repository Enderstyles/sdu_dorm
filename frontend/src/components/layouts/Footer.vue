<template>
  <footer class="footer">
    <div class="footer__content container">
      <div class="footer__content_maininfo">
        <div class="footer__content_maininfo-logo">
          <img src="@/assets/images/webp/sdu-white-logo.webp" alt="sdu-white-logo" @click="$router.push('/')">
        </div>
        <div class="footer__content_maininfo-location">
          <p class="regular-txt">© 2023 All rights reserved</p>
          <p class="regular-txt">Almaty region, Karasai district. <br> 040900, city of Kaskelen, st. Abylai Khan 1/1</p>
        </div>
      </div>

      <div class="footer__content_payment">
        <h2 class="regular-txt">PAYMENT DETAILS</h2>
        <div class="footer__content_payment-details">
          <p class="regular-txt">
            TOO “Dorm-service” 040900 <br>
            Almatyreg., Kaskelen, AbylaiKhan st. 1/1. <br>
            БИН: 110440021346 <br>
            IBAN: KZ626017131000016522 <br>
            БИК: KZKOKZKX <br>
            КБе 17 <br>
            АО «National Bank of Kazakhstan»
          </p>
        </div>
      </div>

      <div class="footer__content_nav">
        <ul class="footer__content_nav-links">
          <li class="regular-txt" @click="$router.push('/news')">NEWS</li>
          <li class="regular-txt" @click="$router.push('/booking')">BOOKING</li>
          <li class="regular-txt" @click="$router.push('/about')">ABOUT</li>
          <li class="regular-txt" v-if="!isAuthenticated" @click="$router.push('/login')">LOGIN</li>
          <li class="regular-txt" v-if="isAuthenticated" @click="$router.push('/personal-account')">ACCOUNT</li>
        </ul>
      </div>

      <div class="footer__content_social">
        <div class="footer__content_social-follow">
          <h2 class="regular-txt">FOLLOW US</h2>
          <div class="footer__content_social-follow-icons">
            <img src="@/assets/images/png/instagram.png" alt="insta">
            <img src="@/assets/images/png/facebook.png" alt="facebook">
            <img src="@/assets/images/png/tiktok.png" alt="tiktok">
            <img src="@/assets/images/png/telegram.png" alt="telegram">
          </div>
        </div>
        <div class="footer__content_social-connection">
          <div class="footer__content_social-connection-item">
            <img src="@/assets/images/png/phone.png" alt="phone">
            <p class="regular-txt">+7 (727) 307 95 65</p>
          </div>
          <div class="footer__content_social-connection-item">
            <img src="@/assets/images/png/mail.png" alt="mail">
            <p class="regular-txt">info@sdu.edu.kz</p>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name:'FooterVue',
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
    isAuthenticated() {
      return this.$store.getters.getAuth;
    },
  },

}
</script>

<style lang="scss" scoped>
.footer {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 64px 0;
  background: $primary;
  color: $white;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  @media screen and (max-width: $laptopSm) {
    padding: 32px 0;
  }
  &__content {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    width: 100%;
    @media screen and (max-width: $laptopSm) {
      flex-direction: column;
      align-items: center;
      gap: 25px;
    }
    &_maininfo {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: min(max(25px, calc(1.5625rem + ((1vw - 3.93px) * 1.4305))), 56px);
      @media screen and (max-width: $laptopSm) {
        width: 100%;
        padding-bottom: 25px;
        border-bottom: 1px solid $white;
      }
      &-logo {
        display: flex;
        width: 100%;
        @media screen and (max-width: $laptopSm) {
          align-items: center;
          justify-content: center;
          width: 100%;
        }
        img {
          width: min(max(100px, calc(6.25rem + ((1vw - 3.93px) * 1.8459))), 140px);
          height: 100%;
          cursor: pointer;
        }
      }
      &-location {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        @media screen and (max-width: $laptopSm) {
          align-items: center;
          justify-content: center;
          text-align: center;
          width: 100%;
        }
        p {
          font-size: 15px;
        }
      }
    }
    &_payment {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      height: 220px;
      justify-content: space-between;
      @media screen and (max-width: $laptopSm) {
        flex-direction: row;
        align-items: center;
        height: 100%;
        gap: 25px;
        width: 100%;
        padding-bottom: 25px;
        border-bottom: 1px solid $white;
      }
      h2 {
        font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
      }
      &-details {
        font-size: 17px;
      }
    }
    &_nav {
      display: flex;
      flex-direction: column;
      @media screen and (max-width: $laptopSm) {
        width: 100%;
        padding-bottom: 25px;
        border-bottom: 1px solid $white;
      }
      &-links {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        height: 220px;
        justify-content: space-between;
        @media screen and (max-width: $laptopSm) {
          width: 100%;
          height: 100%;
          flex-direction: row;
          align-items: center;
          justify-content: center;
          gap: 30px;
        }
        li {
          font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
          cursor: pointer;
          transition: opacity 0.15s linear;
          &:hover {
            padding-bottom: 5px;
            border-bottom: 1px solid $white;
          }
        }
      }
    }
    &_social {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      height: 220px;
      justify-content: space-between;
      @media screen and (max-width: $laptopSm) {
        flex-direction: row;
        height: 100%;
        gap: 30px;
        width: 100%;
        padding-bottom: 25px;
        border-bottom: 1px solid $white;
      }
      &-follow {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 30px;
        h2 {
          font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
        }
        &-icons {
          display: flex;
          align-items: center;
          gap: 10px;
        }
      }
      &-connection {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
        &-item {
          display: flex;
          align-items: center;
          gap: 10px;
        }
      }
    }
  }
}
</style>