<template>
  <header class="header" :class="{'login': $route.path === '/login'}">
    <div class="header__content container">
      <div class="header__content-logo">
        <img src="@/assets/images/png/sdu-logo.png" alt="sdu-logo" @click="$router.push('/')">
      </div>
      <div class="header__content-nav">
        <ul class="header__content-nav-links">
          <li
              class="medium-txt"
              @click="$router.push('/news')"
              :class="{ 'active': $route.path === '/news' }"
          >
            News
          </li>
          <li
              class="medium-txt"
              @click="$router.push('/apply')"
              :class="{ 'active': $route.path === '/apply' }"
          >
            Booking
          </li>
          <li
              class="medium-txt"
              @click="$router.push('/about')"
              :class="{ 'active': $route.path === '/about' }"
          >
            About
          </li>
          <li
              class="medium-txt"
              v-if="!isAuthenticated"
              @click="$router.push('/login')"
              :class="{ 'active': $route.path === '/login' }"
          >
            Login
          </li>
          <li
              class="medium-txt"
              v-if="isAuthenticated"
              @click="$router.push('/personal-account')"
              :class="{ 'active': $route.path === '/personal-account' }"
          >
            {{ getUser.headerName || Account }}
          </li>
        </ul>
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
    };
  },
  methods: {
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
        width: 100px;
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
          &:hover {
            border-bottom: 1px solid $secondary;
          }
        }
      }
    }
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