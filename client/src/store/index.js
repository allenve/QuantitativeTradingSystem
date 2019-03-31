import Vuex from 'vuex';
import company from './modules/company';
import stock from './modules/stock';
import user from './modules/user';
import style from './modules/style';

export default new Vuex.Store({
    modules: {
        company: company,
        stock: stock,
        user: user,
        style: style
    }
})