import Vuex from 'vuex';
import company from './modules/company';
import stock from './modules/stock';

export default new Vuex.Store({
    modules: {
        company: company,
        stock: stock
    }
})