<template>
  <div class="news">
    <div class="news__view container">
      <p class="news__view_results regular-txt">65 results, 5 pages</p>
      <div class="news__view_feed">
        <div class="news__view_feed-filter">
          <h2 class="semi-bold-txt">Filter</h2>
          <div class="news__view_feed-filter-form">
            <div class="news__view_feed-filter-form-input">
              <p class="regular-txt">Starting from:</p>
              <input type="text">
            </div>
            <div class="news__view_feed-filter-form-input">
              <p class="regular-txt">Ending until:</p>
              <input type="text">
            </div>
            <button class="news__view_feed-filter-form-btn">Apply</button>
          </div>
        </div>
        <div class="news__view_feed-content">
          <div class="news__view_feed-content-block">
            <div class="news__view_feed-content-block-pic">
              <div class="news__view_feed-content-block-pic-img"></div>
              <div class="news__view_feed-content-block-pic-date">February 23</div>
              <p class="light-txt">Event</p>
            </div>
            <div class="news__view_feed-content-block-desc">
              <p class="regular-txt">
                Description Description Des Description Description
              </p>
            </div>
          </div>

          <div class="news__view_feed-content-block">
            <div class="news__view_feed-content-block-pic">
              <div class="news__view_feed-content-block-pic-img"></div>
              <div class="news__view_feed-content-block-pic-date">February 23</div>
              <p class="light-txt">Event</p>
            </div>
            <div class="news__view_feed-content-block-desc">
              <p class="regular-txt">
                Description Description Des Description Description
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewsVue",
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
      align-items: flex-start;
      width: 100%;
    }
    &_feed {
      display: flex;
      align-items: flex-start;
      gap: 75px;
      width: 100%;
      &-filter {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        background: #F1F1F1;
        padding: 40px 21px;
        gap: 45px;
        h2 {
          font-size: 36px;
        }
        &-form {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 22px;
          &-input {
            display: flex;
            flex-direction: column;
            gap: 10px;
            p {
              font-size: 24px;
            }
            input {
              width: 180px;
              height: 50px;
              padding: 15px 10px;
              border: 1px solid $black;
            }
          }
          &-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 180px;
            height: 50px;
            margin-top: 15px;
            background: #C1C1C1;
          }
        }
      }

      &-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 75px 100px;
        &-block {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 20px;
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
      }
    }
  }
}
</style>