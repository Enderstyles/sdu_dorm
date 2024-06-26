<template>
  <div class="notification">
    <div class="notification__filter">
      <p class="regular-txt">Filter by:</p>
      <div class="notification__filter-form">
        <div class="notification__filter-form-btn">
          <select name="category" v-model="category" @change="filterByCategory">
            <option value="all" class="regular-txt">All Categories</option>
            <option v-for="cat in categories" :key="cat.id" :value="cat.id" class="regular-txt">{{ cat.category_name }}</option>
          </select>
        </div>
        <div class="notification__filter-form-btn">
          <span
              class="notification__filter-form-btn-reset regular-txt"
              v-if="category !== 'all'"
              @click="resetFilter"
          >
            Reset
          </span>
        </div>
        <div class="notification__filter-form-btn">
          <button
              class="notification__filter-form-btn-button"
              @click="deleteSelectedNotifications"
          >
            <img src="@/assets/images/svg/delete.svg">
            <span class="regular-txt">Delete</span>
          </button>
        </div>
      </div>
      <div class="notification__filter-pages">
        <div class="notification__filter-pages-number">
          <p class="regular-txt">{{ currentPageStart }} - {{ currentPageEnd }} from {{ totalPages }}</p>
        </div>
        <div class="notification__filter-pages-navigation">
          <img src="@/assets/images/svg/notif-arrow-left.svg" alt="notif-arrow-left" @click="prevPage">
          <img src="@/assets/images/svg/notif-arrow-right.svg" alt="notif-arrow-right" @click="nextPage">
        </div>
      </div>
    </div>

    <div class="notification__content">
      <div
          class="notification__content-block"
          v-for="notification in paginatedNotifData"
          :key="notification.id"
      >
        <input
            type="checkbox"
            :value="notification.id"
            @click="chooseNotifId(notification.id)"
        >
        <div class="notification__content-block-message">
          <div class="notification__content-block-message-title">
            <div class="notification__content-block-message-title-txt">
              <p class="bold-txt">{{ notification.news_title }}</p>
              <span class="regular-txt">{{ formatDate(notification.date_of_the_event) }}</span>
            </div>
            <div
                class="notification__content-block-message-title-type"
                :style="{background: eventCategoryType(notification.category_of_the_event)}"
            >
              <p class="regular-txt">{{ getCategoryName(notification.category_of_the_event) }}</p>
            </div>
          </div>
          <div class="notification__content-block-message-desc">
            <p class="regular-txt">{{ notification.news_description }}</p>
          </div>
        </div>
        <div class="notification__content-block-clicker" @click="routeToNews(notification.id)">
          <img src="@/assets/images/svg/notif-arrow.svg" alt="notif-arrow">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data: () => ({
    currentNotifPage: 1,
    pageSize: 6,
    category: 'all',
    selectedNotifications: null,
  }),
  props: ["notifData", "categories"],
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
    currentPageStart() {
      return (this.currentNotifPage - 1) * this.pageSize + 1;
    },
    currentPageEnd() {
      return Math.min(this.currentNotifPage * this.pageSize, this.notifData.length);
    },
    totalPages() {
      return Math.ceil(this.notifData.length / this.pageSize);
    },
    paginatedNotifData() {
      let filteredNotifData = this.notifData;
      if (this.category !== 'all') {
        filteredNotifData = filteredNotifData.filter(notification => {
          return notification.category_of_the_event === this.category;
        });
      }

      const startIndex = (this.currentNotifPage - 1) * this.pageSize;
      return filteredNotifData.slice(startIndex, startIndex + this.pageSize);
    }
  },
  beforeRouteLeave(to, from, next) {
    if (this.currentNotifPage) {
      localStorage.removeItem('currentNotifPage');
      next();
    } else {
      next();
    }
  },
  methods: {
    prevPage() {
      if (this.currentNotifPage > 1) {
        this.currentNotifPage--;
        this.saveNotifPageToLocalStorage();
      }
    },
    nextPage() {
      if (this.currentNotifPage < this.totalPages) {
        this.currentNotifPage++;
        this.saveNotifPageToLocalStorage();
      }
    },
    filterByCategory() {
      this.currentNotifPage = 1;
      this.saveNotifPageToLocalStorage();
    },
    resetFilter() {
      this.category = 'all';
      this.currentNotifPage = 1;
      this.saveNotifPageToLocalStorage();
    },
    routeToNews(newsID) {
      this.$router.push({ name: 'news-detail', params: { newsID: newsID } });
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat.id === categoryId);
      return category ? category.category_name : "";
    },
    formatDate(date) {
      const options = { month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString('en-US', options);
    },
    eventCategoryType(categoryType) {
      if (categoryType === 1) {
        return "#AE2E2E";
      } else if (categoryType === 2) {
        return "#26B2EE";
      } else if (categoryType === 3) {
        return "#1386B7";
      } else {
        return "#F8A46F";
      }
    },
    chooseNotifId(notifId) {
      this.selectedNotifications = notifId;
    },
    deleteSelectedNotifications() {
      if (!this.selectedNotifications) {
        this.$toaster.error("Please select the news you want to delete");
      } else {
        this.$axios.post('unfollow_post/',
            {
              student_id: this.getUser.id,
              post_id: this.selectedNotifications
            }
        )
          .then(response => {
            window.location.reload();
            if(response.message) {
              this.$toaster.error(response.message);
            }
          })
          .catch(error => {
            console.error('Error deleting notifications:', error);
          });
        console.log('Deleting notifications:', this.selectedNotifications);
      }
    },
    saveNotifPageToLocalStorage() {
      localStorage.setItem('currentNotifPage', this.currentNotifPage);
    },
    loadNotifPageFromLocalStorage() {
      const storedPage = localStorage.getItem('currentNotifPage');
      this.currentNotifPage = storedPage ? parseInt(storedPage) : 1;
    },
  },
  async created() {
    await this.loadNotifPageFromLocalStorage();
  },
}
</script>

<style lang="scss" scoped>
.notification {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  gap: 40px;
  &__filter {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: transparent;
    width: 100%;
    height: 50px;
    gap: 25px;
    color: $black;
    @media screen and (max-width: $tablet) {
      height: auto;
      flex-direction: column;
    }
    &-form {
      display: flex;
      align-items: center;
      gap: 10px;
      //@media screen and (max-width: $tablet) {
      //  flex-direction: column;
      //  align-items: flex-start;
      //}
      &-btn {
        display: flex;
        align-items: center;
        p {
          font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
        }
        span {
          font-size: 20px;
          color: $secondary;
          cursor: pointer;
        }
        select {
          max-width: 132px;
          height: 45px;
          padding: 10px 15px;
          font-size: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.1846))), 16px);
          color: $black;
          border: 1px solid $black;
          border-radius: 5px;
          outline: none;
          cursor: pointer;
          option {
            cursor: pointer;
          }
        }
        button {
          box-sizing: border-box;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 10px 20px;
          gap: 10px;
          max-width: 132px;
          height: 45px;
          border: 1px solid $secondary;
          border-radius: 5px;
          color: $secondary;
        }
      }
    }
    &-pages {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      justify-content: flex-end;
      gap: 10px;
      @media screen and (max-width: $tablet) {
        flex-direction: row;
        gap: 15px;
      }
      &-number {
        display: flex;
        align-items: flex-end;
        color: $black;
        p {
          font-size: 16px;
          @media screen and (max-width: $tablet) {
            font-weight: 700;
          }
        }
      }
      &-navigation {
        display: flex;
        align-items: center;
        gap: 5px;
        img {
          max-width: 100%;
          height: auto;
          cursor: pointer;
        }
      }
    }
  }

  &__content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    &-block {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      height: 123px;
      box-sizing: border-box;
      padding: 0px 10px 25px 20px;
      background: $white;
      border-top: 0.3px solid #9C9C9C;
      input[type="checkbox"] {
        cursor: pointer;
        width: 40px;
        height: 40px;
        outline: none;
        background: $white;
      }
      @media screen and (max-width: $tablet) {
        height: auto;
        padding: 20px 10px;
        gap: 20px;
      }
      &-message {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 75%;
        gap: 15px;
        &-title {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          @media screen and (max-width: $tablet) {
            flex-direction: column;
            align-items: flex-start;
            gap: 15px;
          }
          &-txt {
            display: flex;
            align-items: center;
            gap: 25px;
            @media screen and (max-width: $tablet) {
              flex-direction: column;
              align-items: flex-start;
              width: 100%;
              gap: 10px;
            }
            p {
              font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              display: -webkit-box;
              -webkit-line-clamp: 1;
              -webkit-box-orient: vertical;
              overflow: hidden;
              max-width: 70%;
              @media screen and (max-width: $tablet) {
                -webkit-line-clamp: 2;
              }
            }
            span {
              font-size: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.1846))), 16px);
            }
          }
          &-type {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 10px 25px;
            gap: 10px;
            margin-left: 10px;
            width: auto;
            height: 37px;
            border-radius: 5px;
            flex: none;
            flex-grow: 0;
            color: $white;
            @media screen and (max-width: $tablet) {
              margin-left: 0;
            }
          }
        }
        &-desc {
          display: flex;
          align-items: flex-start;
          width: 100%;
          p {
            font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.1846))), 20px);
            display: -webkit-box;
            -webkit-line-clamp: 1;
            -webkit-box-orient: vertical;
            overflow: hidden;
            @media screen and (max-width: $tablet) {
              -webkit-line-clamp: 3;
            }
          }
        }
      }
      &-clicker {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        padding: 10px;
        cursor: pointer;
      }
    }
  }
}
</style>