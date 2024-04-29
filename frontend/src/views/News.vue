<template>
  <div class="news">
    <div class="news__view container">
      <div class="news__view_feed">
        <div class="news__view_feed-filter">
          <div class="news__view_feed-filter-burger">
            <div
                @click.prevent="showNewsFilter"
                :class="{ 'burger-active': isBurgerActive }"
                class="news__view_feed-filter-burger-icon"
            >
              <div>
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
          <div
              class="news__view_feed-filter-form"
              :class="{ 'mobile-form': isBurgerActive }"
          >
            <div class="news__view_feed-filter-form-input">
              <p class="regular-txt">From:</p>
              <input type="date" v-model="fromDate">
            </div>
            <div class="news__view_feed-filter-form-input">
              <p class="regular-txt">Until:</p>
              <input type="date" lang="en-EN" v-model="untilDate">
            </div>
            <div class="news__view_feed-filter-form-input">
              <select name="category" v-model="category">
                <option value="all" class="regular-txt">All categories</option>
                <option v-for="cat in categoryData" :key="cat.id" :value="cat.id" class="regular-txt">{{ cat.category_name }}</option>
              </select>
            </div>
          </div>
          <div class="news__view_feed-filter-search">
            <button
                class="news__view_feed-filter-search-btn"
                @click.prevent="filterNews"
            >
            </button>
            <p
                class="news__view_feed-filter-search-reset regular-txt"
                v-if="filterSearch"
                @click="resetFilterDate"
            >
              Reset
            </p>
          </div>
        </div>



        <div class="news__view_results">
          <p class="regular-txt">{{ results }} results, {{ displayedPageNumbers.length }} pages</p>
        </div>

        <div class="news__view_feed-content">
          <div
              class="news__view_feed-content-posts"
              v-for="item in paginatedNewsData"
              :key="item.id"
          >
            <h2 v-if="newsData.length === 0">No news found.</h2>
            <NewsCard :item="item" :categories="categoryData"/>
          </div>
        </div>

        <div class="news__view_feed-content-pages">
          <div class="news__view_feed-content-pages-btn">
            <button
                v-for="pageNumber in displayedPageNumbers"
                :key="pageNumber"
                class="news__view_feed-content-pages-btn-num"
                @click="goToPage(pageNumber)"
                :class="{'activePage': pageNumber === currentPage}"
            >
              <span class="regular-txt">{{ pageNumber }}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NewsCard from "@/components/NewsCard.vue";

export default {
  components: { NewsCard },
  data() {
    return {
      newsData: [],
      categoryData: [],
      sortedNewsData: [],
      results: 0,
      pages: 1,
      currentPage: 1,
      pageSize: 12,
      category: 'all',
      fromDate: null,
      untilDate: null,
      filterSearch: false,
      isBurgerActive: false,
    }
  },
  beforeRouteLeave(to, from, next) {
    if (this.currentPage) {
      localStorage.removeItem('currentPage');
      next();
    }
  },
  computed: {
    paginatedNewsData() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.sortedNewsData.slice(startIndex, endIndex);
    },
    sortedNewsByDate() {
      let sortNews = this.sortedNewsData;
      sortNews = this.newsData.slice();
      return sortNews.sort((a, b) => {
        return new Date(a.date_of_the_event) - new Date(b.date_of_the_event);
      });
    },
    displayedPageNumbers() {
      const totalPages = Math.ceil(this.results / this.pageSize);
      const maxDisplayedPages = 5; // Максимальное количество кнопок для отображения
      let startPage = Math.max(1, this.currentPage - Math.floor(maxDisplayedPages / 2));
      let endPage = Math.min(totalPages, startPage + maxDisplayedPages - 1);

      if (endPage - startPage + 1 < maxDisplayedPages) {
        startPage = Math.max(1, endPage - maxDisplayedPages + 1);
      }

      return Array.from({ length: endPage - startPage + 1 }, (_, index) => startPage + index);
    },
  },
  methods: {
    async fetchNewsPageData() {
      await this.$axios
          .get('news/',
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            this.newsData = response.data;
            this.results = this.newsData.length;
            this.sortedNewsData = this.sortedNewsByDate;
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
    filterNewsByDate() {
      if (!this.fromDate || !this.untilDate) {
        return this.newsData;
      }
      this.filterSearch = true;
      const fromDate = new Date(this.fromDate);
      const untilDate = new Date(this.untilDate);

      return this.newsData.filter((item) => {
        const eventDate = new Date(item.date_of_the_event);
        return eventDate >= fromDate && eventDate <= untilDate;
      });
    },
    filterNews() {
      this.sortedNewsData = this.filterNewsByDate();
      if (this.category !== 'all') {
        this.sortedNewsData = this.sortedNewsData.filter((item) => {
          return item.category_of_the_event === this.category;
        });
      }
    },
    resetFilterDate() {
      this.fromDate = null;
      this.untilDate = null;
      this.category = 'all';
      this.filterSearch = false;
      this.sortedNewsData = this.sortedNewsByDate;
    },
    goToPage(pageNumber) {
      this.currentPage = pageNumber;
      this.savePageToLocalStorage();
    },
    showNewsFilter() {
      return this.isBurgerActive = !this.isBurgerActive,
          this.openMarsh = false
    },
    savePageToLocalStorage() {
      localStorage.setItem('currentPage', this.currentPage);
    },
    loadPageFromLocalStorage() {
      const storedPage = localStorage.getItem('currentPage');
      this.currentPage = storedPage ? parseInt(storedPage) : 1;
    },
  },
  async created() {
    await this.fetchNewsPageData();
    await this.fetchNewsCategoryData();
    await this.loadPageFromLocalStorage();
  },
}
</script>

<style lang="scss" scoped>
.news {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 200px 0;
  @media screen and (max-width: $desktop) {
    padding: 130px 0;
  }
  &__view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 24px;
    width: 100%;
    &_results {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
    }
    &_feed {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      width: 100%;
      &-filter {
        display: flex;
        align-items: center;
        justify-content: center;
        background: $primary;
        border-radius: 25px;
        width: 100%;
        padding: 40px;
        gap: min(max(30px, calc(1.875rem + ((1vw - 3.93px) * 3.2303))), 100px);
        color: $white;
        @media screen and (max-width: $desktop) {
          justify-content: space-between;
        }
        &-burger {
          display: none;
          &-icon {
            display: block;
            width: 30px;
            height: 30px;
            position: relative;
            cursor: pointer;
            span {
              transition: all .3s ease 0s;
              top: calc(50% - 2px);
              left: 0;
              position: absolute;
              width: 100%;
              height: 2px;
              background-color: $secondary;
              border: 2px solid $secondary;
              border-radius: 25px;
              &:first-child {
                top: 0;
              }
              &:last-child {
                top: auto;
                bottom: 0;
              }
            }
          }
          @media screen and (max-width: $desktop) {
            display: flex;
            align-items: flex-start;
            width: auto;
          }
        }
        &-form {
          display: flex;
          align-items: center;
          gap: 30px;
          @media screen and (max-width: $desktop) {
            display: none;
          }
          &-input {
            display: flex;
            align-items: center;
            width: 100%;
            gap: 10px;
            p {
              font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
            }
            input {
              width: min(max(130px, calc(8.125rem + ((1vw - 3.93px) * 3.2303))), 200px);
              height: 50px;
              padding: 10px 15px;
              border-radius: 25px;
              font-size: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.3692))), 20px);
              cursor: pointer;
              @media screen and (max-width: $desktop) {
                width: 100%;
              }
            }
            select {
              width: min(max(130px, calc(8.125rem + ((1vw - 3.93px) * 3.2303))), 200px);
              height: 50px;
              padding: 10px 15px;
              border-radius: 25px;
              margin-left: 30px;
              font-size: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.3692))), 20px);
              outline: none;
              cursor: pointer;
              option {
                cursor: pointer;
              }
              @media screen and (max-width: $laptopSm) {
                margin-left: 0;
              }
              @media screen and (max-width: $desktop) {
                width: 100%;
              }
            }
          }
        }
        &-search {
          display: flex;
          align-items: center;
          gap: 15px;
          &-btn {
            position: relative;
            width: 80px;
            height: 50px;
            border-radius: 25px;
            transition-duration: 500ms;
            cursor: pointer;
            font-size: 18px;
            background: $secondary;
            overflow: hidden;
            background-image: url('@/assets/images/png/search.png');
            background-repeat: no-repeat;
            background-size: 28px;
            background-position: 50%;
          }
          &-reset {
            font-size: 20px;
            cursor: pointer;
          }
        }
      }
      &-content {
        display: flex;
        align-items: flex-start;
        justify-content: center;
        flex-wrap: wrap;
        gap: 60px 40px;
        width: 100%;
        margin: 35px 0;
        @media screen and (max-width: $laptopSm) {
          gap: 40px 20px;
        }
        &-posts {
          display: flex;
          align-items: center;
          justify-content: center;
          width: auto;
          gap: 40px;
          &-pic {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            position: relative;
            gap: 10px;
            &-img {
              width: 440px;
              height: 400px;
              background: #D9D9D9;
            }
            &-date {
              display: flex;
              align-items: center;
              justify-content: center;
              background: $white;
              width: 162px;
              height: 39px;
              position: absolute;
              top: 16px;
              left: 0;
            }
          }
          &-desc {
            display: flex;
            flex-direction: column;
            width: 100%;
            p {
              font-size: 32px;
            }
          }
        }
        &-pages {
          display: flex;
          align-items: center;
          justify-content: center;
          padding-top: 30px;
          width: 100%;
          &-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            &-num {
              display: flex;
              align-items: center;
              justify-content: center;
              width: 52px;
              height: 49px;
              color: $primary;
              background: transparent;
              border: 1px solid $primary;
              border-radius: 5px;
              p {
                font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              }
              &:hover {
                color: $white;
                background: $primary;
              }
            }
          }
        }
      }
    }
  }
}

.mobile-form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 50%;
  gap: 20px;
}

.activePage {
  color: $white;
  background: $primary;
}

.news-card {
  width: min(max(300px, calc(18.75rem + ((1vw - 3.93px) * 4.6147))), 400px);
  min-height: 0vw;
}
</style>