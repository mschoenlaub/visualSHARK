<template>
  <div class="wrapper">
    <div class="animated fadeIn" v-if="currentProject">
      <router-view></router-view>
    </div>
    <div class="animated fadeIn" v-if="!currentProject">
      <alert type="danger" dismissable>
        <span class="icon-info-circled alert-icon-float-left"></span>
        <strong>No Project Selected</strong>
        <p>
          Select a Project first
        </p>
      </alert>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { alert } from 'vue-strap'

export default {
  name: 'labeling',
  data () {
    return {
    }
  },
  components: {
    alert
  },
  computed: mapGetters({
    currentProject: 'currentProject'
  })
}
</script>

<style>
</style>
