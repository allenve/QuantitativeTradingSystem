<!-- navigation -->
<template>
    <div class="navigation" :class="{'Transparent': backgroundTransparent }">
        <span class="header">多因子量化投资管理系统</span>
        <ul>
            <router-link v-for="(link, i) in links" :key="i" :to="link.link">
                <!-- <sicon :name="link.icon" scale="1.0"></sicon> -->
                <span>{{link.name}}</span>
            </router-link>
        </ul>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
    name: 'navigation',
    data () {
        return {
            links: [
                {name: '首页', link: '/index', icon: 'index'},
                {name: '即时查询', link: '/search', icon: 'search'},
                {name: '我的收藏', link: '/myCollection', icon: 'collection'},
                // {name: '历史回测', link: '/search', icon: 'search'},
                // {name: '行情', link: '/price', icon: 'price'},
                {name: '回测', link: '/backtest', icon: 'backtest'},
                // {name: '交易', link: '/transaction', icon: 'transaction'},
                {name: '我的', link: '/my', icon: 'my'}
            ]
        };
    },

    components: {},

    
    computed: {
        ...mapState({
            backgroundTransparent: state => state.style.backgroundTransparent,
        })
    },

}

</script>

<style scoped lang='less'>
.navigation{
    position: sticky;
    top: 0;
    height: 40px;
    line-height: 40px;
    background: #07111b;
    // box-shadow: 0 5px 4px #ccc;
    z-index: 100;
    &.Transparent {
        background: none;
    }
    span.header {
        display: inline-block;
        margin-left: 20px;
        color: #fff;
        font-size: 15px;
    }
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
            &:hover {
                color: #fff;
            }
        }
    }
}
</style>