# Introduction to Python

### Variables Annotated by Type
Type annotations are optional in Python. They can be very helpful, though, because they make code easier to read. Annotations make the variable types clear to those reading the code.
They can also help you catch errors during compilation. In the example below, we are using the typing module to annotate the different types of variables.

```python
import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}
```

## Use variable without declaring them and explicit conversion

```python
# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests


# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type
```

### Resolve TypeError caused by a data type mismatch issue
The following code causes a type error between a string and an integer:

```python
print("5 * 3 = " + (5*3)) **eroor because we are combining int and string**

Resolution: 
* print("5 * 3 = " + str(5*3))
```
