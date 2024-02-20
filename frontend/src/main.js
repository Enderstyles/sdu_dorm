import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import { createToaster } from "@meforma/vue-toaster";

const app = createApp(App)
    .use(router)
    .use(store);
app.config.silent = true;
// app.config.globalProperties.$axios = { ...axiosInstance }
app.config.globalProperties.$toaster = createToaster({ position: "top-right" });
app.mount("#app");
