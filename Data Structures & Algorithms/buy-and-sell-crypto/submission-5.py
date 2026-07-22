class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # #The index position are the days of the price
        # #prices[i] is the price itself
        # #Profit means Buy price - sell price

        # profit = 0

        # #I would argue to find the cheapest price then sell at the highest price, but the days dont make sense so
        # #If day_buy < day_sell 
        # #found a pattern, i can only sell towards the right side of a buy, forgo left
        # #the best case would be the lowest number in the list is to the left of the highest number in the list

        # #if that is not the case, ill have to compare nearest neighbours
        # for i in range (0,len(prices)-1):  
        #     #set the if condition for the best case first here
        #     for w in range (i,len(prices)):
        #         if i == w:
        #             pass
        #         else:
        #             current_profit = prices[w] - prices[i]
        #             profit = max(current_profit,profit)

        # return profit 

        lowest_price_seen = 0
        best_profit = 0 

        i = 0
        for i in range(i,len(prices)):
            if i == 0:
                lowest_price_seen = prices[i]
            else:
                if prices[i] < lowest_price_seen:
                    lowest_price_seen = prices[i]
                    current_profit = prices[i] - lowest_price_seen
                    best_profit = max(current_profit,best_profit)
                else:
                    current_profit = prices[i] - lowest_price_seen
                    best_profit = max(current_profit,best_profit)
        return best_profit

                

