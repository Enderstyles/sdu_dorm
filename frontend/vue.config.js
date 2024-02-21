const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: true,
  css: {
    loaderOptions: {
      sass: {
        additionalData: `@import "@/assets/styles/main.scss";` // Путь к вашему основному файлу стилей
      }
    }
  }
});
