def busca_binaria(L, x):
    if len(L)==0:
        return False
    else:
        meio_lista = len(L) // 2

        if L[meio_lista] == x:
            return True
        elif x > L[meio_lista]:
            return busca_binaria(L[meio_lista + 1:], x)
        elif x < L[meio_lista]:
            return busca_binaria(L[:meio_lista], x)


List = [3,8,10,11,13]
x = 93
print(busca_binaria(List, x))