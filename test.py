def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif value > data[mid]:
            left = mid + 1
        else:
            right = mid - 1
        
    return None
        

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(data, 5)) 