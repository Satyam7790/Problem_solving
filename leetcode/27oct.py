m = int(input())
n = int(input())

# def ans():
#     mat = []
#     def haha(i,j):
#         nonlocal mat
#         if i >= m :
#             return 
#         if j >= n :
#             print()
#             return haha(i+1,0)
#         if i == 0 :
#             print(".",end=" ")
#             return haha(i,j+1)
#         if j == n-1:
#             print(".",end=" ")
#             return haha(i,j+1)
#         else:
#             print("#",end=" ")
#             return haha(i,j+1)
#     haha(0,0)
#     return mat

def ans(m,n):
    mat = [[""] * n for _ in range(m)]
    def haha(i,j):
        nonlocal mat
        if i >= m :
            return 
        if j >= n :
            return haha(i+1,0)
        if i == 0 :
            mat[i][j] ="."
        elif j == n-1:
            mat[i][j] = "."
        else:
            mat[i][j] ="#"
        haha(i,j+1)
    haha(0,0)
    return ["".join(row) for row in mat]
print(ans(m,n))

