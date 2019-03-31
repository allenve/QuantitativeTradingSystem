<!-- mainWrapper -->
<template>
    <div class='mainWrapper'>
        <h4>国内上市公司基本信息</h4>
        <div class="mainWrapper-stockCompany">
            <!-- <ul class="">
                <li v-for="(company, i) in company_list" :key="i">
                    <span>{{company.name}}</span>
                </li>
            </ul> -->
            <Table border :columns="company_columns" :data="company_list"></Table>
            <Page 
                class-name="mainWrapper-stockCompany-page" 
                :total="count" 
                @on-change="changePage"
                show-total />
            <!-- <span class="mainWrapper-stockCompany-total">共有 {{count}} 条数据</span> -->
        </div>
    </div>
</template>

<script>
import { EXCHANGE } from '../../common/utils.js'

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
            count: 0
        };
    },

    components: {},

    mounted() {
        this.getStockCompany()  
    },

    methods: {
        // api 获取公司列表数据
        getStockCompany() {
            this.$loading("加载中")
            let req = {
                limit: 10,
                pagenum: this.pagenum
            }
            this.$api.post('/quan/getStockCompany/', req).then(res => {
                res.code == 200 ? this.initStockCompany(res.data) : this.$Message.error(res.data.msg);
            })
        },

        // 初始化数据
        initStockCompany(data) {
            this.company_list = data.data.company_list.map(item => {
                item.exchange = EXCHANGE.getValueFromAlias(item.exchange)
                return item;
            })
            this.count = data.data.count;
            this.$closeToast()
        },

        // 分页
        changePage(page) {
            this.pagenum = page;
            this.getStockCompany()
        },
        showCompanyDetail(item) {
            console.log(item);
        }
    },

}

</script>

<style scoped lang='less'>
.mainWrapper{
    padding: 20px;
    h4 {
        font-size: 16px;
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