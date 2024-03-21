def count_pairs(lst):
    lst.sort()  # Sort the list
    left = 0  # Initialize left pointer
    count = 0
    n = len(lst)
    
    for right in range(n):
        while lst[right] - lst[left] > 4:
            left += 1  # Move left pointer forward if difference is more than 4
        count += right - left  # Count pairs for the current right pointer
    
    return count

# Example list
numbers = [1, 5, 9, 12, 15, 20, 24]

# Function call and print result
result = count_pairs(numbers)
print("Number of pairs with difference of 4 or less:", result)
