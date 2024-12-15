# String Mwethods,Slice, Join

```python
animals = "lions tigers and bears"
animals.index("bears") # os 17

animals = "lions tigers and bears"
"horses" in animals #o/s true


int("12345") + int("54321")
```
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

# for(),while() Loop

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

# As a list comprehension:
```Python
even_numbers = **[x for x in range(7) if x % 2 == 0]**
print(even_numbers) # o/s [0, 2, 4, 6]
```

# While

```Python
x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))
```

#Strip()
text.strip()



