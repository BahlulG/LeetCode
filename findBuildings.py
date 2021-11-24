def findBuildings(heights):
    max_height = 0
    stack = []

    for height in range(len(heights) - 1, -1, -1):
        # Here we do for loop in reversed order:
        # (len(heights) - 1: Start point of for loop
        # -1: Stop point of for loop
        # -1: Step of for loop

        if heights[height] > max_height:
            stack.append(height)
            max_height = heights[height]

    return reversed(stack)


heights = [4, 2, 3, 1]
findBuildings(heights)
