export default {
    state: {
        id: '',
        values: [],
        categoryData: [],
        volumes: [],
        date: {
            buy: [],
            sell: []
        }
    },
    mutations: {
        setStockData(state, data) {
            state.id = data.id;
            state.values = data.values;
            state.categoryData = data.categoryData;
            state.volumes = data.volumes;
            if (data.date && data.date.buy && data.date.sell) {
                state.date.buy = data.date.buy;
                state.date.sell = data.date.sell;
            }
        }
    },
    actions: {},
    getters: {
    }
}