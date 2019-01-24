export default {
    state: {
        id: '',
        values: [],
        categoryData: [],
        volumes: []
    },
    mutations: {
        setStockData(state, data) {
            state.id = data.id;
            state.values = data.values;
            state.categoryData = data.categoryData;
            state.volumes = data.volumes;
        }
    },
    actions: {},
    getters: {
    }
}