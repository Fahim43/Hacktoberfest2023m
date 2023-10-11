def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Adjust the lower bound
        else:
            high = mid - 1  # Adjust the upper bound

    return -1  # Element not found

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15]
search_target = 7

result = binary_search(my_list, search_target)

if result != -1:
    print(f"Element {search_target} found at index {result}")
else:
    print(f"Element {search_target} not found in the list")
