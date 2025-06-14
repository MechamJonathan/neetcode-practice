

class Stacks():
    def isValidParenthesis(self, s:str) -> bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for c in s:
            
            if c in closeToOpen:
                if len(stack) != 0 and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False
        
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack.pop()

    
        