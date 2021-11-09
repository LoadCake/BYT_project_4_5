class Multiplication:
    def handle(self, equation):
        if equation.find('*') != -1:
            return int(equation[:equation.find('*')]) * int(equation[equation.find('*')+1:])
        return "bad"

class Division:
    def handle(self, equation):
        if equation.find('/') != -1:
            return int(equation[:equation.find('/')]) / int(equation[equation.find('/')+1:])
        return Multiplication().handle(equation)

class Subtraction:
    def handle(self, equation):
        if equation.find('-') != -1:
            return int(equation[:equation.find('-')]) - int(equation[equation.find('-')+1:])
        return Division().handle(equation)

class Addition:
    def handle(self, equation):
        if equation.find('+') != -1:
            return int(equation[:equation.find('+')]) + int(equation[equation.find('+')+1:])
        return Subtraction().handle(equation)


rownanko = "32/4"
print(Addition().handle(rownanko))