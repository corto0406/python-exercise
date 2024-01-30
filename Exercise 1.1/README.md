## Install Python

First, install Python 3.8.7 on your system. Check your Python version by using the command `python --version` from your terminal.

## Set Up a Virtual Environment

Set up a new virtual environment named “cf-python-base”.

![Step 2](./Exercise 1.1/step2.png)

## Create a Python Script

Install Visual Studio Code or another text editor of your choice and create a Python script named “add.py”. This script will take two numbers from the user input, add them, and print the result. Here's the template for your Python script:

![Step 3](./Exercise 1.1/step3.png)

```python
# Prompt the user to enter the first number
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number
b = int(input("Enter the second number: "))

# Add the two numbers and store the result in variable c
c = a + b

# Print the value of c
print("The sum of", a, "and", b, "is:", c)
```

## Set Up IPython Shell

Set up an IPython shell in the virtual environment "cf-python-base". An IPython shell is similar to the regular Python REPL with additional features like syntax highlighting, auto-indentation, and robust auto-complete features. Install it using pip.

![Step 4](./Exercise 1.1/step4.png)

## Export a Requirements File

Generate a “requirements.txt” file from your source environment. Next, create a new environment called “cf-python-copy”. In this new environment, install packages from the “requirements.txt” file.

![Step 5](./Exercise 1.1/step5.png)
