<template>
  <footer class="footer">
    <div class="footer__content container">
      <div class="footer__content_maininfo">
        <div class="footer__content_maininfo-logo">
          <img src="@/assets/images/png/sdu-white-logo.png" alt="sdu-white-logo" @click="$router.push('/')">
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
  padding: 60px 0 220px 0;
  background: $primary;
  color: $white;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  &__content {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    width: 100%;
    &_maininfo {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 66px;
      &-logo {
        display: flex;
        width: 100%;
        img {
          width: 140px;
          height: 100%;
          cursor: pointer;
        }
      }
      &-location {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
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
      h2 {
        font-size: 24px;
      }
      &-details {
        font-size: 17px;
      }
    }
    &_nav {
      display: flex;
      flex-direction: column;
      &-links {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        height: 220px;
        justify-content: space-between;
        li {
          font-size: 24px;
          cursor: pointer;
        }
      }
    }
    &_social {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      height: 220px;
      justify-content: space-between;
      &-follow {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 30px;
        h2 {
          font-size: 24px;
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