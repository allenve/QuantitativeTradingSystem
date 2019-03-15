<!-- strategy 策略选择 -->
<template>
    <div class='strategy'>
        <div class="wrapper">
            <div class="wrapper-item">
                <h4>基本：</h4>
                <div class="wrapper-item-content basic">
                    <div class="wrapper-item-content-list"><span>初始资金：</span><Input size="small" v-model="initialFunding" placeholder="初始资金" style="width: 120px" /></div>
                    <div class="wrapper-item-content-list"><span>开始时间：</span>
                        <Date-picker size="small" v-model="startTime" type="date" placeholder="开始时间" :options="startDataOption" style="width: 120px"></Date-picker>
                    </div>
                    <div class="wrapper-item-content-list"><span>结束时间：</span>
                        <Date-picker size="small" v-model="endTime" type="date" placeholder="开始时间" :options="startDataOption" style="width: 120px"></Date-picker>
                    </div>
                </div>
            </div>
            <div class="wrapper-item">
                <h4>股池：</h4>
                <div class="wrapper-item-content">
                    <div class="wrapper-item-content-select">
                        <span>股池：</span>
                        <Select size="small" multiple style="width:600px">
                            <Option v-for="(item, i) in stockData" :key="i" :value="item.value">
                                <span>{{item.value}}</span>
                                <span style="float:right; margin-right:20px; color:#ccc">{{item.label}}</span>
                            </Option>
                        </Select>
                    </div>
                </div>
            </div>
            <div class="wrapper-item">
                <h4>买策：</h4>
                <div class="wrapper-item-content-list"><span></span></div>
            </div>
            <div class="wrapper-item">
                <Button type="primary" @click="submitStrategy">确定</Button>
            </div>
        </div>
    </div>
</template>

<script>
    const DAY = 86400000;
    import { COMPANY } from '../../common/utils.js';
    import { mapState } from 'vuex'

    export default {
        name: 'strategy',
        data() {
            return {
                initialFunding: 100000, // 初始资金
                startTime: new Date(Date.now() - DAY * 365 * 5), // 默认开始时间
                endTime: new Date(Date.now()), //默认结束时间
                stockData: COMPANY.toArray(),
                selectStock: '', //
            };
        },

        components: {},

        computed: {
            ...mapState({
                companyName: state => state.company.name
            })
        },
        
        mounted() {
            // this.stockData = COMPANY.toArray();
            this.selectStock = COMPANY.getValueFromText(this.companyName);
            console.log(this.stockData);
            // console.log(this.selectStock);
        },

        methods: {
            submitStrategy() {
                this.$emit("closeStrategyDrawer")
            }
        },

    }
</script>

<style scoped lang='less'>
    .strategy {
        .wrapper {
            .wrapper-item {
                padding: 5px 20px;
                border-bottom: 1px solid #eee;

                h4 {
                    font-size: 15px;
                }

                .wrapper-item-content {
                    padding: 10px 20px;
                    display: flex;
                    flex-wrap: wrap;

                    .wrapper-item-content-list {
                        padding: 10px;
                        width: calc(100%/3);

                        span {
                            vertical-align: middle;
                        }
                    }

                    .wrapper-item-content-select {
                        padding: 10px;
                    }
                }
            }
        }
    }
</style>