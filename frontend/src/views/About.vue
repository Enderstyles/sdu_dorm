<template>
  <div class="about">
    <div class="about__content">
      <div class="about__content_main">
        <div class="about__content_main-tabs container">
          <div
              class="about__content_main-tabs-button"
              v-for="about in aboutData"
              :key="about.id"
              @click="activeTab = about.id"
              :class="{ 'active': activeTab === about.id }"
          >
            <p class="regular-txt">{{ about.type }}</p>
          </div>
        </div>
        <div
            v-if="activeAbout"
            class="about__content_main-info container"
            :key="activeAbout.id"
        >
          <div class="about__content_main-info-desc">
            <p class="regular-txt">
              {{ activeAbout.description }}
            </p>
          </div>
          <div class="about__content_main-info-contacts">
            <h3 class="regular-txt">{{ activeAbout.name_of_head_of_dormitory }}</h3>
            <div class="about__content_main-info-contacts-services">
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Head of boys’ dormitory</p>
                <p class="regular-txt">{{ activeAbout.contacts_head_of_dormitory }}</p>
              </div>
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Reception/plumber services</p>
                <p class="regular-txt">{{ activeAbout.contacts_reception }}</p>
              </div>
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Medical care</p>
                <p class="regular-txt">{{ activeAbout.contacts_medical_care }}</p>
              </div>
              <div class="about__content_main-info-contacts-services-block">
                <p class="bold-txt">Security service</p>
                <p class="regular-txt">{{ activeAbout.contacts_security_service }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="about__content_main-slider">
          <Swiper
              :options="swiperOptions"
              :pagination="paginationOptions"
              :slides-per-view="1"
              :space-between="40"
              ref="swiper"
              class="swiper-info"
          >
            <Swiper-slide v-for="(img, index) in mainAboutImages" :key="index" class="swiper-info-slide">
              <img v-if="img.mainAboutImg" :src="img.mainAboutImg" alt="info-img" />
            </Swiper-slide>
          </Swiper>
          <div class="swiper-pagination"></div>
        </div>
      </div>

      <div class="about__content-apply">
        <button class="about__content-apply-btn">
          <p class="regular-txt">Go to Book</p>
        </button>
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
      mainAboutImages: [],
      mainAboutImg: '',
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
    activeAbout() {
      return this.aboutData.find(item => item.id === this.activeTab);
    }
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
            this.activeAbout = response.data;
            this.mainAboutImages = [];
            for (let i = 1; i <= 5; i++) {
              const imageUrl = response.data[`main_image${i}`];
              if (imageUrl) {
                this.mainAboutImages.push(imageUrl);
              }
            }
          })
          .catch((error) => {
            console.error(error);
          });
    },
  },
  created() {
    this.fetchAboutData();
    console.log(this.mainAboutImages);
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

    &-data {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      gap: 144px;
      &-block {
        display: flex;
        align-items: flex-start;
        gap: 65px;
        &-desc {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 54px;
          h1 {
            font-size: 48px;
          }
          p {
            font-size: 24px;
          }
        }
        &-pics {
          display: flex;
          align-items: center;
          justify-content: flex-end;
          width: 100%;
          height: 100%;
          img {
            width: 660px;
            height: 100%;
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
      margin-top: 73px;
      &-btn {
        padding: 70px 200px;
        background: #B7B7B7;
        p {
          font-size: 40px;
        }
      }
    }
  }
}
.active {
  border-bottom: 6px solid $secondary;
}
</style>