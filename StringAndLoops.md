# String Methods,Slice, Join

### String commonly used function
```python
animals = "lions tigers and bears"
animals.index("bears") # os 17

animals = "lions tigers and bears"
"horses" in animals #o/s true


int("12345") + int("54321")

print("AaBbCcDdEe".lower())
print("AaBbCcDdEe".upper())
print("   Hello   ".lstrip())  # prints "Hello   "
print("   Hello   ".rstrip())           # prints "   Hello"
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))               # prints 2
print("12345".isnumeric())              # prints True
print("-123.45".isnumeric())            # prints False
print("xyzzy".isalpha())                # prints True
print(test.split())    # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
print(test.replace("wood", "plastic"))  # prints "How much plastic would a plasticchuck chuck"```
print("-".join(test.split()))           # prints "How-much-wood-would-a-woodchuck-chuck"
### Extracting Subsets of Strings

* **Slice**: Extract a subset of the original string.

```python
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints "G"
print(string1[4:8]) # Prints "ting"
print(string1[11:]) # Prints "Earthlings"
print(string1[:5])  # Prints "Greet"
```

* **Example:**
  * `string1[:-10]`: Returns the first part of the string (everything except the last 10 characters).
  * `string1[-10:]`: Returns the last part of the string (only the last 10 characters).

```python
string1 = "Hello, this is a sample string!"
print(string1[:-10])  # Output: "Hello, this is a sample "
print(string1[-10:])  # Output: "e string!"
```

### Stride (`::`) Argument

* **Double Colon `::`**: Allows you to define the step size when slicing.
  * `print(string1[0::2])`
    * `0::` Start at the 0th index (beginning of the string).
    * `::2` Use a step of 2 (skip every other character).
  * `print(string1[::-1])`
    * `::` Consider the entire string.
    * `::-1` Step of `-1` reverses the string (read characters from end to beginning).

```python
string1 = "Greetings, Earthlings!"
print(string1[0::2])  # Output: "Getns atlns"
print(string1[::-1])  # Output: "!sgnilhtraE ,sgniteerG"  # Reverses the string completely.
```

### join()

```python
print("Hello" + " " + "world") #Prints “Hello world”
greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"
You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
```

### for(),while() Loop

* range(stop) # range(3) 0,1,2
* range(start, stop) # range(2, 6)    2,3,4,5
* range(start, stop, step) #The third item in the range() function parameters is the incremental step value

```Python
for x in range(7):    
        print(x) #o/s 0 1 2 3 4 5 6
for number in range(2,8):
    print(number**2) # The loop should print 4, 9, 16, 25, 36, 49
for x in range(7):
    if x % 2 == 0:
        print(x) # The loop should print 0, 2, 4, 6
for n in range(1, 8, 6):  
     print(n) 0/s 1 7
for n in range(4, 15+1, 2):
         print(n) 4 6 8 10 12 14
```

### As a list comprehension:
```Python
even_numbers = **[x for x in range(7) if x % 2 == 0]**
print(even_numbers) # o/s [0, 2, 4, 6]
```

### While

```Python
x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))
```

### Strip()
text.strip() - lstrip(),rstrip() remove white space 
text.strip('-')

### join()
* "...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
* O/s- This...is...a...phrase...joined...by...triple...dots

### Split()- 
* It splits the string into list of string. by default it splits by white space however split char can be provided
* "This is another example".split() O/s- ['This', 'is', 'another', 'example']

### int()

### count()
* "This is a string.count("i") O/s 3- count of char occurence

### endswith()
"Forest".endswith("rest") O/s- True

### isnumeric()
* "Forest".isnumeric() O/s - False
* "12345".isnumeric() O/s - False

### int()
* int("2222")

### format() or f"{}"
```Python
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

name = "John"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
```

###  {:>3} 

Format the value to be at least 3 characters wide.
Right-align the value within that width.

```Python
for x in range(0, 101, 10):
    print("{:>3} F".format(x))
  0 F
 10 F
 20 F
 30 F
 40 F
 50 F
 60 F
 70 F
 80 F
 90 F
100 F
```


