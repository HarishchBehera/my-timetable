def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print(f'Factorial of {x} = {fact}')
    
def mul(x,y):
    re=x*y
    print(f'Multiply of {x} & {y} ={re}')
    
def div(x,y):
    re=x/y
    print(f'Division of {x} & {y} ={re}')
    
n=int(input())
m=int(input())
factorial(n)
mul(n,m)
div(n,m)