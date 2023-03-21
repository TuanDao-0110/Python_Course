# Python Programming MOOC 2023

https://programming-23.mooc.fi/

## 1. About this course:

The course start on January 16th 2023. This is the course material page for the Introduction to Programming course (BSCS1001, 5 cr) and the Advanced Course in Programming (BSCS1002, 5 cr) from the Department of Computer Science at the University of Helsinki.

## 2. content vs learing objects:

<h1> Part 1:</h1>
<h2>1.1.Getting started</h2>

<p>You will have written and executed your first Python program</p>
<p>You will know how to use the print command</p>
<p>You will be able to use programming for arithmetic operations</p>

<h2>1.2.Information from the user</h2>

<p>You will know how to write a program which uses input from the user</p>
<p>You will know how to use variables to store input and print it out</p>
<p>You will be able to combine strings</p>

<h2>1.3.More about variables:</h2>
<p>You will be able to use variables in different contexts</p>
<p>You will know what kind of data can be stored in variables</p>
<p>You will understand the difference between strings, integers and floating point numbers</p>

<h2>1.4.Arithmetic operations</h2>
<p>You will be able to use variables in various arithmetic operations</p>
<p>You will know how to deal with numbers in user input</p>
<p>You will know how to cast values into other fundamental data types</p>

|          | arithmetics                      |           |        |
| -------- | -------------------------------- | --------- | ------ |
| Operator | Purpose                          | Example   | Result |
| +        | Addition                         | 2 + 4     | 6      |
| -        | Subtraction                      | 10 - 2.5  | 7.5    |
| \*       | Multiplication                   | -2 \* 123 | -246   |
| /        | Division (floating point result) | 9 / 2     | 4.5    |
| //       | Division (integer result)        | 9 // 2    | 4      |
| %        | Modulo                           | 9 %2      | 1      |
| \*\*     | Exponentiation                   | 2 \*\*3   | 8      |

<h2>1.5. Conditional statements</h2>

```mermaid
---
title: conditional statement
---
stateDiagram-v2
    [*] --> Conditional
    Conditional --> True : condition is true
    True --> [*] : execution continues
    Conditional --> False : condition is false
    False --> [*] : execution continues

```

<p>You will be able to use a simple conditional statement in programming</p>
<p>You will know what a Boolean value is</p>
<p>You will be able to express conditionals with comparison operators</p>

|          | Comparison operators  |         |
| -------- | --------------------- | ------- |
| Operator | Purpose               | Example |
| ==       | Equal to              | a ===b  |
| !=       | Not equal to          | a !=b   |
| >        | Greater than          | a > b   |
| >=       | Greater than          | a>=b    |
| <        | Less than             | a < b   |
| <=       | Less than or equal to | a <=b   |

<br/>
<h1> Part 2:</h1>
<h2>2.1 Programming terminology</h2>
<p> You will be familiar with some essential terminology in programming</p>
<h3> Expression example:

| Expression   |         |                       |                  |
| ------------ | ------- | --------------------- | ---------------- |
| Expression   | Value   | Type                  | Python data type |
| 2 + 4 + 3    | 9       | integer               | int              |
| "abc" + "de" | "abcde" | string                | str              |
| 11/2         | 5.5     | floating point number | float            |
| 2 \* 5 > 9   | True    | boolean value         | bool             |

<p>You will know the difference between a statement and an expression</p>
<p>You will be able to find out the data type of an evaluated expression</p>
<p>You will have learnt to use debugging methods to find mistakes in your code</p>

<h2>2.2 More conditionals</h2>

<p>You will know how to create multiple branches within conditional statements</p>
<p>You will understand the purpose of if, elif and else statements within a conditional statement</p>
<p>You will be able to use the modulo operation % in Boolean expressions</p>

```mermaid
---
title: Conditional Expression
---
stateDiagram-v2
    [*] --> Conditional_expression
    Conditional_expression --> Block_1 : true
    Block_1 --> execution_continues
    Conditional_expression --> Block_2 : false
    Block_2 --> execution_continues
    execution_continues --> [*]
```

<!-- Alternative branches using the elif statement -->

```mermaid
---
title: Alternative branches using the elif statement
---
stateDiagram-v2
    conditional_expression --> block_1 :true
    block_1 --> execution_continues

    conditional_expression --> conditional_expression_2 :false
    conditional_expression_2 --> block_2 :true
    block_2 --> execution_continues
    conditional_expression_2 --> block_3 :false
    block_3 --> execution_continues
    execution_continues --> [*]
```

<h2>2.3 Combining conditions</h2>

<p>You will know how to use the operators and, or and not in conditions</p>
<p>You will be able to write nested conditionals</p>

| Behaviour |       |         |        |
| --------- | ----- | ------- | ------ |
| a         | b     | a and b | a or b |
| False     | False | False   | False  |
| True      | False | False   | True   |
| False     | True  | False   | True   |
| True      | True  | True    | True   |

| Operator 'not' negates a condition |       |
| ---------------------------------- | ----- |
| a                                  | not a |
| True                               | False |
| False                              | True  |

<h2>2.4 Simple Loops</h2>

<p>You will know what a loop means in programming</p>
<p>You will be able to use a while True loop in your programs</p>
<p>You will know how to use the break command to break out of a loop</p>

<br/>

<h1> Part 3:</h1>
<h2> 3.1 Loops with condition </h2>
<p>You will know how to create a while loop with a condition</p>
<p>You will know what roles initialisation, formulating a condition and updating variables perform in a loop</p>
<p>You will be able to create loops with different kinds of conditions</p>

```mermaid
---
title: Loops with conditions
---
stateDiagram-v2
    [*] --> conditional_expression
    conditional_expression --> block :true
    block --> conditional_expression
    conditional_expression --> execution_continues :False
    execution_continues --> [*]
```

<h2> 3.2 Working with strings</h2>
<p>You will be able to use the operators + and * with strings</p>
<p>You will know how to find out the length of a string</p>
<p>You will know what is meant by string indexing</p>
<p>You will know how to look for substrings within a string</p>
<h3>Index string</h3>
<img src='./assets/view1.png' />

<h2> 3.3 More loops</h2>

<p>You will understand when the break command is needed to break out of loops</p>
<p>You will be able to use the continue command to move to the next iteration</p>
<p>You will understand how nested loops work</p>

```mermaid
---
title: The continue command with break
---
stateDiagram-v2
    [*] --> conditional_expression
    conditional_expression --> break :true
    conditional_expression --> execution_continues :false
    break --> execution_continues
    execution_continues --> [*]
```

```mermaid
---
title: The continue command continue
---
stateDiagram-v2
    [*] --> conditional_expression
    conditional_expression --> continue :true
    continue --> conditional_expression
    conditional_expression --> execution_continues :false
    execution_continues --> [*]
```

<h2> 3.4 Defining functions</h2>

<p>You will know how to write and call your own functions</p>
<p>You will understand what is meant by the argument and the parameter of a function</p>
<p>You will be able to define parameters in your own functions</p>
<br/>

<h1> Part 4 </h1>

<h2>The Visual Studio Code editor, Python interpreter and built-in debugging tool </h2>

<p>You will be equipped to use the Visual Studio Code editor to complete exercises on this course
<a href='https://programming-23.mooc.fi/part-4/1-vscode'>reference link</a>
</p>
<p>You will be familiar with the interactive Python interpreter, and will be able to use it to run code</p>

<h2>More functions</h2>
<p>You will know more about the arguments and parameters of functions</p>
<p>You will know how to return values from functions, and how to use the values in your code</p>
<p>You will be able to add type hints for parameters and return values</p>

<h2>Lists</h2>
<p>You will know what lists are in Python</p>
<p>You will be able access a specified item within a list</p>
<p>You will know how to add items to a list, and how to remove them</p>
<p>You will be familiar with built-in list functions and methods</p>

<h2>Definite iteration</h2>
<p>You will know the difference between definite and indefinite iteration</p>
<p>You will know how a Python for loop works</p>
<p>You will be able to use a for loop to iterate through lists and strings</p>

```mermaid
flowchart TD
    A[Start] -->  id1(are there more items in the list ?) 
    style id1 fill:red,stroke:#333,stroke-width:4px
    id1(are there more items in the list) --> |True| id2(Select the next item and store it in the variable)
    id3(Execute code block) --> id1
    id2 --> id3
    id1 -->|False| id4(Execution continues)
    id4 --> B[End]
```

<h2>Print statement formatting</h2>
<p>You will know how to use arguments to format the result of the print command</p>
<p>You will be able to use f-strings to format printouts</p>


<h2>More strings and lists</h2>

<p>You will be familiar with more methods for slicing strings and lists</p>
<p>You will understand what immutability of strings means</p>
<p>You will be able to use the methods count and replace</p>


<br/>
<h1>Part 5:</h1>
<h2>More lists</h2>
<p>You will be able to create lists with different types of items</p>
<p>You will know how to use lists to organise data</p>
<p>You will be able to store a matrix as a two-dimensional list</p>

<a href='https://pythontutor.com/visualize.html#mode=edit'>Visualize tutor link</a>


<h2>References</h2>
<p>You will know what is meant by a reference to a variable</p>
<p>You will understand that there can be multiple references to the same object</p>
<p>You will be able to use lists as parameters in functions</p>
<p>You will know what is meant by a side effect of a function</p>

<h2>Dictionary</h2>
<p>You will be familiar with the dictionary data structure</p>
<p>You will be able to use a dictionary with different types of keys and values</p>
<p>You will know how to traverse through the contents of a dictionary</p>
<p>You will be able to name some typical use cases for dictionaries</p>


<h2>Tuple</h2>
<p>You will be familiar with the tuple data type</p>
<p>You will be able to create tuples from various types of values</p>
<p>You will know the difference between a tuple and a list</p>
<p>You will be able to name some typical use cases for tuples</p>