def quicksort(sequence):

    if len(sequence)<=1:
        return sequence


    elif sequence:

        pivot = sequence.pop()

        smaller_squence  =[]
        bigger_sequence = []

        for i in sequence:
            if i < pivot:
                smaller_squence.append(i)

            elif i > pivot:
                bigger_sequence.append(i)

        return quicksort(smaller_squence)+ [pivot] + quicksort(bigger_sequence)


s = quicksort([9,8,7,6,5,4,2,1])
print(s)
