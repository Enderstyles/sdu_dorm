<template>
  <header class="header">
    <div class="header__content container">
      <div class="header__content-logo">
        <h1 class="regular-txt" @click="$router.push('/')">Logo</h1>
      </div>
      <div class="header__content-nav">
        <ul class="header__content-nav-links">
          <li class="regular-txt">News</li>
          <li class="regular-txt">Apply</li>
          <li class="regular-txt" @click="$router.push('/about')">About</li>
          <li class="regular-txt" @click="$router.push('/login')">Login</li>
          <li class="regular-txt" @click="$router.push('/personal-account')">Account</li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderVue',
  data() {
    return {
    };
  },

}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  align-items: center;
  width: 100%;
  height: 140px;
  background: $sdublue;
  color: $white;
  &__content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    &-logo {
      display: flex;
      align-items: center;
      height: 100%;
      h1 {
        font-size: 24px;
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
</style>