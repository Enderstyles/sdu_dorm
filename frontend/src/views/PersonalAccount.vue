<template>
  <div class="account">
    <div class="account__content container">
      <div class="account__content-info">
        <div class="account__content-info-profile">
          <div class="account__content-info-profile-nav">
            <div class="account__content-info-profile-nav-pic">
              <div class="account__content-info-profile-nav-pic-avatar">
                <img
                    :src="getUser.avatar"
                    alt="avatar"
                >
              </div>
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
                  @click.stop="docsBoard"
                  :class="{ 'activeBoard': documents === true }"
              >
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_1545_14817)">
                    <path d="M2.60002 35.8857L1.42859 15.8857C1.40423 15.6842 1.42308 15.4799 1.48388 15.2863C1.54468 15.0926 1.64604 14.9142 1.78121 14.7628C1.91637 14.6114 2.08224 14.4906 2.26777 14.4083C2.4533 14.326 2.65422 14.2842 2.85716 14.2857H16.0286C16.3488 14.2877 16.6595 14.3951 16.9125 14.5914C17.1656 14.7876 17.347 15.0618 17.4286 15.3714L18.5714 20H37.1429C37.3405 19.9994 37.5361 20.0397 37.7173 20.1186C37.8985 20.1974 38.0614 20.313 38.1957 20.458C38.33 20.603 38.4327 20.7743 38.4973 20.961C38.562 21.1477 38.5873 21.3459 38.5714 21.5429L37.4572 35.8286C37.3996 36.546 37.0733 37.2153 36.5436 37.7027C36.0139 38.19 35.3198 38.4594 34.6 38.4571H5.45716C4.7464 38.4607 4.05983 38.1992 3.53152 37.7237C3.0032 37.2483 2.67109 36.5929 2.60002 35.8857Z" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M9.99998 8.57145V2.85716C9.99998 2.47828 10.1505 2.11492 10.4184 1.84701C10.6863 1.5791 11.0497 1.42859 11.4285 1.42859H35.7143C36.0931 1.42859 36.4565 1.5791 36.7244 1.84701C36.9923 2.11492 37.1428 2.47828 37.1428 2.85716V14.2857" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M21.4286 8.57144H30" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  </g>
                  <defs>
                    <clipPath id="clip0_1545_14817">
                      <rect width="40" height="40" fill="white"/>
                    </clipPath>
                  </defs>
                </svg>
                <p class="regular-txt">Documents</p>
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
              <div class="account__content-info-profile-infoboard-nodata" v-else>
                <div class="account__content-info-profile-infoboard-nodata-message">
                  <p class="regular-txt">You don’t have any notifications yet</p>
                  <span class="regular-txt">Add a reminder about some news and it will appear here</span>
                </div>
                <div class="account__content-info-profile-infoboard-nodata-btns">
                  <button class="main-button" style="width: 361px; height: 69px" @click="$router.push('/news')">Go back to news</button>
                </div>
              </div>
            </template>
            <template v-if="booking">
              <div class="account__content-info-profile-infoboard-nodata" v-if="filteredMyPlace.length === 0">
                <div class="account__content-info-profile-infoboard-nodata-message">
                  <p class="regular-txt">You didn’t book a room yet</p>
                  <span class="regular-txt">After booking all needed information can be found here</span>
                </div>
                <div class="account__content-info-profile-infoboard-nodata-btns">
                  <button class="main-button" style="width: 361px; height: 69px" @click="$router.push('/booking')">Go back to booking</button>
                </div>
              </div>
              <div class="account__content-info-profile-infoboard-haveBooking" v-else>
                <BookingBoard :myPlace="filteredMyPlace"/>
              </div>
            </template>
            <template v-if="documents">
              <div class="account__content-info-profile-infoboard-docs" v-if="!docsUploaded">
                <DocumentsBoard :docsData="documentsData"/>
              </div>
              <div class="account__content-info-profile-infoboard-nodata" v-else>
                <div class="account__content-info-profile-infoboard-nodata-message">
                  <p class="regular-txt">You have already uploaded all the necessary documents</p>
                  <span class="regular-txt">You can ask the administration for all the information</span>
                </div>
                <div class="account__content-info-profile-infoboard-nodata-btns">
                  <button class="main-button" style="width: 361px; height: 69px" @click="$router.push('/')">Go to main page</button>
                </div>
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
import NotificationBoard from "@/components/NotificationBoard.vue";
import BookingBoard from "@/components/BookingBoard.vue";
import DocumentsBoard from "@/components/DocumentsBoard.vue";
export default {
  components: {DocumentsBoard, BookingBoard, NotificationBoard},
  data: () => ({
    profile: false,
    notif: false,
    booking: false,
    documents: false,
    logout: false,
    notifData: [],
    documentsData: [],
    docsUploaded: false,
    categoryData: [],
    myPlace: [],
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
      this.documents = false;
      this.logout = false;
      this.saveSelectedBoardTab('profile');
    },
    bookingBoard() {
      this.booking = true;
      this.notif = false;
      this.profile = false;
      this.documents = false;
      this.logout = false;
      this.saveSelectedBoardTab('booking');
    },
    notifBoard() {
      this.notif = true;
      this.booking = false;
      this.profile = false;
      this.documents = false;
      this.logout = false;
      this.saveSelectedBoardTab('notif');
    },
    docsBoard() {
      this.documents = true;
      this.booking = false;
      this.profile = false;
      this.notif = false;
      this.logout = false;
      this.saveSelectedBoardTab('documents');
    },
    logoutBoard() {
      this.logout = true;
      this.booking = false;
      this.profile = false;
      this.documents = false;
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
    async fetchDocumentsData() {
      await this.$axios
          .get(`get_documents/`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          })
          .then((response) => {
            if (response.data) {
              this.documentsData = response.data;
              this.docsUploaded = true;
            }
          })
          .catch((error) => {
            if (error.response.data.message) {
              this.$toaster.error(error.response.data.message);
              this.docsUploaded = false;
            }
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
    async fetchTakenPlaceData() {
      await this.$axios
          .get('get_taken_places/',
              {
                headers: {
                  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
                },
              }
          )
          .then((response) => {
            this.myPlace = response.data.filter(place => place.taken_by === this.getUser.id);
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
    filteredMyPlace() {
      return this.myPlace.filter(place => place.taken_by === this.getUser.id);
    }
  },
  created() {
    // this.requestUser();
    this.fetchNotificationData();
    this.fetchDocumentsData();
    this.fetchNewsCategoryData();
    this.fetchTakenPlaceData();
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
  padding: 200px 0 100px 0;
  @media screen and (max-width: $pc) {
    padding: 170px 0 100px 0;
  }
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
          justify-content: center;
          box-sizing: border-box;
          width: 35%;
          height: 75lvh;
          border: 1px solid #000000;
          border-radius: 25px;
          gap: min(max(20px, calc(1.25rem + ((1vw - 3.93px) * 0.5538))), 32px);
          &-pic {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            gap: min(max(12px, calc(0.75rem + ((1vw - 3.93px) * 0.5538))), 24px);
            &-avatar {
              display: flex;
              align-items: center;
              justify-content: center;
              max-width: 100%;
              height: 180px;
              border-radius: 25px;
              @media screen and (max-width: $pc) {
                height: 120px;
              }
              img {
                max-width: 100%;
                height: 180px;
                border-radius: 25px;
                @media screen and (max-width: $pc) {
                  height: 120px;
                }
              }
            }
            h3 {
               text-align: center;
            }
          }
          &-board {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.3692))), 24px);
            &-link {
              display: flex;
              align-items: center;
              cursor: pointer;
              position: relative;
              width: 100%;
              gap: 16px;
              p {
                font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5538))), 28px);
              }
              img {
                max-width: 100%;
                height: auto;
                stroke: $black;
              }
              svg {
                width: 30px;
                height: 30px;
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
          padding: 56px 80px;
          @media screen and (max-width: $pc) {
            padding: 28px 80px;
          }
          &-general {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: min(max(28px, calc(1.75rem + ((1vw - 3.93px) * 2.3576))), 64px);
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
                gap: 24px;
              }
              &-user {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 24px;
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
              font-size: min(max(22px, calc(1.375rem + ((1vw - 3.93px) * 1.3098))), 42px);
              text-align: center;
            }
            &-btns {
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 10px;
            }
          }

          &-nodata {
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
                font-size: min(max(22px, calc(1.375rem + ((1vw - 3.93px) * 1.3098))), 42px);
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
          gap: 16px;
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
  padding-bottom: 5px;
  border-bottom: 3px solid $secondary;
}
</style>