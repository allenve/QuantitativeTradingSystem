import ajaxLib from './lib/ajax'
const ajax = ajaxLib.ajax
class Api {
  //hello world
  static async hello() {
    const promise = new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve('hello world!')
      }, 1000)
    })
    return promise
  }
  static async get (url) {
    return new Promise((resolve, reject) => {
      ajax(url)
        .then((response) => {
          resolve(response);
        }).catch((error) => {
          reject(error);
        })
    })
  }
  static async post (url, data) {
    return new Promise((resolve, reject) => {
      ajax.post(url, data)
        .then(response => {
          resolve(response);
        }).catch(error => {
          reject(error);
        })
    })
  }
}
export default {
  install(Vue) {
    Vue.prototype.$api = Api
  }
}
