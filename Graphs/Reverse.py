def RPF(tokens) :
    stack = []
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
            
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            
            elif token == '-':
                stack.append(operand1 - operand2)
                
            elif token == '*' :
                stack.append(operand1 * operand2)
                
            elif token == '/':
                stack.append(int(operand1 / operand2))
                
    return stack[0]

rpn_exp = ["2", "1", "+","3", "*"]
result = RPF(rpn_exp)
            


























