
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 0 

for i in range(len(arr1)):
    flag  = True
    for j in range(len(arr1)):
        if abs(arr1[i] - arr2[j]) <= d :
            flag = False 
    if flag :
        d += 1 

print(d)
        

