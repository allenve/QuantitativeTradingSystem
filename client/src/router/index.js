import Vue from 'vue'
import Router from 'vue-router'
import index from '../views/index/router'
import price from '../views/price/router'
import self from '../views/self/router'
import transaction from '../views/transaction/router'
import my from '../views/my/router'
import backtest from '../views/backTest/router'
import test from '../views/test/router'
import search from '../views/search/router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/index'
    },
    ...index,
    ...price,
    ...self,
    ...transaction,
    ...my,
    ...backtest,
    ...test,
    ...search
  ]
})
