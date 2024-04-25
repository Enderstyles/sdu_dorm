<template>
  <div class="news-card">
    <img :src="item.main_image" alt="news" class="news-card_pic"/>
    <div class="news-card__content">
      <div class="news-card__content-left">
        <div class="news-card__content-left-block1">
          <p class="news-card__content-left-block1-date regular-txt">{{ formatDate(item.date_of_the_event) }}</p>
        </div>
        <div class="news-card__content-left-block2">
          <p class="news-card__content-left-block2-location regular-txt" v-if="item.place_of_the_event">
            {{ item.place_of_the_event }}
          </p>
          <p class="news-card__content-left-block2-location regular-txt" v-else>
            Not defined
          </p>
        </div>
      </div>
      <div class="news-card__content-right">
        <div class="news-card__content-right-txt">
          <div class="news-card__content-right-txt-title">
            <span class="light-txt">{{ getCategoryName(item.category_of_the_event) }}</span>
            <h3 class="medium-txt">{{ item.news_title }}</h3>
          </div>
          <p class="regular-txt" v-text="item.news_description"></p>
        </div>
        <div class="news-card__content-right-more" @click="routeToDetails(item.id)">
          <p class="regular-txt">see more</p>
          <img src="@/assets/images/png/more.png" alt="more">
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data: () => ({
  }),
  props: ["item", "categories"],
  methods: {
    routeToDetails(newsID) {
      this.$router.push({ name: 'news-detail', params: { newsID: newsID } });
      console.log(newsID);
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat.id === categoryId);
      return category ? category.category_name : "";
    },
    formatDate(date) {
      const options = { month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString('en-US', options);
    },
  },
  async created() {
  },
}
</script>
<style lang="scss" scoped>
.news-card {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  background: $white;
  border-radius: 25px;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.1));
  max-width: 510px;
  height: 510px;
  z-index: 3;
  @media screen and (max-width: $pc) {
    height: 450px;
  }
  @media screen and (max-width: $tablet) {
    max-width: 100%;
  }
  &_pic {
    max-width: 100%;
    height: 40%;
    object-fit: cover;
    border-radius: 25px 25px 0 0;
  }
  &__content {
    display: flex;
    align-items: flex-start;
    padding: 25px;
    gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.9229))), 40px);
    &-left {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      border: 1px solid $primary;
      border-radius: 5px;
      width: 30%;
      height: 120px;
      gap: 10px;
      &-block1 {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: $primary;
        text-align: center;
        padding: 5px 0;
        width: 100%;
        color: $white;
        &-date {
          font-size: 16px;
          width: 100%;
        }
      }
      &-block2 {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: transparent;
        text-align: center;
        height: 100%;
        width: 100%;
        color: $primary;
        &-date {
          font-size: 12px;
          width: max-content;
        }
        &-location {
          font-size: 16px;
          padding: 10px;
        }
      }
    }
    &-right {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.6922))), 35px);
      &-txt {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
        &-title {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 5px;
          span {
            color: $grey;
            font-size: 12px;
            font-style: italic;
          }
          h3 {
            font-size: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.7859))), 32px);
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
          }
        }
        p {
          font-size: min(max(14px, calc(0.875rem + ((1vw - 3.93px) * 0.3929))), 20px);
          display: -webkit-box;
          -webkit-line-clamp: 3;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }
      }
      &-more {
        display: flex;
        align-items: center;
        cursor: pointer;
        color: $secondary;
        gap: 10px;
      }
    }
  }
}
</style>