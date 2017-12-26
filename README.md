# Project Name

**Author**: Brendan Davis, Philip Werner
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
This program allows a user to input a string of text of their choosing, it uses predictive test to write a new string. It will then create a dictionary from the inputed text with two words as the keys and the word(s) that follow those keys as the value. The program will then take that dictionary and key input from the user to then randomly generate a 'new story' at the desired length as inputed by the user.

## Getting Started
The Trigrams app can be run directly from the trigrams.py file.

OR

You can run it from the command line while at the root level.

``` python trigrams.py inout_text.txt 500 > my_submission.txt```

## Architecture
This program uses the random and sys libraries. Big part of program is the opening and reading of inputed .txt files as well as the saving of new .txt files

## Change Log
10-19-2017 1:30pm - Added read_file functionality.
10-19-2017 2:00pm - Added function to create dictionary.
10-19-2017 4:00pm - Added function to create new string.
10-20-2017 2:30pm - Added function to write new .txt file with generated string

