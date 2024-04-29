<template>
  <div class="about">
    <div class="about__content">
      <div class="about__content_main">
        <div class="about__content_main-tabs container">
          <div
              class="about__content_main-tabs-button"
              v-for="about in aboutData"
              :key="about.id"
              @click="getActiveTabData(about.id)"
              :class="{ 'active': activeTab === about.id }"
          >
            <p class="regular-txt">{{ about.type }}</p>
          </div>
        </div>
        <div
            class="about__content_main-info container"
            v-if="activeTabData"
            :key="activeTabData.id"
        >
          <div class="about__content_main-info-desc">
            <p class="regular-txt">
              {{ activeTabData.description }}
            </p>
          </div>
          <div class="about__content_main-info-contacts">
            <h3 class="regular-txt">{{ activeTabData.name_of_head_of_dormitory }}</h3>
            <div class="about__content_main-info-contacts-services">
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Head of dormitory</p>
                <p class="regular-txt">{{ activeTabData.contacts_head_of_dormitory }}</p>
              </div>
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Reception/plumber services</p>
                <p class="regular-txt">{{ activeTabData.contacts_reception }}</p>
              </div>
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Medical care</p>
                <p class="regular-txt">{{ activeTabData.contacts_medical_care }}</p>
              </div>
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Security service</p>
                <p class="regular-txt">{{ activeTabData.contacts_security_service }}</p>
              </div>
            </div>
          </div>
        </div>
        <div
            class="about__content_main-slider container"
        >
          <Swiper
              :options="swiperOptions"
              :pagination="paginationOptions"
              :autoplay="true"
              :slides-per-view="1"
              :space-between="40"
              ref="swiper"
              class="swiper-about"
          >
            <Swiper-slide v-for="(img, index) in mainAboutImages" :key="index" class="swiper-about-slide">
              <img v-if="img.mainAboutImg" :src="img.mainAboutImg" alt="info-img" />
            </Swiper-slide>
          </Swiper>
          <div class="swiper-pagination"></div>
        </div>
      </div>

      <div class="about__content-info">
        <div class="about__content-info-social container">
          <div class="about__content-info-social-grid">
            <div class="about__content-info-social-grid-desc">
              <h2 class="semi-bold-txt">Social Life</h2>
              <p class="regular-txt">{{ activeTabData.social_life_description }}</p>
            </div>
            <div
                class="about__content-info-social-pic"
                v-for="(img, index) in socialImages"
                :key="index"
            >
              <img :src="img.socialImg" alt="social-life">
            </div>
          </div>
        </div>
        <div class="about__content-info-safety">
          <div class="about__content-info-safety-block container">
            <h2 class="semi-bold-txt">Safety</h2>
            <div class="about__content-info-safety-block-working">
              <div class="about__content-info-safety-block-working-details">
                <h3 class="semi-bold-txt">{{ activeTabData.safety_members }}</h3>
                <p class="regular-txt">{{ activeTabData.safety_description }}</p>
              </div>
              <div class="about__content-info-safety-block-working-details">
                <h3 class="semi-bold-txt">{{ activeTabData.working_hours }}</h3>
                <p class="regular-txt">{{ activeTabData.working_hours_description }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="about__content-info-apply">
          <button
              class="about__content-info-apply-btn main-button"
              @click="goToBooking"
          >
            <p class="regular-txt">Go to Book</p>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import SwiperCore, {Autoplay, Navigation, Pagination} from 'swiper'
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/swiper-bundle.css';
import {mapGetters} from "vuex";
SwiperCore.use([Pagination, Navigation, Autoplay]);
export default {
  components: {Swiper, SwiperSlide},
  data() {
    return {
      aboutData: [],
      activeTabData: [],
      mainAboutImages: [],
      socialImages: [],
      mainAboutImg: '',
      socialImg: '',
      activeTab: 1,
      swiperOptions: {
        loop: true,
      },
      paginationOptions: {
        el: '.swiper-pagination',
        bulletClass: 'swiper-pagination-bullet',
        clickable: true,
        renderBullet: function (index, className) {
          return '<span class="' + className + '"></span>';
        },
      },
    };
  },
  computed: {
    ...mapGetters(["getAuth"]),
    isAuthenticated() {
      return this.$store.getters.getAuth;
    },
  },
  methods: {
    fetchAboutData() {
      this.$axios
          .get(`/about/`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          })
          .then((response) => {
            this.aboutData = response.data;
            this.activeTabData = this.aboutData[0];
            this.updateMainAboutImages();
            this.updateSocialLifeImages();
          })
          .catch((error) => {
            console.error(error);
          });
    },
    getActiveTabData(tabId) {
      this.activeTab = tabId;
      this.activeTabData = this.aboutData.find(item => item.id === tabId);
      this.updateMainAboutImages();
      this.updateSocialLifeImages();
    },
    updateMainAboutImages() {
      const activeTabData = this.activeTabData;
      if (activeTabData) {
        this.mainAboutImages = [];
        for (let i = 1; i <= 5; i++) {
          const imageUrl = activeTabData[`main_image${i}`];
          if (imageUrl) {
            this.mainAboutImages.push({ mainAboutImg: imageUrl });
          }
        }
      }
    },
    updateSocialLifeImages() {
      const activeTabData = this.activeTabData;
      if (activeTabData) {
        this.socialImages = [];
        for (let i = 1; i <= 8; i++) {
          const imageUrl = activeTabData[`social_life_image${i}`];
          if (imageUrl) {
            this.socialImages.push({ socialImg: imageUrl });
          }
        }
      }
    },
    goToBooking() {
      if (this.isAuthenticated) {
        this.$router.push('/booking');
      } else {
        this.$router.push('/login');
      }
    }
  },
  created() {
    this.fetchAboutData();
  },
}
</script>

<style lang="scss" scoped>
.about {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 140px 0;
  @media screen and (max-width: $pc) {
    padding: 125px 0;
  }
  @media screen and (max-width: $desktop) {
    padding: 95px 0;
  }
  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 4.5842))), 100px);
    &_main {
      display: flex;
      flex-direction: column;
      align-items: center;
      background: $primary;
      padding: 60px 0;
      width: 100%;
      gap: min(max(25px, calc(1.5625rem + ((1vw - 3.93px) * 1.4305))), 56px);
      position: relative;
      @media screen and (max-width: $desktop) {
        padding: 40px 0;
      }
      &-tabs {
        display: flex;
        align-items: center;
        justify-content: center;
        background: $white;
        border-radius: 25px;
        width: 100%;
        gap: 32px;
        @media screen and (max-width: $tablet) {
          justify-content: space-between;
          gap: 20px;
        }
        &-button {
          display: flex;
          align-items: center;
          justify-content: center;
          width: min(max(300px, calc(18.75rem + ((1vw - 3.93px) * 4.1532))), 390px);
          height: min(max(70px, calc(4.375rem + ((1vw - 3.93px) * 0.9229))), 90px);
          margin: 5px 20px;
          cursor: pointer;
          color: $black;
          p {
            font-size: min(max(14px, calc(0.875rem + ((1vw - 3.93px) * 0.4615))), 24px);
            text-align: center;
          }
          &:hover {
            border-bottom: 6px solid $secondary;
          }
        }
      }
      &-info {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        width: 100%;
        color: $white;
        @media screen and (max-width: $desktop) {
          flex-direction: column;
          align-items: center;
          gap: 25px;
        }
        &-desc {
          max-width: 25%;
          height: auto;
          @media screen and (max-width: $laptopSm) {
            max-width: 35%;
          }
          @media screen and (max-width: $desktop) {
            max-width: 100%;
          }
          p {
            font-size: min(max(18px, calc(1.125rem + ((1vw - 3.93px) * 0.5239))), 26px);
          }
        }
        &-contacts {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: flex-start;
          max-width: 50%;
          height: auto;
          gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 1.2921))), 48px);
          @media screen and (max-width: $desktop) {
            max-width: 100%;
          }
          &-services {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.4615))), 30px);
            @media screen and (max-width: $tablet) {
              grid-template-columns: 1fr;
            }
            &-block {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              gap: 15px;
            }
          }
        }
      }
    }

    &-info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 4.5842))), 100px);
      &-social {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        &-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 30px 40px;
          @media screen and (max-width: $desktop) {
            gap: 20px 30px;
          }
          @media screen and (max-width: $mobile) {
            grid-template-columns: repeat(2, 1fr);
          }
          &-desc {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 20px;
            p {
              font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              height: 200px;
              overflow-y: auto;
              @media screen and (max-width: $desktop) {
                height: 180px;
              }
              @media screen and (max-width: $tablet) {
                height: 130px;
              }
            }
          }
        }
        &-pic {
          display: flex;
          align-items: center;
          width: 100%;
          height: auto;
          img {
            max-width: 100%;
            height: 293px;
            border-radius: 25px;
            object-fit: cover;
            @media screen and (max-width: $desktop) {
              height: 200px;
            }
            @media screen and (max-width: $tablet) {
              height: 150px;
            }
          }
        }
      }
      &-safety {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 390px;
        background: #FAFBFF;
        @media screen and (max-width: $desktop) {
          height: auto;
          padding: 40px 0;
        }
        &-block {
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: 50px;
          width: 100%;
          @media screen and (max-width: $laptopSm) {
            flex-direction: column;
            align-items: center;
            gap: 30px;
          }
          &-working {
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;
            width: 100%;
            gap: 80px;
            @media screen and (max-width: $desktop) {
              justify-content: space-between;
              gap: 30px;
            }
            @media screen and (max-width: $mobile) {
              flex-direction: column;
              align-items: center;
              justify-content: center;
            }
            &-details {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              max-width: 440px;
              height: auto;
              gap: min(max(15px, calc(0.9375rem + ((1vw - 3.93px) * 0.6922))), 30px);
              @media screen and (max-width: $mobile) {
                align-items: center;
                justify-content: center;
              }
              p {
                font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
                @media screen and (max-width: $mobile) {
                  text-align: center;
                }
              }
            }
          }
        }
      }
      &-apply {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        &-btn {
          width: min(max(200px, calc(12.5rem + ((1vw - 3.93px) * 11.5367))), 450px);
          height: min(max(90px, calc(5.625rem + ((1vw - 3.93px) * 4.6147))), 190px);
          color: $white;
          p {
            font-size: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.9229))), 40px);
          }
        }
      }
    }
  }
}

.swiper-about {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}
.swiper-about-slide {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 25px !important;
  width: 100% !important;
  height: min(max(250px, calc(15.625rem + ((1vw - 3.93px) * 14.3055))), 560px);
  margin-bottom: 80px;
  img {
    max-width: 100%;
    height: min(max(250px, calc(15.625rem + ((1vw - 3.93px) * 14.3055))), 560px);
    object-fit: cover;
    border-radius: 25px;
  }
}
.swiper-pagination {
  margin-bottom: 60px;
}
.active {
  border-bottom: 6px solid $secondary;
}
</style>