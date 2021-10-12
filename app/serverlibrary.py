

def mergesort(array, byfunc=None):
    if len(array) > 1 and byfunc != None:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergesort(left, byfunc)
        mergesort(right, byfunc)
        leftindex = 0
        rightindex = 0
        arrayindex = 0
        while leftindex < len(left) and rightindex < len(right):
            if byfunc(left[leftindex]) < byfunc(right[rightindex]):
                array[arrayindex] = left[leftindex]
                leftindex += 1
            else:
                array[arrayindex] = right[rightindex]
                rightindex += 1
            arrayindex += 1
            
        while leftindex < len(left):
            array[arrayindex] = left[leftindex]
            leftindex += 1
            arrayindex += 1
        
        while rightindex < len(right):
            array[arrayindex] = right[rightindex]
            rightindex += 1
            arrayindex += 1

    elif len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergesort(left)
        mergesort(right)
        leftindex = 0
        rightindex = 0
        arrayindex = 0
        while leftindex < len(left) and rightindex < len(right):
            if left[leftindex] < right[rightindex]:
                array[arrayindex] = left[leftindex]
                leftindex += 1
            else:
                array[arrayindex] = right[rightindex]
                rightindex += 1
            arrayindex += 1
            
        while leftindex < len(left):
            array[arrayindex] = left[leftindex]
            leftindex += 1
            arrayindex += 1
        
        while rightindex < len(right):
            array[arrayindex] = right[rightindex]
            rightindex += 1
            arrayindex += 1
            
                
            
        
        pass

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        pass

    def pop(self):
        if len(self.__items) >= 1:
            x = self.__items[len(self.__items)-1]
            self.__items.pop(len(self.__items)-1)
            return x
        else:
            return None
        pass

    def peek(self):
        if len(self.__items) >= 1:
            return self.__items[len(self.__items)-1]
        else:
            return None
        pass

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self._expression = string
        pass
      
    @property
    def expression(self):
        return self._expression
        pass
      
    @expression.setter
    def expression(self, new_expr):
        valid = True
        for i in range(len(new_expr)):
            if new_expr[i] not in '0123456789+-*/() ':
                valid = False
        if valid == True:
            self._expression = new_expr
        else:
            self._expression = ""
        pass
    
    def insert_space(self):
        unspaced = list(self._expression)
        for char in range(len(unspaced)):
            if unspaced[char] in "+-*/()":
                unspaced[char] = " " + unspaced[char] + " "
        return "".join(unspaced)
        pass
    
    def process_operator(self, operand_stack, operator_stack):
        if operator_stack.peek() in "+-*/":
            operate = operator_stack.pop()
            second = operand_stack.pop()
            first = operand_stack.pop()
            if operate == "+":
                operand_stack.push(first+second)
            elif operate == "-":
                operand_stack.push(first-second)
            elif operate == "/":
                operand_stack.push(first//second)
            elif operate == "*":
                operand_stack.push(first*second)
        pass

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        for i in range(len(tokens)):
            print(tokens[i])
            if tokens[i].isdigit() == True:
                operand_stack.push(int(tokens[i]))
            elif tokens[i] in "+-":
                while operator_stack.peek() != None and operator_stack.peek() not in "()":
                    EvaluateExpression.process_operator(self, operand_stack, operator_stack)
                operator_stack.push(tokens[i])
            elif tokens[i] in "*/":
                while operator_stack.peek() != None and operator_stack.peek() in "*/":
                    EvaluateExpression.process_operator(self, operand_stack, operator_stack)
                operator_stack.push(tokens[i])
            elif tokens[i] == "(":
                operator_stack.push(tokens[i])
            elif tokens[i] == ")":
                while operator_stack.peek() != None and operator_stack.peek() not in "(":
                    EvaluateExpression.process_operator(self, operand_stack, operator_stack)
                operator_stack.pop()
                
        while operator_stack.peek() != None:
            EvaluateExpression.process_operator(self, operand_stack, operator_stack)
            
        return(str(operand_stack.peek()))



        pass
    



def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





