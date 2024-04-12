import { createStore } from 'vuex'
import axios from "axios";
import router from "@/router";
import {createToaster} from "@meforma/vue-toaster";
// import i18n from "@/i18n";
const toaster = createToaster({ position: "top-right", duration: 1900 });
export default createStore({
    state: {
        auth: localStorage.getItem("access_token") ? true : false,
        user: false,
    },
    getters: {
        getAuth(state) {
            return state.auth;
        },
        getUser: (state) => state.user,
    },
    mutations: {
        SET_AUTH(state, auth) {
            state.auth = auth;
        },
        SET_USER(state, user) {
            state.user = user;
        },
        SET_USER_PROFILE(state, profileData) {
            state.user = { ...state.user, ...profileData };
        },
    },
    actions: {
        checkAuth({ commit }) {
            if (localStorage.getItem("access_token")) {
                commit("SET_AUTH", true);
            }
            else {
                commit("SET_AUTH", false);
            }
        },
        async requestUser({ commit }) {
            let token = localStorage.getItem("access_token");
            if (token) {
                try {
                    const response = await axios.get("profile/", {
                        headers: {
                            'Authorization': `Bearer ${token}`,
                        },
                    });
                    const userProfile  = response.data[0];
                    const profileData = {
                        name:
                            userProfile.first_name && userProfile.last_name
                                ?
                                `${userProfile.first_name} ${userProfile.last_name}`
                                :
                                'Not filled in',
                        headerName:
                            userProfile.first_name && userProfile.last_name
                                ?
                                `${userProfile.first_name} ${userProfile.last_name.charAt(0)}.`
                                : 'Unknown',
                        id: userProfile.student_id || 'Not filled in',
                        major: userProfile.major || 'Not filled in',
                        gender: userProfile.gender === 1 ? 'Male' : 'Female',
                        grade: userProfile.grade || 'Not filled in',
                        age: userProfile.age,
                        status: userProfile.status,
                        avatar: userProfile.profile_pic,
                        reservation: userProfile.reservation
                    };
                    commit("SET_USER_PROFILE", profileData);
                    commit("SET_AUTH", true);
                } catch (err) {
                    commit("SET_USER", false);
                    commit("SET_AUTH", false);
                    localStorage.clear();
                    router.push("/login");
                    console.log(err);
                }
            } else {
                commit("SET_USER", false);
                commit("SET_AUTH", false);
            }
        },
        async logoutUser({ commit }) {
            // try {
            //     const response = await axios.post('logout/', {
            //     }, {
            //         headers: {
            //             Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            //         },
            //         params: {
            //             refresh_token: localStorage.getItem("refresh_token")
            //         }
            //     });
            localStorage.clear();
            router.push("/login");
            commit("SET_USER", false);
            commit("SET_AUTH", false);
            // } catch (err) {
            //     if (err.response && err.response.message) {
            //         toaster.error(err.response.message);
            //     }
            // }
        },
    },
    modules: {
    }
})
