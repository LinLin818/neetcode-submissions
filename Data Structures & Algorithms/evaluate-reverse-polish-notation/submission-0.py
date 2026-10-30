class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for i in tokens:
            # Added lstrip('-') so negative numbers (like "-3") are recognized as numbers
            if i.lstrip('-').isnumeric():
                numStack.append(int(i))
            else:
                operator_1 = numStack.pop() # right operand
                operator_2 = numStack.pop() # left operand
                
                if i == '-':
                    result = operator_2 - operator_1
                elif i == '+':
                    result = operator_2 + operator_1
                elif i == '/':
                    # int() truncates toward zero as required
                    result = int(operator_2 / operator_1)
                else:
                    result = operator_2 * operator_1
                
                # Moved inside the else block so it only runs for operators
                numStack.append(result)
                
        return numStack[0]




