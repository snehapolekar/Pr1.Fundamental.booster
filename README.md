# Pr1.Fundamental.booster

# Interactive Personal Data Collector

A simple Python command-line script that collects basic personal information from a user and displays it back with type and memory information.

## Description

This script prompts the user for their name, age, height, and favourite number. It then displays the collected values along with their Python data type and memory address. Finally, it calculates an approximate birth year based on the entered age.

## Features

- Collects user input: name, age, height, and favourite number
- Displays each value's type using `type()`
- Displays each value's memory address using `id()`
- Calculates an approximate birth year based on a fixed reference year (2026)

## Requirements

- Python 3.x

## Usage

Run the script from the command line:
python "Fundamental_booster.py"

You will be prompted to enter:
1. Your name
2. Your age
3. Your height (in meters)
4. Your favourite number

The script will then display your information along with its type and memory address, followed by an estimated birth year.

## Example Interaction
Welcome to the Interactive Personal Data Collector!!
Please enter your name : John
Please enter your age : 25
Please enter your height in meters : 1.75
Please enter your favourite number : 7
Thank you! Here is the information we collected :
Name: John(Type: <class 'str'>, Memory Address : ...)
age: 25(Type: <class 'int'>, Memory Address : ...)
height: 1.75(Type: <class 'float'>, Memory Address : ...)
fav_num: 7(Type: <class 'int'>, Memory Address : ...)
Your birth year is approximately:2001(based on your age of 17)
Thank you for using the Personal Data Collector.
Goodbye!!

## Known Issues

- The reference year used for birth year calculation (2026) is hardcoded and not dynamically fetched.
- The message "based on your age of 17" is a leftover/hardcoded string and does not reflect the actual age entered by the user.
- No input validation is performed; entering invalid data types (e.g., text instead of a number) will cause the program to crash.

## License

This project is provided as-is for educational purposes.
