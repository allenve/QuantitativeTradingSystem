<!-- companyDetail 公司详细信息 -->
<template>
    <div class='companyDetail'>
        <div class="companyDetail-wrapper">
            <page-header class="header">
                <b class="company-name">{{company_name}}</b>详细信息
            </page-header>
            <div class="companyDetial-opr">
                <div class="collection">
                    <Button :type="isCollection ? 'info' : ''" 
                        class="collection-button" 
                        :loading="isCollectionButtonDisabled"
                        icon="md-heart"
                        @click="collectionCompany">
                        <span v-if="!isCollection">收藏</span>
                        <span v-else>已收藏</span>
                    </Button>
                </div>
            </div>
            <div class="companyDetail-content">
                <div class="company-items" 
                    v-for="(item, index) in companyDataList" 
                    :key="index"
                    :class="index < 9 ? 'company-items-show' : 'company-items-hidden'">
                    <div class="company-items-wrapper">
                        <div class="company-item-key">{{item.text}}：</div>
                        <div class="company-item-value">{{item.value}}</div>
                    </div>
                </div>
            </div>
            <div class="companyDetail-chart" v-if="companyDataList.length > 0">
                <h3>历史股票数据：</h3>
                <div class="companyDetail-options">
                    <span>
                        <b>选择开始时间：</b>
                        <Date-picker v-model="startTime" type="date" size="small" placeholder="开始时间" :options="startDataOption" style="width: 120px"></Date-picker>
                    </span>
                    <span>
                        <b>选择结束时间：</b>
                        <Date-picker v-model="endTime" type="date" size="small" placeholder="结束时间" :options="endDataOption" style="width: 120px"></Date-picker>
                    </span>
                    <span><input class="submit" type="button" value="查看K线图" @click="showChartByTime"></span>
                </div>
                <div class="chart">
                    <k-chart v-if="isShowKChart" :stockDataId="stockDataId" />
                    <div v-else></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import pageHeader from '../../common/pageHeader'
import kChart from '../../common/kChart'
import timeUtils from '../../common/timeUtils.js'
import { COMPANYDETAILLIST } from '../../common/utils.js'
import { mapState, mapMutations } from 'vuex'

const DAY = 86400000; // 一天的毫秒数
export default {
    name: 'companyDetail',
    data () {
        return {
            companyData: {},
            companyDataList: [],
            isCollection: false,
            isCollectionButtonDisabled: true,
            isShowKChart: false,
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

        };
    },

    filters: {
        websiteFilter(val) {
            return 'http://' + val;
        }
    },

    computed: {
        ...mapState({
            company_id: state => state.company.company_id,
            company_name: state => state.company.name,
            company_fullname: state => state.company.fullname,
            company_ts_code: state => state.company.ts_code
        })
    },
    created() {
        if (!this.company_id) {
            this.$router.back();
        }else {
            // this.$loading('加载中。。。')
            this.$api.post('/api/getStockCompanyDetail', {"ts_code": this.company_ts_code})
            .then(res => {
                this.initData(Object.assign({}, {
                    company_name: this.company_name,
                    company_fullname: this.company_fullname
                }, res));
            })
            .then(() => {
                this.isCompanyCollection();
                this.$closeToast();
            })
        }
    },

    components: {
        pageHeader,
        kChart
    },

    methods: {
        initData(data) {
            let companyDataList = [];
            this.companyData = data;
            const company_data = Object.assign({}, data);
            // 去掉vue监控器
            Object.getOwnPropertyNames(company_data).forEach(key => {
                if (key !== 'id') {
                    let item = {
                        key: key,
                        text: COMPANYDETAILLIST.getTextFromAlias(key) || '-',
                        value: data[key]
                    }
                    companyDataList.push(item);
                }
                
            })
            this.companyDataList = companyDataList;
        },
        isCompanyCollection() {
            let user_data = JSON.parse(sessionStorage.getItem('user_data'));
            if (user_data) {
                const payload = Object.assign({}, {
                    user_id: user_data.id,
                    company_id: this.company_id
                })
                this.$api.post('/api/isCompanyCollection', payload).then(res => {
                    if (res.isCollection) {
                        this.isCollection = true;
                    }
                })
            }
            this.isCollectionButtonDisabled = false;
            
        },
        collectionCompany() {
            let user_data = this.$getUserInfo();
            let req_url = '/api/collectionCompany';
            const payload = {
                user_id: user_data.id,
                username: user_data.username,
                company_name: this.company_name,
                company_id: this.company_id,
                ts_code: this.company_ts_code,
                fullname: this.company_fullname
            }

            // 取消收藏
            if (this.isCollection) {
                req_url = '/api/cancelCollectionCompany';
            }

            this.isCollectionButtonDisabled = true;
            this.$api.post(req_url, payload).then(res => {
                this.$Message.success(res.msg)
                this.isCollection = res.isCollection;
                this.isCollectionButtonDisabled = false;
            })
            
        },
        hadCollectionThisCompany() {
            this.isCollection = true;
            // this.$Message.success('你已经收藏过该公司了');
        },
        // 获取k线图数据
        showChartByTime() {
            console.log(this.startTime);
            this.isShowKChart = false;

            let req = {
                code: this.company_ts_code,
                start: timeUtils.toDate(this.startTime),
                end: timeUtils.toDate(this.endTime)
            }
            this.$loading();
            this.$api.post('/api/getStockData', req).then(res => {
                console.log(res);
                this.showChart(this.initStockData(res))
                this.$closeToast();
            })


        },
        // 初始化股票数据
        initStockData(data) {
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
        // 保存股票数据到 vuex
        ...mapMutations({
            setStockData: 'setStockData'
        }),
        showChart(rawData){
            console.log(rawData);
            this.stockDataId = rawData.id;
            this.isShowKChart = true;
        },
    },

}

</script>

<style scoped lang='less'>
.companyDetail{
    width: 100%;
    height: 100%;
    position: absolute;
    top: 40px;
    left: 0;
    right: 0;
    bottom: 0;
    background: #fff;
    z-index: 15;
    .companyDetail-wrapper {
        padding: 20px 30px;
        .header {
            height: 40px;
            line-height: 40px;
            border-bottom: 1px solid #eee;
            .company-name {
                font-weight: 700;
                padding-right: 10px;
            }
        }
        .companyDetial-opr {
            position: relative;
            height: 50px;
            .collection {
                padding: 10px 0;
                .collection-button {
                    // float: right;
                    position: absolute;
                    right: 0;
                    margin-right: 20px;
                }
            }
        }
        .companyDetail-content { 
            padding: 0 20px;
            display: flex;
            flex-wrap: wrap;
            .company-items {
                padding: 5px 20px;
                .company-item-key {
                    font-size: 15px;
                    font-weight: 700;
                    width: 130px;
                    text-align: right;
                }
                .company-item-value {
                    margin-left: 15px;
                    font-size: 13px;
                    line-height: 15px;
                }
            }
            .company-items-show {
                display: flex;
                width: calc(100%/3);
                .company-items-wrapper {
                    display: flex;
                    .company-item-value {
                        flex: 1;
                    }
                }
            }
            .company-items-hidden {
                display: block;
                width: 100%;
                .company-items-wrapper {
                    display: flex;
                    .company-item-value {
                        flex: 1;
                    }
                }
            }
        }
        .companyDetail-chart {
            margin: 50px;
            height: 600px;
            border-top: 1px solid #eee;
            font-size: 0.95rem;
            h3 {
                padding: 10px 0;
                font-size: 14px;
                .company-name {
                    font-weight: 700;
                    padding-right: 10px;
                }
            }
            .companyDetail-options {
                margin: 10px 50px;
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
}
</style>