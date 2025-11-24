**1. Reversing a String using Stack Code: **
def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string
**2. Balancing the brackets Code: **
def is_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    match = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0
**3. Undo Operation **
def undo_operations(stack):
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print("initial stack:", stack)
    stack.pop()  # Undo last operation (4)
    print("After undoing last operation:", stack)
