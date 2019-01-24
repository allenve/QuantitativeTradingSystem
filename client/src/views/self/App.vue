<!-- 自选 -->
<template>
    <div class="self">
        <table-wrapper title="我的自选">
            <div class="self-content">
                <ul>
                    <li v-for="(item, i) in companys" :key="i">
                        <span class="name" @click="showCompanyDetail(item)">{{item.name}}</span>
                    </li>
                </ul>
            </div>
        </table-wrapper>

        <router-view class="self-detail" />
    </div>
</template>

<script>
import tableWrapper from '../common/tableWrapper'
import { mapMutations } from 'vuex'

export default {
    name: 'App',
    data () {
        return {
            companys: [
                {name: '百度', code: 'BIDU'},
                {name: '阿里巴巴', code: 'BABA'},
                {name: '腾讯控股', code: '00700'}
            ]
        };
    },

    components: {
        tableWrapper
    },

    methods: {
        ...mapMutations({
            setCompany: 'setCompany'
        }),
        showCompanyDetail(data){
            console.log(data)
            this.setCompany({name: data.name, code: data.code})
            this.$router.push({
                path: `/self/${data.code}`
            })
        },
    },

}

</script>

<style scoped lang='less'>
.self{
    .self-content{
        ul{
            li{

                font-size: 0.9rem;
                height: 30px;
                line-height: 30px;
                border-bottom: 1px solid #eee;
                span{
                    display: inline-block;
                    padding: 0 10px;
                    &.name{
                        cursor: pointer;
                    }
                }
            }
        }
    }
    .self-detail{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: #fff;
        z-index: 10;
    }
}
</style>