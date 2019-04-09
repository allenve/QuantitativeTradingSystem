<!-- userInfoSetting -->
<template>
    <div class='userInfoSetting'>
        <div>
            <input type="button" value="修改密码" @click="changePassword">
            <input type="button" value="退出登录" @click="loginout">
        </div>
    </div>
</template>

<script>
export default {
    name: 'userInfoSetting',
    data () {
        return {
        };
    },

    components: {},

    methods: {
        loginout() {
            this.$api.get("/api/loginout").then(res => {
                console.log(res);
                
                res.code == 200 ? this.$Message.success(res.data.msg) : this.$Message.error(res.data.msg);
                sessionStorage.removeItem('user_data');
                this.$router.push("/my/login");
            })
        },
        changePassword() {
            
        }
    },

}

</script>

<style scoped lang='less'>
.userInfoSetting{
}
</style>