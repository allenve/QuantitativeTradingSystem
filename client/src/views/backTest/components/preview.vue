<!-- preview -->
<template>
    <div class='preview'>
        <h3>所选公司：{{companyName}}</h3>
        <div class="wrapper">
            <Button @click="strategyState = true" type="primary">策略选择</Button>
            <Drawer title="策略选择" v-model="strategyState" width="800" :mask-closable="false" :styles="styles">
                <strategy v-on:closeStrategyDrawer="closeStrategyDrawer" />
            </Drawer>
        </div>
        <div class="echart-wrapper">

        </div>
        
    </div>
</template>

<script>
    import { mapState } from 'vuex'
    import strategy from './strategy'
    import kChart from '../../common/kChart'
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
            };
        },

        components: {
            strategy,
            kChart
        },

        mounted() {
            if (!this.companyName) {
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
            getStrategyData() {
                this.$loading("策略运行中")
                return this.$api.get("/quan/strategyTrade/").then(res => {
                    this.$closeToast();
                    return res
                })
            },
            closeStrategyDrawer() {
                this.strategyState = false;
                this.getStrategyData().then(res => {
                    console.log(res);
                })
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