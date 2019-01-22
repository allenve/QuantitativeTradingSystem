<!-- table -->
<template>
    <div class="tableWrapper">
        <h2>{{title}}</h2>
        <div class="table-content">
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'tableWrapper',
    data () {
        return {
        };
    },
    props: {
        title: String
    },

    components: {},

}

</script>

<style scoped lang='less'>
.tableWrapper{
    width: 900px;
    margin: 0 auto;
    h2{
        padding: 10px;
    }
    .table-content{
        padding: 5px 15px;
    }
}
</style>