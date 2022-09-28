y = int(input(" elements number: "))
x = [int(input("print element: ")) for i in range(y)]

z=[]

for i in range(y):
    if x[i]%2==0:
        z.append(x[i])
z.sort()
print(z) 
