class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []


        def safe_convert(s):

            try:
                int(s)
                return True

            except ValueError:
                return False

        for i in tokens:
            if safe_convert(i):
                stack.append(int(i))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                if i == "+":
                    stack.append(first_operand + second_operand)
                elif i == "-":
                    stack.append(first_operand - second_operand)
                elif i == "*":
                    stack.append(first_operand * second_operand)
                elif i == "/":
                    stack.append(int(first_operand / second_operand))
        
        return stack[0]
                
