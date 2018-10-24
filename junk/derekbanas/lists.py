
grocery = ["juice", "tomatoes", "potatoes", "bananas"]

print("First item : ", grocery[0])
print("Subset: ", grocery[1:3])

different = ["XD", 3]
print(different)

grocery.append("onions")
grocery.remove("tomatoes")
grocery.insert(0, "pickle")
grocery.sort()
grocery.reverse()

# delete item from list
del grocery[0]

print(grocery)

print("length = ", len(grocery))
print("min = ", min(grocery))

# --- references logic

l = [1, 2, 3]
t = l # assign reference to t
t[0] = 99 # change the same list
print(l) # print using the original reference

# copy list
g = l.copy()
l[0] = 0
print(g) # unchanged l from before ( with 99 )

# alternative
q = []+l
l[0] = 44
print(q) # unchanged 0 from before