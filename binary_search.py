
'''
#iteration
def binary_search (n,target):
    #assume n is a list of integers
    L = 0
    R = len(n)-1


    while (L<R):
        mid = L + ((R - L) // 2)
        if n[mid]> target:
            R= mid+1

        elif n[mid]< target:
            L = mid-1

        elif n[mid]==target:
            return mid

        else:
            return -1

'''

# Recursive

def binary_search (n,L,R,target):
    #assume n is a list of integers
    found = 0
    if n:
        mid = L + ((R - L) // 2)

    else:
        return -1

    if n[mid]> target:
        R=mid-1
        found = binary_search(n,L,R,target)

    elif n[mid]< target:
        L = mid+1
        found = binary_search(n,L,R,target)

    elif n[mid]==target:
        return mid

    return found






n= [1,2,3,4,5,6,7,8]
L = 0
R= len(n)-1


print(binary_search(n,L,R,5))