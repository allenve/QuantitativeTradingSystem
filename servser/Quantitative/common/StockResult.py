class StockResult:
    def __init__(self):
        self.stocks = []
        print('StockResult init')

    def pushStockResult(self, stock_res):
        print('run pushStockResult')
        self.stocks.append(stock_res)

    def returnStockResult(self):
        print('run returnStockResult')
        print(self.stocks)
        return self.stocks