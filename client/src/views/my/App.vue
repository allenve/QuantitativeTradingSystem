<!-- 我的 -->
<template>
    <div class="my">
        <div class="wrapper">
            <!-- <h3>登录/注册</h3> -->
            <router-view />
        </div>
    </div>
</template>

<script>
export default {
    name: 'App',
    data () {
        return {
        };
    },
    components: {},

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