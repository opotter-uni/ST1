# Tutorial 1

## Activity 1

Question 1

What does a professional programmer usually do first to gain an understanding of a problem?
Interview clients to understand pain points etc.
Question 2

How does pseudocode differ from actual code written in a programming language?
Pseudocode is a written representation of the logic behind a program without any formatting or language constraints.
Question 3

Computer programs typically perform what three steps?
Input - process - output
Question 4

What is the difference between floating-point division and integer division?
Integer division - if there is any remainder from the division, it is ignored.
Floating point division proceeds as normal
Question 5

What is a magic number? Why are magic numbers problematic?
A magic number is a unexplained number (usually a constant) within a program such as an offset or multiplier value, or a constant such as pi or the golden ratio. It is usually best practise to assign a magic number to a variable and use it instead. Otherwise, this runs the risk of hurting readability & clarity in the code, incorrectly typing the value, and having to change multiple different instances of it in the code.
Question 6

Assume a program uses the named constant PI to represent the value 3.14159. The program uses the named constant in several statements. What is the advantage of using the named constant instead of the actual value 3.14159 in each statement?
This makes writing the code more efficient to write. Additionally, different approximations may be used i.e. 3.14 or 3.14159 or 3.14159265, and if a constant is used it removes this problem.


## Activity 2

Question 1

Write Python code that prompts the user to enter his or her age and assigns the user’s input to an integer variable named age.
age = input("Enter your age: ")
Question 2

Write Python code to define a variable precise and make it refer to 1.09388641. Print the variable.
precise = 1.09388641
print(precise)
Question 3

Write Python code to define two variables, one named 'length' making it refer to 3.5 and the other named 'width' making it refer to 1.55.
length = 3.5
width = 1.55
Question 4

Given two variables 'person1Age' and 'person2Age', write a Python statement that makes the associated value of 'person1Age', 4 more than that of 'person2Age'. Print both person’s ages
person1Age = person2Age + 4

print(person1Age,person2Age)
Question 5

Given the variables 'taxablePurchases' and 'taxFreePurchases', write an expression corresponding to the total amount purchased. (total amount purchased is sum of taxable and tax free purchases).




Assign the total to 'totalPurchases' variable and print the totalPurchases variable. (Assign appropriate values to the two variables 'taxablePurchases' and 'taxFreePurchases').
taxablePurchases = 250
taxFreePurchases = 120 # Arbitrary values

totalPurchases = taxablePurchases + taxFreePurchases
print(totalPurchases)
Question 6

Given the variables 'full_admission_price' and 'discount_amount', write an expression corresponding to the price of a discount admission. (discount admission is defined as discount amount subtracted from full admission price). (Note the variables are not in camel case notation). Python programmers use PEP coding style.
discounted_price = full_admission_price - discount_amount
Question 7

Given the variable 'pricePerCase', write an expression corresponding to the price of a dozen cases, and assign it to 'price_dozen_cases'. Print the price of dozen cases.
price_dozen_cases = pricePerCase*12
print(pricePerCase,price_dozen_cases)
Question 8

Given the variables 'cost_of_bus_rental' and 'max_bus_riders', write an expression corresponding to the cost per rider (assuming the bus is full). Print the cost per rider.
cost_per_rider = cost_of_bus_rental/max_bus_riders
print(cost_per_rider)
Question 9

Write an expression that computes the remainder of the variable 'principal' when divided by the variable 'divisor'. (Assume that each is associated with an int.). Print the remainder variable.
remainder = principle % divisor
print(remainder)
Question 10

Write an expression that computes the average of the values 12 and 40, and assign it to the variable 'avg'. Print the variable 'avg'.
avg = (12+40)/2
print(avg)
Question 11

Write an expression that computes the average of the variables 'exam1' and 'exam2' and assigns it to another variable 'examAverage'. Print the exam average.
examAverage = exam1+exam2
print(examAverage)
Question 12

Given a variable 'bridge_players', write a statement that increases its value by 4, and display the variable.
bridge_players +=4
print(bridge_players)
Question 13

Given a variable 'profits', write a statement that increases its value by a factor of 10 and displays it on console.
profits *=10
print(profits)
Question 14

Write a statement that increments 'total' by the value associated with 'amount'. That is, add the value associated with 'amount' to that associated with 'total' and assign the result to 'total'. Display the total value.
total +=amount
print(total)


## Activity 3

Question 1

Write a turtle graphics statement that draws a circle with a radius of 75 pixels.
from turtle import *

circle(75)

mainloop()
Question 2

Write the turtle graphics statements to draw a square that is 100 pixels wide on each side and filled with the color blue.
from turtle import *

fillcolor('blue')
begin_fill()
for i in range(4):
forward(100)
right(90)
end_fill()

mainloop()
Question 3

Write the turtle graphics statements to draw a square that is 100 pixels wide on each side and a circle that is centered inside the square. The circle’s radius should be 80 pixels. The circle should be filled with the color red. (The square should not be filled with a color.)
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
penup()
left(90)
forward(50)
right(90)
forward(30)
setheading(0)
pendown()
fillcolor('red')
begin_fill()
circle(80)
end_fill()

mainloop()