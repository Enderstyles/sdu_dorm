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
          <button class="about__content-info-apply-btn main-button" @click="$router.push('/booking')">
            <p class="regular-txt">Go to Book</p>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import SwiperCore, { Pagination } from 'swiper'
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/swiper-bundle.css';
SwiperCore.use([Pagination]);
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
        autoplay: {
          delay: 5000,
          disableOnInteraction: false,
        },
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
  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    gap: 100px;
    &_main {
      display: flex;
      flex-direction: column;
      align-items: center;
      background: $primary;
      padding: 85px 0 65px 0;
      gap: 65px;
      position: relative;
      &-tabs {
        display: flex;
        align-items: center;
        justify-content: center;
        background: $white;
        border-radius: 25px;
        width: 100%;
        gap: 35px;
        &-button {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 390px;
          height: 90px;
          margin: 5px 20px;
          cursor: pointer;
          color: $black;
          p {
            font-size: 24px;
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
        &-desc {
          max-width: 370px;
          height: auto;
          p {
            font-size: 26px;
          }
        }
        &-contacts {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: flex-start;
          max-width: 735px;
          height: auto;
          gap: 50px;
          &-services {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
          }
        }
      }
    }

    &-info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 100px;
      &-social {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        &-grid {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr;
          gap: 30px 40px;
          &-desc {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 20px;
            p {
              font-size: 24px;
              height: 200px;
              overflow-y: auto;
            }
          }
          &-pic {
            display: flex;
            align-items: center;
            img {
              max-width: 100%;
              height: auto;
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
        margin-top: 100px;
        &-block {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          &-working {
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;
            width: 100%;
            gap: 80px;
            &-details {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              max-width: 440px;
              height: auto;
              gap: 30px;
              p {
                font-size: 24px;
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
          width: 510px;
          height: 190px;
          color: $white;
          p {
            font-size: 40px;
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
  height: 560px !important;
  margin-bottom: 80px;
  img {
    max-width: 100%;
    height: 560px;
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