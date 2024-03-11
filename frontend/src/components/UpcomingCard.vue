<template>
  <div class="upcoming-card">
    <img :src="require(`@/assets/images/png/${item.image}`)" alt="news" class="upcoming-card_pic"/>
    <div class="upcoming-card__content">
      <div class="upcoming-card__content-left">
        <div class="upcoming-card__content-left-block">
          <p class="upcoming-card__content-left-block-date regular-txt">{{ item.date }}</p>
        </div>
        <div class="upcoming-card__content-left-block">
          <p class="upcoming-card__content-left-block-location regular-txt">{{ item.location }}</p>
        </div>
      </div>
      <div class="upcoming-card__content-right">
        <div class="upcoming-card__content-right-txt">
          <h1 class="medium-txt">{{ item.title }}</h1>
          <p class="regular-txt" v-text="item.desc"></p>
        </div>
        <div class="upcoming-card__content-right-more">
          <p class="regular-txt">see more</p>
          <img src="@/assets/images/png/more.png" alt="more">
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data: () => ({}),
  props: ["item"]
}
</script>
<style lang="scss" scoped>
.upcoming-card {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  background: $white;
  border-radius: 25px;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.1));
  max-width: 510px;
  height: 500px;
  &_pic {
    max-width: 510px;
    height: auto;
    object-fit: cover;
  }
  &__content {
    display: flex;
    align-items: flex-start;
    padding: 25px;
    gap: 40px;
    &-left {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
      &-block {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 10px 20px;
        border: 2px solid $black;
        text-align: center;
        border-radius: 2px;
        width: 100%;
        &-location {
          font-size: 16px;
        }
      }
    }
    &-right {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 35px;
      &-txt {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
        h1 {
          font-size: 32px;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }
        p {
          font-size: 20px;
          display: -webkit-box;
          -webkit-line-clamp: 4;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }
      }
      &-more {
        display: flex;
        align-items: center;
        color: $secondary;
        gap: 10px;
      }
    }
  }
}
</style>