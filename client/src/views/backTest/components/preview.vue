<!-- preview -->
<template>
    <div class='preview'>
        <!-- <h3>所选公司：{{companyName}}</h3> -->
        <div class="wrapper">
            <Button @click="strategyState = true" type="primary">策略选择</Button>
            <Drawer title="策略选择" v-model="strategyState" width="800" :mask-closable="false" :styles="styles">
                <strategy v-on:closeStrategyDrawer="closeStrategyDrawer" />
            </Drawer>
        </div>
        <div class="info" v-if="strategyData">
            <h3>已选择：</h3>
            <div class="info-wrapper">
                <div><span class="name">初始资金：</span><span>{{strategyData.read_cash}}</span></div>
                <div><span class="name">开始时间：</span><span>{{strategyData.start}}</span></div>
                <div><span class="name">结束时间：</span><span>{{strategyData.end}}</span></div>
                <div><span class="name">股票代码：</span><span>{{strategyData.selectedCompany}}</span></div>
            </div>      
        </div>
        <div class="echart-wrapper">
            <!-- <k-chart v-if="isShowKChart" :stockDataId="stockDataId" /> -->
            <line-chart v-if="mainLineData" :lineData="mainLineData" type="2" cid="mainLineData" />
            <line-chart v-if="profitLineData" :lineData="profitLineData" type="1" cid="profitLineData" />
            <line-chart v-if="benchmarkTrendLineData" :lineData="benchmarkTrendLineData" type="2" cid="benchmarkTrendLineData" />
            <!-- <img :src="imageData" class="image"/> -->
            <div class="buy-info" v-if="orderInfo">
                <h3>交易信息</h3>
                <div class="buy-info-item" v-for="(item, i) in orderInfo" :key="i">
                    <span>{{item.type}}</span>
                    <span>{{item.order}}</span>
                    <span>{{item.Close}}</span>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
    import strategy from './strategy';
    import lineChart from '../../common/lineChart';
    import { mapState, mapMutations } from 'vuex';
    import { FACTORS } from '../../common/utils.js';

    export default {
        name: 'preview',
        data() {
            return {
                strategyState: false,
                styles: {
                    height: 'calc(100% - 55px)',
                    overflow: 'auto',
                    paddingBottom: '53px',
                    position: 'static'
                },
                stockDataId: '',
                isShowKChart: false,
                orderInfo: null,
                strategyData: null,
                profitLineData: null,
                benchmarkTrendLineData: null,
                mainLineData: null,
                imageData: ''
            };
        },

        components: {
            strategy,
            lineChart
        },

        methods: {
            getStrategyData(payload) {
                this.$loading("策略运行中")
                return this.$api.post("/api/runStrategy", payload);
            },
            closeStrategyDrawer(data) {
                this.strategyState = false;
                // 图表数据置空
                this.mainLineData = null;
                this.profitLineData = null;
                this.benchmarkTrendLineData = null;
                this.orderInfo = null;
                if (data) {
                    this.strategyData = data;
                    this.getStrategyData(data).then(res => {
                        this.setMainLineChartData(res);
                        this.orderInfo = res.dispCont_List;
                        return res;
                    }).then(res => {
                        // 初始化资金折线图
                        this.setProfitLineChartData(res.profit);
                        return res;
                    }).then(res => {
                        // this.imageData = 'data:image/png;base64,' + res.image;
                        // this.setBenchmarkRendChartData(res.benchmark_profit, res.trend_profit);
                        this.setBenchmarkRendChartData(res.benchmark_trend);
                        return res;
                    })

                }
            },

            setMainLineChartData(res) {
                let xAxisData = [];
                let CloseData = [];
                let Ma30Data = [];
                let artwinData = [];
                let artlossData = [];
                let markArea = [];
                let orderIndex = 1;

                Object.keys(res.Close).map((item, i) => {
                    xAxisData.push(this.$getLocalTime(Number(item), true));
                    CloseData.push(res.Close[item]);
                    Ma30Data.push(res.Ma30[item]);
                    artwinData.push(res.artwin[item]);
                    artlossData.push(res.artloss[item]);
                });
                res.dispCont_List.map((item, i) => {
                    if (item.type === 'start') {
                        let mark = [
                            {
                                name: orderIndex,
                                xAxis: item.order
                            },
                            {
                                xAxis: res.dispCont_List[i + 1].order
                            }
                        ];
                        orderIndex++;
                        markArea.push(mark);
                    }
                });

                this.mainLineData = {
                    title: '概览',
                    xAxisData: xAxisData,
                    seriesData: [
                        {
                            name: 'Close',
                            type: 'line',
                            data: CloseData,
                            markArea: {
                                data: markArea
                            }
                        },
                        {
                            name: 'Ma30',
                            type: 'line',
                            data: Ma30Data
                        },
                        {
                            name: 'artwin',
                            type: 'line',
                            data: artwinData
                        },
                        {
                            name: 'artloss',
                            type: 'line',
                            data: artlossData
                        }
                    ]
                }

            },
            
            // 设置 profit 图
            setProfitLineChartData(profit) {
                let xAxisData = [];
                let seriesData = [];

                Object.keys(profit).map((item, i) => {
                    let pro = profit[item] - 100000;
                    xAxisData.push(this.$getLocalTime(Number(item), true));
                    seriesData.push(pro);

                });
                this.profitLineData = {
                    title: '总资金',
                    xAxisData: xAxisData,
                    seriesData: seriesData
                };
            },

            // 设置 基准收益、策略收益 对比图
            setBenchmarkRendChartData(data) {
                let xAxisData = [];
                let benchmarkData = [];
                let trendData = [];

                Object.keys(data).map(item => {
                    xAxisData.push(this.$getLocalTime(Number(item), true));
                    benchmarkData.push(data[item].benchmark_profit);
                });
                Object.keys(data).map(item => {
                    trendData.push(data[item].trend_profit);
                });

                this.benchmarkTrendLineData = {
                    title: '基准收益、策略收益',
                    xAxisData: xAxisData,
                    seriesData: [
                        {
                            name: '基准收益',
                            type: 'line',
                            data: benchmarkData
                        },
                        {
                            name: '策略收益',
                            type: 'line',
                            data: trendData
                        }
                    ]
                }
            },
            ...mapMutations({
                setStockData: 'setStockData'
            })
        },

    }
</script>

<style scoped lang='less'>
    .preview {
        .wrapper {
            padding: 20px;
        }
        .info {
            font-size: 12px;
            padding: 20px 0;
            margin: 0 20px;
            border-bottom: 1px solid #eee;
            h3 {
                height: 30px;
                line-height: 30px;
                font-size: 16px;
            }
            .info-wrapper {
                display: flex;
                padding: 0 20px;
                div {
                    flex: 1;
                    span.name {
                        font-weight: 600;
                    }
                }
            }   
            
        }
        .echart-wrapper {
            width: auto;
            height: auto;
            .image {
                display: block;
                width: 800px;
                margin: 0 auto;
            }
            .buy-info {
                width: 700px;
                margin: 0 auto;
                font-size: 14px;
                h3 {
                    font-size: 16px;
                    padding: 10px 0;
                }
                .buy-info-item {
                    padding: 5px 20px;
                }
            }
        }
    }
</style>