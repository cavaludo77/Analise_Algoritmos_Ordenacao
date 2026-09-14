import random

# ----------------------------
# Bubble Sort
# ----------------------------
def bubble_sort(v):
    comp = 0
    trocas = 0

    for i in range(len(v)-1):
        for j in range(len(v)-1-i):
            comp += 1
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                trocas += 1

    return comp, trocas


# ----------------------------
# Insertion Sort
# ----------------------------
def insertion_sort(v):
    comp = 0
    mov = 0

    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1

        while j >= 0:
            comp += 1
            if v[j] > chave:
                v[j+1] = v[j]
                mov += 1
                j -= 1
            else:
                break

        v[j+1] = chave

    return comp, mov


# ----------------------------
# Selection Sort
# ----------------------------
def selection_sort(v):
    comp = 0
    trocas = 0

    n = len(v)

    for i in range(n-1):
        menor = i

        for j in range(i+1, n):
            comp += 1
            if v[j] < v[menor]:
                menor = j

        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            trocas += 1

    return comp, trocas


# ----------------------------
# Quick Sort
# ----------------------------
def quick_sort(v):

    comp = 0
    mov = 0

    def particao(inicio, fim):
        nonlocal comp, mov

        pivo = v[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            comp += 1
            if v[j] <= pivo:
                i += 1
                v[i], v[j] = v[j], v[i]
                mov += 1

        v[i+1], v[fim] = v[fim], v[i+1]
        mov += 1
        return i + 1

    def quick(inicio, fim):
        if inicio < fim:
            p = particao(inicio, fim)
            quick(inicio, p-1)
            quick(p+1, fim)

    quick(0, len(v)-1)

    return comp, mov


# ----------------------------
# Experimentos
# ----------------------------

random.seed(42)

tamanhos = [10, 20, 1000]

print("Tamanho | Bubble(C,T) | Insertion(C,M) | Selection(C,T) | Quick(C,M)")
print("-"*70)

for n in tamanhos:

    original = [random.randint(1, 5000) for _ in range(n)]

    b = original.copy()
    i = original.copy()
    s = original.copy()
    q = original.copy()

    bc, bt = bubble_sort(b)
    ic, im = insertion_sort(i)
    sc, st = selection_sort(s)
    qc, qm = quick_sort(q)

    print(f"{n:7} | ({bc},{bt}) | ({ic},{im}) | ({sc},{st}) | ({qc},{qm})")