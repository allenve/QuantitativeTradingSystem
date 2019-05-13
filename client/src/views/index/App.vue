<!-- App -->
<template>
    <div class="index">
        <div class="index_bg"></div>
        <indexpage />
    </div>
</template>

<script>
    import indexpage from './components/indexpage'
    export default {
        name: 'App',
        data() {
            return {};
        },

        components: {
            indexpage
        },

        mounted() {
            // this.$api.post('/quan/getStockCompany/').then(res => {
            //     console.log(res);
            // })
        },

    }
</script>

<style scoped lang='less'>
    .index {
        position: absolute;
        top: 40px;
        left: 0;
        right: 0;
        bottom: 0;
        overflow-x: hidden;
        .index_bg {
            position: fixed;
            z-index: 0;
            left: 0;
            right: 0;
            bottom: 0;
            top: 0;
            overflow: hidden;
            background: url('../../assets/img/bg_2.png') no-repeat;
            width: 100%;
            height: 100%;
            background-size: 100% 100%;
            animation-name: scaleDraw;
            animation-timing-function: ease-in-out; /*动画的速度曲线*/
            animation-iteration-count: infinite;  /*动画播放的次数*/
            animation-duration: 15s; /*动画所花费的时间*/
            -webkit-animation-name: scaleDraw; /*关键帧名称*/
            -webkit-animation-timing-function: ease-in-out; /*动画的速度曲线*/
            -webkit-animation-iteration-count: infinite;  /*动画播放的次数*/
            -webkit-animation-duration: 15s; /*动画所花费的时间*/
        }
    }

    @keyframes scaleDraw {
        0% {
            transform: scale(1);
            opacity: 1;
        }
        25% {
            transform: scale(1.1);
            opacity: 0.9;
        }
        50% {
            transform: scale(1);
            opacity: 1;
        }
        75% {
            transform: scale(1.1);
            opacity: 1;
        }
    }
</style>