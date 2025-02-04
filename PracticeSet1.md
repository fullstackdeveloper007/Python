## Python Practice Set 
**Question 1**: Write a program which will find all such numbers which are divisible by 7 but are not a 
 multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a 
 comma-separated sequence on a single line.

**Solution:**
```python 
num=[]
for a in range(2000,3201):
    if a%7==0 and a%5!=0:
        num.append(a)
        
print(num)
```

**Question 2**: Write a program which can compute the factorial of a given numbers. The results should be 
printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 
Then,# the output should be: 40320

**Solution:**
```python
def factorial(n):
    num=1
    if n==0:
        return 1
    else:       
        for a in range(1,9):
            num=num*a
            
    return num
#Calling #print(factorial(8)) O/S: 40320

#Recursive :
def factorial(n):
    num=1
    if n==0:
        return 1
    else:
        num=factorial(n-1)*n
            
    return num
```
**Question3:** With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

**Solution:**
```python
def genDictionary(num):
    myDic={}
    for a in range(1,num+1):
        myDic[a]=a*a
    return myDic

print(genDictionary(8))
```

**Question4:**

