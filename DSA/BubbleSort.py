arr = [4, 2 ,1, 6, 7]
n = len(arr)
for i in range(n-1): #count value from 0 to n in an array.
    # take the current value of i = 0 ;  n = total length of the array = 5 ; n - 1 = 5 - 1 = 4 ; n - 1 - i = 5-1-o = 4 ; j = 4 current value. 
    for j in range(n-1-i): 
        if arr[j] > arr[j+1]: #check if the current array value is greater than the +1 ,  if yes
            temp = arr[j] # storing current array value in temporary variable.
            arr[j] = arr[j+1] # updating current j value with the next one if the other one is smaller.
            arr[j+1] = temp #updating the current j value .
            #this loop will run and check all values concurrently until all the values are sorted.
print(arr)

#time of complexity = Big O(n^2) = worst case and in all case.
