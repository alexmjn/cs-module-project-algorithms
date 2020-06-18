'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for i in range(1, len(arr)):
        while (arr[i-1] == 0) and (i != 0):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return arr

    for i in range(len(arr)):
        x = arr[i]
        if x != 0:
            arr = [x] + arr[:i] + arr[i+1:]


# try timing these!
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# pointers tend to make things more efficient

#  pointer that started at the beginning and one that started at end
# and they moved toward each other in the middle

# if left pointer "sees" a zero and the right pointer "sees" a nonzero,
# swap

# left sees a nonzero, increment
# right sees a zero increment

def moving_zeroes_second(array):
    i = 0
    j = len(array)
    while i < j:
        if array[i] == 0 and array[j] != 0:
            array[i], array[j] = array[j], array[i]

        elif array[i] != 0:
            i += 1

        else:
            j -= 1
