   # PyTestVowels:
Counting no. of vowels in a given input string

# User Story:
As a user, I want to input a string so that I can count the number of vowels in it.The program can handle both lowercase and uppercase vowels.

# Test Cases:
***Test Case 01***:

&emsp;**Input**: "Hello"
&emsp;**Expected Result**: 2 (since 'e' and 'o' are vowels)

***Test Case 02***:
 
&emsp;**Input**:  "PYTHON" 
&emsp;**Expected Result**: 1 (since 'O' is a vowel)

***Test Case 03***:
 
&emsp;**Input**: "bcd"
&emsp;**Expected Result**:  0 (no vowels)

***Test Case 04***:

&emsp;**Input**: "aeiou" 

&emsp;**Expected Result**: 5  (all letters are vowels)

***Test Case 05***:

&emsp;**Input**: ""
&emsp;**Expected Result**: Error: No input provided.

# Test Result Summary:
| S.No 	| Test Method Name                     	| Test Description                                                                                                                     	| Input                          	| Expected Output 	| Actual Output 	|
|------	|--------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------	|--------------------------------	|-----------------	|---------------	|
|   1  	| Basic word Checker                	| Check how many vowels are there in the given string input. 	| "Hello "          	| 2            	| 2        	|
|   2  	| All uppercase string checker    	| Check number of vowels on all uppecased letters                                                           	| "Python"            	| 1           	| 1        	|
|   3  	| Sensitivity to different cases       	| Check Anagram algorithm's accuracy over strings of Upper and lower case-characters.                                                  	| "Astronomer" and "Moon Starer" 	| False           	| False         	|
|   4  	| Multi-word phrases accuracy          	| Check Anagram algorithm's accuracy over multi-word strings.                                                                          	| "debit card" and "bad credit"  	| True            	| True          	|
|   5  	| Sensitivity to different data types. 	| Check Anagram algorithm's sensitivity to strings of different data types(string, number).                                            	| 123 and "321"                  	| False           	| False         	|
