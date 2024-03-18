<template>
  <div class="news">
    <div class="news__view container">
      <div class="news__view_feed">
        <div class="news__view_feed-filter">
          <div class="news__view_feed-filter-form">
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
      pageSize: 10,
      category: 'all',
      fromDate: null,
      untilDate: null,
      filterSearch: false,
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
      if (this.category === 'all') {
        this.sortedNewsData = this.sortedNewsByDate;
      } else {
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
  padding: 225px 0;
  &__view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 30px;
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
      gap: 30px;
      width: 100%;
      &-filter {
        display: flex;
        align-items: center;
        justify-content: center;
        background: $primary;
        border-radius: 25px;
        width: 100%;
        padding: 40px;
        gap: 100px;
        color: $white;
        &-form {
          display: flex;
          align-items: center;
          gap: 30px;
          &-input {
            display: flex;
            align-items: center;
            gap: 10px;
            p {
              font-size: 24px;
            }
            input {
              width: 200px;
              height: 50px;
              padding: 10px 15px;
              border-radius: 25px;
              font-size: 20px;
              cursor: pointer;
            }
            select {
              width: 200px;
              height: 50px;
              padding: 10px 15px;
              border-radius: 25px;
              margin-left: 30px;
              font-size: 20px;
              outline: none;
              cursor: pointer;
              option {
                cursor: pointer;
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
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 75px 100px;
        margin: 35px 0;
        &-posts {
          display: flex;
          align-items: flex-start;
          width: 100%;
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
                font-size: 24px;
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

.activePage {
  color: $white;
  background: $primary;
}

.news-card {
  width: 510px;
}
</style>