def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Cria matrizes temporarias
    L = [0] * (n1)
    R = [0] * (n2)
    # Copia dados para as matrizes temporarias L[] and R[]
    for i in range(0, n1):
     L[i] = arr[l + i]
    for j in range(0, n2):
     R[j] = arr[m + 1 + j]
# Mescla as matrizes temporarias em arr[l..r]
i = 0 # Inicia index da primeira submatriz
j = 0 # Inicia index da segunda submatriz
k = l # Inicia index da submatriz mesclada
while i < n1 and j < n2:
    if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
    else:
        arr[k] = R[j]
        j += 1
        k += 1
        39
# Copia os elementos remanescentes de L[], se algum existe
while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1
# Copia os elementos menanescentes de R[], se algum existe
while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1
# l esta para os indices da esquerda e r esta para os indices da direita da
# sub-matriz de arr a ser ordenada
def mergeSort(arr, l, r):
    if l < r:
    # O mesmo que (l+r)//2, mas evita estouros para l e r grandes
        m = l+(r-l)//2
# Classifica a primeira e a segunda metades
mergeSort(arr, l, m)
mergeSort(arr, m+1, r)
merge(arr, l, m, r)
# Teste do codigo
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("A matriz fornecida eh a seguinte:")
for i in range(n):
    print("%d" % arr[i],end=" ")
mergeSort(arr, 0, n-1)
print("\n\nMatriz ordenada:")
for i in range(n):
    print("%d" % arr[i],end=" ")