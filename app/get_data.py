import yfinance as yf

def lower(amount):
    ticker=yf.Ticker("^NSEI")
    data=ticker.history(period="2d",interval="1d")
    if data["Close"].iloc[-1]>data["Close"].iloc[-2]:
        return "If you can take risks for higher profits: Allocate 60% to a Mid/Small-cap Mutual Fund and 40% to a safe Liquid Fund."
    else:
        return "Should prefer Mutual Funds for all your money as market is down today.\nCheck market again tommorow."
    
def middle(amount):
    ticker=yf.Ticker("^NSEI")
    data=ticker.history(period="2d",interval="1d")
    if data["Close"].iloc[-1]>data["Close"].iloc[-2]:
        keep=(amount*40)/100
        invest=amount-keep
        return f"Get {keep} in Hybrid Mutual Funds and {invest} in Small-Cap Equity Mutual Funds or Selective Stocks"
    else:
        return "Market is low, prefer mutual funds."
    
def upper(amount):
    ticker=yf.Ticker("^NSEI")
    data=ticker.history(period="2d",interval="1d")
    keep=(amount*70)/100
    invest=amount-keep
    if data["Close"].iloc[-1]>data["Close"].iloc[-2]:
        return f"Get {keep} in safe bonds and stocks and spread {invest} in equities, debt, gold, real estate."
    else:
        return f"Get most of your money(at least 65%) in safe bonds."