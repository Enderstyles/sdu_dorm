<template>
  <div class="home">
    <div class="home__content">
      <div class="home__content-main">
        <div class="home__content-main-info container">
          <h1 class="extra-bold-txt">SDU Student house</h1>
          <p class="regular-txt">
            SDU Student House is located on the territory of the Smart Campus in the immediate vicinity of the university building (30 meters). For students and guests of the university Next to Student House is a football field, volleyball and basketball courts. 24-hour security protects the campus ensuring the safety of all students and visitors. Moreover, for VIP guests in block “A” there are two VIP rooms with amenities.
          </p>
        </div>
      </div>

      <div class="home__content-rooms container">
        <div class="home__content-rooms-statistics">
          <h1 class="regular-txt">653</h1>
          <p class="regular-txt">
            Available rooms
          </p>
        </div>
        <div class="home__content-rooms-statistics">
          <h1 class="regular-txt">547</h1>
          <p class="regular-txt">
            Occupied rooms
          </p>
        </div>
        <div class="home__content-rooms-statistics">
          <h1 class="regular-txt">16547</h1>
          <p class="regular-txt">
            Students lived here
          </p>
        </div>
      </div>

      <div class="home__content-information container">
        <div class="home__content-information-desc">
          <div class="home__content-information-desc-txt">
            <h1 class="semi-bold-txt">Our mission</h1>
            <p class="regular-txt">
              Main mission of our service team is to create a friendly atmosphere, mutual understanding of each other, and a place to live in unity where youth will be drawn to knowledge. This factor will play a decisive role in the formation of people who will develop Kazakhstan at an international level in all sectors. Our main priority is a student.
            </p>
          </div>
          <div class="home__content-information-desc-txt">
            <h1 class="semi-bold-txt">Our responsibilities</h1>
            <p class="regular-txt">
              Creating the optimal comfortable conditions for our students to stay, proper daily meals, constant psychological support, as well as a promotion of sports and outdoor activities.
            </p>
          </div>
        </div>
        <div class="home__content-information-images">
          <img src="@/assets/images/png/home-info-img.png" alt="home-info-img">
        </div>
      </div>

      <div class="home__content-facilities container">
        <div class="home__content-facilities-title">
          <h1 class="semi-bold-txt">Student house facilities</h1>
        </div>
        <div class="home__content-facilities-pictures">
          <img src="@/assets/images/png/home-facilities.png" alt="home-facilities">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeVue",
  setup() {


    return {}
  }
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
    &-main {
      display: flex;
      flex-direction: column;
      height: 90lvh;
      width: 100%;
      color: $black;
      background: #D9D9D9;
      &-info {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        height: 100%;
        gap: 30px;
        h1 {
          font-size: 96px;
        }
        p {
          font-size: 24px;
          width: 68%;
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
          font-size: 96px;
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
        width: 40%;
        gap: 34px;
        &-txt {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 17px;
          h1 {
            font-size: 36px;
          }
          p {
            font-size: 24px;
          }
        }
      }
      &-images {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 100%;
        height: 100%;
        img {
          width: 730px;
          height: 100%;
        }
      }
    }

    &-facilities {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      gap: 77px;
      margin-bottom: 150px;
      &-title {
        display: flex;
        justify-content: flex-start;
        width: 100%;
        h1 {
          font-size: 64px;
        }
      }
      &-pictures {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        img {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
}
</style>