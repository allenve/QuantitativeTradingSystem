import App from './App.vue'
import CompanyDetail from './components/companyDetail.vue'

export default [
    {
        path: '/search',
    	name: "search",
        component: App,
        keepAlive: true,
        children: [
            {
                path: '/search/:id',
                name: 'companyDetail',
                component: CompanyDetail,
                props: true
            }
        ]
    }
]