##### I COULDN'T SOLVE IT YET. I WILL UPDATE IT AS I COMPLETE #####

class Portfolio():
    def __init__(self):
        super().__init__()
    
class cash(Portfolio):
    def __init__(self, cash_value):
        super().__init__()
        self.cash_value = cash_value
        self.db = {}
    def add(self, cash):
        if cash in self.db:
            sum = self.db + cash
            self.db[cash] = sum
        else: self.db[cash] = {cash}

class stock():  #integers, [0.5X-1.5X] price range
    def __init__(self, stock_ticker):
        super().__init__()
        self.stock_ticker = stock_ticker
        self.db = {}
    def add(self, ticker):
        if ticker in self.db:
            isinstance(ticker , int)
        else: "Stock input is not integer"  
        if ticker in self.db:
            self.db[ticker].add(ticker)
        else: self.db[ticker] = {ticker}
    def add(self, sell_ticker):
        if ticker in self.db:
        self.db = ticker*randrange(0.5,1.5)    
        
class mutual_fund(): # only fractional, [0.9X-1.2X] price range
    def __init__(self, mutual_fund):
        super().__init__()
        self.mutual_fund = mutual_fund
        self.db = {}
    def add(self, mutual_fund):
        if mutual_fund in self.db:
            isinstance(mutual_fund , float)
        else: "Mutual Fund input is not fractional"
        if mutual_fund in self.db:
            self.db[mutual_fund].add(mutual_fund)
        else: self.db[mutual_fund] = {mutual_fund}