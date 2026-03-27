# Tutorial 5

## Activity 1
Question 1

Describe the three steps that must be taken when a file is used by a program.
Open the file
Process the file
Close the file
Question 2

Why should a program close a file when it’s finished using it?
If a file remains open once a program terminates, the opened file will continue to use resources resulting in a memory leak.
Question 3

What is a file’s read position? Where is the read position when a file is first opened for reading?
The read position is an indicator of which part of the file the program is interpreting. It starts at the beginning of the file.
Question 4

Which mode should a file be opened in to allow data to be written to it, without erasing any previous data?
Append mode - "a"
Question 5

If a file does not exist and a program attempts to open it in append mode, what happens?
A new file will be created



## Activity 2
Question 1

Write a program that opens an output file with the filename myName.txt, writes the name of a person “John Locke” to the file, then closes the file.
with open("myName.txt","w") as file:
file.write("John Locke")
Question 2

Write a program that opens the myName.txt file that was created by the program in question 1, reads all of the data from the file before closing it, and then displays the data from the file.
with open("myName.txt", "r") as file:
data = file.read()
print(data)
Question 3

Write code that does the following: opens an output file with the filename number_ list.txt, uses a loop to write the numbers 1 through 100 to the file, then closes the file.
with open("number_list.txt","w"):
for i in range(1,101):
file.write(str(i)+"\n")
Question 4

Write code that does the following: opens the number_list.txt file that was created by the code you wrote in question 3, reads all of the numbers from the file and displays them, then closes the file.
with open("number_list.txt", "r") as file:
print(file.readlines())
Question 5

Modify the code that you wrote in question 4 so it adds all of the numbers read from the file and displays their total.
with open("number_list.txt", "r") as file:
count = 0
for num in file:
count +=int(num)

print(num)
Question 6

Write code that opens an output file with the filename number_list.txt, but does not erase the file’s contents if it already exists.
with open("number_list.txt", "a") as file:
pass
Question 7

A file exists on the disk named students.txt .The file contains several records, and each record contains two fields: (1) the student’s name, and (2) the student’s score for the final exam. Write code that deletes the record containing “John Perz” as the student name.
data = []

\# Take all the data except for John's
with open("students.txt", "r") as file:
for i in file.readlines():
if i[0] != "John Perz":
data.append(i) # assuming each record is [name, score]
\# file closes here

\# then write all other data back to the file
with open("students.txt","w") as file:
for record in data:
file.write(record)
Question 8

A file exists on the disk named students.txt. The file contains several records, and each record contains two fields: (1) the student’s name, and (2) the student’s score for the final exam. Write code that changes Julie Milan’s score to 100.
data = []

\# Take all the data except for John's
with open("students.txt", "r") as file:
for i in file.readlines():
if i[0] == "Julie Milan": i[1] = 100 # assuming each record is [name, score]
data.append(i)
\# file closes here

\# then write all other data back to the file
with open("students.txt","w") as file:
for record in data:
file.write(record)
Question 9

What will the following code display? 



try: x = float('abc123') print('The conversion is complete.')
except IOError: print('This code caused an IOError.')
except ValueError: print('This code caused a ValueError.')
print('The end.')
This code caused a ValueError.
The end.
Question 10

What will the following code display? 



try: x = float(abc123)
print(x)except ValueError: print('This code caused a ValueError.')
except TypeError: print('This code caused a TypeError.')
except NameError: print('This code caused a NameError.')
print('The end.')
This code caused a NameError.
The end.
Question 11

Look at the following statement: numbers = [10, 20, 30, 40, 50]





How many elements does the list have? 

What is the index of the first element in the list? 

What is the index of the last element in the list?
This list has 5 elements
The first element has index 0
The last element has index 4
Question 12

Look at the following statement: letters = ['A', 'B', 'C', 'D']





What value is stored in letters[1]? 

What value is stored in letters[3]? 

What value is stored in letters[−2]?
1. 'B'
2. 'D'
3. 'C'
Question 13

What will the following code display? 



values = [2, 4, 6, 8, 10]  
print(values[1:3])
4,6
Question 14

What will the following code display? 



numbers = [5, 4, 3, 2, 1, 0]
print(numbers[:3])
5,4,3
Question 15

What will the following code display? 



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[−4:])
5,6,7,8
Question 16

What will the following code display? 



values = [2] * 5
print(values)
2,2,2,2,2
Question 17

Assume names references a list. Write a for loop that displays each element of the list.
for e in names:
print(e)
Question 18

Write a function that accepts a list as an argument (assume the list contains integers) and returns the total of the values in the list.
def sum_values(input):
total = 0
for value in input:
total +=value
return total
Question 19

Assume the names variable references a list of strings. Write code that determines whether 'Ruby' is in the names list. If it is, display the message 'Hello Ruby'. Otherwise, display the message 'No Ruby'.
if "Ruby" in names: print("Hello Ruby")
else: print("No Ruby)
Question 20

What will list1 and list2 contain after the following statements are executed?  



list1 = [1, 2] * 2
list2 = [3]
list2 += list1
1,2,1,2
3,1,2,1,2
Question 21

Write a statement that creates a two-dimensional list with 5 rows and 3 columns. Then write nested loops that get an integer value from the user for each element in the list.
list = []
for i in range(5):
list.append([])
for ii in range(3):
list[i].append(None)

for i in range (len(list)):
for ii in range (len(list[i])):
list[i][ii] = input('Enter a value: ')
print(list)