<!-- 行情导航 -->
<template>
    <div class="subNav">
        <ul>
            <router-link v-for="(link, index) in links" :key="index" :to="link.link">{{link.name}}</router-link>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'subNav',
    data () {
        return {
            links: [
                {name: '沪深', icon: 'hz', link: '/price/hz'},
                {name: '港美股', icon: 'gm', link: '/price/gm'}
            ]
        };
    },

    components: {},

}

</script>

<style scoped lang='less'>
</style>