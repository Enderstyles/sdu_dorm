<template>
  <div class="room-map">
    <div class="room-map_main">
      <div class="room-map_main-static">
        <div class="room-map_main-static-icon">
          <img src="@/assets/images/png/study-room.png" alt="study-room">
        </div>
        <div class="room-map_main-static-icon center">
          <img src="@/assets/images/png/bathroom.png" alt="bathroom">
        </div>
        <div class="room-map_main-static-icon">
          <img src="@/assets/images/png/toilet.png" alt="toilet">
        </div>
      </div>

      <div class="room-map_main-rooms">
        <div
            class="room-map_main-rooms-block"
            v-for="(room, index) in filteredRooms.rooms"
            :key="index"
        >
          <div
              class="room-map_main-rooms-block-placement"
              :class="{'activeRoom': room === activeRoom}"
              @click="selectRoom(room)"
          >
            <p class="bold-txt">{{room}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["rooms"],
  data() {
    return {
      activeRoom: parseInt(localStorage.getItem('selectedRoom')) || 0,
    };
  },
  computed: {
    // eslint-disable-next-line vue/return-in-computed-property
    filteredRooms() {
      const selectedTaraf = localStorage.getItem("selectedTaraf");
      const selectedFloor = localStorage.getItem("selectedFloor");
      if (selectedTaraf && selectedFloor) {
        const floor = this.rooms.find(t => t.floor == selectedFloor);
        if (floor) {
          const taraf = floor.taraf.find(t => t.id == selectedTaraf);
          return taraf;
        }
      }
      else {
        return [];
      }
    }
  },
  methods: {
    selectRoom(roomNum) {
      this.activeRoom = roomNum;
      localStorage.setItem("selectedRoom", roomNum);
      this.$router.push({query: {block: this.$route.query.block, taraf: this.$route.query.taraf, room: roomNum}})
      this.$emit("stage-change", 4);
    }
  }
}
</script>

<style lang="scss" scoped>
.room-map {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: auto;
  &_main {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #F6F6F6;
    border: 1px solid black;
    width: 580px;
    height: auto;
    &-static {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      &-icon {
        padding: 30px;
        width: auto;
      }
      .center {
        border-bottom: 1px solid black;
        border-top: 1px solid black;
      }
    }
    &-rooms {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      height: 100%;
      padding: 15px 0;
      &-block {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        height: 100%;
        &-placement {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          background: $available;
          border: 1px solid black;
          width: 240px;
          height: 150px;
          cursor: pointer;
          &:hover {
            background: $secondary;
          }
        }
      }
    }
  }
}
.activeRoom {
  background: $secondary !important;
}
</style>