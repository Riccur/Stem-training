# If statements
X = 0
if X >=1:
  print("hey im still here")
  X-=1
  print(x)
print("done")

#else statements

x = 4
if x == 10: 
  print(x)
else:
  print('get lost')

#Elif to create grading system

grade = int(input("write students grades: "))
if grade >=80 and grade <=100:
  print("students got an A")
elif grade >=70 and grade <80 :
  print("student got a B")
elif grade >60 and grade <70:
  print("student got a c")