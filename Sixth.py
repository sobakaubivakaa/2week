# First
# N = int(input("Enter the size "))
# arr = []
# max=float('-inf')
# av=0
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if max<=arr[i]:
#         max=arr[i]
# for i in range(0,N):
#     av+=arr[i]
# av = av/N
# for i in range(0,N):
#     if arr[i]==0:
#         arr[i]=av
# print(max)
# print(arr)

# Second
# N = int(input("Enter the size "))
# arr = []
# arr2 = []
# arr3=[]
# min=float('inf')
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if arr[i]>=0:
#         arr2.append(arr[i])
#     else:
#         arr3.append(arr[i])
# for i in range(0,N):
#     if min>=arr[i]:
#         min=arr[i]
# print("arr2: ",arr2)
# print("arr3: ",arr3)
# print("Min value: ",min)
# print("Min value index: ",arr.index(min)+1)

# Third
# N = int(input("Enter the size "))
# arr = []
# count = 0
# for i in range(0,N):
#     arr.append(int(input()))
#     if i % 2!=0:
#         count+=arr[i]
# print(count)

# 2)
# arr = [8,8,8,8,8,8,8,18]
# for i in range(0,len(arr)):
#     if arr[i]<15:
#         arr[i]*=2
#         print("num with index ",i+1," was changed, " ,arr[i])
#     else:
#         print("num with index ",i+1," was not changed, " ,arr[i])

# Fourth

# N = int(input("Enter the size "))
# arr = []
# max=float('-inf')
# av=0
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if max<=arr[i]:
#         max=arr[i]
# print(max)
# print(arr.index(max)+1)

# 2)
# N = int(input("Enter the size "))
# arr = []
# arr2 = []
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if arr[i]%2!=0:
#         arr2.append(arr[i])
# print(arr2)

# Fifth
# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# arr.sort()
# print(arr)

# 2)not correct
# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# for i in range(0,10):
#     for k in range(9,-1,-1):
#         if i==k:
#             pass
#         elif arr[i] == arr[k]:
#             arr.pop(k)
# print(arr)

# Sixth
# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# temp = arr[9]
# arr.sort()
# temp = arr.index(temp)
# print("All elements less than max index: " , arr[0:temp])
# print("All elements more than max index: " ,arr[temp:10])

# 2)
# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# sum = 0
# for i in range(0,10):
#     if arr[i]>5:
#         sum+=arr[i]
# print(sum)

# Seventh
# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# sum = 0
# product = 1
# for i in range(0,10):
#     if arr[i]==0:
#         sum+=arr[i]
#     elif arr[i]%2 == 0:
#         sum+=arr[i]
#     else:
#         product*=arr[i]
# print(sum)
# print(product)

# 2)
# N = int(input("Enter the size "))
# arr = []
# temp = []
# min=float('inf')
# max = float('-inf')
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if min>=arr[i]:
#         min=arr[i]
#     if max<=arr[i]:
#         max = arr[i]
# temp.append(arr.index(max))
# temp.append(arr.index(min))
# arr[temp[0]] = min
# arr[temp[1]] = max
# print(arr)

# Eight

# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# sum = 0
# product = 1
# for i in range(0,10):
#     sum+=arr[i]
#     product*=arr[i]
# print(sum)
# print(product)

# 2)
# N = int(input("Enter the size "))
# arr = []
# av=0
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     av+=arr[i]
# av = av/N
# for i in range(0,N):
#     if arr[i]==0:
#         arr[i]=av
# print(arr)

# Ninth

# N = int(input("Enter the size "))
# arr = []
# min = float('inf')
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     arr[i] = abs(arr[i])
#     if min > arr[i]:
#         min=arr[i]
# print(min)
# arr.reverse()
# print(arr)

# 2)
# A =[]
# B =[]
# temp = [0,0,0,0,0,0,0,0,0,0]
# print("Enter numbers for list A")
# for i in range(0,10):
#     A.append(int(input()))
# print("Enter numbers for list B")
# for i in range(0,10):
#     B.append(int(input()))
# for i in range(0,10):
#     temp[i] = A[i]
#     A[i] =B[i]
#     B[i]=temp[i]
# print("Changed A: ", A)
# print("Changed B: ", B)

# Tenth
# 2)
# arr = []
# arr2 = []
# for i in range (0,15):
#     arr.append(int(input()))
# print(arr)
# for i in range (0,15):
#     if arr[i]<10:
#         arr2.append(0)
#     elif arr[i]>20:
#         arr2.append(1)
#     else:
#         arr2.append(arr[i])
# print(arr2)

# Eleventh
# N = int(input("Enter the size "))
# arr = []
# max = float('-inf')
# for i in range(0,N):
#     arr.append(int(input()))
# for  i  in range(0,N):
#     if arr[i]%2==0:
#         if max<arr[i]:
#             max=arr[i]
# print(max)

# 2)
# N = int(input("Enter the size "))
# arr = []
# arr2 = []
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if arr[i]%2==0:
#         if arr[i]<10:
#             arr2.append(arr[i])
# if len(arr2) != 0:
#     print(arr2)
# else:
#     print("There is no such elements")

# Twelve
# N = int(input("Enter the size "))
# arr = []
# min = float('inf')
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if arr[i]%2!=0:
#         if min>arr[i]:
#             min=arr[i]
# print(min)

# 2)
# A =[]
# B =[]
# temp = [0,0,0,0,0,0,0,0,0,0]
# print("Enter numbers for list A")
# for i in range(0,10):
#     A.append(int(input()))
# print("Enter numbers for list B")
# for i in range(0,10):
#     B.append(int(input()))
# for i in range(0,10):
#     temp[i] = A[i]
#     A[i] =B[i]
#     B[i]=temp[i]
# print("Changed A: ", A)
# print("Changed B: ", B)

# Thirteen

# arr = []
# for i in range(0,8):
#     arr.append(int(input()))
# for i in range(0,8):
#     if arr[i]<15:
#         arr[i] = arr[i]*2
# print(arr)

# Fourteen
# N = int(input("Enter the size "))
# arr = []
# temp = []
# min=float('inf')
# max = float('-inf')
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if min>=arr[i]:
#         min=arr[i]
#     if max<=arr[i]:
#         max = arr[i]
# temp.append(arr.index(max))
# temp.append(arr.index(min))
# arr[temp[0]] = min
# arr[temp[1]] = max
# print(arr)

# 2)
# sum = 0
# arr =[]
# for i in range(0,10):
#     arr.append(int(input()))
# for i in range(0,10):
#     sum+= arr[i]
# sum = sum/10 + 1
# for i in range(0,10):
#     arr[i] = sum
# print(arr)

# Fifteen
# arr = []
# for i in range(0,10):
#     arr.append(int(input()))
# for i in range(0,10):
#     for k in range(9,-1,-1):
#         if i==k:
#             pass
#         elif arr[i] == arr[k]:
#             arr.pop(k)
# print(arr)

# 2)
# N = int(input("Enter the size "))
# arr = []
# arr2 = []
# for i in range(0,N):
#     arr.append(int(input()))
# for i in range(0,N):
#     if arr[i]%2!=0:
#         arr2.append(arr[i])
# if len(arr2) !=0:
#     arr2.sort()
#     print(arr2)
# else:
#     print("There is no such element")
