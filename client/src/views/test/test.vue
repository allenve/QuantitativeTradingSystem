<!-- test -->
<template>
    <div>
        <input type="text" v-model="name">
        <input type="button" value="get" @click="getData">
        <echart ref="chart" v-if="showChart" :rawData="rawData" />
    </div>
</template>

<script>
    import echart from '../echarts/App'
    export default {
        name: 'test',
        data() {
            return {
                name: 'BIDU',
                showChart: false,
                rawData: {
                    categoryData: [],
                    values: [],
                    volumes: []
                }
            };
        },

        components: {
            echart
        },

        methods: {
            getData() {
                this.$api.get(`/quan/getdata/?name=${this.name}`).then(res => {
                    console.log(res);
                    this.initData(res.data)
                }, err => {
                    console.log(err);
                })
            },

            initData(data) {
                let rawData = []
                let i = 0;
                for (let item in data) {
                    let row = data[item];
                    this.rawData.values.push([Number(row['Open']), Number(row['Close']), Number(row['Low']), Number(row['High']), Number(row['Volume'])])
                    this.rawData.categoryData.push(this.$getLocalTime(Number(item), true))
                    this.rawData.volumes.push([i, row['Volume'], Number(row['Open']) > Number(row['Close']) ? 1 : -1])
                    i++;
                }

                this.showChart = true;
                // this.$refs.chart
            }
        }

    }
</script>

<style scoped lang='less'>
</style>