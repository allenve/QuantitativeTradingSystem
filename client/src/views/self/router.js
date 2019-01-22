import App from './App.vue'
import companyDetail from './components/companyDetail.vue'

export default [
    {
        path: '/self',
        name: 'self',
        component: App,
        children: [
            {
                path: '/self/:id',
                component: companyDetail
            }
        ]
    }
]