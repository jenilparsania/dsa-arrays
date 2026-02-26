def SellStocks(nums:list):
    n = len(nums)
    max_profit = 0
    min_stock = float("inf")
    for i in range(n):
        min_stock = min(min_stock,nums[i])
        difference= nums[i] - min_stock
        max_profit = max(max_profit,difference)

    return max_profit
    pass

nums =[7 ,1 ,5, 4 ,3, 6]
print(SellStocks(nums))