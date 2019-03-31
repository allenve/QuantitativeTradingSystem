<!-- strategy 策略选择 -->
<template>
    <div class='strategy'>
        <div class="wrapper">
            <!-- 基本信息 -->
            <div class="wrapper-item">
                <h4>基本信息：</h4>
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
            <!-- 股池 -->
            <div class="wrapper-item">
                <h4>股池：</h4>
                <div class="wrapper-item-content">
                    <div class="wrapper-item-content-select">
                        <span>股池：</span>
                        <Select v-model="choice_symbols" size="small" multiple style="width:550px">
                            <Option v-for="(item, i) in stockData" :key="i" :value="item.value">
                                <span>{{item.value}}</span>
                                <span style="float:right; margin-right:20px; color:#ccc">{{item.label}}</span>
                            </Option>
                        </Select>
                    </div>
                </div>
            </div>
            <!-- 策略选择 -->
            <div class="wrapper-item">
                <h4>策略选择：</h4>
                <div class="wrapper-item-content">
                    <div class="wrapper-item-content-select">
                        <span>买入策略：</span>
                        <Select size="small" multiple style="width:550px">
                            <Option v-for="(item, i) in buy_factors" :key="i" :value="item.value">
                                <span>{{item.value}}</span>
                                <span style="float:right; margin-right:20px; color:#ccc">{{item.label}}</span>
                            </Option>
                        </Select>
                    </div>
                    <div class="wrapper-item-content-select">
                        <span>卖出策略：</span>
                        <Select size="small" multiple style="width:550px">
                            <Option v-for="(item, i) in sell_factors" :key="i" :value="item.value">
                                <span>{{item.value}}</span>
                                <span style="float:right; margin-right:20px; color:#ccc">{{item.label}}</span>
                            </Option>
                        </Select>
                    </div>
                </div>
            </div>
            <div class="wrapper-button">
                <input type="button" value="确定" @click="submitStrategy">
                <input type="button" value="取消" @click="cancle">
            </div>
        </div>
    </div>
</template>

<script>
    const DAY = 86400000;
    import { COMPANY } from '../../common/utils.js';

    export default {
        name: 'strategy',
        data() {
            return {
                initialFunding: 100000, // 初始资金
                startTime: new Date(Date.now() - DAY * 365 * 5), // 默认开始时间
                endTime: new Date(Date.now()), //默认结束时间
                choice_symbols: [], // 股池
                buy_factors: [], // 买入策略
                sell_factors: [], // 卖出策略
                stockData: COMPANY.toArray()
            };
        },

        components: {},

        methods: {
            submitStrategy() {
                let strategData = {
                    read_cash: this.initialFunding,
                    start: this.$getLocalTime(this.startTime, true),
                    end: this.$getLocalTime(this.endTime, true),
                    choice_symbols: this.choice_symbols.map(item => {return COMPANY.getAliasFromValue(item)}),
                    buy_factors: this.buy_factors,
                    sell_factors: this.sell_factors

                }
                // console.log(strategData);
                this.$emit("closeStrategyDrawer", strategData)
            },
            cancle() {
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
                        span {
                            display:  inline-block;
                            width: 70px;
                        }
                    }
                }
            }
            .wrapper-button {
                padding: 20px 30px;
                input {
                    margin: 5px 10px;
                }
            }
        }
    }
</style>