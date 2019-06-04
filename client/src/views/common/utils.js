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

export const COMPANYDETAILLIST = new Enum(
    {alias: 'company_name', text: '名称'},
    {alias: 'company_fullname', text: '公司全称'},
    {alias: 'ts_code', text: '股票代码'},
    {alias: 'exchange', text: '交易所代码'},
    {alias: 'chairman', text: '法人代表'},
    {alias: 'manager', text: '总经理'},
    {alias: 'secretary', text: '董秘'},
    {alias: 'reg_capital', text: '注册资本'},
    {alias: 'setup_date', text: '注册日期'},
    {alias: 'province', text: '所在省份'},
    {alias: 'city', text: '所在城市'},
    {alias: 'introduction', text: '公司介绍'},
    {alias: 'website', text: '公司主页'},
    {alias: 'email', text: '电子邮件'},
    {alias: 'office', text: '办公室'},
    {alias: 'employees', text: '员工人数'},
    {alias: 'main_business', text: '主要业务及产品'},
    {alias: 'business_scope', text: '经营范围'},
)

export const BUY_FACTORS = new Enum(
    {alias: 'FactorBuyNdayBreak', text: 'N日趋势突破策略', value: 'FactorBuyNdayBreak'},
    {alias: 'FactorBuyAverBreak', text: '单均线突破策略', value: 'FactorBuyAverBreak'}
)

export const SELL_FACTROS = new Enum(
    {alias: 'FactorSellNdayBreak', text: 'N日趋势突破策略', value: 'FactorSellNdayBreak'},
    {alias: 'FactorSellAverBreak', text: '单均线突破策略', value: 'FactorSellAverBreak'},
    {alias: 'FactorSellAtrStop', text: 'ATR止盈止损风险策略', value: 'FactorSellAtrStop'}
)
export const FACTORS = new Enum(
    {alias: 'DoubleTrendFusion', text: '双趋势融合策略'}
)
