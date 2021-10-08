if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if i + j + k != n:
                    result.append([i, j, k])

    print(result)