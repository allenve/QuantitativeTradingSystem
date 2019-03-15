<!-- userInfoDetail -->
<template>
    <div class='userInfoDetail'>
        <h3>我的信息</h3>
        <div class="userInfoDetail_wrapper">
            <div class="userInfoDetail_wrapper_button">
                <input type="button" value="修改资料" @click="showChangeWrapper">
                <Modal
                    v-model="userInfoModal"
                    title="修改个人信息"
                    @on-ok="changeUserInfo"
                    @on-cancel="cancel">
                    <div id="userInfoDetail_wrapper_change_wrapper">
                        <div class="userInfoDetail_wrapper_change_wrapper_list">
                            <span>昵称：</span>
                            <div class="userInfoDetail_wrapper_change_wrapper_list_input">
                                <Input v-model="nickname" placeholder="昵称" style="width: 200px" />
                            </div>
                        </div>
                        <div class="userInfoDetail_wrapper_change_wrapper_list">
                            <span>电话：</span>
                            <div class="userInfoDetail_wrapper_change_wrapper_list_input">
                                <Input v-model="mobile" placeholder="电话" style="width: 200px" />
                            </div>
                        </div>
                        <div class="userInfoDetail_wrapper_change_wrapper_list">
                            <span>邮箱：</span>
                            <div class="userInfoDetail_wrapper_change_wrapper_list_input">
                                <Input v-model="email" type="email" placeholder="邮箱" style="width: 200px" />
                            </div>
                        </div>
                        <div class="userInfoDetail_wrapper_change_wrapper_list">
                            <span>性别：</span>
                            <div class="userInfoDetail_wrapper_change_wrapper_list_input">
                                <Select v-model="sex" placeholder="性别" style="width:200px">
                                    <Option v-for="item in sexList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                </Select>
                            </div>
                        </div>
                        <div class="userInfoDetail_wrapper_change_wrapper_list">
                            <span>城市：</span>
                            <div class="userInfoDetail_wrapper_change_wrapper_list_input">
                                <al-selector v-model="cityArr" data-type="name" level="0" style="width:200px; display:inline-block"/>
                            </div>
                        </div>
                        <div class="userInfoDetail_wrapper_change_wrapper_list">
                            <span>个性签名：</span>
                            <div class="userInfoDetail_wrapper_change_wrapper_list_input">
                                <Input v-model="signature" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="个性签名" />
                            </div>
                        </div>
                    </div>
                    
                </Modal>
            </div>
            <div class="userInfoDetail_wrapper_ul">
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">用户名</span>
                    <span class="userInfoDetail_wrapper_list_val">{{username}}</span>
                </div>
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">昵称</span>
                    <span class="userInfoDetail_wrapper_list_val">{{nickname}}</span>
                </div>
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">电话</span>
                    <span class="userInfoDetail_wrapper_list_val">{{mobile}}</span>
                </div>
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">邮箱</span>
                    <span class="userInfoDetail_wrapper_list_val">{{email}}</span>
                </div>
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">性别</span>
                    <span class="userInfoDetail_wrapper_list_val">{{sex}}</span>
                </div>
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">城市</span>
                    <span class="userInfoDetail_wrapper_list_val">{{city}}</span>
                </div>
                <div class="userInfoDetail_wrapper_list">
                    <span class="userInfoDetail_wrapper_list_key">个性签名</span>
                    <span class="userInfoDetail_wrapper_list_val">{{signature}}</span>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
export default {
    name: 'userInfoDetail',
    data () {
        return {
            id: '',
            nickname: '',
            mobile: '',
            userInfoModal: false,
            sex: '',
            city: '',
            cityArr: [],
            signature: '',
            sexList: [{value: '男', label: '男'}, {value: '女', label: '女'}],
        };
    },

    components: {},
    mounted() {
        this.setUserInfo(this.$getUserInfo());
    },
    methods: {
        showChangeWrapper() {
            this.userInfoModal = true;
            console.log("showChangeWrapper");
            console.log(this.city);
            this.cityArr = this.city.split(",")
        },
        changeUserInfo() {
            this.$loading('用户信息修改中。。。')
            let req = {
                id: this.id,
                mobile: this.mobile,
                nickname: this.nickname,
                email: this.email,
                sex: this.sex,
                city: this.cityArr[0],
                signature: this.signature
            }
            this.$api.post('/quan/setUserInfo/', req).then(res => {
                console.log(res);
                this.$closeToast();
                res.code == 200 ? this.changeSuccess(res.data.data) : this.$Message.error(res.data.msg);
            })
        },
        setUserInfo(user_data) {
            this.id = user_data.id;
            this.city = user_data.city;
            this.username = user_data.username;
            this.nickname = user_data.nickname;
            this.sex = user_data.sex;
            this.mobile = user_data.mobile;
            this.email = user_data.email;
            this.signature = user_data.signature;
        },
        changeSuccess(user_data) {
            this.$Message.success('用户信息修改成功');
            sessionStorage.setItem('user_data', JSON.stringify(user_data))
            this.setUserInfo(user_data);
        }
    },

}

</script>

<style scoped lang='less'>
.userInfoDetail{
    text-align: left;
    padding-left: 30px;
    h3 {
        font-size: 18px;
        font-weight: 800;
        height: 50px;
        line-height: 50px;
        border-bottom: 1px solid #d0d6d9;
    }
    .userInfoDetail_wrapper {
        padding: 10px 35px;
        .userInfoDetail_wrapper_button {
            height: 30px;
            input {
                cursor: pointer;
                height: 28px;
                float: right;
            }
        }
        .userInfoDetail_wrapper_ul {
            .userInfoDetail_wrapper_list {
                margin: 10px 0;
                height: 50px;
                line-height: 50px;
                display: flex;
                font-size: 15px;
                span {
                    &.userInfoDetail_wrapper_list_key {
                        flex: 1;
                        text-align: center;
                        background-color: #f3f5f7;
                        color: #07111b;
                        font-weight: 600;
                    }
                    &.userInfoDetail_wrapper_list_val {
                        flex: 5;
                        margin-left: 10px;
                        padding-left: 25px;
                        border-bottom: 1px solid #d0d6d9;
                    }
                }
            }
        }
        
    }
}
#userInfoDetail_wrapper_change_wrapper {
    div.userInfoDetail_wrapper_change_wrapper_list {
        height: auto;
        display: flex;
        margin: 8px;
        align-items: center;
        span {
            flex: 1;
        }
        .userInfoDetail_wrapper_change_wrapper_list_input {
            flex: 5;
        }
    }
}
</style>