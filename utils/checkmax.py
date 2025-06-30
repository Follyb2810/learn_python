def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if(num > maximum):
            maximum= num
    return maximum
