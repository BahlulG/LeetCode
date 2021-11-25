def checkValidString(s):
    stack_brackets = []
    stack_star = []
    for value in range(len(s)):
        if stack_brackets or stack_star:
            if s[value] == '(':
                stack_brackets.append(value)
            elif s[value] == ')':
                if stack_brackets:
                    stack_brackets.pop(-1)
                elif stack_star:
                    stack_star.pop(-1)
            else:
                stack_star.append(value)

        else:
        # Add first value to stack
        # If value is closing bracket, then return False. Why?
        # ')*()': in this case even star turns to opening or closing bracket,
        # it won't change the situation: '))()' or ')(()'
            if s[value] == '(':
                stack_brackets.append(value)
            elif s[value] == '*':
                stack_star.append(value)
            else:
                return False

    if stack_brackets and stack_star:
    # Here if 'stack_brackets' and 'stack_star' is not empty,
    # if index of star higher than open bracket, then pop from both of the stacks
        # It means, star is after the openening bracket
        # because star turns to closing bracket, we delete full bracket
        # idx: 1 4 == 1 4
        # val: ( * == ( )
    # if index of star lower than open bracket, then pop from star_stack
        # Because star falls behind the opening bracket, if it turns to closing bracket
        # it doesn't change anything
        # idx: 1 4 == 1 4
        # val: * ( == ) (
        
        while stack_brackets and stack_star:
            if stack_brackets[0] < stack_star[0]:
                stack_brackets.pop(0)
                stack_star.pop(0)
            elif stack_brackets[0] > stack_star[0]:
                stack_star.pop(0)
            else:
                return False
    return len(stack_brackets) == 0


s = "(*)"
checkValidString(s)
