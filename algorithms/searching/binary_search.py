def binary_search(arr,val_to_find):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high)//2
        if val_to_find == arr[mid]:
            return mid
        if val_to_find < arr[mid]:   ## less from mid so the value of high get changed
            high = mid - 1
        else:
            # val_to_find > arr[mid]:    
            low = mid +1               ## more than mid so lower value get changed
    return False                          ## if value is not in arr use false here
                



arr = [1,34,56,78,88,89,94,98,99]
val_to_find = 98
print(binary_search(arr,val_to_find))