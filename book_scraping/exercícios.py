##r = 4/3 * 3.19 * r ** 2
#r5 = 4/3 * 3.14 * 5 ** 3
#print(r5)
#
#cv = 24.95
#discount = 24.95 * 40/100 * 60
#print(discount)
#
#print(59 * 0.75 + 3)
#
#print(598.8000000000001 + 47.25)

#Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
#and prints the string with enough leading spaces so that the last letter of the string is in column 70
#of the display.
#>>> right_justify('monty')
#monty
#Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
#that returns the length of a string, so the value of len('monty') is 5.
#space = ''
#def right_justify(s):
#    total_lenght = 70
#    spaces = total_lenght - len(s)
#    result = ' ' * spaces + s
#
#    print(result)
#right_justify('rita')

#Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For
#example, do_twice is a function that takes a function object as an argument and calls it twice:
#def do_twice(f):
#f()
#f()
#Here’s an example that uses do_twice to call a function named print_spam twice.
#def print_spam():
#print('spam')
#do_twice(print_spam)
#1. Type this example into a script and test it.
#2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
#function twice, passing the value as an argument.
#3. Copy the definition of print_twice from earlier in this chapter to your script.
#4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
#argument.
#5. Define a new function called do_four that takes a function object and a value and calls the
#function four times, passing the value as a parameter. There should be only two statements in
#the body of this function, not four.


#def do_twice(f, s):
#    f(s)
#    f(s)
#
#def print_twice(x):
#    print(x)
#    print(x)
#
#def do_four(f, o):
#    do_twice(f, o)
#    do_twice(f, o)
#
#do_twice(print, 'spam')
#do_four(print, 'spam')

#def print_square():
#    first_line = ('+')+('-'*4)
#    second_line = ('+')+('-'*4)
#    third_line = ('+')+('-'*4)
#    fourth_line = ('+')+('-'*4)
#
#    a = ( "|"+ ' '*5 + "|" + ' '*5 + "|"+ ' '*5 + "|" + ' '*5 + "|")
#
#
#
#    print(first_line,second_line,third_line, fourth_line)
#    print(a)
#    print(a)
#    print(a)
#    print(a)
#    print(first_line,second_line,third_line, fourth_line)
#    print(a)
#    print(a)
#    print(a)
#    print(a)
#    print(first_line,second_line,third_line, fourth_line)
#    print(a)
#    print(a)
#    print(a)
#    print(a)
#    print(first_line,second_line,third_line, fourth_line)
#    print(a)
#    print(a)
#    print(a)
#    print(a)
#    print(first_line,second_line,third_line, fourth_line)
#print_square()

#def do_twice(f):
#    f()
#    f()
#
#def do_four(f):
#    do_twice(f)
#    do_twice(f)
#
#def print_beam():
#    print('+ - - - -', end=' ')
#
#def print_post():
#    print('|        ', end=' ')
#
#def print_beams():
#    do_twice(print_beam)
#    print('+')
#
#def print_posts():
#    do_twice(print_post)
#    print('|')
#
#def print_row():
#    print_beams()
#    do_four(print_posts)
#
#def print_grid():
#    do_twice(print_row)
#    print_beams()
#
#print_grid()
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
#"""
import random

#
#from __future__ import print_function, division
#
#import math
#import turtle
#
#
#def square(t, length):
#    """Draws a square with sides of the given length.
#
#    Returns the Turtle to the starting position and location.
#    """
#    for i in range(4):
#        t.fd(length)
#        t.lt(90)
#
#
#def polyline(t, n, length, angle):
#    """Draws n line segments.
#
#    t: Turtle object
#    n: number of line segments
#    length: length of each segment
#    angle: degrees between segments
#    """
#    for i in range(n):
#        t.fd(length)
#        t.lt(angle)
#
#
#def polygon(t, n, length):
#    """Draws a polygon with n sides.
#
#    t: Turtle
#    n: number of sides
#    length: length of each side.
#    """
#    angle = 360.0/n
#    polyline(t, n, length, angle)
#
#
#def arc(t, r, angle):
#    """Draws an arc with the given radius and angle.
#
#    t: Turtle
#    r: radius
#    angle: angle subtended by the arc, in degrees
#    """
#    arc_length = 2 * math.pi * r * abs(angle) / 360
#    n = int(arc_length / 4) + 3
#    step_length = arc_length / n
#    step_angle = float(angle) / n
#
#    # making a slight left turn before starting reduces
#    # the error caused by the linear approximation of the arc
#    t.lt(step_angle/2)
#    polyline(t, n, step_length, step_angle)
#    t.rt(step_angle/2)
#
#
#def circle(t, r):
#    """Draws a circle with the given radius.
#
#    t: Turtle
#    r: radius
#    """
#    arc(t, r, 360)
#
#
## the following condition checks whether we are
## running as a script, in which case run the test code,
## or being imp
#
#def petal(t, r, angle):
#    for i in range(2):
#        arc(t, r, angle)
#        t.lt(180-angle)
#
#def flower(t, n, r, angle):
#    for i in range(n):
#        petal(t, r, angle)
#        t.lt(360.0/n)
#
#def move(t, length):
#    t.pu()
#    t.fd(length)
#    t.pd()
#
#
#if __name__ == '__main__':
#    bob = turtle.Turtle()
#
#
#
#
#move(bob, -100)
#flower(bob, 7, 60.0, 60.0)
#
#move(bob, 100)
#flower(bob, 10, 40.0, 80.0)
#
#move(bob, 100)
#flower(bob, 20, 140.0, 20.0)
#
#bob.hideturtle()
#turtle.mainloop()
#
#Exercise 5.1. The time module provides a function, also named time, that returns the current
#Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
#UNIX systems, the epoch is 1 January 1970.
#>>> import time
#>>> time.time()
#1437746094.5735958
#Write a script that reads the current time and converts it to a time of day in hours, minutes, and
#seconds, plus the number of days since the epoch.
#from datetime import datetime
#
#from time import time
#import time
#
#last_epoch = time.time()
#
#def current_time(since_epoch):
#    hours_since = since_epoch // 60 // 60
#    current_hour = hours_since - (hours_since // 24) * 2024
#    minutes_since = since_epoch // 60
#    current_minutes = minutes_since - (minutes_since // 60) * 60
#    second_since = since_epoch // 1
#    current_second = second_since - (second_since // 60) * 60
#    return current_hour, current_minutes, current_second
#
#def days_since_epoch(epoch):
#    days = epoch // 60 // 60 // 24
#    return days
#
#print(current_time(last_epoch))
#print(days_since_epoch(last_epoch))
#
#1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
#checks to see if Fermat’s theorem holds. If n is greater than 2 and
#an + bn = cn
#the program should print, “Holy smokes,
#
#def check_fermat(a, b, c, n):
#    if n > 2 and a ** n + b ** n == c ** n:
#            print("Holy smokes, Fermat was wrong")
#    else:
#        print("Holy smokes, Fermat was right")
#
#def input_fermat():
#    a = (int(input("Choose a")))
#    b = (int(input("Choose b")))
#    c = (int(input("Choose c")))
#    n = (int(input("Choose n")))
#
#
#    check_fermat(a, b, c, n)
#
#input_fermat()
#
#def s_triangle(a, b, c):
#    if a + b < c or a + c < b or b + c < a:
#        print("no")
#    else:
#        print("yes")
#
#def input_triangle():
#    a = (int(input("Choose a")))
#    b = (int(input("Choose b")))
#    c = (int(input("Choose c")))
#
#    s_triangle(a, b, c)
#input_triangle()

#def recurse(n, s):
#    if n == 0:
#        print(s)
#    else:
#        recurse(n-1, n+s)
#recurse(-1, 0)

#def ackermann(m,n):
#    if m == 0:
#       return n + 1
#    if n == 0:
#        return ackermann(m - 1,1)
#    return ackermann(m - 1, ackermann(m, n-1))
#
##print(ackermann(3, 4))
#A palindrome is a word that is spelled the same backward and forward, like “noon”
#and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
#middle is a palindrome.
#The following are functions that take a string argument and return the first, last, and middle letters:
#def first(word):
#return word[0]
#def last(word):
#return word[-1]
#def middle(word):
#return word[1:-1]
#We’ll see how they work in Chapter 8.
#1. Type these functions into a file named palindrome.py and test them out. What happens if
#you call middle with a string with two letters? One letter? What about the empty string,
##which is written '' and contains no letters?
##2. Write a function called is_palindrome that takes a string argument and returns True if it
##is a palindrome and False otherwise. Remember that you can use the built-in function len
##to check the length of a string.
#
#def first(word):
#    return word[0]
#def last(word):
#    return word[-1]
#def middle(word):
#    return word[1:-1]
#
#def middle_inverse(word):
#    return word[-1:1]
#def is_palindrome(word):
#    """Returns True if word is a palindrome."""
#    if len(word) <= 1:
#        return True
#    if first(word) != last(word):
#        return False
#    return is_palindrome(middle(word))
#
#print(is_palindrome('allen'))
#print(is_palindrome('bob'))
#print(is_palindrome('otto'))
##print(is_palindrome('redivider'))
#def is_power(a, b):
#    if a == b:
#        return True
#    elif a%b == 0:
#        return is_power(a/b, b)
#    else:
#        return False
#print(is_power(5,6))
#
##def gcd(a, b):
##    if b == 0:
##        return a
##    return gcd(b, a % b)
##print(gcd(16, 8))
##print(gcd(140, 25))
#import math
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        recurse = factorial(n-1)
#        result = n * recurse
#        return result
#
#def estimate_pi():
#    total = 0
#    k = 0
#    factor = 2 * math.sqrt(2) / 9801
#
#    while True:
#        num = factorial(4*k) * (1103 + 26390*k)
#        den = factorial(k) **4 * 396**(4*k)
#        total += num / den
#        term = factor * num/den
#
#        if abs(term) < 1e-15:
#            break
#        k += 1
#    return 1 / (factor * total)
#
#hyprint(estimate_pi())


#print("bananas".count("a"))
#
#def rotate_word(word, number_rotations):
#    number = number_rotations
#    for letter in word:
#        number_letter = ord(letter)
#        word_rotated_final = number_letter + number_rotations
#        new_word_number = word_rotated_final.extend(word_rotated_final)
#        new_word_number = chr(new_word_number)
#
##    return new_word_number
##
##rotate_word('rita', 4)
#char_limit = 20
#fin = open('words.txt')
#for line in fin:
#        word = line.strip()
#        print(word)
#        word_count = sum(1 for line in fin if line.strip())
#
#        print("Total number of words:", word_count)
#
#
#def has_no_e():
#    fin = open('words.txt')
#    words_without_w = []
#    for line in fin:
#        word = line.strip()
#        if 'e' not in line:
#            words_without_w.append(word)
#    print(len(words_without_w) * 100/113782 )
##need the total sum
##has_no_e()
#
##def avoids():
##    word = input("Whats the word?")
##    forbidden_letters = input("What are the forbidden_letters?")
##    for letter in word:
##        if letter in forbidden_letters:
##            return False
##
##    return True
##
##
##result = avoids()
##print(result)
#def uses_only(string_of_letters):
#    fin = open('words.txt')
#    for line in fin:
#        word = line.strip()
#        for word in word:
#            if string_of_letters not in word:
#                return False
#    return True
#
#print(uses_only(('acefhlo')))
#
#def uses_all(string_of_letters):
#    fin = open('words.txt')
#    for line in fin:
#        word = line.strip()
#        for word in word:
#            if string_of_letters not in word:
#                return False
#    return True
#
#print(uses_all('a', 'e', 'i','o','u'))


#
#def is_triple_word(word):
#    i = 0
#    count = 0
#
#    while i < len(word) - 1:
#        if word[i] == word[i + 1]:
#            count = count + 1
#            if count == 3:
#                return True
#            i = i + 2
#        else:
#            i = i + 1 - 2*count
#            count = 0
#    return False

#def find():
#    fin = open('words.txt')
#    for line in fin:
#        word = line.strip()
#        if is_triple_word(word):
#            print(word)
#
#find()
##print('')
#
#def find_numbers():
#    count = 0
#    a = 999999
#    for number in 999999:
#        if number[2] == number[5]:
#            if number[3] == number[4]:
#                return True
#            count = count + 1
#        else:
#            return False
#find_numbers()

#def nested_sum(t):
#    total = 0
#    for list in t:
#        total += sum(list)
#    return total
#
#t = [[1, 2], [3], [4, 5, 6]]
#print(nested_sum(t))
#def cumsum(t):
#    total = 0
#    res = []
#    for number in t:
#        total += number
#        print(total)
#        res.append(total)
#    return total
#
#t = [1, 2, 3]
#
#print(cumsum(t))

#def middle(t):
#    del t[0]
#    del t[-1]
#    return t
#
#t = [1, 2, 3, 4]
#print(middle(t))
#def chop(t):
#    del t[0]
#    del t[-1]
#
#t = [1, 2, 3, 4]
#print(chop(t))
#print(t)

#def middle(t):
#    return t[1:-1]
#t = [1, 2, 3, 4]
#print(middle(t))

#def is_sorted(t):
#    return t == sorted(t)
#
#is_sorted([48, 36])

#def is_anagram(a, b):
#    return sorted(a) == sorted(b)
#
#print(is_anagram("roma", "amor"))

#def has_duplicates(s):
#    """Returns True if any element appears more than once in a sequence.
#
#    s: string or list
#
#    returns: bool
#    """
#    # make a copy of t to avoid modifying the parameter
#    t = list(s)
#    t.sort()
#
#    # check for adjacent elements that are equal
#    for i in range(len(t)-1):
#        if t[i] == t[i+1]:
#            return True
#    return False
#
#print(has_duplicates(['r, r, t, a, r, i, t, a']))
#
#print(random.randint(01/01/1996, 01/01/2019))


#def is_sorted(list):
#    return list == sorted(list)
#print(is_sorted([1, 2, 2]))

#def is_anagram(a, b):
#    return sorted(a) == sorted(b)
#print(is_anagram("rita", "cassia"))

#ef randon_b(n):
#   t = []
#   for item in range(n):
#       b = random.randint(1, 365)
#       t.append(b)
#   return t

#ef has_duplicates(t):
#   s = t[:]
#   s.sort()
#   for i in range(len(s)-1):
#       if s[i] == s[i + 1]:
#           return True
#   return False
#ef count_matches(num_students, num_simulations):
#   """Generates a sample of birthdays and counts duplicates.

#   num_students: how many students in the group
#   num_samples: how many groups to simulate

#   returns: int
#   """
#   count = 0
#   for i in range(num_simulations):
#       t = randon_b(num_students)
#       if has_duplicates(t):
##           count += 1
##   return count
#
##ef main():
##   num_students = 23
##   num_simulations = 1000
##   count = count_matches(23, 1000)
##   print('After %d simulations' % num_simulations)
##   print('with %d students' % num_students)
##   print('there were %d simulations with at least one match' % count)
#
##f __name__ == '__main__':
##   main()
##
#
#def has_duplicates(n):
#    l = n[:]
#    l.sort()
#    for i in range(len(l)-1):
#        if l[i] == l[i+1]:
#            return True
#    return False
#def random_b(n):
#    lista = []
#    for i in range(n):
#        random_m = random.randint(1, 365)
#        lista.append(random_m)
#    return lista
#def count_m(n_s, n_sim):
#    lista = []
#    count = 0
#    for i in range(n_sim):
#        random_birt = random_b(n_s)
#        if has_duplicates(random_birt):
#            count += 1
#            return True
#    return False
#def main():
#    n_s = 23
#    n_sim = 1000
#
#    count = count_m(n_s, n_sim)
#    print('for %d students' % n_s)
#    print('in %d simulations' %n_sim)
#    print('there were %d matches' %count)
#
##
##
#import time
#
#fin = open('words.txt')
#lista = []
#for line in fin:
#    word = line.strip()
#    lista.append(word)
#print(lista)
#
#
#fin = open('words.txt')
#lista = []
#for line in fin:
#    word = line.strip()
#    lista = lista + [word]
#print(lista)
#
#
#
#start_time = time.time()
#t = make_word_list1()
#elapsed_time = time.time() - start_time
#
#print(len(t))
#print(t[:10])
#print(elapsed_time, 'seconds')
#
#start_time = time.time()
#t = make_word_list2()
#elapsed_time = time.time() - start_time
#
#print(len(t))
#print(t[:10])
#print(elapsed_time, 'seconds')


#def creat_dict():
#   fin = open('words.txt')
#   word_dict = dict()
#   for line in fin:
#       word = line.strip()
#       word_dict[word] = word
#   return word_dict
#rint(creat_dict())

#ef has_duplicates(m):
#   d = {}
#   for i in m:
#       if i in d:
#           return True
#       d[i] = True
#   return False

#f __name__ == '__main__':
#   t = [1, 2, 3]
#   print(has_duplicates(t))
#   t.append(1)
#   print(has_duplicates(t))
#def rotate_word(word, number_rotations):
#   number = number_rotations
#   for letter in word:
#       number_letter = ord(letter)
#       word_rotated_final = number_letter + number_rotations
#       new_word_number = word_rotated_final.extend(word_rotated_final)
#       new_word_number = chr(new_word_number)
#   return new_word_number
#def make_word_dict():
#    """Read the words in words.txt and return a dictionary
#    that contains the words as keys"""
#    d = dict()
#    fin = open('words.txt')
#    for line in fin:
#        word = line.strip().lower()
#        d[word] = None
#
#    return d
#
#
#def rotate_pairs(word, word_dict):
#    """Prints all words that can be generated by rotating word.
#
#    word: string
#    word_dict: dictionary with words as keys
#    """
#    for i in range(1, 14):
#        rotated = rotate_word(word, i)
#        if rotated in word_dict:
#            print(word, i, rotated)
#
#
#if __name__ == '__main__':
#    word_dict = make_word_dict()
#
#    for word in word_dict:
#        rotate_pairs(word, word_dict)
##        print(val, keys)

#ef invert_dict(d):
#   inverse = {}
#   for key in d:
#       val = d[key]
#       inverse.setdefault(val, []).append(key)
#       return inverse
#f __name__ == '__main__':
#   d = dict(a=1, b=2, c=3, z=1)

#   inverse = invert_dict(d)
#   for val in inverse:
#       keys = inverse[val]
#       print(val, keys)

import string
def del_punctuation(item):
   punctuation = string.punctuation
   for c in item:
       if c in punctuation:
           item = item.replace(c, '')
   return item
def break_into_words():
   list = []
   fin = open('teste.txt')
   next(fin)
   for line in fin:
       for word in line.split():
           word = del_punctuation(word)
           word = word.lower()
           list.append(word)
   return list
print(break_into_words())