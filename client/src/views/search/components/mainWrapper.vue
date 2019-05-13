<!-- mainWrapper -->
<template>
    <div class='mainWrapper'>
        <div class="mainWrapper-header">
            <h4>国内上市公司基本信息</h4>
            <div class="searchBox">
                <AutoComplete
                    v-model="companyNameKeyWord"
                    @on-search="searchCompany"
                    icon="ios-search"
                    placeholder="请输入你想搜索的公司"
                    style="width:300px">
                    <Option 
                        v-for="(item,i) in companyNameList" 
                        @on-select-selected="onSelect(item)"
                        :key="i">{{item.name}}/{{item.ts_code}}</Option>
                </AutoComplete>
            </div>
        </div>
        <div class="mainWrapper-stockCompany">
            <Table border :columns="company_columns" :data="company_list"></Table>
            <Page 
                class-name="mainWrapper-stockCompany-page" 
                :total="count" 
                @on-change="changePage"
                show-total />
        </div>
    </div>
</template>

<script>
import { EXCHANGE } from '../../common/utils.js'
import { mapState,mapMutations } from 'vuex'

export default {
    name: 'mainWrapper',
    data () {
        return {
            company_columns: [
                {
                    title: '名称', 
                    key: 'name', 
                    render: (h, params) => {
                        return h('div', [
                            h('b', {
                                style: {
                                    fontWeight: 600
                                }
                            }, params.row.name)
                        ]);
                    }},
                {title: '股票代码', key: 'ts_code'},
                {title: '公司全称', key: 'fullname'},
                {title: '交易所', key: 'exchange'},
                {
                    title: '操作', 
                    align: 'center',
                    width: 150,
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'small'
                                },
                                style: {
                                    padding: '3px 10px'
                                },
                                on: {
                                    click: () => {
                                        this.showCompanyDetail(params.row)
                                    }
                                }
                            }, '查看详情')
                        ])
                    }
                }
            ],
            company_list: [],
            pagenum: 1,
            count: 0,
            // 搜索相关
            companyNameList: [],
            companyNameKeyWord: ''
        };
    },

    components: {},

    mounted() {
        this.getStockCompany()  
    },

    methods: {
        ...mapMutations({
            setCompanyData: 'setCompanyData'
        }),
        // api 获取公司列表数据
        getStockCompany() {
            this.$loading("加载中");
            let req = {
                limit: 10,
                pagenum: this.pagenum
            };
            this.$api.post('/api/getStockCompany', req).then(res => {
                this.initStockCompany(res);
            })
        },

        // 初始化数据
        initStockCompany(data) {
            this.company_list = data.company_list.map(item => {
                item.exchange = EXCHANGE.getValueFromAlias(item.exchange)
                return item;
            })
            this.count = data.count;
            this.$closeToast();
        },

        // 分页
        changePage(page) {
            this.pagenum = page;
            this.getStockCompany()
        },
        showCompanyDetail(item) {
            // 保存到vuex
            this.setCompanyData(item);
            this.$router.push(`/search/${item.id}`);
        },

        // search
        onSelect(val) {
            val && this.showCompanyDetail(val);
        },
        searchCompany() {
            const payload = {
                "name": this.companyNameKeyWord
            }
            this.$api.post('/api/searchStockCompany', payload).then(res => {
                this.companyNameList = [];
                this.companyNameList = res.company_list
            });
        }
    },

}

</script>

<style scoped lang='less'>
.mainWrapper{
    padding: 0 20px;
    .mainWrapper-header {
        padding-top: 8px;
        height: 32px;
        h4 {
            display: inline-block;
            font-size: 16px;
            line-height: 32px;
        }
        .searchBox {
            // display: inline-block;
            float: right;
            margin-right: 20px;
        }
    }
    
    .mainWrapper-stockCompany {
        margin: 20px;
        .mainWrapper-stockCompany-page {
            padding: 20px;
            float: right;
            font-size: 12px;
        }
    }
}
</style>