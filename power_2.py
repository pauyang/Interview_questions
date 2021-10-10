#
# def isPowerOfTwo(n):
#     if n ==0:
#         return False
#
#     while(n!=1):
#         if n ==0:
#             return True
#         elif (n%2 ==0):
#             n=n//2
#
#         elif (n%2!=0):
#             return False
#     return True

# print (isPowerOfTwo(6))



def isPowerOfTwo(n):
    if n ==1:
        return True
    elif n%2 !=0:
        return False
    else:
       return isPowerOfTwo(n//2)

print (isPowerOfTwo(7))