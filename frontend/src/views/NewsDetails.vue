<template>
  <div class="news-details">
    <div class="news-details__back container">
      <button class="news-details__back-btn" @click="$router.go(-1)">
        <img src="@/assets/images/svg/arrow-return.svg" alt="arrow-return">
        <p class="light-txt">Back</p>
      </button>
    </div>
    <div class="news-details__content container">
      <div class="news-details__content-box">
        <div class="news-details__content-box-info">
          <img :src="main_image" alt="details">
          <div class="news-details__content-box-info-block">
            <div class="news-details__content-box-info-block-text">
              <p class="news-details__content-box-info-block-text-bold bold-txt">Date:</p>
              <p class="regular-txt">{{ formattedDate }}</p>
            </div>
            <div class="news-details__content-box-info-block-text">
              <p class="news-details__content-box-info-block-text-bold bold-txt">Time:</p>
              <p class="regular-txt">{{ formattedTime }}</p>
            </div>
            <div class="news-details__content-box-info-block-text">
              <p class="news-details__content-box-info-block-text-bold bold-txt">Place:</p>
              <p class="regular-txt">{{ place_of_the_event }}</p>
            </div>
          </div>
        </div>
        <div class="news-details__content-box-btn">
          <button
              :style="{ background: notificationButtonColor }"
              class="main-button"
              @click="alertNotification"
          >
            Alert me
          </button>
        </div>
      </div>

      <div class="news-details__content-main">
        <div class="news-details__content-main-title">
          <span class="light-txt">{{ getCategoryName(category_of_the_event) }}</span>
          <h2 class="medium-txt">{{ news_title }}</h2>
        </div>

        <div class="news-details__content-main-desc">
          <div class="news-details__content-main-desc-txt">
            <p class="regular-txt" v-html="news_description">
            </p>
          </div>
          <div class="news-details__content-main-desc-txt">
            <p class="bold-txt">What to expect:</p>
            <p class="regular-txt" v-html="what_to_expect">
            </p>
          </div>
          <div class="news-details__content-main-desc-txt">
            <p class="bold-txt">Registration:</p>
            <p class="regular-txt" v-html="registration">
            </p>
          </div>
          <div class="news-details__content-main-desc-txt">
            <p class="bold-txt">Additional:</p>
            <p class="regular-txt" v-html="additional_info">
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
    return {
      date_of_the_event: '',
      time_of_the_event: '',
      place_of_the_event: '',
      category_of_the_event: 0,
      news_title: '',
      news_description: '',
      what_to_expect: '',
      registration: '',
      additional_info: '',
      main_image: '',
      formattedDate: '',
      formattedTime: '',
      categories: [],
      notifications: [],
      news_id: null,
    }
  },
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
    isNotificationDisabled() {
      return this.notifications.some(notification => notification.id === this.news_id);
    },
    notificationButtonColor() {
      return this.isNotificationDisabled ? '#9C9C9C' : '#F8A46F';
    }
  },
  methods: {
    async fetchNewsDetailData(newsID) {
      await this.$axios
          .get(`news/${newsID}/`,
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            const newsDetailData = response.data;
            this.news_title = newsDetailData.news_title;
            this.news_description = newsDetailData.news_description;
            this.formattedDate = this.formatDate(newsDetailData.date_of_the_event);
            this.formattedTime = this.formatTime(newsDetailData.time_of_the_event);
            this.place_of_the_event = newsDetailData.place_of_the_event;
            this.category_of_the_event = newsDetailData.category_of_the_event;
            this.main_image = newsDetailData.main_image;
            this.what_to_expect = newsDetailData.what_to_expect;
            this.registration = newsDetailData.registration;
            this.additional_info = newsDetailData.additional_info;
            this.news_id = newsDetailData.id;
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
            this.categories = response.data;
          })
          .catch((e) => {
            console.log(e);
          });
    },
    async alertNotification() {
      if (this.isNotificationDisabled) {
        this.$toaster.error("You have already added this event to notifications");
      } else {
        await this.$axios
            .post(`follow_post/`, {
                  student_id: this.getUser.id,
                  post_id: this.news_id
                },
                {
                  headers: {
                    Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                  },
                }
            )
            .then((response) => {
              if (response.status === 200) {
                this.$toaster.success("The event has been added! Available in profile/notifications");
                window.location.reload();
              }
            })
            .catch((err) => {
              if (err.response.data.messages) {
                this.$toaster.error(err.response.data.messages[0].message);
              } else if (err.response.data.detail) {
                this.$toaster.error(err.response.data.detail);
              }
            });
      }
    },
    async fetchNotificationData() {
      await this.$axios
          .get(`get_followed_posts/`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          })
          .then((response) => {
            this.notifications = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat.id === categoryId);
      return category ? category.category_name : "";
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString('en-US', options);
    },
    formatTime(time) {
      const [hour, minute] = time.split(':');
      return `${hour}:${minute}`;
    }
  },
  async created() {
    const newsID = this.$route.params.newsID;
    await this.fetchNewsDetailData(newsID);
    await this.fetchNewsCategoryData();
    await this.fetchNotificationData();
  },
  watch: {
  }
}
</script>

<style lang="scss" scoped>
.news-details {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.4615))), 30px);
  width: 100%;
  height: 100%;
  padding: 200px 0;
  @media screen and (max-width: $desktop) {
    padding: 130px 0;
  }
  &__back {
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    width: 100%;
    &-btn {
      display: flex;
      align-items: center;
      gap: 15px;
      font-size: 20px;
      color: $grey;
    }
  }
  &__content {
    display: flex;
    align-items: flex-start;
    width: 100%;
    gap: 56px;
    @media screen and (max-width: $desktop) {
      flex-direction: column;
      gap: 24px;
    }
    &-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      width: 40%;
      gap: 30px;
      @media screen and (max-width: $desktop) {
        width: 100%;
      }
      &-info {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        img {
          max-width: 100%;
          height: auto;
          object-fit: cover;
        }
        &-block {
          width: 100%;
          padding: 20px 24px;
          border: 1px solid $black;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 10px;
          &-text {
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 20px;
            &-bold {
              width: 75px;
              height: auto;
            }
            p {
              font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
            }
          }
        }
      }
      &-btn {
        button {
          &:hover {
            color: $white;
            background: transparent;
            border: 1px solid $secondary;
          }
        }
      }
    }

    &-main {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      width: 50%;
      gap: 44px;
      @media screen and (max-width: $desktop) {
        width: 100%;
        gap: 24px;
      }
      &-title {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        @media screen and (max-width: $desktop) {
          width: 100%;
          align-items: center;
          justify-content: center;
        }
        span {
          color: $grey;
          font-size: 12px;
          font-style: italic;
          @media screen and (max-width: $desktop) {
            font-size: 16px;
            font-weight: 600;
          }
        }
      }
      &-desc {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.3692))), 28px);
        p {
          font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
        }
        &-txt {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 10px;
        }
      }
    }
  }
}
</style>