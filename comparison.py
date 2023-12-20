def max_num(num1, num2, num3):
   if num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3
       

print(max_num(1,2,4))

# conparison operators
# == equal to
# >= greater than or equal to
# <= less than or equal to
# !=  not equal to