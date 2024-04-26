import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/Home.vue'
import LoginPage from "@/views/Login.vue";
import AboutPage from "@/views/About.vue";
import PersonalAccount from "@/views/PersonalAccount.vue";
import News from "@/views/News.vue";
import NewsDetails from "@/views/NewsDetails.vue";
import Booking from "@/views/Booking.vue";
import store from "@/store";
import Confirmation from "@/views/Confirmation.vue";
import NotFound from "@/views/NotFound.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/about',
        name: 'about',
        component: AboutPage
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/personal-account',
        name: 'personal-account',
        component: PersonalAccount
    },
    {
        path: '/booking',
        name: 'booking',
        component: Booking
    },
    {
        path: '/confirmation',
        name: 'confirmation',
        component: Confirmation,
    },
    {
        path: '/news',
        name: 'news',
        component: News,
    },
    {
        path: '/news/:newsID',
        name: 'news-detail',
        component: NewsDetails,
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'not-found',
        component: NotFound
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
    scrollBehavior() {
        document.getElementById('app').scrollIntoView({ behavior: 'smooth' });
    },
})

router.beforeEach((to, from, next) => {
    if (localStorage.getItem('access_token')) {
        if (to.name === 'login') {
            next('/');
        } else {
            next();
        }
    } else {
        if (to.meta.requiresAuth) {
            if (store.getters.getAuth) {
                next();
            } else {
                next('/login');
            }
        } else {
            next();
        }
    }
});

export default router;
