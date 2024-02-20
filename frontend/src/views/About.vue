<template>
  <div class="about">
    <div class="about__content container">
      <div class="about__content-tabs">
        <div class="about__content-tabs-button">
          <p class="regular-txt">Boys’ dormitory</p>
        </div>
        <div class="about__content-tabs-button">
          <p class="regular-txt">Girls’ dormitory</p>
        </div>
        <div class="about__content-tabs-button">
          <p class="regular-txt">Guest House</p>
        </div>
      </div>

      <div class="about__content-data">
        <div class="about__content-data-block">
          <div class="about__content-data-block-desc">
            <h1 class="semi-bold-txt">Main info</h1>
            <p class="regular-txt">
              Boys’ dormitory takes two 3 and 4-floor buildings at SDU Student house. There are 20 rooms with 4 student places on each floor. Each floor has rooms for student assistants, ready to respond. Overall each floor takes 1000 square meters, including bathrooms and showers.
            </p>
          </div>
          <div class="about__content-data-block-pics">
            <img src="@/assets/images/png/home-info-img.png" alt="home-info-img">
          </div>
        </div>

        <div class="about__content-data-block">
          <div class="about__content-data-block-pics">
            <img src="@/assets/images/png/home-info-img.png" alt="home-info-img">
          </div>
          <div class="about__content-data-block-desc">
            <h1 class="semi-bold-txt">Social life</h1>
            <p class="regular-txt">
              There are various events and competitions taking place through the year. Welcome party, Cinema parties, Dormitory cup on football, Student house party, mountain picnics, workshops and holidays are celebrated each year.
            </p>
          </div>
        </div>

        <div class="about__content-data-block">
          <div class="about__content-data-block-desc">
            <h1 class="semi-bold-txt">Safety</h1>
            <p class="regular-txt">
              SDU Student house hires about 70 staff members to provide medical, electricity, plumbing, painting, cleaning, washers, administrative and other services for students 24 hours. For students’ safety dormitory working hours are from 6.00 am to 22.00 pm with lights-off at 23.00.
            </p>
          </div>
          <div class="about__content-data-block-pics">
            <img src="@/assets/images/png/home-info-img.png" alt="home-info-img">
          </div>
        </div>
      </div>

      <div class="about__content-apply">
        <button class="about__content-apply-btn">
          <p class="regular-txt">Apply</p>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutVue",
  setup() {


    return {}
  }
}
</script>

<style lang="scss" scoped>
.about {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  margin: 60px 0;
  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    gap: 160px;
    &-tabs {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      gap: 18px;
      &-button {
        padding: 30px;
        background: #D2D2D2;
        cursor: pointer;
        p {
          font-size: 24px;
        }
      }
    }

    &-data {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      gap: 144px;
      &-block {
        display: flex;
        align-items: flex-start;
        gap: 65px;
        &-desc {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 54px;
          h1 {
            font-size: 48px;
          }
          p {
            font-size: 24px;
          }
        }
        &-pics {
          display: flex;
          align-items: center;
          justify-content: flex-end;
          width: 100%;
          height: 100%;
          img {
            width: 660px;
            height: 100%;
          }
        }
      }
    }

    &-apply {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      margin-top: 73px;
      &-btn {
        padding: 70px 200px;
        background: #B7B7B7;
        p {
          font-size: 40px;
        }
      }
    }
  }
}
</style>