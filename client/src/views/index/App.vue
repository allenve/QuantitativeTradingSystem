<!-- App -->
<template>
    <div class="index">
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

}

</script>

<style scoped lang='less'>
.index {
    margin: 20px;
    .demo {
        border: 1px solid #eee;
        width: 200px;
        height: 200px;
        float: left;
        display: flex;
        p {
            flex: 1;
            height: 30px;
            border: 1px solid #aaa;
        }
        span {
            flex: 4
        }
    }
}
</style>