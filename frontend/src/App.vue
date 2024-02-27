<template>
  <div class="main">
    <Header />
      <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from './components/layouts/Header.vue';
import Footer from './components/layouts/Footer.vue';

export default {
  name: "App",
  components:{
    Header,
    Footer
  },
};
</script>

<style lang="scss">
body {
  padding: 0;
  margin: 0;
  border: 0;
  position: relative;
}
</style>
