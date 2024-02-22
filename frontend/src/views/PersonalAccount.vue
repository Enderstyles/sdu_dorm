<template>
  <div class="account">
    <div class="account__content container">
      <div class="account__content-info">
        <div class="account__content-info-profile">
          <div class="account__content-info-profile-pic">
            <img
                :src="
                getUser.avatar
                  ? getUser.avatar
                  : require('@/assets/images/svg/user-add.svg')
              " alt="avatar"
            >
          </div>
          <div class="account__content-info-profile-user">
            <div class="account__content-info-profile-user-form">
              <p class="medium-txt">Name Surname</p>
              <p class="medium-txt">Id</p>
              <p class="medium-txt">Major</p>
              <p class="medium-txt">Gender</p>
              <p class="medium-txt">Grade</p>
              <p class="medium-txt">Status <span></span></p>
            </div>
            <div class="account__content-info-profile-user-student">
              <p class="light-txt">{{ getUser.name }}</p>
              <p class="light-txt">{{ getUser.id }}</p>
              <p class="light-txt">{{ getUser.major }}</p>
              <p class="light-txt">{{ getUser.gender }}</p>
              <p class="light-txt">{{ getUser.grade }}</p>
              <p class="light-txt">{{ getUser.status }} <span></span></p>
            </div>
          </div>
        </div>
        <div class="account__content-info-reservation">
          <div class="account__content-info-reservation-room">
            <h1 class="medium-txt">My reservation</h1>
            <p class="light-txt">{{ getUser.reservation }}</p>
          </div>
          <div class="account__content-info-reservation-btns">
            <button class="account__content-info-reservation-btns-modify">Modify</button>
            <button class="account__content-info-reservation-btns-cancel">Cancel</button>
          </div>
        </div>
      </div>
      <div class="account__content-reservation">
        <h2 class="regular-txt">Additional information:</h2>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
export default {
  data: () => ({
  }),
  methods: {
    ...mapActions(["requestUser"]),
  },
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
  },
  created() {
    this.requestUser();
  },
}
</script>

<style lang="scss" scoped>
.account {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  margin: 160px 0;
  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    gap: 90px;
    &-info {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      width: 100%;
      &-profile {
        display: flex;
        align-items: flex-start;
        gap: 90px;
        &-pic {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 242px;
          height: 289px;
          background: #D9D9D9;
          img {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 289px;
          }
        }
        &-user {
          display: flex;
          align-items: flex-start;
          gap: 50px;
          &-form {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: space-between;
            height: 289px;
          }
          &-student {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: space-between;
            height: 289px;
          }
        }
      }
      &-reservation {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: space-between;
        height: 289px;
        &-room {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 15px;
          h1 {
            font-size: 48px;
          }
          p {
            font-size: 32px;
          }
        }
        &-btns {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 15px;
          &-modify {
            padding: 20px 70px;
            background: #B7B7B7;
            color: $black;
          }
          &-cancel {
            padding: 20px 70px;
            background: #FFFFFF;
            color: $black;
            border: 1px solid $black;
          }
        }
      }
    }
  }
}
</style>