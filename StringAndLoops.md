# Slice and Join

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


