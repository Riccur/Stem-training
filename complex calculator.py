#Jefferey's calculator set up. LETS GET IT!
type = input("what type of data would you want?: ")
if type=="float":
  x=float(input("assign a value for x: "))
  y =float(input("assign a value for y: "))
else:
  x=int(input("assign a value for x: "))
  y =int(input("assign a value for y: "))

operation = input('enter an operation: ')
##elif is used to combine else and if
if operation == "+":
  print(x+y)
elif operation == "_":
  print(x-y)
elif operation == "*":
  print(x*y)
elif operation == "/":
  print(x/y)
Solution = (x+y) or (x-y) or (x*y) or (x/y)