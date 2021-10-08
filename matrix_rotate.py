matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
looks= [[3,6,9],
        [2,5,8],
        [1,4,7]]

n = len(matrix)

for i in range(n):
    for j in range(i):
        #print (f'[{i},{j}]')
        print(f'[{j},{i}] = [{i},{j}]')
        print (f'[{i},{j}] = [{j},{i}]')

#         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
#
# for i in reversed(matrix):
#     print (i)



# for i in range(n):
#     for j in range(i):
#         print (i, j)
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for i in matrix:
#     i.reverse()
#

