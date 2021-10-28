import datetime
import backtrader as bt
import backtrader.feeds as btfeeds

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.stochslow = bt.indicators.Stochastic()
#get reference to fast k line
        self.k_line = self.stochslow.percK
#get reference to slow d line
        self.d_line = self.stochslow.percD
        self.signal = bt.indicators.CrossOver(self.k_line, self.d_line)
        self.order = None
        self.wait_candles = 0

    def next(self):
        self.wait_candles += 1

#if we are NOT in the market, we are looking to enter?
        if not self.position:  
            if self.signal > 0:
# fast crosses above slow so go long
                self.order = self.buy(size = 1, exectype=bt.Order.Limit)
            if self.signal < 0:
# fast crosses below slow so go short
                self.order = self.sell(size = 1, exectype=bt.Order.Limit)

#if we are IN the market, check for exit signal i.e. number of candles past
        if self.position and (self.wait_candles > 6):
            self.close()
            self.wait_candles = 0

        if self.position and (len(self)+1 >self.data.buflen()):
            self.close

data = bt.feeds.YahooFinanceCSVData(
    dataname='BTC-USD.csv',
    timeframe=bt.TimeFrame.Days,
    reverse = False,
    fromdate=datetime.datetime(2018, 10, 23),
    todate=datetime.datetime(2021, 10, 20))
    #fromdate=datetime.datetime(2016, 10, 23),
    #todate=datetime.datetime(2018, 10, 23))
#####################################################
if __name__ == '__main__':
# create a Cerebro instance
    challengeTest = bt.Cerebro()
    challengeTest.broker.setcash(100000.0)
    print('Starting Portfolio Value: %.2f' % challengeTest.broker.getvalue())

#Add a strategy
challengeTest.addstrategy(MyStrategy)
#create a data feed
challengeTest.adddata(data)
#run the strategy
challengeTest.run()
print('Final Portfolio Value: %.2f' % challengeTest.broker.getvalue())
challengeTest.plot()
quit()