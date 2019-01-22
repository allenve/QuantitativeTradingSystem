import App from './App.vue'

export default [
    {
        path: '/price',
        name: 'price',
        component: App,
        children: [
            {
                path: '/price/hz',
                
            }
        ]
    }
]