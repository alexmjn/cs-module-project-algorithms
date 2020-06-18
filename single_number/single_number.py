'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    result = arr[0]

    for i in range(1, len(arr)):
        result = result ^ arr[i]

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# def single_number(arr):
#     for elem in arr:
#         if arr.count(elem) == 1:
#             return elem

# def single_number_optimized(nums):
#     counts = {}

#     for num in nums:
#         if num in counts:
#             del counts[num]

#         else:
#             counts[num] = 1

#     return counts.keys()[0]
