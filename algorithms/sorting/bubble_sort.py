
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):                     ## to check interal members
            if arr[j] > arr[j+1]:                          ##check statement
                arr[j],arr[j+1] = arr[j+1],arr[j]       ## swapping

arr = [12,32,44,21,22,45,89,9]
bubble_sort(arr)
print(arr)