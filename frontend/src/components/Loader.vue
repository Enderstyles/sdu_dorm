<template>
  <div class="loader container">
    <div class="spinner"></div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.loader {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100lvh;
}
.spinner {
  position: relative;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.spinner::before,
.spinner::after {
  border: 6.7px solid $primary;
  border-radius: 50%;
  position: absolute;
  content: '';
  display: block;
}

.spinner::before {
  width: 33.6px;
  height: 33.6px;
  border-bottom-color: transparent;
  border-left-color: transparent;
  animation: spinner-1o3y8q 0.75s infinite linear reverse;
}

.spinner::after {
  animation: spinner-1o3y8q 0.5s infinite linear;
  height: 56px;
  width: 56px;
  border-right-color: transparent;
  border-top-color: transparent;
}

@keyframes spinner-1o3y8q {
  to {
    transform: rotate(360deg);
  }
}
</style>