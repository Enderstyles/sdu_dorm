<template>
  <div class="modal-wrapper" v-if="isOpen">
    <div class="modal-overlay" @click="closeModal"></div>
    <div class="modal">
      <img class="close-modal" :src="require('@/assets/icons/x.svg')" @click="closeModal" alt="close-modal" />
      <div class="modal-content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  props: ["isOpen"],
  methods: {
    closeModal() {
      this.$emit('close')
    },
  },
  watch: {
    isOpen() {
      this.isOpen === false ? this.trues = true : null
      this.isOpen ? document.documentElement.style.overflowY = 'hidden' : document.documentElement.style.overflowY = 'auto'
    }
  }
};
</script>

<style lang="scss" scoped>
.modal-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal-overlay {
  position: absolute;
  top: 0;
  z-index: -1;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal {
  background: $white;
  overflow-y: auto;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
  animation: modal-appear 0.5s;
  position: relative;
  @media screen and (max-width: $mobile) {
    padding: 37px 20px;
    width: 90vw;
    height: auto;
  }
  &-content {
    width: auto;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    @media screen and (max-width: $mobile) {
      width: 100%;
    }
    &-row {
      margin-top: 20px;
      display: flex;
      align-items: center;
      gap: 20px;
    }
    &-col {
      margin-top: 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    @media screen and (max-width: $mobile) {
      width: 100%;
    }
  }
}

.close-modal {
  position: absolute;
  cursor: pointer;
  top: 15px;
  right: 30px;
  z-index: 999;
  &:hover {
    transform: scale(1.1);
  }
}

@keyframes modal-appear {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
