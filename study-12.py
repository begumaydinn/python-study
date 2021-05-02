#Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

i=0
fibo=[0,1]
while max(fibo)<55:
  x = fibo[i] + fibo[i+1]
  i += 1
  fibo.append(x)
print(fibo)
