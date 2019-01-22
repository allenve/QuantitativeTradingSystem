<!-- 行情 -->
<template>
    <div class="price">
        <sub-nav />
        <router-view />
    </div>
</template>

<script>
import subNav from './components/subNav'
export default {
    name: 'App',
    data () {
        return {
        };
    },

    components: {
        subNav
    },

}

</script>

<style scoped lang='less'>
</style>