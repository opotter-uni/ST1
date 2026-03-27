# Tutorial 4

## Activity 1

Question 1

What is a condition-controlled loop?
A loop that will run if a given condition is true and break if the condition is false
Question 2

What is a count-controlled loop?
A count controlled loop iterates a specific amount of times.
Question 3

What is an infinite loop? Write the code for an infinite loop.
An infinite loop is a loop that repeats forever until broken.

while True:
pass

Usually the loop will be broken at some point.

while True:
(some code)
if break_condition == True:
break
Question 4

How are an accumulator variable and a loop used to calculate a running total?
An accumulator variable is defined before a loop. As the loop is running, the variable is increased
Question 5

Why must the value chosen for use as a sentinel be carefully selected?
Sentinel value - value indicating that a break is required.
A sentinel value must be unique so it does not pass as a regular value.
For an example of a list of non-negative integers, I use either -1 or an empty non-integer value such as "", None, or [] as an indication to break the loop.
Question 6

What does the phrase “garbage in, garbage out” in the context of loop statements mean?
This saying refers to a process recieving poor data results in poor output. This is usually caused by unsanitised data.
Question 7

Give a general description of the input validation process.
An input validation process aka data sanitisation involves cleaning data to avoid a process erroring due to inconsistent data e.g. unexpected varying datatypes, missing values, extra spaces, or typos. When a user enters data, if the data is bad, indicate that and have the user reenter values.



## Activity 2

Question 1

Write a while loop that lets the user enter a number. The number should be multiplied by 10, and the result assigned to a variable named product and displayed on console. The loop should iterate as long as product is less than 100.
value = input("Enter a number: ")
while value <100:
value *=10
print(value)
Question 2

Write a while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If so, the loop should repeat, otherwise it should terminate.
while True:
num1 = input("Number 1: ")
num2 = input("Number 2: ")
print(int(num1)+int(num2))
if input("Repeat? y/n") != "y":
break
Question 3

Write code that prompts the user to enter a number in the range of 1 through 100 and validates the input.
valid = False
while not valid:
num = int(input("Enter a value between 1 and 100: "))
if num in range(1,101):
break
Question 4

Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
cal_per_min = 4.2
for i in [10,15,20,25,30]:
print("Calories burnt after",i,"minutes of running:",i*cal_per_min)
Question 5

A firefly collector collects fireflies every day for five days. Write a program that keeps a running total of the number of flies collected during the five days. The loop should ask for the number of fireflies collected for each day, and when the loop is finished, the program should display the total number of fireflies collected.
days = 5
total = 0
for i in range(days):
total +=input("Enter fireflies collected on day",i+1,":")
print(total)