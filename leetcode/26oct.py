matrix =  [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
n = int(input())
k = int(input())

# def rec(n):
#     def haha(i,j):
#         if i >= n :
#             return 
#         if j == n :
#             print()
#             return haha(i+1,0)
#         print("*",end = " ")
#         haha(i,j+1)

#     haha(0,0)
# rec(n)



def rec(n):
    global matrix 
    island = 0
    def haha(i,j):
        nonlocal island
        if i >= n :
            return 
        if j == n :
            return haha(i+1,0)
        ans += matrix[i][j]
        if matrix[i][j] % k == 0 :
            island += 1
        if i+1 < n :
            if (matrix[i][j] + matrix[i+1][j]) % k == 0 :
                island += 1
        if j+1 < n :
            if (matrix[i][j] + matrix[i][j+1]) % k == 0 :
                island += 1
        if i-1 < n :
            if (matrix[i][j] + matrix[i-1][j]) % k == 0 :
                island += 1
        if j-1 < n :
            if (matrix[i][j] + matrix[i][j-1]) % k == 0 :
                 island += 1
        if i+1 < n :
             if (matrix[i][j] + matrix[i+1][j]) % k == 0 :
                island += 1
        if i+1 < n :
            if (matrix[i][j] + matrix[i+1][j]) % k == 0 :
                island += 1
        if i+1 < n :
            if (matrix[i][j] + matrix[i+1][j]) % k == 0 :
                island += 1

        if i +1 < len(matric[0]):
            matrix[i][j] = matrix[j][i]
            return 
        else :
            return None 

    haha(0,0)
    return         


p = [[1],[-1]]
    
