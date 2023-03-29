from AlgorithmImports import *

class MeasuredFluorescentPinkCow(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021, 1, 1)
        self.SetCash(100000)

        spy = self.AddEquity("SPY", Resolution.Daily)
        # self.AddForex, self.AddFuture...
        
        spy.SetDataNormalizationMode(DataNormalization.Raw)

        self.spy = spy.Symbol

        self.SetBenchmark("SPY")
        self.SetBrokarageModel(BrokerageName.InteractiveBrokersBrokarage, AccountType.Margin)

        self.entryPrice = 0
        self.period = timedelta(31)
        self.nextEntryTime = self.Time

    def OnData(self, data): # every time a tick event occurs or a bar reaches its end time
        pass
