from numpy import array as vec

va = vec([1, 2])
vb = vec([3, 3])

print(va + vb)

S1 = 0.5*(va + vb)
print(S1)

print(3*va) # reálny súčin
print(va*vb) # vektorový súčin
print(va.dot(vb)) # skalárny súčin