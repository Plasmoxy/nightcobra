# postupnost cisel
X = [1, -2, 4, 5, -1, -5, 2, 7]

# ZADANIE : najdi suctom najvacsi rozsah cisel v postupnosti X


# straightforward algoritmus
# otestuje vsetko
m = 0
for i in range(len(X)):
    for j in range(i, len(X)):
        s = 0
        for k in range(i, j+1):
            s = s + X[k]
        m = max(m, s)

print('ALG 1 : ' + str(m)) # sucet


m = 0
for i in range(len(X)):
    s = 0
    for j in range(i, len(X)):
        s = s + X[j]
        m = max(m, s)

print('ALG 2 : ' + str(m)) # sucet

m = 0
k = 0
for i in range(len(X)):
    k = max(k, 0) + X[i] # = max(k + X[i], X[i])
    m = max(m, k)

print('ALG 3 : ' + str(m)) # sucet