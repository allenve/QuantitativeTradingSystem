<!-- userInfo -->
<template>
    <div class='userInfo'>
        <div class="userInfo_nav">
            <div class="user_info_nav_avatar">
                <div class="user_info_nav_avatar_wrapper">
                    <img src="https://quantitative-1252092265.cos.ap-chengdu.myqcloud.com/user.png" alt="">
                </div>
                <div class="user_info_nav_username">
                    <span class="nickname">{{nickname}}</span>
                    <span class="username">用户名：{{username}}</span>
                </div>
            </div>
            <div class="user_info_nav_tab">
                <h3>账号管理</h3>
                <ul>
                    <li v-for="(link, i) in navList" :key="i">
                        <router-link :to="link.link">{{link.name}}</router-link>
                    </li>
                </ul>
            </div>
        </div>
        <div class="userInfo_detail">
            <router-view />
        </div>
    </div>
</template>

<script>
export default {
    name: 'userInfo',
    data () {
        return {
            username: '',
            nickname: '',
            navList: [
                {name: '我的信息', link: '/my/detail', icon: 'my'},
                {name: '我的收藏', link: '/myCollection', icon: 'collect'},
                {name: '设置', link: '/my/setting', icon: 'setting'}
            ]
        };
    },

    components: {},

    created () {
        let user_data = this.$getUserInfo();
        if (user_data) {
            this.username = user_data.username;
            this.nickname = user_data.nickname
        }
        
    },
}

</script>

<style scoped lang='less'>
.userInfo{
    width: 900px;
    height: 100%;
    margin: 0 auto;
    // border: 1px solid #eee;
    background: #f8fafc;
    display: flex;
    .userInfo_nav {
        flex: 1;
        .user_info_nav_avatar {
            width: auto;
            height: auto;
            .user_info_nav_avatar_wrapper {
                width: 100px;
                height: 100px;
                margin: 25px auto;
                border-radius: 50%;
                overflow: hidden;
                img {
                    width: 100px;
                    height: 100px;
                }
            }
            .user_info_nav_username {
                height: 50px;
                span {
                    display: block;
                    margin: 8px 0;
                    &.nickname {
                        font-size: 18px;
                        font-weight: 600;
                    }
                    &.username {
                        font-size: 12px;
                    }
                    
                }
            }
        }
        .user_info_nav_tab {
            width: auto;
            padding: 0 30px;
            text-align: left;
            h3 {
                height: 50px;
                line-height: 50px;
                font-size: 18px;
                font-weight: 800;
                color: #111;
            }
            ul {
                padding: 10px 0 20px;
                border-top: 2px solid #d9dde1;
                li {
                    a {
                        display: block;
                        padding-left: 30px;
                        font-size: 15px;
                        height: 50px;
                        line-height: 50px;
                        color: #1c1f21;
                        transition: padding .3s ease-in-out;
                        &:hover {
                            font-weight: 600;
                            color: #0ba0ef;
                            padding-left: 40px;
                        }
                        &.router-link-active {
                            font-weight: 600;
                            color: #0ba0ef;
                            padding-left: 30px;
                        }
                    }
                }
            }
        }
    }
    .userInfo_detail {
        flex: 3;
        background: #fff;
    }
}
</style>