"""You are given an array of integers 'prices' of size 'n', where ‘prices[i]’ is the price of a given stock on an ‘i’-th day. You want to maximize the profit by choosing a single day to buy one stock and a different day to sell that stock.



Please note that you can’t sell a stock before you buy one.



Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= 'n' <= 10 ^ 5
1 <= ‘prices[i]’<= 10 ^ 9

Time Limit: 1 sec
Sample Input 1:
6
7 1 5 4 3 6


Sample Output 1 :
5
"""

def SellStocks(prices:list):
    maxPro = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                maxPro = max(prices[j] - prices[i], maxPro)

    return maxPro
    pass

nums =[7 ,1 ,5, 4 ,3, 6]
print(SellStocks(nums))