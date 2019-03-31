<!-- pageHeader -->
<template>
    <div class='pageHeader'>
        <slot></slot>
        <div class="back" @click="back" v-if="withBackBtn">
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

        props: {
            withBackBtn: {
                type: Boolean,
                default: true
            }
        },

        components: {},

        methods: {
            back() {
                this.$routerBack();
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
            transition: .2s right ease-in-out;
            &:hover{
                font-weight: 500;
                right: 10px;
            }
        }
    }
</style>