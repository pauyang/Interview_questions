

def bubble_sort (array):

    n = len(s)
    i=0


    for i in range(n):
        for j in range(n-i-1):
            if array[j]<array[j+1]:
                array[j] = array[j+1]
                array[j+1] = array[j]

    return array



s=[9,8,7,6,5,4,3,2,1]

p=bubble_sort(s)
print(p)