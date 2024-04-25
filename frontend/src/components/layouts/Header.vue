<template>
  <header class="header" :class="{'login': $route.path === '/login'}">
    <div class="header__content container">
      <div class="header__content-logo">
        <img src="@/assets/images/webp/sdu-logo.webp" alt="sdu-logo" @click="$router.push('/')">
      </div>
      <div class="header__content-nav">
        <ul class="header__content-nav-links">
          <router-link
              class="medium-txt"
              to="/news"
              :class="{ 'active': $route.path === '/news' }"
          >
            News
          </router-link>
          <router-link
              class="medium-txt"
              v-if="isAuthenticated"
              to="/booking"
              :class="{ 'active': $route.path === '/booking' }"
          >
            Booking
          </router-link>
          <router-link
              class="medium-txt"
              v-if="!isAuthenticated"
              to="/login"
          >
            Booking
          </router-link>
          <router-link
              class="medium-txt"
              to="/about"
              :class="{ 'active': $route.path === '/about' }"
          >
            About
          </router-link>
          <router-link
              class="medium-txt"
              v-if="!isAuthenticated"
              to="/login"
              :class="{ 'active': $route.path === '/login' }"
          >
            Login
          </router-link>
          <router-link
              class="medium-txt"
              v-if="isAuthenticated"
              to="/personal-account"
              :class="{ 'active': $route.path === '/personal-account' }"
          >
            {{ getUser.headerName || Account }}
          </router-link>
        </ul>
      </div>
    </div>
  </header>

  <header class="header-mobile">
    <div class="header-mobile__nav container">
      <div class="header-mobile__nav_top">
        <div class="header-mobile__nav_top_logo" @click="$router.push('/')">
          <img src="@/assets/images/webp/sdu-logo.webp" alt="sdu-logo">
        </div>
        <div class="header-mobile__nav_top_profile">
          <div class="header-mobile__nav_top_profile-burger">
            <div
                @click.prevent="showBurgerMenu"
                :class="{ 'burger-active': isBurgerActive }"
                class="header-mobile__nav_top_profile-burger-icon"
            >
              <div>
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
          class="header-mobile__nav_links"
          :class="{'header-mobile__botactive': isBurgerActive}"
      >
        <div class="header-mobile__nav_links-block">
          <router-link
              :class="{'active': $route.path === '/news'}"
              to="/news"
              class="header__nav_links-block-item medium-txt"
          >
            News
          </router-link>
          <router-link
              :class="{'active': $route.path === '/booking'}"
              to="/booking"
              class="header__nav_links-block-item medium-txt"
          >
            Booking
          </router-link>
          <router-link
              :class="{'active': $route.path === '/about'}"
              to="/about"
              class="header__nav_links-block-item medium-txt"
          >
            About
          </router-link>
          <router-link
              :class="{'active': $route.path === '/login'}"
              v-if="!isAuthenticated"
              to="/login"
              class="header__nav_links-block-item medium-txt"
          >
            Login
          </router-link>
          <router-link
              :class="{'active': $route.path === '/personal-account'}"
              v-if="isAuthenticated"
              to="/personal-account"
              class="header__nav_links-block-item medium-txt"
          >
            {{ getUser.headerName || Account }}
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
export default {
  name: 'HeaderVue',
  data() {
    return {
      isBurgerActive: false,
    };
  },
  methods: {
    showBurgerMenu() {
      return this.isBurgerActive = !this.isBurgerActive,
          this.openMarsh = false
    },
  },
  computed: {
    ...mapActions(["requestUser"]),
    ...mapGetters(["getUser", "getAuth"]),
    isAuthenticated() {
      return this.$store.getters.getAuth;
    },
  },
  created() {
    this.requestUser;
  }
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  padding: 20px 0;
  background: #FAFBFF;
  color: $primary;
  border-radius: 0 0 50px 50px;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  z-index: 999;
  @media screen and (max-width: $tablet) {
    display: none;
  }
  &__content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 0px 10px;
    &-logo {
      display: flex;
      align-items: center;
      height: 100%;
      img {
        width: min(max(50px, calc(3.125rem + ((1vw - 3.93px) * 3.2744))), 100px);
        height: 100%;
        cursor: pointer;
      }
    }
    &-nav {
      display: flex;
      &-links {
        display: flex;
        align-items: center;
        gap: min(max(24px, calc(1.5rem + ((1vw - 3.93px) * 2.215))), 72px);
        a {
          font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
          cursor: pointer;
          padding-bottom: 5px;
          &:hover {
            border-bottom: 1px solid $secondary;
          }
        }
      }
    }
  }
}

.header-mobile {
  display: none;
  @media screen and (max-width: $tablet) {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    padding: 20px 0;
    background: #FAFBFF;
    color: $primary;
    border-radius: 0 0 50px 50px;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    z-index: 999;
  }
  &__nav {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    gap: 20px;
    &_top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      &_logo {
        display: flex;
        align-items: center;
        height: 100%;
        img {
          width: min(max(50px, calc(3.125rem + ((1vw - 3.93px) * 3.2744))), 100px);
          height: 100%;
          cursor: pointer;
        }
      }
      &_profile {
        display: flex;
        align-items: center;
        gap: 10px;
        &-burger {
          display: flex;
          align-items: flex-end;
          width: auto;
          &-icon {
            display: block;
            width: 30px;
            height: 30px;
            position: relative;
            cursor: pointer;
            span {
              transition: all .3s ease 0s;
              top: calc(50% - 2px);
              left: 0;
              position: absolute;
              width: 100%;
              height: 2px;
              background-color: $secondary;
              border: 2px solid $secondary;
              border-radius: 25px;
              &:first-child {
                top: 0;
              }
              &:last-child {
                top: auto;
                bottom: 0;
              }
            }
          }
        }
      }
    }

    &_links {
      display: none;
      &-block {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 100%;
        height: auto;
        gap: 15px;
      }
    }
  }
  &__botactive {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    border-top: 1px solid $primary;
    margin: 0 12px;
    padding: 20px 0;
    gap: 20px;
    width: 100%;
    height: auto;
    z-index: 100;
    color: $primary;
    transition: ease all 0.5s;
    border-radius: 0 0 10px 10px;
  }
}

.active {
  border-bottom: 1px solid $secondary;
  font-weight: 700;
}
.login {
  display: none;
}
</style>