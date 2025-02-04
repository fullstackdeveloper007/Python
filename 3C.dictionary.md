
## Dictionary 
Defining a dictionary

```python
empty_dict = {}
#Using the dict() Constructor:
my_dict = dict(name='Alice', age=25, city='New York')
or
employee ={"name":"Zak","age":25}
```


* Sample programe  
```

for value in file_counts.values():
  print(value)

file_counts.keys()

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
#Calling
count_letters("aaaaa")
```

# Operations
- **Get the number of items in a dictionary:**
  ```python
  len(dictionary)
  ```

- **Get the number of items in a dictionary:**
  ```python
  my_dict.pop('city')  # Removes 'city' key
  ```

- **Iterate over each key in a dictionary:**
  ```python
  for key in dictionary:
      print(key)
  ```

- **Iterate over each key-value pair in a dictionary:**
  ```python
  for key, value in dictionary.items():
      print(f"{key}: {value}")
  ```

- **Iterate Over Values:**
  ```python
  for value in my_dict.values():
    print(value)
  ```

- **Check whether a key is in a dictionary:**
  ```python
  if key in dictionary:
      print("Key found!")
  ```

- **Access a value using the associated key from a dictionary:**
  ```python
  value = dictionary[key]
  ```

- **Set a value associated with a key:**
  ```python
  dictionary[key] = value
  ```

- **Remove a value using the associated key from a dictionary:**
  ```python
  del dictionary[key]
  ```

## Methods

- **Get a value for a key with a default if the key doesn't exist:**
  ```python
  value = dictionary.get(key, default)
  ```

- **Get all keys in a dictionary:**
  ```python
  keys = dictionary.keys()
  ```

- **Get all values in a dictionary:**
  ```python
  values = dictionary.values()
  ```

- **Append a new value to an existing list for a key:**
  ```python
  dictionary[key].append(value)
  ```

- **Update a dictionary with another dictionary:**
  ```python
  dictionary.update(other_dictionary)
  ```

- **Clear all items from a dictionary:**
  ```python
  dictionary.clear()
  ```

- **Make a copy of a dictionary:**
  ```python
  new_dict = dictionary.copy()
  ```
  * Example 
  ```
  def email_list(domains: dict) -> list:
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(f"{user}@{domain}")
    return emails

```
