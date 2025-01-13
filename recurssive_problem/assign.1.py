#how to approach recurssive problem
# question no.1-->Write a recursive function  to print N natural numbers.
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
#printN(20)
def Reverse_number(n):
    if n>0:
        print(n,end=' ')
        Reverse_number(n-1)
#Reverse_number(20)
def odd_number(n):
    if n>0:
        odd_number(n-1)
        print(2*n-1,end=" ")
#odd_number(20)
def even_number(n):
    if n>0:
        even_number(n-1)
        print(2*n,end=" ")
#even_number(10) 
def sumNumber(n):#
    if n>0:
        return n+sumNumber(n-1)
    else:
        return 0
#print(sumNumber(10))
def oddnumber(n):
    if n>0:
        return (2*n-1)+ oddnumber(n-1)
    else:
        return 0
print(oddnumber(20))
def sum_evennumber(n):
    if n>0:
        return (2*n)+sum_evennumber(n-1)
    else:
        return 0
print(sum_evennumber(20))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
def square_sum(n):
    if n>0:
        return (n*n)+square_sum(n-1)
    else:
        return 0  
print(square_sum(10))

