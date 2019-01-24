<!-- companyDetail -->
<template>
    <div class="companyDetail">
        <page-header class="detail-titles">
            <h3>
                <span>公司名称：<b>{{companyName}}</b></span>
                <span>股票代码：<b>{{companyCode}}</b></span>
            </h3>
        </page-header>
        <div class="detail-wrapper">
            <div class="options">
                <span>
                    <b>选择开始时间：</b>
                    <Date-picker v-model="startTime" type="date" size="small" placeholder="开始时间" :options="startDataOption" style="width: 120px"></Date-picker>
                </span>
                <span>
                    <b>选择结束时间：</b>
                    <Date-picker v-model="endTime" type="date" size="small" placeholder="结束时间" :options="endDataOption" style="width: 120px"></Date-picker>
                </span>
                <span><input class="submit" type="button" value="K线图" @click="showChartByTime"></span>
                <span><input class="backTest" type="button" value="开始回测" @click="startBackTest"></span>
            </div>
            <div class="chart">
                <k-chart v-if="isShowKChart" :stockDataId="stockDataId" />
            </div>
        </div>
    </div>
</template>

<script>
    import { COMPANY } from '../../common/utils.js'
    import timeUtils from '../../common/timeUtils.js'
    import pageHeader from '../../common/pageHeader'
    import kChart from '../../common/kChart'
    import { mapState, mapMutations } from 'vuex'

    const DAY = 86400000;

    export default {
        name: 'companyDetail',
        data() {
            return {
                startTime: new Date(Date.now() - DAY * 365 * 5), //默认开始时间 五年前
                endTime: new Date(Date.now()), // 默认结束时间
                startDataOption: {
                    disabledDate(date) {
                        return date && date.valueOf() > Date.now() - DAY;
                    }
                }, // 开始时间不可选配置
                endDataOption: {
                    disabledDate(date) {
                        return date && date.valueOf() > Date.now();
                    }
                }, // 结束时间不可选配置
                isShowKChart: false,
                stockDataId: ''
            };
        },

        components: {
            pageHeader,
            kChart
        },

        created() {

        },

        mounted() {
            // let code = this.$route.params.id;
            // this.companyCode = code;
            if(this.companyCode && this.companyName) {
                this.isShowKChart = false;
                setTimeout(() => {
                    this.showChartByTime()
                }, 500)
            }else {
                this.$routerBack();
            }
            
        },

        computed: {
            ...mapState({
                companyName: state => state.company.name,
                companyCode: state => state.company.code
            })
        },
        methods: {
            // 获取k线图数据
            showChartByTime() {
                console.log(this.startTime);
                this.isShowKChart = false;

                let req = {
                    code: this.companyCode,
                    start: timeUtils.toDate(this.startTime),
                    end: timeUtils.toDate(this.endTime)
                }
                this.$loading();
                this.$api.post('/quan/getStockData/', req).then(res => {
                    console.log(res);
                    this.showChart(this.initData(res.data))
                    this.$closeToast();
                })


            },
            // 初始化数据
            initData(data) {
                let rawData = {
                    id: this.$GenNonDuplicateID(),
                    values: [],
                    categoryData: [],
                    volumes: []
                }
                Object.keys(data).map((item, i) => {
                    let row = data[item];
                    rawData.values.push([Number(row['Open']), Number(row['Close']), Number(row['Low']), Number(row['High']), Number(row['Volume'])])
                    rawData.categoryData.push(this.$getLocalTime(Number(item), true))
                    rawData.volumes.push([i, row['Volume'], Number(row['Open']) > Number(row['Close']) ? 1 : -1])
                })
                
                this.setStockData(rawData);
                return rawData;
            },
            ...mapMutations({
                setStockData: 'setStockData'
            }),
            // 显示k线图
            showChart(rawData){
                console.log(rawData);
                this.stockDataId = rawData.id;
                this.isShowKChart = true;
            },
            // 开始回测
            startBackTest() {
                this.$router.push("/backtest");
            }
        },

    }
</script>

<style scoped lang='less'>
    .companyDetail {
        padding: 20px;

        .detail-titles {
            border-bottom: 2px solid #f6f6f6;

            h3 {
                height: 35px;
                line-height: 35px;

                span {
                    display: inline-block;
                    padding: 0 10px;

                    b {
                        font-weight: 500;
                        color: #111;
                    }
                }
            }
        }

        .detail-wrapper {
            margin: 15px 20px;
            font-size: 0.95rem;

            .options {
                height: 26px;

                span {
                    display: inline-block;
                    margin-right: 20px;

                    b {
                        vertical-align: middle;
                    }

                    input {
                        cursor: pointer;
                        width: auto;
                        padding: 0 18px;
                        height: 26px;
                        background: #0ba0ef;
                        // border: 1px solid #fff;
                        color: #fff;
                        vertical-align: middle;
                        border-radius: 5px;
                        font-size: 0.85rem;
                        &.backTest{
                            background: #43c936;
                        }
                    }
                }
            }

            .chart {
                width: 100%;
                height: auto;
                padding-top: 30px;
            }
        }
    }
</style>