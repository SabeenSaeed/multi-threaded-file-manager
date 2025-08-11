**Flashcard 1**
Q: What are Python modules and how are they imported?
A: Modules encapsulate reusable code. Use import or from ... import ... to access functionality.

from pathlib import Path
from datetime import datetime

**Flashcard 2**
Q: What is a class in Python?
A: A class bundles data and methods into objects for modular and reusable code.
class FileScanner:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)


**Flashcard 3**
Q: What does the __init__ method do?
A: It initializes an object’s attributes during creation.
def __init__(self, root_dir):
    self.root_dir = Path(root_dir)

**Flashcard 4**
Q: How do instance methods and self work?
A: Instance methods operate on object data accessed via self.
def scan(self):
    for file_path in self.root_dir.rglob('*'):
        if file_path.is_file():
            yield self.get_metadata(file_path)

**Flashcard 5**
Q: What advantages does pathlib.Path provide?
A: Object-oriented, cross-platform file system manipulation with intuitive methods like .rglob() and .is_file().
for file_path in self.root_dir.rglob('*'):
    if file_path.is_file():
        ...

**Flashcard 6**
Q: Explain Python generators and yield.
A: Generators produce one item at a time with yield, improving memory efficiency for large datasets.
def scan(self):
    yield self.get_metadata(file_path)

**Flashcard 7**
Q: How are dictionaries used for structured data?
A: They store metadata in key-value pairs for easy access.
def get_metadata(self, file_path):
    return {
        'name': file_path.name,
        'size_kb': round(file_path.stat().st_size / 1024, 2),
        ...
    }

**Flashcard 8**
Q: Why use try-except blocks?
A: To catch and handle exceptions gracefully, preventing crashes.
try:
    # risky file read operations
except Exception as e:
    return f"[Error reading file: {e}]"

**Flashcard 9**
Q: How do you safely read part of a text file?
A: Use a context manager (with open) with encoding and limit read size.
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    return f.read(max_chars).strip()

**Flashcard 10**
Q: How do Python f-strings enhance readability?
A: Embed variables directly in strings cleanly and efficiently.
return f"[Image: {img.format}, {img.size[0]}x{img.size[1]} px, Mode: {img.mode}]"

**import re**
The re module is much more powerful than just checking "confidential" in file names — it’s Python’s built-in regular expression engine, meaning it can search, match, split, and replace text based on patterns.

import re
text = "My phone number is 0300-1234567"
match = re.search(r"\d{4}-\d{7}", text)  # pattern: 4 digits, dash, 7 digits
if match:
    print(match.group())  # 0300-1234567

**Lambda functions**

lambda f: f['extension'] in ['.txt', '.pdf', '.docx']
Lambda: An anonymous function — a one-line, throwaway function without def.

Here:

f is the argument (each file dictionary).

f['extension'] → looks at the file’s extension.

in [...] → checks if that extension is in the allowed list.

Returns True or False.

Advantage: We can store these tiny functions directly in dictionaries for quick mapping.

**Regular expressions**

re.search(r'(secret|confidential)', f['name'], re.IGNORECASE)
re.search(pattern, string, flags): Looks for the first match of a regex pattern in a string.

Pattern: (secret|confidential) → matches "secret" OR "confidential".

re.IGNORECASE → makes it case-insensitive (Secret.txt will match too).

Returns a match object if found, otherwise None.

This is how we detect special names like "confidential_notes.txt".



**Higher-order programming**
"Functions are treated like normal things (data) — you can store them, pass them around, and call them later."

**Step 1 — A normal function**


def say_hello(name):
    return f"Hello {name}"
If you call say_hello("Sabeen") → it runs immediately and gives back "Hello Sabeen".

**Step 2 — Store the function in a variable**


greet = say_hello
print(greet("Sabeen"))  # Hello Sabeen
Here, greet now holds the function itself, not the result.
We can call it just like the original.

**Step 3 — Store functions in a dictionary**


actions = {
    "morning": say_hello,
    "evening": lambda name: f"Good evening {name}"
}

print(actions["morning"]("Ali"))   # Hello Ali
print(actions["evening"]("Sara"))  # Good evening Sara
We are storing functions as values in a dictionary.
This is higher-order programming — treating functions like normal data.

**Step 4 — Your project example**
In your EXTENSION_TAGS:


EXTENSION_TAGS = {
    'document': lambda f: f['extension'] in ['.txt', '.pdf', '.docx'],
    'image': lambda f: f['extension'] in ['.jpg', '.png']
}
Here:

Key = "document", "image"

Value = function (lambda) that checks the file.

You loop over them and call the stored function later:


for tag, rule in EXTENSION_TAGS.items():
    if rule(file):  # calling the stored function
        tags.append(tag)

**In-place mutation**
"You change the actual object, not make a copy."

**Step 1 — Without mutation**
data = {"name": "Ali"}
new_data = data.copy()
new_data["age"] = 25

print(data)     # {'name': 'Ali'}
print(new_data) # {'name': 'Ali', 'age': 25}

**Step 2 — With in-place mutation**
data = {"name": "Ali"}
data["age"] = 25  # directly add to original

print(data)  # {'name': 'Ali', 'age': 25}

