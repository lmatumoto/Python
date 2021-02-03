# -*- coding: utf-8 -*-

"""Even, Odd, Positive and Negative

Make a program that reads five integer values. Count how many  of these values are even, odd, positive and negative. 
Print these information like following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, 
indicating how many of these values ​​are even, odd, positive and negative.
"""

values = []
i = 0
while (i < 5):
    n = int(input())
    values.append(int(n))
    i += 1
    
even = 0
odd = 0
positive = 0
negative = 0
    
for k in range(5):
    if values[k] % 2 == 0:
        even += 1
    else:
        odd += 1
    if values[k] > 0:
        positive += 1
    elif values[k] < 0:
        negative += 1
        
print(even,"valor(es) par(es)")
print(odd,"valor(es) impar(es)")
print(positive,"valor(es) positivo(s)")
print(negative,"valor(es) negativo(s)")