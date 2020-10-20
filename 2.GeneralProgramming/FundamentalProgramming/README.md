# LATT-FundamentalProgramming
Learn All The Things - Fundamental Programming Concepts

A quick overview of the almost "univerisal" programming building blocks. Regardless of the language you use, you will find some version of the below

## Basics

### Variables

Either can by dynamically inferred or statically typed. 

- Static: Means you specify the variable type. (Ex: int, str, float, double, bool, etc)
- Dynamic: Means you specify a variable name, and possibly the type of variable (let, const, etc) and let the interpreter infer at runtime.

There are pros/cons to each in regards to speed of execution and testing for errors.

### Arithmetic 

Need to be able to do math. Typically supports all the basic PEMDAS operations. 

### Lists or Arrays

Most languages have some way of storing many variables in a single data structure called a list or an Array, sometimes both are available.

- Lists are going to be able to expand and shrink corresponding to the elements that are in the list at any given time.
- An Array is going to be at a set finite sizing and elements can only be removed but not added past the initial allocation

Accessing individual elements usually has a language-specific way.

A programming language usually has many methods to work with these types of data structures.

- pop: Removes either the last element or element at a specified point
- push: Puts a new element as the last element
- append: Attachs an element to end of the structure
- prepend: Attachs an element at the beginning
- find: Finds an element in the structure based on certain critifer
- filter: Returns another structure only the results that return true on the condition specified
- map: Returns another structure of the results of a executed function on each element
- zip: Combines two structures together into tuples and returns them.

Lists and Arrays are the foundation of other structures like Queues, Stacks, etc.

### Strings

Strings are usually just Arrays or Lists of single characters. 
A lot of languages allow you to interact with Strings like you do a list. 
Most languages have common ways to interact with strings like creating substrings, reversing the order, etc.
Most languages have specific ways to concatenate strings and variables together along with short-hand formatting.

### Dictionaries

Most languages have some way to define data structures that contain key/value pairs. 
These structures are much faster and more efficient to look up than lists/arrays as we can look up by hashing algorithms. 
Accessing elements is done by calling the specific key on the dictionary.

### Conditionals

Every language is going to have conditionals that result in either true or false which dictate the flow of a program.
These conditions can be branched by using if/else and can usually support complex conditional statements.

### Looping

Most languages are either going to have a For loop or a While loop or both. These are used to run a set amount of code multiple times. 
- For Loop: Usually a loop construct utilized when you have a known amount of iterations
- While Loop: A loop typically used to execute some code when it needs to run until a user specified condition or until a condition a met

### Functions

A predefined set of code specified with a specicic name that can be reran as many times in the code base. Used to organize and reuse code. Can usually accept parameters and return results. The foundation of functional programming.

### Scope

Scope is how specicic variables can be accessed by other parts of the code. 

- Local Scope: Some variables, depending on where and how they were defined, can only be accessed by code that exists where it was defined 
- Global Scope: Variables can be accessed anywhere

## Object Oriented Programming

OOP is a way for use to define structures of objects that will be reused and have common functionality through a code base. Most languages are either OOP in nature or functional in nature.

### Classes

Classes are the way to define and spec out objects which privately scoped attributes and methods.

Most classes will have a constructor which is used to intialize the object and it's attributes.

- Attributes or Properties: contain specific data about the object and try to only allow themselves to be edited in specified ways.
- Methods: Functions that the object can call.



 

