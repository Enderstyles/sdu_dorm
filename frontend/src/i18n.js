import { createI18n } from "vue-i18n";

let appLanguage = 'en'
if (localStorage.getItem("lang")) {
    appLanguage = localStorage.getItem("lang")
} else {
    appLanguage = navigator.language.startsWith("ru") ? 'ru' : navigator.language.startsWith("kk") ? 'kz' : 'ru'
}
export default createI18n({
    locale: appLanguage,
    fallbackLocale: "ru",
    messages: {
        ru: require("./locales/ru.json"),
        kz: require("./locales/kz.json"),
    },
});