<template>
  <div class="container">
    <div class="notfound">
      <h1 class="bold-txt">404</h1>
      <div class="notfound__content">
        <h3 class="medium-txt">Not Found</h3>
        <router-link to="/">Return to main page</router-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {

}
</script>
<style lang="scss" scoped>
.notfound {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100lvh;
  gap: 24px;
  color: $black;
  @media screen and (max-width: $tablet) {
    flex-direction: column;
  }
  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 16px;
    a {
      color: $secondary;
    }
  }
}
</style>