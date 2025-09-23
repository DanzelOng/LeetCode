class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        To solve this problem, a stack is used to process the 
        tokens. At each iteration, the token is checked to see
        if its either (1) an operator or (2) a number. 
        
        If it is an operator, the 2 operands are popped from the 
        stack and the operator is applied and the result is pushed 
        back to the stack. Otherwise, the number is pushed onto the 
        stack.

        After processing all tokens, the stack will contain exactly
        one item, which is the result.

        '''

        stack = []
        operators = set('+*/-')

        for token in tokens:
            if token in operators:
                num1, num2 = stack.pop(), stack.pop()

                if token == '+': 
                    result = num2 + num1

                elif token == '*':
                    result = num2 * num1

                elif token == '/':
                    result = int(num2 / num1)

                else:
                    result = num2 - num1

                stack.append(result)

            else:
                stack.append(int(token))

        return stack[0]