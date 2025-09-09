import re




class Calculator:
    """
    this is a stack based calculator
    use for parenthesis order of operation
    """
    def calculate(self, s):
        """
        takes in a string s and returns a number
        """''
        result = 0
        current = 0
        sign = 1
        stack = []   #stack - last in, last out LIFO   #queue - first in, first out FIFO
        for ss in s:
            if ss.isdigit():
                current = int(ss) + 10*current
            elif ss in ["*", "/"]:
                print("this operation is not supported.")
                break
            elif ss in ["-", '+']:
                result += sign * current
                current = 0
                if ss == "+":
                    sign = 1
                else:
                    sign = -1
            elif ss is ['(']:
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ss == [')']:
                result += current * sign
                result *= stack.pop()
                result += stack.pop
                current = 0




        return result + current * sign


print("launching the calculator....")
calc = Calculator()
user_input = ""
while user_input not in ["exit", "stop", "close", "cls", "quit"]:
    regex = re.search('[a-zA-Z]', user_input)
    if regex != None:
        print('Please write a math expression.')
    user_input = input(">")
    output = calc.calculate(user_input)
    print(output)
print('Closing the calculator...')