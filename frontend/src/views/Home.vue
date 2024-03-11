<template>
  <div class="home">
    <div class="home__content">
      <div
          class="home__content-main"
          :style="{ backgroundImage: `url('${mainBanner}')` }"
      >
        <div class="home__content-main-info container">
          <h1 class="extra-bold-txt">{{ mainTitle }}</h1>
          <p class="regular-txt">
            {{ mainDesc }}
          </p>
          <button class="main-button" @click="$router.push('/')">See details</button>
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
            <button class="home__content-upcoming-view-title-btn">See All</button>
          </div>
          <div class="home__content-upcoming-view-events">
            <Swiper
                :slides-per-view="3"
                :space-between="40"
                :navigation="{
                  nextEl: '.swiper-button-next',
                  prevEl: '.swiper-button-prev'
                }"
                :breakpoints="{
                }"
                class="swiper-container"
            >
              <SwiperSlide
                  v-for="item in upcomingData"
                  :key="item.id"
              >
                <UpcomingCard :item="item" />
              </SwiperSlide>
            </Swiper>
            <div class="swiper-button-prev"><img src="@/assets/images/svg/arrow-left.svg" alt="left"></div>
            <div class="swiper-button-next"><img src="@/assets/images/svg/arrow-right.svg" alt="right"></div>
          </div>
        </div>
      </div>

      <div class="home__content-requirements container">
        <div class="home__content-requirements-deadlines">
          <div class="home__content-requirements-deadlines-title">
            <h3 class="semi-bold-txt">{{ deadlinesTitle }}</h3>
          </div>
          <div class="home__content-requirements-deadlines-info">
            <ul class="home__content-requirements-deadlines-info-list">
              <li class="regular-txt">Applications are accepted till August 25.</li>
              <li class="regular-txt">Student house check-in – August 28</li>
            </ul>
            <p class="regular-txt">The number of places at the dormitory are limited. 1st year students are given priority when allocating the places. Students of 2, 3, 4 years can submit their applications after August 25.</p>
          </div>
        </div>

        <div class="home__content-requirements-docs">
          <div class="home__content-requirements-docs-title">
            <h3 class="semi-bold-txt">{{ docsTitle }}</h3>
          </div>
          <ul class="home__content-requirements-docs-list">
            <li class="regular-txt">3х4cm sized 2 photos;</li>
            <li class="regular-txt">Copy of Medical №075</li>
            <li class="regular-txt">Copy of National ID;</li>
            <li class="regular-txt">Copy of payment invoice.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UpcomingCard from "@/components/UpcomingCard.vue";
import { Swiper, SwiperSlide } from 'swiper/vue';
import SwiperCore, { Navigation, Pagination, Autoplay } from 'swiper'
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/swiper-bundle.css';
SwiperCore.use([Navigation, Pagination, Autoplay]);
export default {
  name: "HomeVue",
  components: { Swiper, SwiperSlide, UpcomingCard },
  data() {
    return {
      furnitureData: [
        { icon: 'beds.png', count: 4, info: 'Beds' },
        { icon: 'desks.png', count: 2, info: 'Writing desks' },
        { icon: 'shelves.png', count: 4, info: 'Book shelves' },
        { icon: 'cupboards.png', count: 4, info: 'Storage cupboards' },
      ],
      featureData: [
        { icon: 'kitchen.png', feature: 'Kitchen' },
        { icon: 'canteen.png', feature: 'Canteen' },
        { icon: 'laundry.png', feature: 'Laundry' },
        { icon: 'ironing.png', feature: 'Ironing room' },
        { icon: 'lounge.png', feature: 'Lounge room' },
        { icon: 'reading.png', feature: 'Reading room' },
        { icon: 'medical.png', feature: 'Medical service' },
        { icon: 'gym.png', feature: 'Gym' },
        { icon: 'billiard.png', feature: 'Billiard' },
        { icon: 'chess.png', feature: 'Chess' },
        { icon: 'tennis.png', feature: 'Tennis' },
        { icon: 'basketball.png', feature: 'Basketball court' },
        { icon: 'football.png', feature: 'Football court' },
        { icon: 'volleyball.png', feature: 'Volleyball court' },
      ],
      upcomingData: [
        {
          image: 'upcoming-img1.png',
          title: 'Club Fair',
          desc: 'This event allows you to apply and gain any information about university clubs',
          date: '8 February',
          location: 'on campus'
        },
        {
          image: 'upcoming-img2.png',
          title: 'Workshop “Investments in  IT”',
          desc: 'Here we are going to show how to attract investments on your project.',
          date: '23 February',
          location: 'online'
        },
        {
          image: 'upcoming-img3.png',
          title: 'Football',
          desc: 'This event allows you to apply and gain any information about university clubs',
          date: '8 February',
          location: 'on campus'
        },
        {
          image: 'upcoming-img3.png',
          title: 'Football',
          desc: 'This event allows you to apply and gain any information about university clubs',
          date: '8 February',
          location: 'on campus'
        }
      ],
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
            ]
          })
          .catch((e) => {
            console.log(e);
          });
    }
  },
  async created() {
    await this.fetchMainPageData();
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
    gap: 150px;
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
      &-info {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        height: 100%;
        gap: 30px;
        p {
          font-size: 24px;
          text-align: center;
          width: 60%;
        }
      }
    }

    &-rooms {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 100px;
      &-statistics {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 55px;
        h1 {
          font-style: italic;
        }
        p {
          font-size: 32px;
        }
      }
    }

    &-information {
      display: flex;
      align-items: flex-start;
      gap: 120px;
      margin-top: 20px;
      &-desc {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 35%;
        gap: 34px;
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
            font-size: 24px;
          }
        }
      }
      &-picture {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 730px;
        height: auto;
        position: relative;
        .swiper-info {
          width: 100%;
          height: 100%;
        }
        .swiper-info-slide {
          display: flex;
          align-items: flex-start;
          justify-content: center;
          width: auto;
          max-height: 555px;
          margin-bottom: 50px;
        }
        img {
          width: auto;
          max-height: 555px;
          object-fit: cover;
          margin-bottom: 70px;
          border-radius: 25px;
        }
      }
    }

    &-facilities {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      gap: 77px;
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
        gap: 60px;
        width: 100%;
        height: 100%;
        img {
          max-width: 100%;
          height: auto;
        }
        &-furniture {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          &-block {
            display: flex;
            align-items: flex-start;
            justify-content: center;
            width: max-content;
            gap: 25px;
            &-info {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              height: max-content;
              width: 30%;
              gap: 5px;
              p {
                font-size: 24px;
              }
            }
          }
        }
        &-features {
          display: grid;
          grid-template-columns: repeat(7, 1fr);
          gap: 40px 60px;
          &-block {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: max-content;
            gap: 25px;
            p {
              font-size: 24px;
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
      height: 910px;
      &-view {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        position: relative;
        gap: 60px;
        &-title {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          button {
            font-size: 24px;
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
            width: 100%;
            height: 510px;
            margin-bottom: 100px;
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
            img {
              width: 50px;
              height: 50px;
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
            img {
              width: 50px;
              height: 50px;
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
      &-deadlines {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 55px;
        width: 50%;
        &-title {
          width: 100%;
          h3 {
            padding-bottom: 5px;
            border-bottom: 1px solid $secondary;
            width: 230px;
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
        gap: 55px;
        width: 25%;
        &-title {
          display: flex;
          align-items: flex-end;
          h3 {
            padding-bottom: 5px;
            border-bottom: 1px solid $secondary;
            width: 300px;
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