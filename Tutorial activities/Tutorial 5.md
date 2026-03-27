# Tutorial 5

## Activity 1

Question 1

How do functions help facilitate teamwork?
Functions facilitate teamwork by dividing large sections of code into small individual blocks, and allowing that same block of code to be executed multiple times as needed
Question 2

Name and describe the two parts of a function definition.
Header & body - the header statement defines the function name and parameters while the body is the actual code the function will run
Question 3

When a function is executing, what happens when the end of the function block is reached?
The interpreter will return to where the function was called.
Question 4

What is a local variable? What statements are able to access a local variable?
A local variable is a variable only defined within the function it was declared in and is undefined if accessed elsewhere.
Question 5

What scope do local variables have?
The variable's scope ends when the function it was declared in ends
Question 6

Why do global variables make a program difficult to debug?
If the same global variable is used in multiple places for example i in for loops, the variable may remain defined and interfere with the expected behaviour of the program.
Question 7

Suppose you want to select a random number from the following sequence: 0, 5, 10, 15, 20, 25, 30, what function will you use?
import random
list = [0, 5, 10, 15, 20, 25, 30]
result = random.choice(list)
print(result)
Question 8

What statement do you have to have in a value-returning function?
return value
Question 9

What is a Boolean function?
A function that returns as either true or false
Question 10

What are the advantages of breaking a large program into modules?
Modularising a program reduces clutter, instead of having a sequence of functions at the start of a program it can be reduced to a single import statement. Additionally, this allows functions to be used in multiple different programs.



## Activity 2
Question 1

Examine the following function header, then write a statement that calls the function, passing 12 as an argument.



def show_value(quantity):
show_value(12)
Question 2

Look at the following function header:



def my_function(a, b, c):


Now look at the following call to my_function: 



my_function(3, 2, 1)


When this call executes, what value will be assigned to a? What value will be assigned to b? What value will be assigned to c?
Value a will be assigned 3
Value b will be assigned 2
Value c will be assigned 1
Question 3

What will the following program display? 



def main():
x = 1
y = 3.4
print(x, y)
change_us(x,y)
print(x,y)


def change_us(a, b):
a = 0
b = 0
print(a, b)

main()
1 3.4
0 0
1 3.4
Question 4

Write a statement that generates a random number in the range of 1 through 100 and assigns it to a variable named rand.
import random
rand = random.randrange(1,100)
Question 5

The following statement calls a function named half, which returns a value that is half that of the argument. (Assume the number variable references a float value.).



result = half(number)

Write code for the function.
def half(num):
return num/2
Question 6

A program contains the following function definition:



def cube(num):
return num * num * num

Write a statement that passes the value 4 to this function and assigns its return value to the variable result.
result = cube(4)
Question 7

Write a function named times_ten that accepts a number as an argument. When the function is called, it should return the value of its argument multiplied times.
def times_ten(num):
return 10*num