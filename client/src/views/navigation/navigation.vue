<!-- navigation -->
<template>
    <div class="navigation">
        <ul>
            <router-link v-for="(link, i) in links" :key="i" :to="link.link">
                <!-- <sicon :name="link.icon" scale="1.0"></sicon> -->
                <span>{{link.name}}</span>
            </router-link>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'navigation',
    data () {
        return {
            links: [
                {name: '首页', link: '/index', icon: 'index'},
                {name: '行情', link: '/price', icon: 'price'},
                {name: '自选', link: '/self', icon: 'self'},
                {name: '交易', link: '/transaction', icon: 'transaction'},
                {name: '我的', link: '/my', icon: 'my'}
            ]
        };
    },

    components: {},

}

</script>

<style scoped lang='less'>
.navigation{
    position: sticky;
    top: 0;
    height: 40px;
    line-height: 40px;
    background: #07111b;
    box-shadow: 0 5px 4px #ccc;
    ul{
        float: right;
        margin-right: 20px;
        a{
            display: inline-block;
            padding: 0 10px;
            font-size: 0.8rem;
            // color: #666;
            color: rgba(255,255,255,.6);
            &.router-link-active{
                color: #fff;
                font-weight: 500;
            }
        }
    }
}
</style>