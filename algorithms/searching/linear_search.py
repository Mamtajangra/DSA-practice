def linear_search(arr,val_to_find):
    n = len(arr)
    for i in range(n):
        if arr[i] == val_to_find:
            return i
    return False


arr = [12,43,22,1,32,11,23,31]
val_to_find = 32
print(linear_search(arr,val_to_find))
     