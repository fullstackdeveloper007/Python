## Python Practice Set 
* Question: Write a program which will find all such numbers which are divisible by 7 but are not a 
 multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a 
 comma-separated sequence on a single line.

#Answer
```python 
num=[]
for a in range(2000,3201):
    if a%7==0 and a%5!=0:
        num.append(a)
        
print(num)
```
