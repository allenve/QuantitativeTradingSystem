import Enum from '@/global/Enum'

export const COMPANY = new Enum(
    {alias: 'usBIDU', text: '百度', value:'百度', label: 'US'},
    {alias: 'BABA', text: '阿里巴巴', value: '阿里巴巴', label: 'US'},
    {alias: '00700', text: '腾讯控股', value: '腾讯控股', label: 'HK'}
)

export const EXCHANGE = new Enum(
    {alias: 'SSE', text: '上交所', value: '上交所', label: 'SSE'},
    {alias: 'SZSE', text: '深交所', value: '深交所', label: 'SZSE'},
    {alias: 'HKEX', text: '港交所', value: '港交所', label: 'HKEX'},
)