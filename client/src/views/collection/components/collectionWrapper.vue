<!-- collectionWrapper -->
<template>
    <div class='collectionWrapper'>
        <div class="collectionWrapper-company">
            <Table border :columns="company_columns" :data="collection_list"></Table>
            <Page 
                class-name="collectionWrapper-company-page" 
                :total="count" 
                @on-change="changePage"
                show-total />
        </div>
    </div>
</template>

<script>
import timeUtils from '../../common/timeUtils.js'
import { mapMutations } from 'vuex'
export default {
    name: 'collectionWrapper',
    data () {
        return {
            userData: null,
            company_columns: [
                {
                    title: '名称', 
                    key: 'company_name', 
                    render: (h, params) => {
                        return h('div', [
                            h('b', {
                                style: {
                                    fontWeight: 600
                                }
                            }, params.row.company_name)
                        ]);
                    }
                },
                {title: '公司全称', key: 'fullname'},
                {title: '股票代码', key: 'ts_code'},
                {title: '收藏时间', key: 'createTime'},
                {
                    title: '操作', 
                    align: 'center',
                    width: 250,
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'small'
                                },
                                style: {
                                    padding: '3px 10px',
                                    marginRight: '10px'
                                },
                                on: {
                                    click: () => {
                                        this.showCompanyDetail(params.row)
                                    }
                                }
                            }, '查看详情'),
                            h('Button', {
                                props: {
                                    type: 'warning',
                                    size: 'small'
                                },
                                style: {
                                    padding: '3px 10px'
                                },
                                on: {
                                    click: () => {
                                        this.cancelCollectedThisCompany(params.row)
                                    }
                                }
                            }, '取消收藏')
                        ])
                    }
                }
            ],
            collection_list: [],
            pagenum: 1,
            count: 0,
        };
    },

    components: {},
    created() {
        this.userData = this.$getUserInfo();
    },

    mounted () {
        if (this.userData) {
            this.$loading('加载中。。。');
            this.loadCollectedList().then(response => {
                this.collection_list = response.list;
            })
        }
        
    },

    methods: {
        loadCollectedList() {
            const payload = {
                user_id: this.userData.id,
                pageNum: this.pagenum,
                limit: 10
            }
            return this.$api.post('/api/getUserColledCompany', payload).then(res => {
                return res;
            })
        },
        changePage() {},
        ...mapMutations({
            setCompanyData: 'setCompanyData'
        }),
        showCompanyDetail(item) {
            const row = {
                id: item.company_id,
                name: item.company_name,
                ts_code: item.ts_code,
                fullname: item.fullname
            }
            // 保存到vuex
            this.setCompanyData(row);
            this.$router.push(`/search/${item.company_id}`);
        },
        cancelCollectedThisCompany(item) {
            this.$loading('正在取消');
            const payload = {
                user_id: this.userData.id,
                company_id: item.company_id
            };
            this.$api.post('/api/cancelCollectionCompany', payload).then(res => {
                this.$Message.success('成功取消收藏');
                setTimeout(() => this.reload(), 0);
            });
        },
        reload() {
            this.loadCollectedList().then(response => {
            this.collection_list = response.list;
        })
        }
    }

}

</script>

<style scoped lang='less'>
.collectionWrapper{
    padding: 0 20px;
    .collectionWrapper-company {
        margin: 20px;
        .collectionWrapper-company-page {
            padding: 20px;
            float: right;
            font-size: 12px;
        }
    }
}
</style>