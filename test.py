def isValid(s):
    arr1 = []
    if len(s) == 0:
        return True
    for i in s:
        if i == "(" or i == "[" or i == "{":
            arr1.append(i)
        elif i == ")" and len(arr1) and arr1[-1] == "(":
            arr1.pop()
        elif i == "]" and len(arr1) and arr1[-1] == "[":
            arr1.pop()
        elif i == "}" and len(arr1) and arr1[-1] == "{":
            arr1.pop()
        else: return False
            
    return True if len(arr1) == 0 else False


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("("))
print(isValid(")"))
