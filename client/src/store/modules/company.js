export default {
    state: {
        company_id: '',
        name: '',
        fullname: '',
        ts_code: ''
    },
    mutations: {
        setCompanyData(state, data) {
            state.company_id = data.id;
            state.name = data.name;
            state.fullname = data.fullname;
            state.ts_code = data.ts_code;
        }
    },
    actions: {},
    getters: {
        getCompanyName: state => {
            return state.name
        }
    }
}