"""
This	problem asks	you	to	sum	up	all	of	the	numbers	within	an	array,	but	the	array	may	also	contains	
other	arrays	with	numbers.	This	is	what	we	call a	nested	array. For	example:
[1, 1, 1, [3, 4, [8]], [5]]
is	a	nested	array	and	summing	all	the	elements	should	produce	23
"""


numbers = [1, 1, 1, [3, 4, [8]], [5]]

def sum_recursive(l):
    s = 0
    for o in l:
        if type(o) is list:
            s += sum_recursive(o)
        elif isinstance(o, int):
            s += o
    return s

print(sum_recursive(numbers))