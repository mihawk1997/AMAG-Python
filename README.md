# AMAG-Python
Python coding challenge - AMAG

# Introduction
The project involves building a simple calculator which performs actions based on basic operations like Addition,Subtraction,Multiplication and division.

# Tools and libraries used
To build this the follwing tools were used:

Programming language: Python - To build all functions of the calculator.
Librarries: pandas, Numpy, uniitest

# Folder structure
The folder structure is as follows:
1. src- Contians the Cal.py file which has the calculator code
2. data- Conatains sample data for the calculator
3. unit test - Contains the unit_test.py file which has various test conditions.
4. results - Contains the excel file with correct answers retrived from the Cal.py.
5. docs - Contains the software architecture,Folder recommendations and Unit test plan. 


# How to use the project:
1. Download and run the Cal.py from the src folder
2. Make sure you have all the files in one directory

# Test conditions: 
1. You can run the unit_test.py from the unit test folder to see various test coniditons.
2. You can also modify and add your own test conditions.

# Create your own test functions: 
```
def test_add(self):
        self.assertEqual(Cal.get_calc(4,4,'addition'),8)
```
The above code snippet shows the testing done for the addition function.
Here assertEqual checks if 'addition' of 4 and 4 is 8?
If yes, it runs and provides the pass condition

```
def create_your_own_functionname(self):
        self.assertEqual(Cal.get_cal(x,y,'operation'),Expected value)
```
To create your own test function, pass in the function name,x,y and any operator in any case-senstive manner.
Then pass in the expected value.
If the operation and expected value are the same,you will get a test pass messsage or else, it will show an error message.

# Review results
The results.xlsx file shows the correct answers to the input sample calculated by Cal.py

# Credits
Sample data : AMAG group

