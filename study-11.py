#Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

x = int(input("Enter a number to check if it is a prime number"))
count=0
for i in range(1, x+1):
  if not x % i :
    count += 1
if(x == 0) or (x == 1) or (count >= 3):
  print(x,"is not a prime number")
else:
  print(x, "is a prime number")
