# Задание 3

def bracket_balance(s):
    stack = []
    opening_brackets = {'{', '[', '('}
    closing_brackets = {'}': '{', ']': '[', ')': '('}
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False
    
    return not stack

# Тесты
print(bracket_balance("{[()]}"))  # True
print(bracket_balance("{[()}"))   # False
print(bracket_balance("}"))       # False
print(bracket_balance("[]{"))     # False
print(bracket_balance(")("))      # False
