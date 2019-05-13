import App from './App.vue'
import login from './components/login';
import register from './components/register';
import userInfoDetail from './components/userComponents/userInfoDetail.vue'
import userInfoCollect from './components/userComponents/userInfoCollect.vue'
import userInfoSetting from './components/userComponents/userInfoSetting.vue'

export default [
    {
        path: '/my',
        name: 'my',
        redirect: '/my/detail',
        component: App,
        children: [
            {
                path: '/my/detail',
                name: 'userInfoDetail',
                component: userInfoDetail
            },
            {
                path: '/my/collect',
                name: 'userInfoCollect',
                component: userInfoCollect
            },
            {
                path: '/my/setting',
                name: 'userInfoSetting',
                component: userInfoSetting
            },
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: login,
    },
    {
        path: '/register',
        name: 'register',
        component: register,
    }
]