# n = int(input())
# arr = list(map(int,input().split()))

# def rec(n):
#     l = []
#     l2 = []
#     def backtrack(n,i):
#         nonlocal l 
#         nonlocal l2
#         if i >= n :
#             print(*l2)
#             return 
#         l.append(arr[i])
#         l2.append(max(l))
#         backtrack(n,i+1)
#     return backtrack(n,0)
# rec(n)

# def rec(i,ma):
#     if i == n:
#         return
#     print(max(ma,arr[i]), end=" ")
#     rec(i+1,max(ma,arr[i]))
#     l = []

# def rec(n):
#     arr = []
#     def ans(i):
#         if i >= n :
#             return 

#     ans(0)