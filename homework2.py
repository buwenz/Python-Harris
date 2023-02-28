# PPHA 30535
# Spring 2022
# Homework 2

# Buwen Zhang
# buwenz

# Due date: Sunday April 17th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]
def sum_compare (org_list):
    re_sum = list(sum(item) for item in org_list)
    result = list()
    for i in range(len(re_sum)):
        if re_sum[i] == 10:
            result.append('just right')
        elif re_sum[i] > 10:
            result.append('big')
        elif re_sum[i] < 10:
            result.append('small')
    return result

result = sum_compare(start_list)
print(result)


# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 30
    return a + b
x = my_func()

# This way is prefered to the old way because a is now an argument (not a global variable) 
# and it can be given any value with the function still works.
def my_func(a):
    b = 30
    return a + b
x = my_func(10)


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random
import random
listofkeys = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
specialkeys = '!@#$%^&*'
def random_password(length=8, special_chars=True):
    if length >=8 and length <=16:
        if special_chars:
            keys = listofkeys+specialkeys
        else:
            keys = listofkeys
        ans = ''
        for i in range(length):
            ans += keys[random.randint(0,len(keys)-1)]
        return ans
    else:
        raise Exception('length not in [8,16]')

print(random_password(10, True)) #this line can be changed

  
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for three people:
#
# Aaron, Moderna, 1, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes any number of these instances and 
# returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class Person():
    def __init__(self, name:str, vaccine:str, num:int, hadCOVID:bool):
        self.name = name
        self.vaccine = vaccine
        self.num = num
        self.hadCOVID = hadCOVID
    
    def get_record(self):
        return '{0} has {1} dose{2} of {3} and have {4}had COVID.'.format(self.name, self.num,\
            's' if self.num >= 2 else '', self.vaccine, '' if self.hadCOVID else 'not ')

    def same_shot(self, anotherp):
        if self.vaccine == anotherp.vaccine:
            return True
        else:
            return False


def all_data(listofperson):
    return [[p.name, p.vaccine, p.num, p.hadCOVID] for p in listofperson]


p = Person('Aaron', 'Moderna', 1, False)
print(p.get_record())
people=[]
people.append(p)
people.append(Person('Ashu', 'Pfizer', 2, False))
people.append(Person('Alison', 'none', 0, True))
people.append(Person('Asma', 'Pfizer', 1, True))
print(all_data(people))
print(people[1].same_shot(people[-1]))

result_list = [people[0].get_record(), people[1].get_record(), people[2].get_record(), people[3].get_record()]
print(result_list)
