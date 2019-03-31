export default {
    state: {
        backgroundTransparent: false
    },
    mutations: {
        changeBackgroundTransparent(state, bool) {
            bool = bool || false;
            state.backgroundTransparent = bool;
        }
    },
    actions: {},
    getters: {}
}