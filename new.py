num1 = int(input("Enter your first number: "))
operator = (input("Enter your operator: "))
num2 = int(input("Enter your second number: "))
# num1 = int(num1)
# num2 = int(num2)


if operator == "+": # Here will perform task with two operands with one operator.
    print(num1 + num2)
    
elif operator == "-":# Here will perform task with two operands with one operator.
    print(num1 - num2)
   
elif operator == "/":# Here will perform task with two operands with one operator.
    print(num1 / num2)
    

elif operator == "*":# Here will perform task with two operands with one operator.
    print(num1 * num2)
    
elif operator == "%":# Here will perform task with two operands with one operator.
    print(num1 % num2)

elif operator == "^":# Here will perform task with two operands with one operator.
    print(num1 ** num2)

else:
    print("Invalid number!")
    
print("MADE BY AKASH GUPTA")
