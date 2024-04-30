import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import axios from "axios";
import { createToaster } from "@meforma/vue-toaster";

const axiosInstance = axios.create({
    // baseURL: 'https://admin.sdudorm.kz/api/',
    baseURL: 'http://localhost:8000/api/',
})

// axios.defaults.baseURL = 'https://admin.sdudorm.kz/api/';
axios.defaults.baseURL = 'http://localhost:8000/api/';

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
