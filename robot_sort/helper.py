def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        value = arr[i]
        left_index = i - 1
        while value < arr[left_index] and left_index >= 0:
            arr[left_index + 1] = arr[left_index]
            left_index -= 1
        arr[left_index + 1] = value
    return arr
from helper import selection_sort
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = arrA + arrB
    final_arr = selection_sort(merged_arr)
    print(f'merged_arr: {final_arr}')
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = int(len(arr) / 2)
        left_arr = arr[:middle] 
        right_arr = arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        sortedA = selection_sort(left_arr)
        sortedB = selection_sort(right_arr)
        arr_merge = merge(sortedA, sortedB)
        return arr_merge
    else:
        return arr
