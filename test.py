def selection_sort (array):
    mi = 0
    for i in range(len(array)):
        for j in range(mi+1,len(array)):
            if array[j]<array[mi]:
                array[j],array[mi]=array[mi],array[j]
        mi+=1

    return array

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] >array[j+1]:
                array[j+1],array[j]= array[j],array[j+1]


    return array

def quicksort(array):

    if len(array)>1:
        pivot = array.pop()
        less =[]
        more =[]
        equal =[pivot]

        for i in range(len(array)):
            if array[i]<pivot:
                less.append(array[i])
            elif array[i]>pivot:
                more.append(array[i])
            else:
                equal.append(array[i])

        return quicksort(less)+equal+quicksort(more)

    else:
        return array





array = [4,5,3,1,7,8,2]
#t=selection_sort(array)
#t= bubble_sort(array)
t=quicksort(array)
print(t)