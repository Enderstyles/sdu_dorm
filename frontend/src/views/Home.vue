<template>
  <Loader v-if="loading"/>
  <div class="home" v-else>
    <div class="home__content">
      <div
          class="home__content-main"
          :style="{ backgroundImage: `url('${mainBanner}')` }"
      >
        <div class="home__content-main-back"></div>
        <div class="home__content-main-info container">
          <h1 class="extra-bold-txt">{{ mainTitle }}</h1>
          <p class="regular-txt">
            {{ mainDesc }}
          </p>
          <button class="main-button" @click="$router.push('/about')">See details</button>
        </div>
      </div>

      <div class="home__content-rooms container">
        <div class="home__content-rooms-statistics">
          <h1 class="light-txt">653</h1>
          <p class="regular-txt">
            Available rooms
          </p>
        </div>
        <div class="home__content-rooms-statistics">
          <h1 class="light-txt">547</h1>
          <p class="regular-txt">
            Occupied rooms
          </p>
        </div>
        <div class="home__content-rooms-statistics">
          <h1 class="light-txt">16547</h1>
          <p class="regular-txt">
            Students lived here
          </p>
        </div>
      </div>

      <div class="home__content-information container">
        <div class="home__content-information-desc">
          <div class="home__content-information-desc-txt">
            <h3 class="semi-bold-txt">{{ missionTitle }}</h3>
            <span></span>
            <p class="regular-txt">
              {{ missionDesc }}
            </p>
          </div>
          <div class="home__content-information-desc-txt">
            <h3 class="semi-bold-txt">{{ responseTitle }}</h3>
            <span></span>
            <p class="regular-txt">
              {{ responseDesc }}
            </p>
          </div>
        </div>
        <div class="home__content-information-picture">
          <Swiper
              :options="swiperOptions"
              :pagination="paginationOptions"
              :autoplay="true"
              :space-between="40"
              ref="swiper"
              @swiper="onSwiper"
              @slideChange="onSlideChange"
              class="swiper-info"
          >
            <Swiper-slide v-for="(img, index) in dormImages" :key="index" class="swiper-info-slide">
              <img v-if="img.dormImg" :src="img.dormImg" alt="info-img" />
            </Swiper-slide>
          </Swiper>
          <div class="swiper-pagination"></div>
        </div>
      </div>

      <div class="home__content-facilities container">
        <div class="home__content-facilities-title">
          <h2 class="semi-bold-txt">Student house facilities</h2>
        </div>
        <div class="home__content-facilities-filling">
          <div class="home__content-facilities-filling-furniture">
            <div
                class="home__content-facilities-filling-furniture-block"
                v-for="frntr in furnitureData"
                :key="frntr.id"
            >
              <img :src="require(`@/assets/icons/${frntr.icon}`)" alt="furniture">
              <div class="home__content-facilities-filling-furniture-block-info">
                <h4 class="semi-bold-txt">{{ frntr.count }}</h4>
                <p class="regular-txt">{{ frntr.info }}</p>
              </div>
            </div>
          </div>
          <div class="home__content-facilities-filling-features">
            <div
                class="home__content-facilities-filling-features-block"
                v-for="feature in featureData"
                :key="feature.id"
            >
              <img :src="require(`@/assets/icons/${feature.icon}`)" alt="furniture">
              <p class="regular-txt">{{ feature.feature }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="home__content-upcoming">
        <div class="home__content-upcoming-view container">
          <div class="home__content-upcoming-view-title">
            <h2 class="semi-bold-txt">Upcoming events</h2>
            <button
                class="home__content-upcoming-view-title-btn"
                @click="$router.push('/news')"
            >
              See All
            </button>
          </div>
          <div class="home__content-upcoming-view-events">
            <Swiper
                v-if="upcomingData.length > 2"
                :slides-per-view="3"
                :space-between="40"
                :navigation="{
                  nextEl: '.swiper-button-next',
                  prevEl: '.swiper-button-prev'
                }"
                :breakpoints="{
                  1920: {
                    slidesPerView: 3,
                    spaceBetween: 40,
                  },
                  1024: {
                    slidesPerView: 2,
                    spaceBetween: 30,
                  },
                  768: {
                    slidesPerView: 1,
                    spaceBetween: 30,
                  },
                  425: {
                    slidesPerView: 1,
                    spaceBetween: 20,
                  },
                  375: {
                    slidesPerView: 1,
                    spaceBetween: 20,
                  },
                }"
                class="swiper-container"
            >
              <SwiperSlide
                  class="swiper-slide"
                  v-for="item in upcomingData"
                  :key="item.id"
              >
                  <UpcomingCard :item="item" :categories="categoryData" />
              </SwiperSlide>
            </Swiper>
            <div class="swiper-button-prev" v-if="upcomingData.length > 2">
              <img src="@/assets/images/svg/arrow-left.svg" alt="left">
            </div>
            <div class="swiper-button-next" v-if="upcomingData.length > 2">
              <img src="@/assets/images/svg/arrow-right.svg" alt="right">
            </div>
            <h3 class="semi-bold-txt" v-else>There are no upcoming events yet</h3>
          </div>
        </div>
      </div>

      <div class="home__content-requirements container">
        <div class="home__content-requirements-deadlines">
          <div class="home__content-requirements-deadlines-title">
            <h3 class="semi-bold-txt">{{ deadlinesTitle }}</h3>
          </div>
          <div class="home__content-requirements-deadlines-info">
            <p class="regular-txt">{{ deadlinesDesc }}</p>
          </div>
        </div>

        <div class="home__content-requirements-docs">
          <div class="home__content-requirements-docs-title">
            <h3 class="semi-bold-txt">{{ docsTitle }}</h3>
          </div>
          <ul class="home__content-requirements-docs-list">
            <p class="regular-txt">{{ docsDesc }}</p>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UpcomingCard from "@/components/NewsCard.vue";
import { Swiper, SwiperSlide } from 'swiper/vue';
import SwiperCore, { Navigation, Pagination, Autoplay } from 'swiper'
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/swiper-bundle.css';
import Loader from "@/components/Loader.vue";
SwiperCore.use([Navigation, Pagination, Autoplay]);
export default {
  components: {
    Loader,
    Swiper,
    SwiperSlide,
    UpcomingCard
  },
  data() {
    return {
      furnitureData: [
        { icon: 'beds.webp', count: 4, info: 'Beds' },
        { icon: 'desks.webp', count: 2, info: 'Writing desks' },
        { icon: 'shelves.webp', count: 4, info: 'Book shelves' },
        { icon: 'cupboards.webp', count: 4, info: 'Storage cupboards' },
      ],
      featureData: [
        { icon: 'kitchen.webp', feature: 'Kitchen' },
        { icon: 'canteen.webp', feature: 'Canteen' },
        { icon: 'laundry.webp', feature: 'Laundry' },
        { icon: 'ironing.webp', feature: 'Ironing room' },
        { icon: 'lounge.webp', feature: 'Lounge room' },
        { icon: 'reading.webp', feature: 'Reading room' },
        { icon: 'medical.webp', feature: 'Medical service' },
        { icon: 'gym.webp', feature: 'Gym' },
        { icon: 'billiard.webp', feature: 'Billiard' },
        { icon: 'chess.webp', feature: 'Chess' },
        { icon: 'tennis.webp', feature: 'Tennis' },
        { icon: 'basketball.webp', feature: 'Basketball court' },
        { icon: 'football.webp', feature: 'Football court' },
        { icon: 'volleyball.webp', feature: 'Volleyball court' },
      ],
      categoryData: [],
      upcomingData: [],
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
      mainTitle: '',
      mainDesc: '',
      mainBanner: '',
      missionTitle: '',
      missionDesc: '',
      responseTitle: '',
      responseDesc: '',
      deadlinesTitle: '',
      deadlinesDesc: '',
      docsTitle: '',
      docsDesc: '',
      dormImg: '',
      dormImages: [],
      currentSlide: 0,
      loading: true,
    };
  },
  methods: {
    onSwiper(swiper) {
      this.$refs.swiper.swiper = swiper;
    },

    onSlideChange() {
      this.currentSlide = this.$refs.swiper.swiper.realIndex;
    },
    async fetchMainPageData() {
      this.loading = true;
      await this.$axios
          .get('main_page/',
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            const mainData = response.data[0];
            this.mainTitle = mainData.main_title;
            this.mainDesc = mainData.main_description;
            this.mainBanner = mainData.main_banner_img;
            this.missionTitle = mainData.mission_title;
            this.missionDesc = mainData.mission_description;
            this.responseTitle = mainData.responsibilities_title;
            this.responseDesc = mainData.responsibilities_description;
            this.deadlinesTitle = mainData.deadlines_title;
            this.deadlinesDesc = mainData.deadlines_description;
            this.docsTitle = mainData.docs_required_title;
            this.docsDesc = mainData.decs_required_description;
            this.dormImages = [
              { dormImg: mainData.dorm_image1 },
              { dormImg: mainData.dorm_image2 },
              { dormImg: mainData.dorm_image3 },
              { dormImg: mainData.dorm_image4 },
              { dormImg: mainData.dorm_image5 },
            ].filter(img => img.dormImg !== null);
          })
          .catch((e) => {
            console.log(e);
          });
    },
    async fetchNewsUpcomingData() {
      await this.$axios
          .get('news/',
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            this.upcomingData = response.data;
          })
          .catch((e) => {
            console.log(e);
          });
    },
    async fetchNewsCategoryData() {
      await this.$axios
          .get(`news_categories/`,
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            this.categoryData = response.data;
          })
          .catch((e) => {
            console.log(e);
          });
    },
  },
  async created() {
    try {
      await this.fetchMainPageData();
      await this.fetchNewsUpcomingData();
      await this.fetchNewsCategoryData();
      this.loading = false;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  },
}
</script>

<style lang="scss" scoped>
.home {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 4.5842))), 100px);
    padding-bottom: 150px;
    &-main {
      display: flex;
      flex-direction: column;
      background-position: center center;
      background-repeat: no-repeat;
      background-size: cover;
      height: 100lvh;
      width: 100%;
      color: $white;
      padding: 90px 0;
      position: relative;
      z-index: 1;
      &-back {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        background: rgba(38, 38, 38, 0.5);
        z-index: 2;
      }
      &-info {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        height: 100%;
        gap: 30px;
        z-index: 3;
        text-align: center;
        p {
          font-size: min(max(14px, calc(0.875rem + ((1vw - 3.93px) * 0.4615))), 24px);
          width: 60%;
          @media screen and (max-width: $tablet) {
            width: 100%;
          }
        }
      }
    }

    &-rooms {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 3.2303))), 100px);
      &-statistics {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: min(max(24px, calc(1.5rem + ((1vw - 3.93px) * 1.4767))), 56px);
        h1 {
          font-style: italic;
          @media screen and (max-width: $mobile) {
            font-size: 24px;
            font-weight: 800;
          }
        }
        p {
          font-size: min(max(18px, calc(1.125rem + ((1vw - 3.93px) * 0.6461))), 32px);
          text-align: center;
        }
      }
    }

    &-information {
      display: flex;
      align-items: flex-start;
      gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 4.6147))), 120px);
      margin-top: 20px;
      @media screen and (max-width: $desktop) {
        flex-direction: column;
        align-items: center;
      }
      &-desc {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 35%;
        gap: 34px;
        @media screen and (max-width: $laptopSm) {
          width: 50%;
        }
        @media screen and (max-width: $desktop) {
          width: 100%;
        }
        &-txt {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 17px;
          h3 {
            border-bottom: 2px solid $secondary;
            padding-bottom: 5px;
          }
          p {
            font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
          }
        }
      }
      &-picture {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 60%;
        height: auto;
        position: relative;
        @media screen and (max-width: $desktop) {
          width: 100%;
        }
        .swiper-info {
          width: 100%;
          height: 100%;
          display: flex;
          align-items: center;
        }
        .swiper-info-slide {
          display: flex;
          align-items: flex-start;
          justify-content: center;
          border-radius: 25px !important;
          width: auto;
          max-height: 555px !important;
          margin-bottom: 50px;
        }
        img {
          width: 100%;
          max-height: 555px;
          object-fit: cover;
          margin-bottom: 70px;
          border-radius: 25px;
          @media screen and (max-width: $laptopSm) {
            margin-bottom: 50px;
          }
          @media screen and (max-width: $mobile) {
            margin-bottom: 25px;
          }
        }
      }
    }

    &-facilities {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 2.6195))), 60px);
      &-title {
        display: flex;
        justify-content: flex-start;
        width: 100%;
      }
      &-filling {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 2.6195))), 60px);
        width: 100%;
        height: 100%;
        &-furniture {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          @media screen and (max-width: $desktop) {
            align-items: flex-start;
          }
          &-block {
            display: flex;
            align-items: flex-start;
            justify-content: center;
            width: max-content;
            gap: min(max(15px, calc(0.9375rem + ((1vw - 3.93px) * 0.4615))), 25px);
            @media screen and (max-width: $desktop) {
              width: 20%;
              flex-direction: column;
              align-items: center;
            }
            img {
              @media screen and (max-width: $laptopSm) {
                height: 90px;
              }
              @media screen and (max-width: $desktop) {
                width: 75px;
                height: 75px;
              }
              @media screen and (max-width: $tablet) {
                width: 65px;
                height: 65px;
              }
            }
            &-info {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              height: max-content;
              width: 30%;
              gap: 5px;
              @media screen and (max-width: $desktop) {
                width: 100%;
                align-items: center;
                justify-content: center;
              }
              p {
                font-size: min(max(14px, calc(0.875rem + ((1vw - 3.93px) * 0.4615))), 24px);
                @media screen and (max-width: $desktop) {
                  text-align: center;
                }
              }
            }
          }
        }
        &-features {
          display: grid;
          grid-template-columns: repeat(7, 1fr);
          gap: 40px 60px;
          @media screen and (max-width: $laptopSm) {
            grid-template-columns: repeat(6, 1fr);
          }
          @media screen and (max-width: $desktop) {
            grid-template-columns: repeat(5, 1fr);
            gap: 30px 50px;
          }
          @media screen and (max-width: $tablet) {
            grid-template-columns: repeat(4, 1fr);
            gap: 20px 40px;
          }
          @media screen and (max-width: $mobile) {
            grid-template-columns: repeat(3, 1fr);
            gap: 15px 30px;
          }
          &-block {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: max-content;
            gap: 25px;
            img {
              max-width: 100%;
              height: auto;
              @media screen and (max-width: $laptopSm) {
                max-width: 70%;
              }
              @media screen and (max-width: $tablet) {
                max-width: 50%;
              }
            }
            p {
              font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              text-align: center;
            }
          }
        }
      }
    }

    &-upcoming {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      background: #FAFBFF;
      padding: 80px 0 170px 0;
      width: 100%;
      height: auto;
      @media screen and (max-width: $pc) {
        padding: 60px 0 80px 0;
      }
      @media screen and (max-width: $desktop) {
        padding: 30px 0 40px 0;
      }
      &-view {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        position: relative;
        width: 100%;
        gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 1.3844))), 60px);
        &-title {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          button {
            font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
            border-bottom: 1px solid $secondary;
          }
        }
        &-events {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 100%;
          height: 100%;
          .swiper-container {
            display: flex;
            align-items: flex-start;
            justify-content: flex-start;
            max-width: 100%;
            height: auto;
            margin-bottom: 100px;
            @media screen and (max-width: $pc) {
              margin-bottom: 50px;
            }
            @media screen and (max-width: $desktop) {
              margin-bottom: 25px;
            }
          }
          .swiper-wrapper {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            max-width: 100%;
            height: 520px;
            gap: 40px;
            z-index: 1;
          }
          .swiper-slide {
            width: 100%;
            height: 520px;
          }
          .swiper-button-prev {
            position: absolute;
            top: auto;
            bottom: 0;
            left: 0;
            border: 3px solid $grey;
            border-radius: 50%;
            padding: 40px;
            z-index: 999;
            @media screen and (max-width: $laptopSm) {
              padding: 30px;
            }
            @media screen and (max-width: $desktop) {
              padding: 20px;
            }
            img {
              width: 50px;
              height: 50px;
              @media screen and (max-width: $laptopSm) {
                width: 40px;
                height: 40px;
              }
              @media screen and (max-width: $desktop) {
                width: 30px;
                height: 30px;
              }
              @media screen and (max-width: $tablet) {
                width: 25px;
                height: 25px;
              }
            }
            &:after {
              display: none;
            }
          }
          .swiper-button-next {
            position: absolute;
            top: auto;
            bottom: 0;
            left: 100px;
            border: 3px solid $secondary;
            border-radius: 50%;
            padding: 40px;
            z-index: 999;
            @media screen and (max-width: $laptopSm) {
              padding: 30px;
              left: 70px;
            }
            @media screen and (max-width: $desktop) {
              padding: 20px;
              left: 50px;
            }
            img {
              width: 50px;
              height: 50px;
              @media screen and (max-width: $laptopSm) {
                width: 40px;
                height: 40px;
              }
              @media screen and (max-width: $desktop) {
                width: 30px;
                height: 30px;
              }
              @media screen and (max-width: $tablet) {
                width: 25px;
                height: 25px;
              }
            }
            &:after {
              display: none;
            }
          }
        }
      }
    }

    &-requirements {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      width: 100%;
      @media screen and (max-width: $desktop) {
        flex-direction: column;
        align-items: center;
        gap: 30px;
      }
      &-deadlines {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.5538))), 32px);
        width: 50%;
        @media screen and (max-width: $desktop) {
          width: 100%;
        }
        &-title {
          h3 {
            padding-bottom: 5px;
            border-bottom: 1px solid $secondary;
            width: 230px;
            @media screen and (max-width: $laptopSm) {
              width: 100%;
            }
          }
        }
        &-info {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 20px;
          ul li {
            list-style: disc;
            margin-left: 20px;
          }
        }
      }
      &-docs {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.5538))), 32px);
        width: 25%;
        @media screen and (max-width: $desktop) {
          width: 100%;
        }
        &-title {
          display: flex;
          align-items: flex-end;
          h3 {
            padding-bottom: 5px;
            border-bottom: 1px solid $secondary;
            width: 300px;
            @media screen and (max-width: $laptopSm) {
              width: 100%;
            }
          }
        }
        ul li {
          list-style: disc;
          margin-left: 20px;
        }
      }
    }
  }
}
</style>