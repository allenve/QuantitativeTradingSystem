<!-- 我的 -->
<template>
    <div class="my">
        <div class="wrapper">
            <user-info />
        </div>
    </div>
</template>

<script>
import userInfo from './components/userInfo'
export default {
    name: 'App',
    data () {
        return {
        };
    },
    components: {
        userInfo
    },

    methods: {
    },

}

</script>

<style scoped lang='less'>
.my {
    padding: 20px;
    font-size: 13px;
    text-align: center;
    .wrapper {
        width: auto;
        height: 100%;
        input { 
            cursor: pointer;
            padding: 5px 10px;
        }
    }
}
</style>