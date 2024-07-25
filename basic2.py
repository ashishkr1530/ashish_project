#factorial
def factorial(n):
    
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n - 1))
         
num=5
print("factorial is:",num,"ka" ,factorial(num))


#simple interest
def simple_interest(p,r,t):
    print("the principle is:",p)
    print("the rate is:",r)
    print("the time is:",t)
    si=p*r*t/100
    print("simple interest is:",si)
simple_interest(8,6,8)

#maximum number
def max_num(a,b):
    if a>b:
        return a
    else:
        return b
a=1
b=2
print(max_num(a,b))

#find area of circle
def findArea(r):
    pi=3.14
    return pi*(r*r)
ass=findArea(5)
print(ass)

#to check prime number
num=11
if num>1:
    for i in range(2,int(num/2)+1):
        if(num%i)==0:
            print("it not prime number", num)
            break
    else:
        print("number is prime",num)
else:
    print("number is not prime", num)

#fibonacci programm with nth
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:               #N IS LESS THAN ZERO
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
 
print(fibonacci(10))  #0,1,1,2,3,5,8,13,21,34

# Python program to print ASCII Value of Character
c='g'
# print the ASCII value of assigned character in c  #using ord dunction
print("The ASCII value of '" + c + "' is", ord(c))

#break and continue with digit
count=0
for i in range(0,10):
    if i==5:
        break               #using break
    print(i)
        

count=0
for i in range(0,10):
    if i==5:
        continue            #using continue
    print(i)

#Return the sum of square of first n natural numbers
def square_sum(n):
    sm=0
    for i in range (1,n+1):
        sm=sm+(i*i)
    return sm
n=4        
print(square_sum(n))

#second method of sum of square
def square_sum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

n=4
print(square_sum(n))

#prime from 1 to 100
def prime_num(n):
    if (n==0 or n==1):
        return False
    for i in range(2,(n//2)+1):
        if (n%i==0):
            return False
    return True
n=100
for i in range(1,n+1):
  if(prime_num(i)):
    print(i,end=" ")

#print even print
count=0                                         #normal for loop
for num in range(1,100):
     if(num%2== 0):
         print(num)

#print odd number 
count=0                                         #normal for loop
for num in range(1,100):
     if(num%2!= 0):
         print(num)

#even print 
def even_num(num):               #using function
    for i in range(1,100):
        if(num%2== 0):
            return True
    return False
num=100
for i in range(1,num+1):
    if (even_num(i)):
        print(i)

#odd print
def odd_num(num):               #using function
    for i in range(1,100):
        if(num%2!= 0):
            return True
    return False
num=100
for i in range(1,num+1):
    if (odd_num(i)):
        print(i)

def is_palindrome(s):
    return s==s[::-1]

s="malayalam"
print(is_palindrome(s))
      

def is_palindrome(s):
    return s==s[::-1]

s="malayalam"
print(is_palindrome(s))
if s :
    print("yes")
else :
    print("no")


#Using and condition to get 7 divisible and 5 multiple in range
count=0
for i in range (2000,3000):
    if ((i%7==0) and (i%5==0)):
        count+=1
        print (i)
print(count)