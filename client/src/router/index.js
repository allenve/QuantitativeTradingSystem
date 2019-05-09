import Vue from 'vue'
import Router from 'vue-router'
import index from '../views/index/router'
import transaction from '../views/transaction/router'
import my from '../views/my/router'
import backtest from '../views/backTest/router'
import search from '../views/search/router'
import myCollection from '../views/collection/router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/index'
    },
    ...index,
    ...transaction,
    ...my,
    ...backtest,
    ...search,
    ...myCollection
  ]
})
