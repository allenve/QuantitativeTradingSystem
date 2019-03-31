# # 历史数据回测
# from .. abupy import AbuFactorBuyBreak
# from .. abupy import AbuFactorAtrNStop
# from .. abupy import AbuFactorPreAtrNStop
# from .. abupy import AbuFactorCloseAtrNStop
# from .. abupy import AbuMetricsBase

# from .. abupy import abu, FactorBuyBu, FactorSellBu, CoreBu, AlphaBu, TradeBu


class RunLoopBack():
    def __init__(self, request):
        #初始资金
        self.read_cash="1000000"
        #选股因子 None为不使用
        self.stock_pickers = None
        #买入因子
        self.buy_factors = [
            # {'class': abupy.FactorBuyBu.ABuFactorBuyDM.AbuDoubleMaBuy}
            {'class': FactorBuyBu.ABuFactorBuyDM.AbuDoubleMaBuy, 'slow': -1, 'fast': -1}
        ]
        #卖出因子
        self.sell_factors = [
            {'stop_loss_n':1.0, 'stop_win_n': 3.0, 'class': AbuFactorAtrNStop},
            {'class': AbuFactorPreAtrNStop, 'pre_atr_n': 1.5},
            {'class': AbuFactorCloseAtrNStop, 'close_atr_n': 1.5}
        ]
        #股票池
        self.choice_symbols=['usBIDU']
        #开始时间
        self.start = '2013-07-10'
        self.end = '2016-07-26'


    def runLoopBack(self, request):
        print("========================================>")
        #初始资金
        read_cash="10000000"
        #选股因子 None为不使用
        stock_picks = None
        #买入因子
        # buy_factors = [
        #     {'xd': 60, 'class': AbuFactorBuyBreak},
        #     {'xd': 42, 'class': AbuFactorBuyBreak}
        # ]
        buy_factors = [
            # {'class': abupy.FactorBuyBu.ABuFactorBuyDM.AbuDoubleMaBuy}
            {'class': FactorBuyBu.ABuFactorBuyDM.AbuDoubleMaBuy, 'slow': -1, 'fast': -1}
        ]
        #卖出因子
        sell_factors = [
            {'class': FactorSellBu.ABuFactorAtrNStop.AbuFactorAtrNStop, 'stop_win_n': 3.0, 'stop_loss_n': 1.0}
        ]
        #股票池
        choice_symbols=['usBIDU']
        #开始时间
        start = '2014-07-25'
        end = '2016-07-26'

        # 如果只有1支股票回测，直接使用这个股票做为做为对比基准
        benchmark = TradeBu.ABuBenchmark.AbuBenchmark(choice_symbols[0], start=start, end=end)
        capital = TradeBu.AbuCapital(read_cash, benchmark)

        orders_pd, action_pd, _ = AlphaBu.ABuPickTimeExecute.do_symbols_with_same_factors(choice_symbols,
                                                                                      benchmark,
                                                                                      buy_factors,
                                                                                      sell_factors,
                                                                                      capital, show=True)

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("orders_pd:")                                                                
        print(orders_pd)
        print("------------------")
        print("action_pd:")
        print(action_pd),
        print("_:")
        print(_)
        print("------------------")
        abu_result_tuple = CoreBu.ABuStore.AbuResultTuple(orders_pd, action_pd, capital, benchmark)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<end")
        metrics = AbuMetricsBase(orders_pd, action_pd, capital, benchmark)
        # #运行策略
        # abu_result_tuple, kl_pd_manger = CoreBu.ABu.run_loop_back(read_cash,
        #                                                 buy_factors,
        #                                                 sell_factors,
        #                                                 stock_picks,
        #                                                 choice_symbols=choice_symbols,
        #                                                 n_folds=2,
        #                                                 start=start,
        #                                                 end=end,
        #                                                 commission_dict=commission_dict)
        # print("----------------------result:")
        # print(abu_result_tuple.capital.capital_pd)
        # metrics = AbuMetricsBase(*abu_result_tuple)
        # # print("metrics.plot_returns_cmp()")
        # metrics.fit_metrics()
        # self._metrics_out_put(metrics, abu_result_tuple)

        # # metrics.plot_returns_cmp()
        # # stock_result=metrics.plot_returns_cmp()
        # print("----------------------result:")
        # print(stock_result)
        # print(kl_pd_manger)

    def _metrics_out_put(self, metrics, abu_result_tuple):
        print("针对输出结果和界面中的设置进行输出操作")
        if metrics is None:
            return

        # if self.tt.metrics_mode.value == 0:
        metrics.plot_returns_cmp(only_show_returns=True)
        # else:
            # metrics.plot_order_returns_cmp(only_info=True)

        # pd.options.display.max_rows = self.tt.out_put_display_max_rows.value
        # pd.options.display.max_columns = self.tt.out_put_display_max_columns.value

        # if self.tt.metrics_out_put.value == 0 or self.tt.metrics_out_put.value == 3:
        #     show_msg_func(u'交易买卖详情单：')
        #     display(abu_result_tuple.orders_pd)
        # if self.tt.metrics_out_put.value == 1 or self.tt.metrics_out_put.value == 3:
        #     show_msg_func(u'交易行为详情单：')
        #     display(abu_result_tuple.action_pd)
        # if self.tt.metrics_out_put.value == 2 or self.tt.metrics_out_put.value == 3:
        #     show_msg_func(u'交易资金详细单：')
        #     display(abu_result_tuple.capital.capital_pd)
        #     show_msg_func(u'交易手续费详单：')
        #     display(abu_result_tuple.capital.commission.commission_df)

        # if self.tt.save_out_put.value is True:
        #     # 本地保存各个交易单到文件
        #     store_abu_result_out_put(abu_result_tuple)