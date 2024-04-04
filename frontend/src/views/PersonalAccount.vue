<template>
  <div class="account">
    <div class="account__content container">
      <div class="account__content-info">
        <div class="account__content-info-profile">
          <div class="account__content-info-profile-nav">
            <div class="account__content-info-profile-nav-pic">
              <img
                  :src="getUser.avatar"
                  alt="avatar"
              >
              <h3 class="semi-bold-txt">{{ getUser.name }}</h3>
            </div>
            <div class="account__content-info-profile-nav-board">
              <div
                  class="account__content-info-profile-nav-board-link"
                  @click.stop="profileBoard"
                  :class="{ 'activeBoard': profile === true }"
              >
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M33.3332 35V31.6667C33.3332 29.8986 32.6308 28.2029 31.3806 26.9526C30.1303 25.7024 28.4346 25 26.6665 25H13.3332C11.5651 25 9.86937 25.7024 8.61913 26.9526C7.36888 28.2029 6.6665 29.8986 6.6665 31.6667V35" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M20.0002 18.3333C23.6821 18.3333 26.6668 15.3486 26.6668 11.6667C26.6668 7.98477 23.6821 5 20.0002 5C16.3183 5 13.3335 7.98477 13.3335 11.6667C13.3335 15.3486 16.3183 18.3333 20.0002 18.3333Z" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <p class="regular-txt">Profile</p>
              </div>
              <div
                  class="account__content-info-profile-nav-board-link"
                  @click.stop="notifBoard"
                  :class="{ 'activeBoard': notif === true }"
              >
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M30 13.3333C30 10.6812 28.9464 8.13762 27.0711 6.26226C25.1957 4.3869 22.6522 3.33333 20 3.33333C17.3478 3.33333 14.8043 4.3869 12.9289 6.26226C11.0536 8.13762 10 10.6812 10 13.3333C10 25 5 28.3333 5 28.3333H35C35 28.3333 30 25 30 13.3333Z" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M22.8829 35C22.5899 35.5051 22.1693 35.9244 21.6633 36.2159C21.1572 36.5073 20.5835 36.6608 19.9995 36.6608C19.4156 36.6608 18.8419 36.5073 18.3358 36.2159C17.8298 35.9244 17.4092 35.5051 17.1162 35" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <p class="regular-txt">Notifications</p>
                <span v-if="notifData.length > 0"></span>
              </div>
              <div
                  class="account__content-info-profile-nav-board-link"
                  @click.stop="bookingBoard"
                  :class="{ 'activeBoard': booking === true }"
              >
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M20 13.3333C28.2843 13.3333 35 11.0948 35 8.33334C35 5.57192 28.2843 3.33334 20 3.33334C11.7157 3.33334 5 5.57192 5 8.33334C5 11.0948 11.7157 13.3333 20 13.3333Z" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M35 20C35 22.7667 28.3333 25 20 25C11.6667 25 5 22.7667 5 20" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M5 8.33334V31.6667C5 34.4333 11.6667 36.6667 20 36.6667C28.3333 36.6667 35 34.4333 35 31.6667V8.33334" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <p class="regular-txt">Booking</p>
              </div>
              <div
                  class="account__content-info-profile-nav-board-link"
                  @click.stop="logoutBoard"
                  :class="{ 'activeBoard': logout === true }"
              >
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15 35H8.33333C7.44928 35 6.60143 34.6488 5.97631 34.0237C5.35119 33.3986 5 32.5507 5 31.6667V8.33333C5 7.44928 5.35119 6.60143 5.97631 5.97631C6.60143 5.35119 7.44928 5 8.33333 5H15" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M26.6665 28.3333L34.9998 20L26.6665 11.6667" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M35 20H15" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <p class="regular-txt">Log out</p>
              </div>
            </div>
          </div>
          <div class="account__content-info-profile-infoboard">
            <template v-if="profile">
              <div class="account__content-info-profile-infoboard-general">
                <h3 class="semi-bold-txt">General Infromation:</h3>
                <div class="account__content-info-profile-infoboard-general-blank">
                  <div class="account__content-info-profile-infoboard-general-blank-form">
                    <p class="medium-txt">Student ID:</p>
                    <p class="medium-txt">Major:</p>
                    <p class="medium-txt">Gender:</p>
                    <p class="medium-txt">Grade:</p>
                    <p class="medium-txt">Age:</p>
                  </div>
                  <div class="account__content-info-profile-infoboard-general-blank-user">
                    <p class="light-txt">{{ getUser.id }}</p>
                    <p class="light-txt">{{ getUser.major }}</p>
                    <p class="light-txt">{{ getUser.gender }}</p>
                    <p class="light-txt">{{ getUser.grade }}</p>
                    <p class="light-txt">{{ getUser.age }}</p>
                  </div>
                </div>
                <div class="account__content-info-profile-infoboard-general-status">
                  <div class="account__content-info-profile-infoboard-general-status-booking">
                    <p class="medium-txt">Status of booking:</p>
                    <p class="status light-txt"><span></span> {{ getUser.status }}</p>
                  </div>
                  <button class="unfilled-button" style="width: 361px; height: 69px">Check your booking</button>
                </div>
              </div>
            </template>
            <template v-if="notif">
              <div class="account__content-info-profile-infoboard-haveNotif" v-if="notifData.length > 0">
                <NotificationBoard :notifData="notifData" :categories="categoryData"/>
              </div>
              <div class="account__content-info-profile-infoboard-noNotif" v-else>
                <div class="account__content-info-profile-infoboard-noNotif-message">
                  <p class="regular-txt">You don’t have any notifications yet</p>
                  <span class="regular-txt">Add a reminder about some news and it will appear here</span>
                </div>
                <div class="account__content-info-profile-infoboard-noNotif-btns">
                  <button class="main-button" style="width: 361px; height: 69px" @click="$router.push('/news')">Go back to news</button>
                </div>
              </div>
            </template>
            <template v-if="booking">
<!--              <div class="account__content-info-profile-infoboard-noBooking">-->
<!--                <div class="account__content-info-profile-infoboard-noBooking-message">-->
<!--                  <p class="regular-txt">You didn’t book a room yet</p>-->
<!--                  <span class="regular-txt">After booking all needed information can be found here</span>-->
<!--                </div>-->
<!--                <div class="account__content-info-profile-infoboard-noBooking-btns">-->
<!--                  <button class="main-button" style="width: 361px; height: 69px" @click="$router.push('/booking')">Go back to booking</button>-->
<!--                </div>-->
<!--              </div>-->
              <div class="account__content-info-profile-infoboard-haveBooking">
                <BookingBoard/>
              </div>
            </template>
            <template v-if="logout">
              <div class="account__content-info-profile-infoboard-logout">
                <p class="regular-txt">Are you sure to log out from this account?</p>
                <div class="account__content-info-profile-infoboard-logout-btns">
                  <button class="main-button" style="width: 361px; height: 69px" @click="logoutAcc">Yes, log out</button>
                  <button class="unfilled-button" style="width: 361px; height: 69px" @click="$router.push('/')">No, go to the main page</button>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import router from "@/router";
import NotificationBoard from "@/components/NotificationBoard.vue";
import BookingBoard from "@/components/booking/BookingBoard.vue";
export default {
  components: {BookingBoard, NotificationBoard},
  data: () => ({
    profile: false,
    notif: false,
    booking: false,
    logout: false,
    notifData: [],
    categoryData: []
  }),
  beforeRouteLeave(to, from, next) {
    const selectedTab = localStorage.getItem('selectedBoardTab');
    if (selectedTab) {
      localStorage.removeItem('selectedBoardTab');
      next();
    } else {
      next();
    }
  },
  methods: {
    ...mapActions(["requestUser", "logoutUser"]),
    profileBoard() {
      this.profile = true;
      this.notif = false;
      this.booking = false;
      this.logout = false;
      this.saveSelectedBoardTab('profile');
    },
    bookingBoard() {
      this.booking = true;
      this.notif = false;
      this.profile = false;
      this.logout = false;
      this.saveSelectedBoardTab('booking');
    },
    notifBoard() {
      this.notif = true;
      this.booking = false;
      this.profile = false;
      this.logout = false;
      this.saveSelectedBoardTab('notif');
    },
    logoutBoard() {
      this.logout = true;
      this.booking = false;
      this.profile = false;
      this.notif = false;
      this.saveSelectedBoardTab('logout');
    },
    async logoutAcc() {
      await this.logoutUser();
      this.$toaster.error("You have successfully logged out of your account");
    },
    async fetchNotificationData() {
      await this.$axios
          .get(`get_followed_posts/`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          })
          .then((response) => {
            if (response.data) {
              this.notifData = response.data;
            }
          })
          .catch((error) => {
            console.error(error);
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
    saveSelectedBoardTab(tabName) {
      localStorage.setItem('selectedBoardTab', tabName);
    },
    setSelectedBoardTabFromStorage() {
      const selectedTab = localStorage.getItem('selectedBoardTab');
      if (selectedTab) {
        this[selectedTab] = true;
      } else {
        this.profile = true;
      }
    },
  },
  computed: {
    ...mapGetters(["getUser", "getAuth"]),
  },
  created() {
    // this.requestUser();
    this.fetchNotificationData();
    this.fetchNewsCategoryData();
    this.setSelectedBoardTabFromStorage();
  },
}
</script>

<style lang="scss" scoped>
.account {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 200px 0;
  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    gap: 90px;
    &-info {
      display: flex;
      align-items: flex-start;
      width: 100%;
      &-profile {
        display: flex;
        align-items: flex-start;
        width: 100%;
        gap: 64px;
        &-nav {
          display: flex;
          flex-direction: column;
          align-items: center;
          box-sizing: border-box;
          width: 35%;
          height: 900px;
          border: 1px solid #000000;
          border-radius: 25px;
          padding: 55px 70px;
          gap: 95px;
          &-pic {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            gap: 25px;
            img {
              display: flex;
              align-items: center;
              justify-content: center;
              background: #838383;
              max-width: 100%;
              height: 172px;
              border-radius: 25px;
            }
            h3 {
               text-align: center;
            }
          }
          &-board {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 35px;
            &-link {
              display: flex;
              align-items: center;
              cursor: pointer;
              position: relative;
              width: 100%;
              gap: 15px;
              p {
                font-size: 32px;
              }
              img {
                max-width: 100%;
                height: auto;
                stroke: $black;
              }
              svg path {
              }
              span {
                content: "";
                background: #F9E423;
                width: 20px;
                height: 20px;
                aspect-ratio: 2;
                border-radius: 50%;
              }
              &:hover {
                svg path {
                  stroke: $secondary;
                }
                color: $secondary;
                border-bottom: 3px solid $secondary;
              }
            }
          }
        }
        &-infoboard {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          height: auto;
          width: 65%;
          box-sizing: border-box;
          background: #FAFBFF;
          border: 1px solid #000000;
          border-radius: 25px;
          padding: 80px;
          &-general {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 70px;
            &-blank {
              display: flex;
              align-items: flex-start;
              gap: 50px;
              p {
                font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              }
              &-form {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                width: 130px;
                gap: 23px;
              }
              &-user {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 23px;
              }
            }

            &-status {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              gap: 32px;
              &-booking {
                display: flex;
                align-items: center;
                gap: 30px;
                p {
                  font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
                }
                .status {
                  position: relative;
                  padding-left: 32px;
                  span {
                    content: "";
                    background: #6ED23F;
                    position: absolute;
                    width: 24px;
                    height: 24px;
                    top: 2px;
                    left: 0;
                    aspect-ratio: 2;
                    border-radius: 50%;
                  }
                }
              }
            }
          }

          &-logout {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            gap: 52px;
            p {
              font-size: 42px;
              text-align: center;
            }
            &-btns {
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 10px;
            }
          }

          &-noBooking {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            gap: 52px;
            &-message {
              display: flex;
              flex-direction: column;
              align-items: center;
              text-align: center;
              gap: 20px;
              p {
                font-size: 42px;
              }
              span {
                font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              }
            }
            &-btns {
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 10px;
            }
          }

          &-noNotif {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            gap: 60px;
            &-message {
              display: flex;
              flex-direction: column;
              align-items: center;
              text-align: center;
              gap: 20px;
              p {
                font-size: 42px;
              }
              span {
                font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
              }
            }
            &-btns {
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 10px;
            }
          }
          &-haveNotif {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            height: 100%;
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

.activeBoard {
  svg path {
    stroke: $secondary;
  }
  color: $secondary;
  border-bottom: 3px solid $secondary;
}
</style>