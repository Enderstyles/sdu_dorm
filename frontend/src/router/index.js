import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/Home.vue'
import LoginPage from "@/views/Login.vue";
import AboutPage from "@/views/About.vue";
import PersonalAccount from "@/views/PersonalAccount.vue";
import News from "@/views/News.vue";
import NewsDetails from "@/views/NewsDetails.vue";
import Booking from "@/views/Booking.vue";

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
        path: '/news',
        name: 'news',
        component: News,
    },
    {
        path: '/news/:newsID',
        name: 'news-detail',
        component: NewsDetails,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
    scrollBehavior() {
        document.getElementById('app').scrollIntoView({ behavior: 'smooth' });
    },
})

// router.beforeEach((to, from, next) => {
//     // Check if the user is already authenticated
//     if (store.getters.getAuth) {
//         // If authenticated, prevent access to 'login' and 'create-account' pages
//         if (to.name === 'login') {
//             // Redirect to the home page or another appropriate page
//             next('/');
//         } else {
//             // Allow access to other routes
//             next();
//         }
//     } else {
//         // User is not authenticated, continue with the regular logic
//         // Check if the route requires authentication
//         if (to.meta.requiresAuth) {
//             // Check if the user is authenticated
//             if (store.getters.getAuth) {
//                 // User is authenticated, proceed to the route
//                 next();
//             } else {
//                 // User is not authenticated, redirect to the login page
//                 next('/login');
//             }
//         } else {
//             next();
//         }
//     }
// });

export default router;
