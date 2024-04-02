<template>
  <div class="booking">
    <div class="booking__content container">
      <div class="booking__content_roadmap">
        <span
            class="medium-txt"
            @click="changeStage(1)"
        >
          Building
        </span>
        <span
            class="medium-txt"
            @click="changeStage(2)"
            v-if="selectedBlock"
        >
          // Block {{ selectedBlockLetter }}
        </span>
        <span
            class="medium-txt"
            @click="changeStage(3)"
            v-if="selectedTaraf"
        >
          // Taraf {{ selectedTaraf }}
        </span>
        <span
            class="medium-txt"
            @click="changeStage(4)"
            v-if="selectedRoom"
        >
          // Room {{ selectedRoom }}
        </span>
      </div>
      <div class="booking__content_information">
        <h2 class="semi-bold-txt">Map Of Dormitory</h2>
        <p class="regular-txt">Choose the block you want to live in. Pay attention to fact that A and B blocks are for females, C and D blocks for males</p>
      </div>
      <div class="booking__content_map">
        <div class="booking__content_map-view">
          <BlockMap v-if="bookingStages === 1" @stage-change="changeStage"/>
        </div>
        <div class="booking__content_map-view">
          <TarafMap v-if="bookingStages === 2" @stage-change="changeStage" :tarafs="tarafs"/>
        </div>
        <div class="booking__content_map-view">
          <RoomMap v-if="bookingStages === 3" @stage-change="changeStage" :rooms="tarafs"/>
        </div>
        <div class="booking__content_map-view">
          <BedMap v-if="bookingStages === 4"/>
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
    selectedBlock: parseInt(localStorage.getItem('selectedBlock')) || 0,
    selectedFloor: parseInt(localStorage.getItem('selectedFloor')) || 0,
    selectedTaraf: parseInt(localStorage.getItem('selectedTaraf')) || 0,
    selectedRoom :  parseInt(localStorage.getItem('selectedRoom')) || 0,
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
      localStorage.removeItem('bookingStage');
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
  },
  created() {
    this.loadStageFromLocalStorage();
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
  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
    width: 100%;
    &_roadmap {
      display: flex;
      align-items: flex-start;
      gap: 5px;
      width: 100%;
      span {
        cursor: pointer;
        font-size: 16px;
        color: $black;
        &:hover {
          color: $secondary;
        }
      }
    }
    &_information {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 20px;
      width: 100%;
    }
    &_map {
      display: flex;
      align-items: center;
      justify-content: center;
      height: auto;
      padding-top: 64px;
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
</style>