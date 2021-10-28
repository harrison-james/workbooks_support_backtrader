import datetime
import backtrader as bt
import backtrader.feeds as btfeeds

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.stochslow = bt.indicators.Stochastic()
        self.k_line = self.stochslow.percK
        self.d_line = self.stochslow.percD
        self.signal = bt.indicators.CrossOver(self.k_line, self.d_line)
    def next(self):
        pass



data = bt.feeds.YahooFinanceCSVData(
    dataname='BTC-USD.csv',
    timeframe=bt.TimeFrame.Days,
    reverse = False,
    fromdate=datetime.datetime(2016, 10, 23),
    todate=datetime.datetime(2018, 10, 23))
#####################################################
if __name__ == '__main__':
# create a Cerebro instance
    challengeTest = bt.Cerebro()
    challengeTest.broker.setcash(100000.0)
    print('Starting Portfolio Value: %.2f' % challengeTest.broker.getvalue())
total = 0
#Add a strategy
challengeTest.addstrategy(MyStrategy)
#create a data feed
challengeTest.adddata(data)
#run the strategy
challengeTest.run()
print('Starting Portfolio Value: %.2f' % challengeTest.broker.getvalue())
challengeTest.plot()
quit()