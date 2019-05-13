<!-- 即时查询 -->
<template>
    <div class='App'>
        <div class="search-wrapper">
            <h3>即时查询</h3>
            <mainWrapper />
            <router-view />
        </div>
    </div>
</template>

<script>
import mainWrapper from './components/mainWrapper'

export default {
    name: 'App',
    data () {
        return {
        };
    },

    components: {
        mainWrapper
    },

}

</script>

<style scoped lang='less'>
.App{
    padding: 20px 30px;
    .search-wrapper {
        h3 {
            height: 40px;
            line-height: 40px;
            border-bottom: 2px solid #eee;
        }
    }
}
</style>