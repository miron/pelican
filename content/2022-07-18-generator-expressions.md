Title: Generator Expressions and List Comprehensions  
Date: 2022-07-18  
Category: Python  
Tags: python, comprehensions, expressions  
Slug: generator-expressions  
Author: streetyogi  
Summary: Explicit is better than implicit, I know, but where is the fun in that :)   

I can't help myself, but I feel pretty comfortable with generator expressions and comprehensions, so much that I always prefer them over for loops.

Take this examples:

Calculate the future value of your savings account:  
Today 100$  
Year after 10$  
Year after 20$  
Year after 50$    
Year after 30$  
Year after 25$  

Whats the value after 5 years with an interest rate of 3% p.a.?  

    :::python
    cf = [100, 10, 20, 50, 30, 25]
    n = range(6)[::-1]
    f = 1.03
    sum(cf[i] * f**n[i] for i in n)
    
    # Or without n
    sum(cf[-i-1] * f**i for i in range(6))
  
Another example:  
Payout plan:  
50$ Year one  
60$ Year two  
70$ Year three  
80$ Year four  
100$ Year five  

Calculate and print funding amount to pay with an interest rate of 4%

    :::python
    cf = [50, 60, 70, 80, 100]  
    f = 1.04  
    PV = [print(cf[i]/ f**(i+1)) for i in range(5)]  
  
