<!-- register -->
<template>
    <div class='register'>
        <h3>注册</h3>
        <div class="input-wrapper">
            <div class="input-wrapper-list">
                <span>用户名:</span>
                <input type="text" placeholder="用户名" v-model="username">
            </div>
            <div class="input-wrapper-list">
                <span>Email:</span>
                <input type="text" placeholder="Email" v-model="email">
            </div>
            <div class="input-wrapper-list">
                <span>密码:</span>
                <input type="text" placeholder="密码" v-model="password">
            </div>
            <div class="input-wrapper-list">
                <span>确认密码:</span>
                <input type="text" placeholder="确认密码" v-model="surepassword">
            </div>
            <div class="input-wrapper-btn">
                <input class="input-wrapper-btn-register" type="button" value="立即注册" @click="register">
                <input class="input-wrapper-btn-back" type="button" value="返回登录" @click="toLogin">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'register',
    data () {
        return {
            username: '',
            email: '',
            password: '',
            surepassword: '',
            BolleanPassword: false
        };
    },

    watch: {
        username(val, old) {
            return val;
        },
        password(val) {
            if (val === this.surepassword && val !== '') {
                console.log("ture");
                this.BolleanPassword = true;
            } else {
                console.log("false");
                this.BolleanPassword = false;
            }
        },
        surepassword(val) {
            if (val === this.password && val !== '') {
                this.BolleanPassword = true;
            } else { 
                this.BolleanPassword = false;
            }
        }
    },

    components: {},

    methods: {
        register() {
            console.log("register now");
            if (this.BolleanPassword) { 
                let req = {
                    username: this.username,
                    password: this.password,
                    email: this.email || ''
                }
                
                this.$loading('注册中。。。')
                this.$api.post("/api/register", req).then(res => {
                    this.$Message.success(`${res.msg}，即将返回登录`);
                    setTimeout(() => this.toLogin(), 1000);
                })
            } else {
                this.$Message.error('两次输入密码不一致')
            }
            
           
        },
        toLogin() {
            this.$router.push("/login");
        }
    },

}

</script>

<style scoped lang='less'>
.register{
    text-align: center;
    font-size: 13px;
    margin-top: 50px;
    h3 {
        font-size: 15px;   
    }
    .input-wrapper {
        padding: 20px 30px;
        .input-wrapper-list {
            margin: 0 auto;
            width: 300px;
            height: 45px;
            span {
                display: inline-block;
                width: 70px;
                text-align: left;
            }
            input {
                width: 150px;
                height: 30px;
                padding: 0 5px;
            }
            
        }
        .input-wrapper-btn {
            margin-top: 20px;
            input {
                cursor: pointer;
                width: 80px;
                padding: 10px 15px;
                margin: 0 10px;
                color: #fff;
                &.input-wrapper-btn-register { 
                    background-color: @btn-color-1;
                }
                &.input-wrapper-btn-back {
                    background-color: @btn-color-2;
                }
                &:hover {
                    font-weight: 700;
                }
            }
        }
    }
}
</style>