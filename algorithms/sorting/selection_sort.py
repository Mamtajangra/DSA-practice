# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        # another loop trying to check the value with minimum
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

# swapping 
        arr[i],arr[min_idx] = arr[min_idx],arr[i]


arr = [12,76,1,34,2,23,89]
selection_sort(arr)
print(arr)