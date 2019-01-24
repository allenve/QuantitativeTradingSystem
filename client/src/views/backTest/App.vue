<!-- 回测界面 -->
<template>
    <div class='App'>
        <page-header>
            <h3>历史数据回测</h3>
        </page-header>
        <preview />
    </div>
</template>

<script>
import pageHeader from '../common/pageHeader'
import preview from './components/preview'

export default {
    name: 'App',
    data () {
        return {
        };
    },

    components: {
        pageHeader,
        preview
    },

}

</script>

<style scoped lang='less'>
.App{
    padding: 20px 30px;
}
</style>