def asteroidCollision(asteroids):
    stack = []  # Create an empty Stack

    for asteroid in asteroids:
        while stack and stack[-1] > 0 > asteroid:
            # If 'asteroid' smaller than last element of the 'stack' then break
            if stack[-1] + asteroid > 0:
                break

            # If 'asteroid' bigger than last element of the 'stack' then delete last element of the 'stack'
            # until the end of the 'stack', or until 'asteroid' smaller than last element of the 'stack'
            elif stack[-1] + asteroid < 0:
                stack.pop(-1)

            # If 'asteroid' is equal to the last element of the 'stack' then delete last element of the 'stack'
            else:
                stack.pop(-1)
                break

        # If none of above conditions meet, then append the element to the 'stack'
        else:
            stack.append(asteroid)

    return stack


asteroids = [10, 2, -5]

asteroidCollision(asteroids)
