import marimo

__generated_with = "0.18.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Brief Python Refresher
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Table of Contents
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - [ 1 - Lists](#1)
      - [ 1.1 Introduction](#1-1)
      - [ 1.2 List Comprehensions](#1-2)
    - [ 2 - Dictionaries](#2)
      - [ 2.1 Introduction](#2-1)
      - [ 2.2 The method `.items`](#2-2)
    - [ 3 - f-strings](#3)
      - [ 3.1 Introduction](#3-1)
      - [ 3.2 f-strings in Action](#3-2)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <a id='1'></a>

    ## 1 - Lists

    <a id='1-1'></a>

    ### 1.1 Introduction

    A list is a built-in data type in Python used to store collections of items. Lists are ordered, changeable, and allow duplicate values.
    """)
    return


@app.cell
def _():
    # Example of a list
    list1 = ["RAG", "is", "awesome"]
    print(f"Original list: {list1}")

    # Adding an item
    list1.append("!")
    print(f"List after adding '!': {list1}")

    # Removing an item
    list1.remove("awesome")
    print(f"List after removing 'awesome': {list1}")
    return (list1,)


@app.cell
def _(list1):
    # .remove and .append change the list and have no return
    _result = list1.append('This is a test')
    print(_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <a id='1-2'></a>

    ### 1.2 List Comprehensions

    List comprehensions provide a concise way to create lists, making your code more readable and expressive. They serve as a simpler alternative to using `for` loops. While [there is a small performance gain](https://stackoverflow.com/a/22108640) when using list comprehensions, their primary advantage lies in their readability and simplicity rather than any significant performance improvement.
    """)
    return


@app.cell
def _():
    # An example of list comprehension to create a list of squares
    squares = [_x ** 2 for _x in range(10)]
    print(f'Squares of numbers from 0 to 9: {squares} (with list comprehension)')
    squares_for_loop = []
    # The same example using for loop
    for _x in range(10):
        squares_for_loop.append(_x ** 2)
    print(f'Squares of numbers from 0 to 9: {squares_for_loop} (with for loop)')
    return


@app.cell
def _():
    # Conditional list comprehension
    even_squares = [_x ** 2 for _x in range(10) if _x % 2 == 0]
    print(f'Squares of even numbers from 0 to 9: {even_squares} (with list comprehension)')
    even_squares_for_loop = []
    # Without list comprehension
    for _x in range(10):
        if _x % 2 == 0:
            even_squares_for_loop.append(_x ** 2)
    print(f'Squares of even numbers from 0 to 9: {even_squares_for_loop} (with for loop)')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <a id='2'></a>

    ## 2 - Dictionaries

    <a id='2-1'></a>

    ### 2.1 Introduction

    Dictionaries are used to store data values in `key:value` pairs and are unordered, changeable, and do not allow duplicates.
    """)
    return


@app.cell
def _():
    # Example of a dictionary
    person = {"name": "Aimer", "age": 32, "city": "Tokyo"}

    print(f"Person dictionary: {person}")

    # Accessing a value
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age', 'N/A')}")

    # Adding a new key-value pair
    person["email"] = "aimer@contact.jp"
    print(f"Updated person dictionary: {person}")
    return (person,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <a id='2-2'></a>

    ### 2.2 The method `.items`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can also iterate over the pairs key/values in the dictionary with the method `.items`:
    """)
    return


@app.cell
def _(person):
    for key, value in person.items():
        print(f"Key: {key}\tValue: {value}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you itereate directly on the dictionary, you will be iterating over its `keys`:
    """)
    return


@app.cell
def _(person):
    for val in person:
        print(val)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <a id='3'></a>

    ## 3 - f-strings

    <a id='3-1'></a>

    ### 3.1 Introduction

    Python's f-strings (formatted string literals) provide a means to embed expressions inside string literals, using curly braces `{}`. You just need to add an "f" before the string to turn it into an f-string.
    """)
    return


@app.cell
def _():
    # Basic f-string example
    name = "Nemo"
    country = "Switzerland"
    greeting = f"Hello {name}, you are from {country}."
    print(greeting)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <a id='3-2'></a>

    ### 3.2 f-strings in Action

    A common way to generate a string from a set of data is by using the following method. Suppose you have a list of dictionaries containing people's information, and you want to create strings in the format:

    ```
    Name: Alice Johnson, Age: 28, E-mail: alice.johnson@example.com, Location: New York, NY
    Name: Michael Smith, Age: 34, E-mail: michael.smith@example.com, Location: Los Angeles, CA
    ... (continues)
    ```
    """)
    return


@app.cell
def _():
    # A list of dictionaries - this structure will come up a lot in this course!
    people = [
        {
            "name": "Alice Johnson",
            "age": 28,
            "email": "alice.johnson@example.com",
            "location": "New York, NY",
        },
        {
            "name": "Michael Smith",
            "age": 34,
            "email": "michael.smith@example.com",
            "location": "Los Angeles, CA",
        },
        {
            "name": "Emily Davis",
            "age": 22,
            "email": "emily.davis@example.com",
            "location": "Austin, TX",
        },
        {
            "name": "John Brown",
            "age": 45,
            "email": "john.brown@example.com",
            "location": "Chicago, IL",
        },
        {
            "name": "Sarah Wilson",
            "age": 31,
            "email": "sarah.wilson@example.com",
            "location": "Seattle, WA",
        },
    ]
    return (people,)


@app.cell
def _(people):
    sentences = []
    for person_1 in people:
        sentences.append(f"Name: {person_1['name']}, Age: {person_1['age']}, E-mail: {person_1['email']}, Location: {person_1['location']}")
    _result = '\n'.join(sentences)
    print(_result)
    return


@app.cell
def _(people):
    # Another way of creating strings that depend on parameters is the following
    template = 'Name: {name}, Age: {age}, E-mail: {email}, Location: {location}'
    sentences_2 = []
    for person_2 in people:
        sentences_2.append(template.format(name=person_2['name'], age=person_2['age'], email=person_2['email'], location=person_2['location']))
    formatted_result = '\n'.join(sentences_2)
    print(formatted_result)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
