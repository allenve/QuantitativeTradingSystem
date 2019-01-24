import {
    DatePicker, 
    Message,
    Drawer,
    Button
} from 'iview';
import 'iview/dist/styles/iview.css';

export default {
    install(Vue) {
        Vue.component('Date-picker', DatePicker)
        Vue.component('Drawer', Drawer)
        Vue.prototype.$Message = Message
    }
}