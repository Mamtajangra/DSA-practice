# determine a function
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n-1):
        # taking current value 
        curr_val = arr[i]
        # j will be the previous element of i
        j = i-1
        # check the condition
        while curr_val < arr[j] and j>=0:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = curr_val
            

# main
array = [23,1,10,5,2,8,7] 
insertion_sort(array)
print(array)           

        
    