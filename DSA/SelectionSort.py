arr = [2 ,3 ,4 ,9 ,1 ,3, 7 , 34 ,43, 2 ]
n = len(arr)
for i in range(n-1): #
    min_Index = i
    for j in range(i+1 , n):
        if arr[j] < min_Index:
            min_Index = arr[j]
print(arr)