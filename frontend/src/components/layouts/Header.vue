<template>
  <header class="header" :class="{'login': $route.path === '/login'}">
    <div class="header__content container">
      <div class="header__content-logo">
        <img src="@/assets/images/png/sdu-logo.png" alt="sdu-logo" @click="$router.push('/')">
      </div>
      <div class="header__content-nav">
        <ul class="header__content-nav-links">
          <li class="regular-txt">News</li>
          <li class="regular-txt">Apply</li>
          <li class="regular-txt" @click="$router.push('/about')">About</li>
          <li class="regular-txt" v-if="!isAuthenticated" @click="$router.push('/login')">Login</li>
          <li class="regular-txt" v-if="isAuthenticated" @click="$router.push('/personal-account')">Account</li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
import {mapGetters} from "vuex";
export default {
  name: 'HeaderVue',
  data() {
    return {
    };
  },
  methods: {
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
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 193px;
  background: #FAFBFF;
  color: $primary;
  border-radius: 0 0 50px 50px;
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
        width: 126px;
        height: 100%;
        cursor: pointer;
      }
    }
    &-nav {
      display: flex;
      &-links {
        display: flex;
        align-items: center;
        gap: 72px;
        li {
          font-size: 24px;
          cursor: pointer;
        }
      }
    }
  }
}
.login {
  display: none;
}
</style>