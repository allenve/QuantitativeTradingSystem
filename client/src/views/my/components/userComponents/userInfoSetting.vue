<!-- userInfoSetting -->
<template>
    <div class='userInfoSetting'>
        <div>
            <Button type="primary" @click="psdModal = true">修改密码</Button>
            <Button type="warning" @click="loginout">退出登录</Button>
        </div>
        <Modal title="修改密码"
            class-name="psdModal"
            v-model="psdModal"
            :loading="loading"
            @on-ok="checkPassword"
            @on-cancel="cancel">
            <div class="psdModal-wrapper">
                <div class="psdModal-row">
                    <span>原密码:</span>
                    <Input type="password" v-model="oldPassword" style="width: 200px"/>
                </div>
                <div class="psdModal-row">
                    <span>新密码:</span>
                    <Input type="password" v-model="newPassowrd" style="width: 200px"/>
                </div>
                <div class="psdModal-row">
                    <span>确认新密码:</span>
                    <Input type="password" v-model="sureNewPassowrd" style="width: 200px"/>
                </div>
            </div>
        </Modal>
    </div>
</template>

<script>
export default {
    name: 'userInfoSetting',
    data () {
        return {
            userData: null,
            loading: true,
            psdModal: false,
            oldPassword: '',
            newPassword: '',
            sureNewPassowrd: ''
        };
    },

    components: {},

    created () {
        this.userData = this.$getUserInfo();
    },

    methods: {
        loginout() {
            this.$api.get("/api/loginout").then(res => {
                this.$Message.success(res.msg)
                this.toLogin();
            })
        },
        checkPassword() {
            if (this.oldPassword !== '' || this.newPassword!== '' || this.sureNewPassowrd !== '') {

            } else {
                this.$Message.warning('旧密码、新密码不能为空');
            }
        },
        changePassword() {
            const payload = {
                id: this.userData.id,
                oldPsd: this.oldPassword,
                newPsd: this.newPassword
            }
            this.$api.post('/api/changePsd', payload).then(res => {
                this.$Message.success(`${res.msg}，请重新登录`);
                this.toLogin();
            })
        },
        toLogin() {
            sessionStorage.removeItem('user_data');
            this.$router.push("/login");
        }
    },

}

</script>

<style scoped lang='less'>
.userInfoSetting{
}
</style>