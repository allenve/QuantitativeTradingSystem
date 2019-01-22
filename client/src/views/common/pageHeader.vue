<!-- pageHeader -->
<template>
    <div class='pageHeader'>
        <slot></slot>
        <div class="back" @click="back">
            <sicon name="back" scale="1.3"></sicon>
            <span>返回</span>
        </div>


    </div>
</template>

<script>
    export default {
        name: 'pageHeader',
        data() {
            return {};
        },

        components: {},

        methods: {
            back() {
                this.$router.back();
            }
        },

    }
</script>

<style scoped lang='less'>
    .pageHeader {
        height: 35px;
        line-height: 35px;
        position: relative;

        .back {
            cursor: pointer;
            font-size: 0.95rem;
            display: inline-block;
            position: absolute;
            top: 0;
            right: 20px;
            &:hover{
                transform: scale(0.9);
                font-weight: 500;
            }
        }
    }
</style>