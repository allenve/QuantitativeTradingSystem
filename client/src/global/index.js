import Vue from 'vue'

import filters from './filters'

export default {
  install(Vue) {
    Vue.use(filters)
  }
}