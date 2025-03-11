vector1 = [19,30,3.9,15.60]
for i in vector1:
    print(i)

matrix1 = [[12, 4 ,5], [5,7,9], [19, 0.5, 34]]
print(matrix1[-1])

def busca_linear(L, x):
    achou = False
    i = 0
    while i < len(L) and not achou:
        if (L[i] == x):
            achou = True
            pos = i
        else:
             i = i+1

    if achou:
        return pos
    else:
        return achou

if __name__ == "__main__":
    L = [12, 99, 37, 24, 2, 15]
    result =  busca_linear(L, 12)
    print(result)