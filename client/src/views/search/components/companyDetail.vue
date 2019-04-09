<!-- companyDetail 公司详细信息 -->
<template>
    <div class='companyDetail'>
        <div class="companyDetail-wrapper">
            <page-header class="header"><b class="company-name">{{payload.name}}</b>详细信息</page-header>
            <div class="companyDetial-opr">
                <div class="collection">
                    <Button :type="isCollection ? 'info' : ''" 
                        class="collection-button" 
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
        </div>
    </div>
</template>

<script>
import pageHeader from '../../common/pageHeader'
import { COMPANYDETAILLIST } from '../../common/utils.js'

export default {
    name: 'companyDetail',
    data () {
        return {
            companyData: {},
            companyDataList: [],
            payload: {},
            isCollection: false,

        };
    },

    filters: {
        websiteFilter(val) {
            return 'http://' + val;
        }
    },

    created() {
        if (!this.$route.params.ts_code) {
            this.$router.back();
        }
        this.$loading('加载中。。。')
        this.payload = this.$route.params

        this.$api.post('/api/getStockCompanyDetail', this.payload).then(res => {
            this.$closeToast();
            res.code == 200 ? this.initData(Object.assign({}, this.payload, res.data)) : this.$Message.error(res.data.msg);
        })
    },

    components: {
        pageHeader
    },

    methods: {
        initData(data) {
            let companyDataList = [];
            this.companyData = data;
            const company_data = Object.assign({}, data);
            // 去掉vue监控器
            Object.getOwnPropertyNames(company_data).forEach(key => {
                let item = {
                    key: key,
                    text: COMPANYDETAILLIST.getTextFromAlias(key) || '-',
                    value: data[key]
                }
                companyDataList.push(item);
            })
            this.companyDataList = companyDataList;
        },
        collectionCompany() {
            let user_data = this.$getUserInfo();
            const payload = Object.assign({}, user_data, this.companyData)
            console.log(payload);
        }
    },

}

</script>

<style scoped lang='less'>
.companyDetail{
    width: 100%;
    height: auto;
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
            height: 40px;
            .collection {
                padding: 10px 0;
                .collection-button {
                    float: right;
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
    }
}
</style>