<!-- login -->
<template>
    <div class='login'>
        <h3>登录</h3>
        <div class="input-wrapper">
            <div class="input-wrapper-list">
                <span>用户名:</span>
                <input type="text" placeholder="用户名" v-model="username">
            </div>
            <div class="input-wrapper-list">
                <span>密码:</span>
                <input type="text" placeholder="密码" v-model="password">
            </div>
            <div class="input-wrapper-btn">
                <input type="button" value="登录" @click="login">
                <input type="button" value="没有账号" @click="toRegister">
            </div>
            
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    name: 'login',
    data () {
        return {
            username: '',
            password: ''
        };
    },

    components: {},

    methods: {
        ...mapMutations({
            setUserInfo: 'setUserInfo'
        }),
        login() {
            let req = {
                username: this.username,
                password: this.password
            }
            this.$loading('登录中。。。')
            this.$api.post("/api/login", req).then(res => {
                this.$closeToast();
                console.log(res);
                res.code == 200 ? this.loginSuccess(res.data.data) : this.$Message.error(res.data.msg);
            })
        },
        toRegister() {
            this.$router.push("/my/register")
        },
        loginSuccess(user_data) {
            this.$Message.success('登录成功');
            this.setUserInfo(user_data);
            sessionStorage.setItem('user_data', JSON.stringify(user_data))

            let redirectHref = '/my/userInfo';
            if (this.$route.fullPath.indexOf("?") !== -1 && this.$route.fullPath.indexOf('redirect') !== -1) {
                console.log("redirect href");
                redirectHref = decodeURIComponent(this.$route.fullPath.split("?")[1].split("=")[1]);
            }

            setTimeout(() => {
                this.$router.push(redirectHref);
            }, 1000)
            
        }
    },

}

</script>

<style scoped lang='less'>
.login{
    .input-wrapper {
        width: auto;
        padding: 20px 30px;
        .input-wrapper-list {
            margin: 0 auto;
            width: 300px;
            height: 45px;
            span {
                display: inline-block;
                width: 60px;
                text-align: left;
            }
            input {
                width: 150px;
                height: 30px;
                padding: 0 5px;
            }
        }
        .input-wrapper-btn {
            input {
                cursor: pointer;
            }
        }
    }
}
</style>