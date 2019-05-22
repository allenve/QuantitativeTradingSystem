<!-- lineChart折线图 -->
<template>
    <div class="lineChart" :id="'lineChart' + cid"></div>
</template>

<script>
    export default {
        name: 'lineChart',
        data() {
            return {};
        },
        props: {
            lineData: Array,
            type: String,
            cid: String
        },
        components: {},

        mounted() {
            // console.log(this.lineData);
            this.type == 1 && this.setOption(this.lineData);
            this.type == 2 && this.setMultipeOption(this.lineData);
            
        },

        methods: {
            setOption(data) {
                let lineChart = this.$echarts.init(document.getElementById(`lineChart${this.cid}`));
                const title_text = data.title;
                const xAxisData = data.xAxisData;
                const seriesData = data.seriesData;
                const option = {
                    title: {
                        text: title_text,
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'axis',
                        position: function(pt) {
                            return [pt[0], '10%'];
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: xAxisData
                    },
                    yAxis: {
                        type: 'value',
                        boundaryGap: ['50%', '100%']
                    },
                    dataZoom: [{
                        type: 'inside',
                        start: 0,
                        end: 100
                    }, {
                        start: 0,
                        end: 0,
                        handleSize: '80%',
                        handleStyle: {
                            color: '#fff',
                            shadowBlur: 3,
                            shadowColor: 'rgba(0, 0, 0, 0.6)',
                            shadowOffsetX: 2,
                            shadowOffsetY: 2
                        }
                    }],
                    series: {
                        name: '收益',
                        type: 'line',
                        smooth: true,
                        symbol: 'none',
                        sampling: 'average',
                        itemStyle: {
                            color: 'rgb(255, 70, 131)'
                        },
                        areaStyle: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(255, 158, 68)'
                            }, {
                                offset: 1,
                                color: 'rgb(255, 70, 131)'
                            }])
                        },
                        data: seriesData
                    }
                }

                lineChart.setOption(option);
            },
            setMultipeOption(data) {
                let lineChart = this.$echarts.init(document.getElementById(`lineChart${this.cid}`));

                const colors = ['#5793f3', '#d14a61', '#675bba', '#7efa6e'];
                const xAxisData = data.xAxisData;
                const seriesData = data.seriesData;
                const title_text = data.title;

                const option = {
                    color: colors,
                    title: {
                        text: title_text,
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxisData
                    },
                    yAxis: {
                        type: 'value'
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    series: seriesData
                };

                lineChart.setOption(option);
            }
        },

    }
</script>

<style scoped lang='less'>
    .lineChart {
        width: 800px;
        height: 300px;
        margin: 0 auto;
    }
</style>