# OldProgrammingCampChallenges
 I attended a programming camp that had a challenge packet at the end, time to see if 4 years later I've gotten better
 I think this challenge is good for new programmers, reguardless of the language they're working in this is a good right
 of passage to show you know the basics

## the challenge reads as follows:
### Bob Jones University Computer Science Camp Programming Contenst 2018
#### Thursday July 19 2018
### Problem 1: Message Encoding
#### The Problem
Read a Message and encode the message according to this encoding scheme:
1. Encode all digits by adding 3 to the digit and wrap around anything that exceeds 9. for example 3 would become 6 and 7 would become 0
2. Encode all alphabetic characters according to this sequence:  
`
ABCDEFGHIJKLMNOPQRSTUVWXYZ  
DJPGOAQWHCTLZXSBVYUFNRMIKE
`
3. leave all other characters the same  

#### The Input
a bunch of characters terminated by the end of line. There is no limit to the length of the input.
#### The Output
Encoded characters terminated by end of line.
#### Sample Input
I was born in 1957 A.D.
#### Sample Output
H mdu jsyx hx 4280 D.G.
### Problem 2: Triangle Printer
note: I made a more sophisticated repository for this purpose because I got bored in class and remembered this was a thing. 
[Triangle Generator](https://github.com/Lubba-64/TriangleAsTextGenerator)
#### The Problem
Given an Integer X from 1 to 40, Print an inverted triangle using .'s with X levels Do this process 5 times
#### The Input
5 integers 1-40, each on a separate line.
#### The Output
The inverted triangle using .'s, each separated by a blank line
#### Sample Input
`5  2  3  1  2  `
#### Sample Output
.....    
....  
...  
..  
.  
  
..   
.  
 
...  
..  
.

. 
  
..  
.
### Problem 3: Data on the Range!
#### The Problem
One of the measures taken on a group of data is the range of the data. the range of a grou of data is defined as the absolute value of the difference of the largest element and the smallest element. write a program to compute the range of different data sets
#### The Input
The input to your program will be one or more data sets.  
The first value in each data set will be N, the number of values in the data set.  
The next N values of that data set will be the values you compute the range for.
The end of all input is a data set containing no values. this set should not be processed
#### The Output
For each collection, print the set number and range of the set. Have a blank line after each line to separate the sets.
#### Sample Input
`3  10  20  15  2  -1  1  0  `
#### Sample Output
`
Data set 1 has range: 10  
Data set 2 has range: 2
`
### Problem 4: Factorial Sum
#### The Problem
a factorial is a mathematical function:  
`fact(x)=x*(x-1)*(x-2)*...*3*2*1`  
Note: `fact(0)=1`, and the function is undefined for negative numbers, so in that case return NaN (Not a Number).  
Example: `fact(5)=5*4*3*2*1=120`  
#### The Input
A number to compute the function for
#### The Output
the output of the function
#### Sample Input
`5`
#### Sample Output
`120`
### Problem 5: Gauss Sum
#### The Problem
Write a program to do what Gauss did.
Given a number N, compute the sum of the integers 1 to N
#### The Input
A number to compute the function for
#### The Output
the output of the function
#### Sample Input
`100`
#### Sample Output
`5050`