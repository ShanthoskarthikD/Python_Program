class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            rValueError("Invalid number of arguments")
calc = Calculator()
print("Add(5, 10):", calc.add(5, 10))         
print("Add(5, 10, 15):", calc.add(5, 10, 15)) 
