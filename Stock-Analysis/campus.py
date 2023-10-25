'''
a = int(input("enter the number u want"))
result = 0
fact =1 


for i in range(1,a+1):
    fact = fact*i 
    result = result +i/fact

print(result)

a = int(input("enter the number u want"))
for i in range (1,a+1):
    for j in range (1,i+1):
        print(j ,end= " ")
    for k in range (i-1,0,-1):
        print(k,end= " ")
    print()

import random
jpot =  random.randint(1,100)

guess = int(input("guess the number"))
counter = 1

while guess!= jpot:

    if guess >jpot:
        print("guess lower")
    else:
        print("guess higher")

    guess = int(input("guess the number"))
    counter+=1

else:
    print("coreect guess")

sal =int(input("enter ur sal"))
ctc = 18

if sal<500000:
  print("no deduction because its belowlvl sal")
elif sal> 500000 and  sal < 1000000:
  a= sal*0.28
  print(a)
  print("in hand sal will be ",sal-a)
 

elif sal > 1000000 and sal <2000000:
  sal-ctc/0.20
  #print(sal)
else:

  sal-ctc*0.30
  #print(sal)


r= int(input("enter the num"))

for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end = " ")
    print()

Exercise 12: Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34
a = 0
b  =1  

for i in range(1,11):
    print(a)

    c = a+b
    a =b
    b =c


#Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
a = int(input("enter the number"))
sum=0
i=1

while i < a+1:
    if i % 5==0:
        i+=1
        continue
    sum =sum+i

    if sum > 300:
        sum = sum-i
        break
    i = i+1
print(sum)

#Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

sum = 0 
count = 0

while True:
    num = int(input("enter number "))
    if num ==0:
        break
    sum = sum+num
    count = count+1 

print('sum',sum)
print('count',count)

'''
#Problem 9: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

l = []
for i in range (2000,3200):
    if i%7==0 and i*5!=0:
        l.append(str(i))
print(",".join(l))
       
