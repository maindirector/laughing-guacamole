lis = [2, 4, 1, 5, 10, 3]
for n in range (len(lis)-1):   
    for i in range(len(lis)-1):   
        if lis[i] > lis[i + 1]:
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
        else:
            None
print(lis)

lis = ['hello', 'dg', 'sdfsg', 's']
for n in range(len(lis)-1):
    for i in range(len(lis)-1):
        if len(lis[i]) > len(lis[i+1]):
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
print(lis)

lis = [2, 4, 1]
for n in range (len(lis)-1):   
    for i in range(len(lis)-1):   
        if lis[i] < lis[i + 1]:
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
        else:
            None
print(lis)






