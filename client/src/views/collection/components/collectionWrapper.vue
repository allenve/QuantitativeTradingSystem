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
                    }},
                {title: '股票代码', key: 'ts_code'},
                {title: '收藏时间', key: 'createTime'},
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
            collection_list: [],
            pagenum: 1,
            count: 0,
        };
    },

    components: {},
    created() {
        this.loadCollectedList().then(response => {
            this.collection_list = response.list;
        })
    },

    methods: {
        loadCollectedList() {
            const payload = {
                user_id: this.$getUserInfo().id,
                pageNum: this.pagenum,
                limit: 10
            }
            return this.$api.post('/api/getUserColledCompany', payload).then(res => {
                res.code === 200 ? this.$Message.success('success') : this.$Message.error(res.data.msg);
                return res.code === 200 ? res.data : [];
            })
        },
        changePage() {},
        ...mapMutations({
            setCompanyData: 'setCompanyData'
        }),
        showCompanyDetail(item) {
            // 保存到vuex
            console.log(item);
            const row = {
                id: item.company_id,
                name: item.company_name,
                ts_code: item.ts_code
            }
            this.setCompanyData(row);
            this.$router.push(`/search/${item.company_id}`);
        },
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