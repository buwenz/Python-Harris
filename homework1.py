# PPHA 30535
# Spring 2021
# Homework 1

# Buwen Zhang
# buwenz

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
q1_list = ['a', 'b', 'c', 'd', 'e']
for value in q1_list:
    print(f'The value at position {q1_list.index(value)} is {value}.')


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

# define punctuation (the method of removing punctuations is adapted from: https://www.programiz.com/python-programming/examples/remove-punctuation)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
def check_palindrome(my_str):
    for char in my_str:
        if char in punctuations:
            my_str = my_str.replace(char, " ")
            my_str = my_str.replace(" ", "")
    my_str_ad = my_str.strip().lower()
    if my_str_ad == my_str_ad[::-1]:
        return "Yes"
    else:
        return "No"

q2_list = ["radar", "A man, a plan, a canal, Panama!", "Apple", "This isn't a palindrome"]
for x in q2_list:
   print(check_palindrome(x))


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
while choice not in available_vegetables:
    print('You made an invalid choice and please pick again.')
    choice = input('Please pick a vegetable I have available: ') 
print(f'You can have the vegetable {choice}')
  

# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
str_list = ['Anthropology', 'Business', 'COMPUTER SCIENCE', 'data science', 'ECONOMICS']
new_list = [name.lower() for name in str_list if name[0].lower() == 'a' or name[0].lower() == 'b']
print(new_list)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]
end_list = [start_list[len(start_list)-i-1]*2 for i in range(len(start_list))]
print(end_list)

#Alternative
start_list = [3, 5, 7, 9, 11, 13]
print([start_list[len(start_list)-i-1]*2 for i in range(len(start_list))])


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
name_dictionary = dict(zip(short_names, long_names)) # this function is found on: https://careerkarma.com/blog/python-convert-list-to-dictionary/
print(name_dictionary)
#or
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
print(dict(zip(short_names, long_names)))
