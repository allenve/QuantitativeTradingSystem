import {DatePicker, Message} from 'iview';
import 'iview/dist/styles/iview.css';

export default {
    install(Vue) {
        Vue.component('Date-picker', DatePicker)
        Vue.prototype.$Message = Message
    }
}