def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in '+-*/':  # Check if element not in operators, then append it to 'stack'
            stack.append(int(token))
        else:  # If element in operators, based on operator do operation to last to elements in 'stack'
            number_2, number_1 = stack.pop(), stack.pop()
            if token == '+':
                result = int(number_1 + number_2)
                stack.append(result)
            elif token == '-':
                result = int(number_1 - number_2)
                stack.append(result)
            elif token == '*':
                result = int(number_1 * number_2)
                stack.append(result)
            elif token == '/':
                result = int(number_1 / number_2)
                stack.append(result)
    return stack.pop()


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evalRPN(tokens)
