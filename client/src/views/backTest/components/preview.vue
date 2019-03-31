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
        <div class="echart-wrapper">
            <k-chart v-if="isShowKChart" :stockDataId="stockDataId" />
        </div>
        
    </div>
</template>

<script>
    import strategy from './strategy'
    import kChart from '../../common/kChart'
    import { mapState, mapMutations } from 'vuex'

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
            };
        },

        components: {
            strategy,
            kChart
        },

        mounted() {
            // if (!this.companyName) {
            //     this.$routerBack();
            // }
        },

        methods: {
            getStrategyData() {
                this.$loading("策略运行中")
                return this.$api.get("/quan/strategyTrade/").then(res => {
                    this.$closeToast();
                    this.$Message.success("成功，正在初始化数据")
                    return res.data
                })
            },
            closeStrategyDrawer(data) {
                this.strategyState = false;
                if (data) {
                    this.getStrategyData().then(res => {
                        this.initStockDataAndLoadEchart(res)
                    })
                }
                
                // this.getStrategyData().then(res => {
                //     console.log(res);
                // })
            },

            ...mapMutations({
                setStockData: 'setStockData'
            }),
            initStockDataAndLoadEchart(data) {
                console.log(data);
                let stockData = this.$initStockData(data.stock)
                stockData = Object.assign({}, stockData, {date: data.date})
                console.log(stockData);
                this.setStockData(stockData, data.date);
                this.stockDataId = stockData.id;
                this.isShowKChart = true;
                // this.
                
            }
        },

    }
</script>

<style scoped lang='less'>
    .preview {
        .wrapper {
            padding: 20px;
        }
    }
</style>