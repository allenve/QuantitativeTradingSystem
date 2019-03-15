export default {
    state: {
        id: '',
        username: ''
    },
    mutations: {
        setUserInfo(state, data) {
            state.id = data.id;
            state.username = data.username
        }
    },
    actions: {},
    getters: {}
}