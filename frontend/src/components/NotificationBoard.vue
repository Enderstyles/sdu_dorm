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
<!--        <div class="notification__filter-form-btn">-->
<!--          <select name="category" v-model="category">-->
<!--            <option value="all" class="regular-txt">All categories</option>-->
<!--            <option v-for="cat in categories" :key="cat.id" :value="cat.id" class="regular-txt">{{ cat.category_name }}</option>-->
<!--          </select>-->
<!--        </div>-->
        <div class="notification__filter-form-btn">
          <button class="notification__filter-form-btn-button">
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
export default {
  data: () => ({
    currentNotifPage: 1,
    pageSize: 6,
    category: 'all'
  }),
  props: ["notifData", "categories"],
  computed: {
    // Вычисляемое свойство для определения начального и конечного индексов текущей страницы
    currentPageStart() {
      return (this.currentNotifPage - 1) * this.pageSize + 1;
    },
    currentPageEnd() {
      return Math.min(this.currentNotifPage * this.pageSize, this.notifData.length);
    },
    // Вычисляемое свойство для общего количества страниц
    totalPages() {
      return Math.ceil(this.notifData.length / this.pageSize);
    },
    // Вычисляемое свойство для пагинации данных
    paginatedNotifData() {
      // Фильтруем уведомления по категории
      let filteredNotifData = this.notifData;
      if (this.category !== 'all') {
        filteredNotifData = filteredNotifData.filter(notification => {
          return notification.category_of_the_event === this.category;
        });
      }

      // Вычисляем начальный и конечный индексы для текущей страницы
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
    &-form {
      display: flex;
      align-items: center;
      gap: 10px;
      &-btn {
        display: flex;
        align-items: center;
        p {
          font-size: 24px;
        }
        span {
          font-size: 20px;
          color: $secondary;
          cursor: pointer;
        }
        select {
          width: 132px;
          height: 100%;
          padding: 10px 15px;
          font-size: 16px;
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
          flex-direction: row;
          align-items: center;
          padding: 11px 24px;
          gap: 10px;
          width: 131px;
          height: 100%;
          border: 1px solid $secondary;
          border-radius: 5px;
          flex: none;
          flex-grow: 0;
          color: $secondary;
          margin-left: 20px;
        }
      }
    }
    &-pages {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      justify-content: flex-end;
      gap: 8px;
      &-number {
        display: flex;
        align-items: flex-end;
        color: $black;
        font-size: 16px;
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
          &-txt {
            display: flex;
            align-items: center;
            gap: 25px;
            p {
              font-size: 24px;
              display: -webkit-box;
              -webkit-line-clamp: 1;
              -webkit-box-orient: vertical;
              overflow: hidden;
              max-width: 70%;
            }
            span {
              font-size: 16px;
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
          }
        }
        &-desc {
          display: flex;
          align-items: flex-start;
          width: 100%;
          p {
            font-size: 20px;
            display: -webkit-box;
            -webkit-line-clamp: 1;
            -webkit-box-orient: vertical;
            overflow: hidden;
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