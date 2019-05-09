<!-- App 我的收藏 -->
<template>
    <div class='App'>
        <div class="myCollection-wrapper">
            <h3>我收藏的公司</h3>
        </div>
        <collectionWrapper />
    </div>
</template>

<script>
import collectionWrapper from './components/collectionWrapper'
export default {
    name: 'App',
    data () {
        return {
        };
    },

    components: {
        collectionWrapper
    },

}

</script>

<style scoped lang='less'>
.App{
    padding: 20px 30px;
    .myCollection-wrapper {
        h3 {
            height: 40px;
            line-height: 40px;
            border-bottom: 2px solid #eee;
        }
    }
}
</style>