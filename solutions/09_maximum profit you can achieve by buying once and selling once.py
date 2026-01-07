def max_profit(prices : list[int]) -> int:
    min_price = float("+inf")
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else :
            profit = price - min_price
            max_profit = max(max_profit, profit)
        #few line
        # min_price = min(min_price, price)
        # max_profit = max(max_profit, price - min_price)
            
    return max_profit