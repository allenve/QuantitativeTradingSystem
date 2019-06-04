<!-- indexpage -->
<template>
    <div class='indexpage'>
        <div class="main-title">
            <h3>多因子量化投资管理系统</h3>
            <h4>"沪深股票"、"国内上市公司"实时查询</h4>
            <h4>多因子量化交易策略</h4>
            <h4>随时 · 随地 · 洞悉全局</h4>
            <div class="buttons">
                <input type="button" @click="routerToSearch" value="即时查询">
                <input type="button" @click="routerToBackTest" value="历史回测">
            </div>
        </div>
        <div class="wrapper">
            <div class="wrapper-list">
                <div class="wrapper-list-item">
                    <h3>数据丰富</h3>
                    <p>拥有国内所以上市公司基本信息，股票数据。</p>
                </div>
            </div>
            <div class="wrapper-list">
                <div class="wrapper-list-item">
                    <h3>操作简单</h3>
                    <p>操作方式简单易懂，不需要丰富的金融知识，即刻上手。</p>
                </div>
            </div>
            <div class="wrapper-list">
                <div class="wrapper-list-item last-child">
                    <h3>量化策略</h3>
                    <p>精准分析，让决策更快一步。</p>
                </div>
            </div>
        </div>
        <div class="footer">
            <p>By yupeng</p>
        </div>
    </div>
</template>

<script>

export default {
    name: 'indexpage',
    data () {
        return {
        };
    },

    components: {},

    created() {
        
    },

    mounted() {
    },

    methods: {
        routerToSearch() {
            this.$router.push("/search");
        },
        routerToBackTest() {
            this.$router.push("/backtest");
        }
    },

}

</script>

<style scoped lang='less'>
.indexpage{
    width: 100%;
    height: 100%;
    // margin-top: 200px;
    position: absolute;
    // left: 0;
    // right: 0;
    // top: 0;
    // bottom: 0;
    z-index: 10;
    overflow-y: auto;
    .main-title {
        margin-top: 200px;
        width: 100%;
        // margin: 100px 0;
        text-align: center;
        color: #fff;
        h3 {
            height: 70px;
            line-height: 70px;
            font-size: 40px;
            font-weight: 900;
        }
        h4 {
            font-weight: 300;
            height: 40px;
            line-height: 40px;
            color: #FAFAFA;
        }
        .buttons {
            margin: 50px 0;
            input {
                margin: 0 20px;
                padding: 18px 30px;
                font-size: 12px;
                background-color: rgb(45, 190, 96);
                border: none;
                color: #fff;
                transition: all .5s ease-in-out;
                &:hover {
                    padding: 18px 40px;
                    background-color: #2d8cf0;
                }
            }
        }
    }
    .wrapper {
        width: 90%;
        height: auto;
        margin: 100px auto;
        background: #fff;
        display: flex;
        border-radius: 5px;
        .wrapper-list{
            flex: 1;
            .wrapper-list-item {
                margin: 30px 0;
                padding: 20px;
                text-align: center;
                border-right: 1px solid #eee;
                &.last-child {
                    border-right: none;
                }   
                h3 {
                    height: 60px;
                    font-size: 15px;
                    color: #252826;
                }
                p {
                    color: #606661;
                }
            }
        }
    }
    .footer {
        padding: 20px;
        text-align: center;
        color:  #fff;
    }
}
</style>