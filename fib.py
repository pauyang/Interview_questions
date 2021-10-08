

#Fib sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
#from functools import lru_cache

#@lru_cache


# d = {}
#
# def fib(n):
#
#
#     if n == 0:
#         return 0
#     elif n <=2:
#         return 1
#     elif str(n) in d.keys():
#             return d[str(n)]
#     else:
#         d[str(n)]= fib(n-1)+fib(n-2)
#         print (d)
#         return fib(n-1)+fib(n-2)
#
#
# t = fib(100)
#
# print (t)

def fib(n):

    last = 0
    last_two = 1

    if n == 0:
        return 0
    elif n <=2:
        return 1

    for i in range(n):

        result = last + last_two
        last_two = last
        last = result

    return result

print(fib(100000))