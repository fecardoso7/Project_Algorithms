# Function to check if two strings are anagrams
def is_anagram(first_string, second_string):
    # If both strings are empty, they are trivially anagrams
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    # Convert strings to lowercase and create arrays of characters
    array_a, array_b = list(first_string.lower()), list(second_string.lower())

    # Sort character arrays using merge sort
    array_a = merge_sort(array_a)
    array_b = merge_sort(array_b)

    # Convert sorted arrays back to strings
    array_a, array_b = "".join(array_a), "".join(array_b)

    # Return sorted strings and check if they are equal
    return (array_a, array_b, array_a == array_b)


# Merge sort implementation to sort character arrays
def merge_sort(numbers):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(numbers) <= 1:
        return numbers

    # Split the array into two halves and recursively sort them
    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])

    # Merge the sorted halves and return the merged array
    return merge(left_half, right_half)


# Merge function to combine two sorted arrays into a single sorted array
def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Compare elements from the left and right arrays and merge them
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append remaining elements from both arrays to the merged array
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
