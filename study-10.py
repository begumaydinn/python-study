#Task:

#Find out if a given number is an "Armstrong Number".

#An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
#371 = 33 + 73 + 13;
#9474 = 94 + 44 + 74 + 44;
#93084 = 95 + 35 + 05 + 85 + 45.

#Write a Python program that;
#takes a positive integer number from the user,
#checks the entered number if it is Armstrong,
#consider the negative, float and any entries other than numeric values then display a warning message to the user.


num=int(input("Enter positive number :"))
sayı=str(num)
üst=len(sayı)
toplam=0
for i in sayı:
  rakam = int(i)**len(sayı)  
  toplam += rakam
  
if toplam==num:
    print("This is an armstrong number :", num)
else:
    print("This is not an armstrong number :", num)
  
