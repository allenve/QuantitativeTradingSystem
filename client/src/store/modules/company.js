export default {
    state: {
        name: '',
        code: ''
    },
    mutations: {
        setCompany(state, data) {
            state.name = data.name;
            state.code = data.code;
        }
    },
    actions: {},
    getters: {
        getCompanyName: state => {
            return state.name
        }
    }
}