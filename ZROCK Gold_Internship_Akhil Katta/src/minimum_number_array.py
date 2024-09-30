def find_minimum(arr):
    if len(arr) == 0:
        return None  
    min_num = arr[0]  
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num


array = [3, 5, 1, 9, -2, 7]
min_value = find_minimum(array)
print("The minimum number in the array is:", min_value)