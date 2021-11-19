def longestConsecutive(nums):
    if len(nums) == 0:
        return 0

    count = 0
    final = 0
    nums = list(sorted(set(nums)))
    print(nums)

    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1] - 1:
            count += 1
        else:  # If 'nums[num] != nums[num + 1] - 1'
            if count >= final:
                final = count
            count = 0  # Here we decrease 'count' down to zero
            if nums[num] == nums[num + 1] - 1:  # Here we continue for loop for Non-Consecutive numbers
                count += 1

    # When we increase 'count', we don't consider last number
    # Let's say our list is [5, 6, 7, 8]
    #  if 6 - 1 = 5  then count(0) + 1
    #  if 7 - 1 = 6  then count(1) + 1
    #  if 8 - 1 = 7  then count(2) + 1
    # What about 8? As 8 is the last number and there is nothing left to compare, we add 1 at the end of the last loop
    return max(count, final) + 1


nums = [7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0]
print(longestConsecutive(nums))
