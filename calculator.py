class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        #original code is 
        #return b-a
        return a - b

    def multiply(self, a, b):
        result = 0
        #chage from range(b+1) to range(b)
        if b >= 0:
            for i in range(b):
                result = self.add(result, a)
        else:
            newB = self.subtract(0,b)
            for i in range(newB):
                result = self.subtract(result, a)

        return result

    def divide(self, a, b):
        result = 0
        aLessThanZeroFlag = 0
        bLessThanZeroFlag = 0
        if b == 0:
            return ZeroDivisionError
        if a < 0:
            aLessThanZeroFlag = 1
            a = 0-a
        if b < 0:
            bLessThanZeroFlag = 1
            b = 0-b
        while a >= b:
            a = self.subtract(a, b)
            if aLessThanZeroFlag == bLessThanZeroFlag:
                result += 1
            else:
                result -= 1
        return result
    
    def modulo(self, a, b):
        # while a >= b:
        #     a = a-b
        c = self.divide(a,b)
        if c == ZeroDivisionError:
            return c
        d = self.subtract(a,self.multiply(c,b))
        if c < 0:
            d = d+b
        return d

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))