# 2. Python 

Python is **not purely compiled** and **not purely interpreted** either. It’s a mix of both. Let me clarify 👇

## 🔹 How Python Runs Your Code

1. **Source Code → Bytecode**

   * When you run a `.py` file, Python **compiles it into bytecode** (low-level instructions).
   * This bytecode is stored in `.pyc` files inside the `__pycache__` folder.

   Example:

   ```bash
   myscript.py  -->  myscript.pyc (bytecode)
   ```

2. **Bytecode → Interpreter**

   * The **Python Virtual Machine (PVM)** (part of CPython) executes the bytecode line by line.
   * This step makes Python look like an **interpreted language**.

---

## 🔹 So, Is Python Compiled or Interpreted?

* **Compiled?** ✅ Yes, to bytecode (not machine code like C/C++).
* **Interpreted?** ✅ Yes, because the PVM interprets bytecode at runtime.
* **Final Answer:** Python is a **“interpreted, bytecode-compiled language.”**

---
## 🔹 Python Memory Management

Python manages memory automatically for you — you don’t need to manually allocate or free memory (like in C).

### 1. **Memory Allocation**

* **Stack memory** → Stores local variables, function calls, control flow.
* **Heap memory** → Stores objects (lists, dicts, class instances).
* Python objects (even integers, strings) live in the **heap**.
* Python maintains an internal **memory manager** that handles:

  * **Object allocation**
  * **Deallocation (freeing unused memory)**

### 2. **Reference Counting**

* Each Python object has a **reference count**: how many variables point to it.
* When reference count goes to **zero**, the object is deleted.

📌 Example:

```python
import sys

a = [1, 2, 3]
b = a
print(sys.getrefcount(a))  # reference count for the list
```
## 🔹 Garbage Collection in Python
Reference counting works well, but there’s a problem: **circular references** (objects referring to each other).
Example of circular reference:
```python
class Node:
    def __init__(self):
        self.ref = None
a = Node()
b = Node()
a.ref = b
b.ref = a   # circular reference
```
Even if `a` and `b` go out of scope, their reference count never reaches 0 → **memory leak**.
### ✅ Solution: Garbage Collector
* Python has a **cyclic garbage collector** (module `gc`) to detect and clean up cycles.
* It periodically checks objects and frees memory of unreachable cycles.
You can control it:
```python
import gc

print(gc.isenabled())   # Check if GC is enabled
gc.collect()            # Force garbage collection
```
---

## 🔹 Key Points
* **Automatic memory management** via reference counting + garbage collector.
* **Small objects** (like integers, strings) may be cached in memory for performance (e.g., integers from -5 to 256).
* The **`gc` module** allows tuning garbage collection.
* Developers usually don’t need to manage memory directly, but being aware helps optimize performance.
---

👉 In interviews, you can summarize:

> *“Python uses automatic memory management based on reference counting. When objects are no longer referenced, they are destroyed. For cyclic references, Python has a garbage collector that periodically frees memory by detecting unreachable objects.”*
---



# Topic Python Virtual Environment and pip

* pip acronym of preferred installer programe
* pip install requests(requests pkg) -- This install the pkg globally 
* pip list -- List all the packages installed globally
* pip uninstall requests
* pip install  -U requests (Update the pkg)
* pip show requests (it will show all the details of pkg and its dependent pkges
* `pip freeze` - This will list all the python pkgs in the current env, along with the versions
* `pip freeze > requirements.txt` - This will create a file called requirment.txt and mention all the project dependencies


## Virtial Environmenment (venv)
How to create a Virtial Env?
* `py -m venv .venv` (This will create a folder inside a solution folder namely `.venv`. `.venv`is the name of virtual environment. 
* `.venv\Scripts\activate.bat` (from command prompt, from python prompt getting error Activate.ps1 is not digitally signed)
* source .venv/Scripts/activate (Bash cmd on windows)
* `deactivate` This will deactivate the virtual environment
*  pip


## `.env` Environment Variable File: This file can be used for keeping environment variable, like API keys
* `from dotenv import load_dotenv` This is the command for loading the env variable and `load_dotenv()` is also required after import code

* 
