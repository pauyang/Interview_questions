'''

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Input: coins = [1], amount = 1
Output: 1

Input: coins = [1], amount = 2
Output: 2
'''

class Solution:
    def coinChange(self, coins, amount):

        #initializing the array of answers
        dp=[amount+1]*(amount+1)
        dp[0] =0

        for a in range(1,amount+1):
            for coin in coins:
                if a-coin >=0:
                    dp[a] = min(dp[a], 1+dp[a-coin])


        return dp[amount] if dp[amount] != amount+1 else -1




#
s = Solution()
t = s.coinChange([1,2,5],11)
print (t)




