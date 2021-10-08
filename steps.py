'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

n=2
1+1
2

n=3
1+1+1
2+1
1+2

n=4
1+1+1+1
1+1+2
2+1+1
2+2

n=5

1+1+1+1+1
1+1+1+2
1+2+2
2+2+1
2+1+1+1
2+1+2

n=6
1+1+1+1+1+1
1+1+1+1+2
1+1+2+2
2+2+2
2+1+1+1+1
2+2+1+1
1+2+1+1+1
1+1+2+1+1



# '''
# #c = {}
#
# def steps(n):
#     c={}
#     if n ==1:
#         return 1
#
#     if n ==2:
#         return 2
#
#
#     elif str(n) in c.keys():
#         return c[str(n)]
#     else:
#         c[str(n)]= steps(n-2)+steps(n-1)
#         return steps(n-2)+steps(n-1)
#
# step_count = steps(105)
#
# print (step_count)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        else:
            # c[str(n)]= steps(n-2)+steps(n-1)
            return self.climbStairs(n - 2) + self.climbStairs(n - 1)


S = Solution()
t=S.climbStairs(10)
print(t)
