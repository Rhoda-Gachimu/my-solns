first_num = float(input("Enter your first number:"))
operators = input("Enter an operator:")
second_num =float( input("Enter your second number:"))

if operators == "+" :
    print(first_num + second_num)

elif operators == "-":
    print(first_num-second_num)

elif operators == "*" :
    print(first_num*second_num)

elif operators == "/":
    print(first_num/second_num)
else:
    print("Operator Invalid")