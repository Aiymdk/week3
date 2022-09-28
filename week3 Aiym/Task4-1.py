y = int(input("elements number: "))
x = [int(input("print element: ")) for i in range(y)]

g = 0
for i in range(y):
    if x[i] > g:
        g = x[i]
print("greatest ",str(g))
print(str(x.index(g,0,len(x)))," - ordinal number")
