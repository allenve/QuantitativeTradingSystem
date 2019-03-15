import App from './App.vue'
import register from './components/register.vue'
import login from './components/login.vue'
import userInfo from './components/userInfo.vue'
import userInfoDetail from './components/userComponents/userInfoDetail.vue'
import userInfoCollect from './components/userComponents/userInfoCollect.vue'
import userInfoSetting from './components/userComponents/userInfoSetting.vue'

export default [
    {
        path: '/my',
        name: 'my',
        redirect: '/my/userInfo',
        component: App,
        children: [
            {
                path: '/my/register',
                name: 'register',
                component: register
            },
            {
                path: '/my/login',
                name: 'login',
                component: login
            },
            {
                path: '/my/userInfo',
                redirect: '/my/userInfo/detail',
                name: 'userInfo',
                component: userInfo,
                children: [
                    {
                        path: '/my/userInfo/detail',
                        name: 'userInfoDetail',
                        component: userInfoDetail
                    },
                    {
                        path: '/my/userInfo/collect',
                        name: 'userInfoCollect',
                        component: userInfoCollect
                    },
                    {
                        path: '/my/userInfo/setting',
                        name: 'userInfoSetting',
                        component: userInfoSetting
                    },
                ]
            }
        ]
    }
]