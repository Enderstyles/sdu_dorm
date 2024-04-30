<template>
  <div class="booking">
    <div class="booking__content container">
      <div class="booking__content_information">
        <h2 class="semi-bold-txt">Map Of Dormitory</h2>
        <p class="regular-txt" v-if="bookingStages === 1">
          Choose the block you want to live in. Pay attention to fact that A and B blocks are for females, C and D blocks for males
        </p>
        <p class="regular-txt" v-if="bookingStages === 2">
          Choose the taraf you want to live in. Every taraf has WC and shower
        </p>
        <p class="regular-txt" v-if="bookingStages === 3">
          Choose the room you want to live in
        </p>
        <p class="regular-txt" v-if="bookingStages === 4">
          Choose the taraf you want to live in. Every taraf has WC and shower
        </p>
      </div>
      <div class="booking__content_roadmap">
        <div class="booking__content_roadmap-link">
          <span
              class="stage semi-bold-txt"
              @click="changeStage(1)"
              :class="{'activeStage': bookingStages === 1}"
          >
            Building
          </span>
        </div>
        <div class="booking__content_roadmap-link" v-if="selectedBlock">
          <span class="semi-bold-txt">>></span>
          <span
              class="stage semi-bold-txt"
              @click="changeStage(2)"
              :class="{'activeStage': bookingStages === 2}"
          >
            Block {{ selectedBlockLetter }}
          </span>
        </div>
        <div class="booking__content_roadmap-link" v-if="selectedTaraf">
          <span class="semi-bold-txt">>></span>
          <span
              class="stage semi-bold-txt"
              @click="changeStage(3)"
              :class="{'activeStage': bookingStages === 3}"
          >
            Taraf {{ selectedTaraf }}
          </span>
        </div>
        <div class="booking__content_roadmap-link" v-if="selectedRoom">
          <span class="semi-bold-txt">>></span>
          <span
              class="stage semi-bold-txt"
              @click="changeStage(4)"
              :class="{'activeStage': bookingStages === 4}"
          >
            Room {{ selectedRoom }}
          </span>
        </div>
        <div class="booking__content_roadmap-link" v-if="timer">
          <span class="semi-bold-txt">>></span>
          <span
              class="stage semi-bold-txt"
              @click="$router.push('/confirmation')"
          >
            Confirmation
          </span>
        </div>
      </div>
      <div class="booking__content_map">
        <div class="booking__content_map-view">
          <BlockMap v-if="bookingStages === 1" @stage-change="changeStage"/>
        </div>
        <div class="booking__content_map-view">
          <TarafMap v-if="bookingStages === 2" @stage-change="changeStage" :tarafs="tarafs"/>
        </div>
        <div class="booking__content_map-view">
          <RoomMap v-if="bookingStages === 3" @stage-change="changeStage" :rooms="tarafs" :takenPlaces="takenPlaces"/>
        </div>
        <div class="booking__content_map-view">
          <BedMap v-if="bookingStages === 4" :takenPlaces="takenPlaces"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BlockMap from "@/components/booking/BlockMap.vue";
import TarafMap from "@/components/booking/TarafMap.vue";
import RoomMap from "@/components/booking/RoomMap.vue";
import BedMap from "@/components/booking/BedMap.vue";

export default {
  components: {BedMap, RoomMap, TarafMap, BlockMap},
  data: () => ({
    bookingStages: 1,
    takenPlaces: [],
    selectedBlock: parseInt(localStorage.getItem('selectedBlock')) || 0,
    selectedFloor: parseInt(localStorage.getItem('selectedFloor')) || 0,
    selectedTaraf: parseInt(localStorage.getItem('selectedTaraf')) || 0,
    selectedRoom :  parseInt(localStorage.getItem('selectedRoom')) || 0,
    timer: parseInt(localStorage.getItem('timerStart')) || 0,
    tarafs: [
      {
        floor: 2,
        taraf:[
          {id: 1, rooms: [200, 201, 202, 203, 204]},
          {id: 2, rooms: [205, 206, 207, 208, 209]},
          {id: 3, rooms: [210, 211, 212, 213, 214]},
          {id: 4, rooms: [215, 216, 217, 218, 219]},
        ]
      },
      {
        floor: 3,
        taraf:[
          {id: 1, rooms: [300, 301, 302, 303, 304]},
          {id: 2, rooms: [305, 306, 307, 308, 309]},
          {id: 3, rooms: [310, 311, 312, 313, 314]},
          {id: 4, rooms: [315, 316, 317, 318, 319]},
        ]
      },
      {
        floor: 4,
        taraf:[
          {id: 1, rooms: [400, 401, 402, 403, 404]},
          {id: 2, rooms: [405, 406, 407, 408, 409]},
          {id: 3, rooms: [410, 411, 412, 413, 414]},
          {id: 4, rooms: [415, 416, 417, 418, 419]},
        ]
      },
    ]
  }),
  beforeRouteLeave(to, from, next) {
    if (this.bookingStages) {
      next();
    }
  },
  computed: {
    selectedBlockLetter() {
      const blockMapping = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
      };
      return blockMapping[this.selectedBlock] || '';
    }
  },
  methods: {
    changeStage(stage) {
      this.bookingStages = stage;
      this.saveStageToLocalStorage();
    },
    saveStageToLocalStorage() {
      localStorage.setItem('bookingStage', this.bookingStages);
    },
    loadStageFromLocalStorage() {
      const storedPage = localStorage.getItem('bookingStage');
      this.bookingStages = storedPage ? parseInt(storedPage) : 1;
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
            this.takenPlaces = response.data;
          })
          .catch((e) => {
            console.log(e);
          });
    },
  },
  created() {
    this.loadStageFromLocalStorage();
    this.fetchTakenPlaceData();
    setInterval(() => {
      this.fetchTakenPlaceData();
    }, 60000);
  },
  watch: {
    $route() {
      this.selectedBlock = parseInt(localStorage.getItem('selectedBlock'))
      this.selectedFloor = parseInt(localStorage.getItem('selectedFloor'))
      this.selectedTaraf = parseInt(localStorage.getItem('selectedTaraf'))
      this.selectedRoom  = parseInt(localStorage.getItem('selectedRoom'))
    }
  }
}
</script>

<style lang="scss" scoped>
.booking {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 200px 0;
  @media screen and (max-width: $desktop) {
    padding: 130px 0;
  }
  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
    width: 100%;
    &_roadmap {
      display: flex;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;
      padding-top: 24px;
      gap: 5px;
      width: 100%;
      height: auto;
      &-link {
        display: flex;
        align-items: center;
        font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
        color: $black;
        gap: 5px;
        .stage {
          cursor: pointer;
          &:hover {
            color: $secondary;
          }
        }
      }
    }
    &_information {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 20px;
      width: 100%;
      p {
        font-size: min(max(16px, calc(1rem + ((1vw - 3.93px) * 0.5239))), 24px);
        width: 60%;
        @media screen and (max-width: $desktop) {
          width: 100%;
        }
      }
    }
    &_map {
      display: flex;
      align-items: center;
      justify-content: center;
      height: auto;
      padding-top: 64px;
      @media screen and (max-width: $desktop) {
        padding-top: 32px;
      }
      &-view {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
      }
    }
  }
}
.activeStage {
  color: $secondary;
}
</style>