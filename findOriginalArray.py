import collections


def findOriginalArray(changed):
    if len(changed) % 2 == 1:  # Return empty array, if array length is not even
        return

    original = []
    numbers = collections.Counter(changed)

    for num in sorted(changed):
        double = num * 2

        # In order to understand below rest of code, use https://pythontutor.com/visualize.html#mode=edit link
        # copy paste all the code and view implementation step-by-step
        if numbers[num] > 0 and numbers[double] > 0:
            original.append(num)
            numbers[num] -= 1
            numbers[double] -= 1
        elif num % 2 != 0 or num // 2 not in numbers:
            return

    return original


array = [1, 3, 4, 2, 6, 8]

findOriginalArray(array)
