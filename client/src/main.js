// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

//vue的全局资源filters
import global from './global'
Vue.use(global)

// vuex
import store from './store'
Vue.use(store);

//第三方插件库
import lib from './lib'
Vue.use(lib)

//全局接口
import api from './api'
Vue.use(api)

//自定义css
import './assets/css/reset.css'
import './assets/css/common.less'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
