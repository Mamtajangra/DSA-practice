def merge(left_arr,right_arr):
    i=j=0
    M=[]
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            M.append(left_arr[i])
            i=i+1
        else:
            M.append(right_arr[j])    
            j=j+1

    while i <len(left_arr):
           M.append(left_arr[i])
           i=i+1
    while j< len(right_arr):
           M.append(right_arr[j])
           j=j+1

    return M



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid_idx = len(arr)//2
    left_side = arr[:mid_idx]  
    right_side = arr[mid_idx:] 
    sorted_left = merge_sort(left_side)
    sorted_right = merge_sort(right_side)  

    return merge(sorted_left,sorted_right) 



arr = [23,43,22,76,32,12,66,67]
sorted_arr = merge_sort(arr)
print(sorted_arr)
# print(arr)
          
                
        





















arr = [23,43,22,76,32,12,66,67]