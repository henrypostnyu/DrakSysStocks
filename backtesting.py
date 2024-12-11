import backtrader as bt

class TestStrategy(bt.Strategy):
    def next(self):
        if self.data.close[0] > self.data.open[0]:
            self.buy(size=10)
        elif self.data.close[0] < self.data.open[0]:
            self.sell(size=10)

cerebro = bt.Cerebro()
data = bt.feeds.PandasData(dataname=yf.download("AAPL", start="2022-01-01", end="2022-12-31"))
cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.run()
cerebro.plot()
