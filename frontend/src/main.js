import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import axios from "axios";
import { createToaster } from "@meforma/vue-toaster";

const axiosInstance = axios.create({
    baseURL: 'http://77.243.80.198:8000/api/',
    // baseURL: 'http://localhost:8000/api/',
    params: {
        lang: store.getters.getLang
    }
})

axios.defaults.baseURL = 'http://77.243.80.198:8000/api/';
// axios.defaults.baseURL = 'http://localhost:8000/api/';
// axios.defaults.params = {
//     lang: store.getters.getLang
// }

axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');

        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }

        return config;
    },

    (error) => {
        return Promise.reject(error);
    }
);
axiosInstance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');

        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }

        return config;
    },

    (error) => {
        return Promise.reject(error);
    }
);

const app = createApp(App)
    .use(router)
    .use(store);
app.config.silent = true;
app.config.globalProperties.$axios = { ...axiosInstance }
app.config.globalProperties.$toaster = createToaster({ position: "top-right" });
app.mount("#app");
