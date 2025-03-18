# conquer step to add individuals
def merge(left_arr,right_arr):
    i=j=0
    M = []                   ##blank list
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            M.append(left_arr[i])
            i=i+1
        else:
            M.append(right_arr[j])
            j=j+1 
    while i <len(left_arr):
            M.append(left_arr[i])
            i=i+1
    while j < len(right_arr):
            M.append(right_arr[j])
            j=j+1
    return M
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid_index = len(arr)//2
    left_side = arr[:mid_index]
    right_side = arr[mid_index:]

    sorted_left = merge_sort(left_side) 
    sorted_right = merge_sort(right_side) 
    return merge(sorted_left,sorted_right)
arr = [32,55,12,23,43,76,98,22,13,17]
sorted_arr = merge_sort(arr)
print(sorted_arr)


